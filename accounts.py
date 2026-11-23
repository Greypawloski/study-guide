"""User accounts and server-side progress storage (SQLite).

The database and the session secret live in ./data/, which is git-ignored,
so `git pull` never touches them.
"""

import json
import re
import secrets
import sqlite3
import time
from pathlib import Path

from werkzeug.security import check_password_hash, generate_password_hash

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "app.db"
SECRET_PATH = DATA_DIR / "secret_key"

USERNAME_RE = re.compile(r"^[A-Za-z0-9_.-]{3,30}$")
MIN_PASSWORD = 8


def load_secret_key():
    DATA_DIR.mkdir(exist_ok=True)
    if not SECRET_PATH.exists():
        SECRET_PATH.write_text(secrets.token_hex(32))
        SECRET_PATH.chmod(0o600)
    return SECRET_PATH.read_text().strip()


def _db():
    DATA_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with _db() as c:
        c.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE COLLATE NOCASE,
                pw_hash TEXT NOT NULL,
                created REAL NOT NULL
            );
            CREATE TABLE IF NOT EXISTS progress (
                user_id INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
                data TEXT NOT NULL,
                updated REAL NOT NULL
            );
            CREATE TABLE IF NOT EXISTS login_failures (
                username TEXT NOT NULL COLLATE NOCASE,
                at REAL NOT NULL
            );
            """
        )


# ---------------------------------------------------------------- users

def create_user(username, password):
    """Returns (user_id, None) or (None, error message)."""
    username = (username or "").strip()
    if not USERNAME_RE.match(username):
        return None, "Usernames must be 3–30 characters: letters, numbers, dots, dashes or underscores."
    if len(password or "") < MIN_PASSWORD:
        return None, f"Passwords must be at least {MIN_PASSWORD} characters."
    try:
        with _db() as c:
            cur = c.execute(
                "INSERT INTO users (username, pw_hash, created) VALUES (?, ?, ?)",
                (username, generate_password_hash(password), time.time()),
            )
            return cur.lastrowid, None
    except sqlite3.IntegrityError:
        return None, "That username is taken."


def too_many_failures(username, limit=8, window=15 * 60):
    with _db() as c:
        c.execute("DELETE FROM login_failures WHERE at < ?", (time.time() - window,))
        n = c.execute(
            "SELECT COUNT(*) FROM login_failures WHERE username = ?", (username,)
        ).fetchone()[0]
    return n >= limit


def check_login(username, password):
    """Returns (user_row, None) or (None, error message)."""
    username = (username or "").strip()
    if too_many_failures(username):
        return None, "Too many failed attempts. Wait 15 minutes and try again."
    with _db() as c:
        row = c.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if row and check_password_hash(row["pw_hash"], password or ""):
            c.execute("DELETE FROM login_failures WHERE username = ?", (username,))
            return row, None
        c.execute("INSERT INTO login_failures VALUES (?, ?)", (username, time.time()))
    return None, "Wrong username or password."


def get_user(user_id):
    with _db() as c:
        return c.execute("SELECT id, username FROM users WHERE id = ?", (user_id,)).fetchone()


# ------------------------------------------------------------- progress

def get_progress(user_id):
    with _db() as c:
        row = c.execute("SELECT data FROM progress WHERE user_id = ?", (user_id,)).fetchone()
    return json.loads(row["data"]) if row else None


def put_progress(user_id, data):
    with _db() as c:
        c.execute(
            "INSERT INTO progress (user_id, data, updated) VALUES (?, ?, ?) "
            "ON CONFLICT(user_id) DO UPDATE SET data = excluded.data, updated = excluded.updated",
            (user_id, json.dumps(data, separators=(",", ":")), time.time()),
        )


def delete_progress(user_id):
    with _db() as c:
        c.execute("DELETE FROM progress WHERE user_id = ?", (user_id,))


def save_merged(user_id, incoming):
    """Merge a device's copy into the stored copy, save, and return the result."""
    merged = merge(get_progress(user_id), incoming)
    put_progress(user_id, merged)
    return merged


# ---------------------------------------------------------------- merge
# Two devices may study offline and sync later, so progress is merged
# field by field instead of overwritten. Toggles (lessons, flags) store a
# signed timestamp: positive = on, negative = off; the newest wins.

def _num(x, default=0):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) else default


