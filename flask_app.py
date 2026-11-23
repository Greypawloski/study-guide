"""Arizona Life Producer Exam Prep — Flask app.

PythonAnywhere's WSGI file imports `app` from this module, so keep the name.
"""

import random

from flask import Flask, abort, render_template, request

from content.bootcamp import BOOTCAMP
from content.flashcards import FLASHCARDS
from content.lessons import ARIZONA_NUMBERS, EXAM_INFO, SECTION_BY_ID, SECTIONS
from content.questions import QUESTIONS

app = Flask(__name__)

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
    }


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
