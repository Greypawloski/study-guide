#!/usr/bin/env python3
"""Generate ElevenLabs narration for the explainer videos.

Runs anywhere with Python 3 and internet access to api.elevenlabs.io (your Mac
or a PythonAnywhere console). Uses only the standard library.

Your API key is read from the ELEVENLABS_API_KEY environment variable. It is
never written to disk, printed, or committed.

Commands
  python3 tools/narrate.py check                      plan usage + what's left to generate (free)
  python3 tools/narrate.py voices                     list voices on your account (free)
  python3 tools/narrate.py use-voice NAME_OR_ID       save the narrator voice (e.g. use-voice Eric)
  python3 tools/narrate.py generate SLUG [SLUG ...]   generate missing/changed segments (uses credits)
  python3 tools/narrate.py generate all               ...for every approved script
  python3 tools/narrate.py status                     which segments are done, changed or missing

Audio is cached per segment in tools/explainers/audio/<slug>/<segment>.mp3 with
a matching .json (text hash + character timestamps). Editing one sentence or
changing the voice only regenerates the segments that changed.
"""

import base64
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "explainers"
NARR = ROOT / "narration"
AUDIO = ROOT / "audio"
API = "https://api.elevenlabs.io"


# ------------------------------------------------------------------ helpers

def config():
    return json.loads((NARR / "config.json").read_text())


def save_config(c):
    (NARR / "config.json").write_text(json.dumps(c, indent=2) + "\n")


def scripts(only=None):
    out = []
    for p in sorted(NARR.glob("*.json")):
        if p.name == "config.json":
            continue
        d = json.loads(p.read_text())
        if only and d["slug"] not in only:
            continue
        out.append(d)
    return out


def seg_hash(text, cfg):
    key = json.dumps([text, cfg["voice_id"], cfg["model_id"], cfg["voice_settings"], cfg["output_format"], cfg.get("seed")], sort_keys=True)
    return hashlib.sha256(key.encode()).hexdigest()[:16]


def seg_state(slug, seg, cfg):
    meta = AUDIO / slug / f"{seg['id']}.json"
    if not meta.exists() or not (AUDIO / slug / f"{seg['id']}.mp3").exists():
        return "missing"
    m = json.loads(meta.read_text())
    if m.get("fake"):
        return "placeholder"
    return "done" if m.get("hash") == seg_hash(seg["text"], cfg) else "changed"


def key():
    k = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not k:
        sys.exit("ELEVENLABS_API_KEY isn't set. Run:  export ELEVENLABS_API_KEY='your key'  (then try again)")
    return k


def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 headers={"xi-api-key": key(), "Content-Type": "application/json", "Accept": "application/json"},
                                 data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:500]
        sys.exit(f"ElevenLabs returned HTTP {e.code}: {detail}")
    except urllib.error.URLError as e:
        sys.exit(f"Couldn't reach ElevenLabs ({e.reason}). This machine may block outside connections.")


def pending_chars(cfg, only=None):
    total = 0
    for d in scripts(only):
        if d.get("status") != "approved":
            continue
        for s in d["segments"]:
            if seg_state(d["slug"], s, cfg) != "done":
                total += len(s["text"])
    return total


# ----------------------------------------------------------------- commands

def cmd_check():
    sub = call("GET", "/v1/user/subscription")
    used, limit = sub.get("character_count", 0), sub.get("character_limit", 0)
    cfg = config()
    print(f"Plan: {sub.get('tier')}")
    print(f"Characters used this period: {used:,} of {limit:,}  ({limit - used:,} left)")
    print(f"Voice: {cfg.get('voice_name') or 'not chosen yet'}  ({cfg.get('voice_id') or 'run: voices, then use-voice'})")
    if cfg.get("voice_id"):
        need = pending_chars(cfg)
        print(f"Still to generate for approved scripts: {need:,} characters")
        if need > limit - used:
            print("⚠ That's more than you have left this period.")


def cmd_voices():
    data = call("GET", "/v1/voices")
    voices = data.get("voices", [])
    print(f"{len(voices)} voices on your account:\n")
    for v in sorted(voices, key=lambda v: v.get("name", "")):
        labels = ", ".join(f"{k}: {val}" for k, val in (v.get("labels") or {}).items())
        print(f"  {v.get('name'):<28} {v.get('voice_id')}   {labels}")
    print("\nPick one, then run:  python3 tools/narrate.py use-voice NAME   (e.g. use-voice Eric)")


