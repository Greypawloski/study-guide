"""Arizona Life Producer Exam Prep — Flask app.

PythonAnywhere's WSGI file imports `app` from this module, so keep the name.
"""

import random
from datetime import timedelta
from urllib.parse import urlparse

from flask import (Flask, abort, g, jsonify, redirect, render_template, request,
                   session, url_for)

import accounts

from content.bootcamp import BOOTCAMP
from content.flashcards import FLASHCARDS
from content.lessons import ARIZONA_NUMBERS, EXAM_INFO, SECTION_BY_ID, SECTIONS
from content.questions import QUESTIONS
from content.videos import VIDEOS, VIDEOS_BY_LESSON

app = Flask(__name__)
app.config.update(
    SECRET_KEY=accounts.load_secret_key(),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    PERMANENT_SESSION_LIFETIME=timedelta(days=90),
    MAX_CONTENT_LENGTH=2 * 1024 * 1024,
)
accounts.init_db()

SECTION_META = [
    {k: s[k] for k in ("id", "num", "title", "weight", "icon", "summary")}
    | {
        "lessons": len(s["lessons"]),
        "questions": sum(1 for q in QUESTIONS if q["section"] == s["id"]),
        "cards": sum(1 for c in FLASHCARDS if c["section"] == s["id"]),
    }
    for s in SECTIONS
]

QMETA = [{"id": q["id"], "section": q["section"]} for q in QUESTIONS]
CMETA = [{"id": c["id"], "section": c["section"]} for c in FLASHCARDS]


@app.context_processor
def inject_globals():
    return {
        "exam": EXAM_INFO,
        "section_meta": SECTION_META,
        "nav": request.endpoint,
        "qmeta": QMETA,
        "cmeta": CMETA,
        "bootcamp": BOOTCAMP,
        "user": g.get("user"),
        "server_progress": g.get("server_progress"),
        "lesson_videos": lambda sid, i: VIDEOS_BY_LESSON.get((sid, i), []),
    }


@app.before_request
def load_user():
    g.user = None
    uid = session.get("uid")
    if uid:
        row = accounts.get_user(uid)
        if row:
            g.user = {"id": row["id"], "username": row["username"]}
        else:
            session.clear()
    # Pages get the saved progress embedded so it shows without a delay.
    if g.user and request.method == "GET" and not request.path.startswith(("/api/", "/static/")):
        g.server_progress = accounts.get_progress(g.user["id"])


def _safe_next(target):
    """Only allow redirects back to pages on this site."""
    if not target:
        return url_for("home")
    p = urlparse(target)
    if p.scheme or p.netloc or not target.startswith("/") or target.startswith("//"):
        return url_for("home")
    return target


# ------------------------------------------------------------- accounts

@app.route("/register", methods=["GET", "POST"])
def register():
    if g.user:
        return redirect(url_for("home"))
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if password != request.form.get("confirm", ""):
            error = "The passwords don't match."
        else:
            uid, error = accounts.create_user(username, password)
            if uid:
                session.clear()
                session.permanent = True
                session["uid"] = uid
                return redirect(url_for("home", welcome=1))
    return render_template("auth.html", mode="register", error=error,
                           username=request.form.get("username", ""))


@app.route("/login", methods=["GET", "POST"])
def login():
    nxt = _safe_next(request.values.get("next"))
    if g.user:
        return redirect(nxt)
    error = None
    if request.method == "POST":
        row, error = accounts.check_login(request.form.get("username"), request.form.get("password"))
        if row:
            session.clear()
            session.permanent = True
            session["uid"] = row["id"]
            return redirect(nxt)
    return render_template("auth.html", mode="login", error=error, next=nxt,
                           username=request.form.get("username", ""))


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("home"))


def _require_json_user():
    if not g.user:
        abort(401)
    if not request.is_json:  # blocks cross-site form posts
        abort(415)


@app.route("/api/progress", methods=["GET", "POST"])
def api_progress():
    if not g.user:
        return jsonify({"error": "not logged in"}), 401
    if request.method == "GET":
        return jsonify(accounts.get_progress(g.user["id"]) or {})
    _require_json_user()
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "bad data"}), 400
    return jsonify(accounts.save_merged(g.user["id"], data))


@app.route("/api/progress/reset", methods=["POST"])
def api_progress_reset():
    _require_json_user()
    stamp = (request.get_json(silent=True) or {}).get("resetAt")
    accounts.put_progress(g.user["id"], {"resetAt": stamp, "updated": stamp})
    return jsonify({"ok": True})


@app.route("/")
def home():
    return render_template(
        "home.html",
        total_q=len(QUESTIONS),
        total_cards=len(FLASHCARDS),
        total_lessons=sum(len(s["lessons"]) for s in SECTIONS),
    )


@app.route("/bootcamp")
def bootcamp_page():
    return render_template("bootcamp.html")


@app.route("/study")
def study():
    return render_template("study.html", sections=SECTIONS)


@app.route("/study/<sid>")
def lesson(sid):
    section = SECTION_BY_ID.get(sid)
    if not section:
        abort(404)
    idx = SECTIONS.index(section)
    prev_s = SECTIONS[idx - 1] if idx > 0 else None
    next_s = SECTIONS[idx + 1] if idx < len(SECTIONS) - 1 else None
    checks = {}
    for q in QUESTIONS:
        if q["section"] == sid and "lesson" in q:
            checks.setdefault(q["lesson"], []).append(q)
    return render_template(
        "lesson.html", s=section, prev_s=prev_s, next_s=next_s, checks=checks
    )


@app.route("/flashcards")
def flashcards():
    return render_template("flashcards.html", cards=FLASHCARDS)


@app.route("/practice")
def practice():
    return render_template("practice.html")


@app.route("/quiz")
def quiz():
    # Configuration is read client-side from the query string; the page gets
    # the full bank so "missed" and "weak" modes can use saved progress.
    return render_template("quiz.html", questions=QUESTIONS, mode="quiz")


@app.route("/exam")
def exam_intro():
    return render_template("exam_intro.html")


@app.route("/exam/start")
def exam_start():
    return render_template("quiz.html", questions=QUESTIONS, mode="exam")


@app.route("/review")
def review():
    return render_template("review.html", questions=QUESTIONS)


@app.route("/videos")
def videos():
    groups = []
    for s in SECTIONS:
        vids = [v for v in VIDEOS if v["lesson"] and v["lesson"][0] == s["id"]]
        if vids:
            groups.append((s, vids))
    extra = [v for v in VIDEOS if not v["lesson"]]
    return render_template("videos.html", groups=groups, extra=extra, total=len(VIDEOS))


@app.route("/cheatsheet")
def cheatsheet():
    return render_template("cheatsheet.html", numbers=ARIZONA_NUMBERS, sections=SECTIONS)


@app.route("/glossary")
def glossary():
    cards = sorted(FLASHCARDS, key=lambda c: c["term"].lower())
    return render_template("glossary.html", cards=cards)


@app.route("/progress")
def progress():
    return render_template("progress.html")


@app.route("/tips")
def tips():
    return render_template("tips.html")


@app.route("/daily")
def daily():
    # A deterministic "question of the day" so everyone sees the same one.
    from datetime import date

    rng = random.Random(date.today().toordinal())
    q = rng.choice(QUESTIONS)
    return render_template("quiz.html", questions=[q], mode="daily")


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