def _toggle(v):
    if v is True:
        return 1
    return _num(v)


def _merge_toggles(a, b):
    out = {}
    for k in set(a) | set(b):
        va, vb = _toggle(a.get(k)), _toggle(b.get(k))
        out[k] = va if abs(va) >= abs(vb) else vb
    return out


def _merge_answers(a, b):
    out = {}
    for k in set(a) | set(b):
        x, y = a.get(k), b.get(k)
        if not isinstance(x, dict):
            out[k] = y
            continue
        if not isinstance(y, dict):
            out[k] = x
            continue
        newer = x if _num(x.get("t")) >= _num(y.get("t")) else y
        out[k] = {
            "r": max(_num(x.get("r")), _num(y.get("r"))),
            "w": max(_num(x.get("w")), _num(y.get("w"))),
            "last": newer.get("last"),
            "t": max(_num(x.get("t")), _num(y.get("t"))),
        }
    return out


def _merge_tasks(a, b):
    out = {}
    for k in set(a) | set(b):
        x, y = a.get(k), b.get(k)
        if not isinstance(x, dict) or not isinstance(y, dict):
            out[k] = x if isinstance(x, dict) else y
            continue
        newer = x if _num(x.get("date")) >= _num(y.get("date")) else y
        rec = dict(newer)
        if not rec.get("removed"):
            bests = [v for v in (x.get("best"), y.get("best")) if isinstance(v, (int, float))]
            rec["best"] = max(bests) if bests else None
        out[k] = rec
    return out


def _merge_boot(a, b, ats, bts):
    # The most recently changed plan wins (so "restart the plan" sticks).
    if ats == bts:
        newer = a or b
    else:
        newer = a if ats > bts else b
    if not isinstance(newer, dict):
        return None
    if isinstance(a, dict) and isinstance(b, dict) and a.get("start") and a.get("start") == b.get("start"):
        newer = dict(newer)
        newer["tasks"] = _merge_tasks(a.get("tasks") or {}, b.get("tasks") or {})
    return newer


def merge(stored, incoming):
    a = stored if isinstance(stored, dict) else {}
    b = incoming if isinstance(incoming, dict) else {}
    if not a:
        return b
    if not b:
        return a

    # A reset on either side wipes everything older than the reset.
    ra, rb = _num(a.get("resetAt")), _num(b.get("resetAt"))
    if ra != rb:
        newer_reset, other = (a, b) if ra > rb else (b, a)
        if _num(other.get("updated")) <= max(ra, rb):
            return newer_reset

    def d(x, k):
        v = x.get(k)
        return v if isinstance(v, dict) else {}

    def l(x, k):
        v = x.get(k)
        return v if isinstance(v, list) else []

    cards_a, cards_b = d(a, "cards"), d(b, "cards")
    due_a, due_b = d(a, "cardDue"), d(b, "cardDue")
    cards, due = {}, {}
    for k in set(cards_a) | set(cards_b):
        if _num(due_a.get(k)) >= _num(due_b.get(k)) and k in cards_a:
            cards[k], due[k] = cards_a[k], due_a.get(k)
        else:
            cards[k], due[k] = cards_b.get(k, cards_a.get(k)), due_b.get(k, due_a.get(k))

    exams, seen = [], set()
    for e in l(a, "exams") + l(b, "exams"):
        key = isinstance(e, dict) and e.get("date")
        if key and key not in seen:
            seen.add(key)
            exams.append(e)
    exams.sort(key=lambda e: e.get("date"))

    bts_a, bts_b = _num(a.get("bootTs")), _num(b.get("bootTs"))
    return {
        "answers": _merge_answers(d(a, "answers"), d(b, "answers")),
        "lessons": _merge_toggles(d(a, "lessons"), d(b, "lessons")),
        "flagged": _merge_toggles(d(a, "flagged"), d(b, "flagged")),
        "cards": cards,
        "cardDue": due,
        "exams": exams,
        "quizzes": max(_num(a.get("quizzes")), _num(b.get("quizzes"))),
        "days": sorted(set(l(a, "days")) | set(l(b, "days"))),
        "boot": _merge_boot(a.get("boot"), b.get("boot"), bts_a, bts_b),
        "bootTs": max(bts_a, bts_b),
        "resetAt": max(ra, rb),
        "updated": max(_num(a.get("updated")), _num(b.get("updated"))),
    }