def cmd_use_voice(choice):
    """Accepts a voice ID or a voice name (e.g. "Eric"), case-insensitive."""
    voices = call("GET", "/v1/voices").get("voices", [])
    match = next((v for v in voices if v.get("voice_id") == choice), None)
    if not match:
        want = choice.strip().lower()
        named = [v for v in voices if (v.get("name") or "").lower() == want
                 or (v.get("name") or "").lower().split(" - ")[0].strip() == want]
        if len(named) > 1:
            sys.exit("More than one voice has that name: " + ", ".join(f"{v['name']} ({v['voice_id']})" for v in named))
        match = named[0] if named else None
    if not match:
        sys.exit("No voice with that name or ID on your account. Run `voices` to see the list (add library voices to My Voices first).")
    voice_id = match["voice_id"]
    cfg = config()
    cfg["voice_id"], cfg["voice_name"] = voice_id, match.get("name")
    save_config(cfg)
    print(f"Narrator set to {match.get('name')}. Every video will use this voice.")


def cmd_status():
    cfg = config()
    for d in scripts():
        states = [seg_state(d["slug"], s, cfg) for s in d["segments"]]
        print(f"{d['slug']:<26} {d.get('status', 'draft'):<9} " + " ".join(f"{s['id']}:{st}" for s, st in zip(d["segments"], states)))


def cmd_generate(slugs, assume_yes=False):
    cfg = config()
    if not cfg.get("voice_id"):
        sys.exit("Choose a voice first:  python3 tools/narrate.py voices   then   use-voice VOICE_ID")
    only = None if slugs == ["all"] else slugs
    docs = [d for d in scripts(only) if d.get("status") == "approved"]
    if not docs:
        sys.exit("No approved scripts match. Check the slug, or set \"status\": \"approved\" in its narration file.")
    todo = [(d, i, s) for d in docs for i, s in enumerate(d["segments"]) if seg_state(d["slug"], s, cfg) != "done"]
    chars = sum(len(s["text"]) for _, _, s in todo)
    if not todo:
        print("Everything is already generated. Nothing to spend.")
        return
    sub = call("GET", "/v1/user/subscription")
    left = sub.get("character_limit", 0) - sub.get("character_count", 0)
    print(f"Voice: {cfg.get('voice_name')}  ·  {len(todo)} segment(s)  ·  {chars:,} characters  ·  {left:,} left on your plan")
    if chars > left:
        sys.exit("Not enough characters left this period. Nothing was generated.")
    if not assume_yes and input("Generate now? [y/N] ").strip().lower() != "y":
        sys.exit("Cancelled. Nothing was generated.")
    for d, i, s in todo:
        segs = d["segments"]
        body = {
            "text": s["text"],
            "model_id": cfg["model_id"],
            "voice_settings": cfg["voice_settings"],
            "previous_text": segs[i - 1]["text"] if i > 0 else None,
            "next_text": segs[i + 1]["text"] if i + 1 < len(segs) else None,
        }
        if cfg.get("seed") is not None:
            body["seed"] = cfg["seed"]
        print(f"  {d['slug']} / {s['id']} ...", end="", flush=True)
        res = call("POST", f"/v1/text-to-speech/{cfg['voice_id']}/with-timestamps?output_format={cfg['output_format']}", body)
        out = AUDIO / d["slug"]
        out.mkdir(parents=True, exist_ok=True)
        (out / f"{s['id']}.mp3").write_bytes(base64.b64decode(res["audio_base64"]))
        (out / f"{s['id']}.json").write_text(json.dumps({
            "hash": seg_hash(s["text"], cfg), "text": s["text"], "voice_id": cfg["voice_id"],
            "voice_name": cfg.get("voice_name"), "model_id": cfg["model_id"],
            "alignment": res.get("alignment"),
        }) + "\n")
        print(" done")
    print("\nAll set. Now send the audio to GitHub:")
    print("  git add tools/explainers && git commit -m \"Add narration audio\" && git push")


def main(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    yes = "--yes" in rest
    rest = [r for r in rest if r != "--yes"]
    if cmd == "check":
        cmd_check()
    elif cmd == "voices":
        cmd_voices()
    elif cmd == "use-voice" and rest:
        cmd_use_voice(rest[0])
    elif cmd == "status":
        cmd_status()
    elif cmd == "generate" and rest:
        cmd_generate(rest, yes)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
