"""The 7-Day Pass Bootcamp: a guided, gated study plan.

Task types (how each one is completed):
  lessons    - every lesson in the listed sections is marked done (checkpoints do this)
  quiz       - finish the linked quiz with a score at or above `target`
  cards      - every flashcard in the listed sections has been reviewed at least once
  mock       - finish a full mock exam (score at or above `target` to pass the task)
  review     - finish a review quiz of missed questions (auto-done if nothing is missed)
  read       - a page to read; checked off by hand
"""

PASS_TARGET = 80

DAYS = [
    {
        "day": 1,
        "title": "Rules of the game",
        "focus": "Arizona regulation and how insurance contracts work",
        "goal": "Know the Arizona licensing numbers cold and understand insurance contract law.",
        "tasks": [
            {"type": "read", "title": "Read the Arizona cheat sheet once", "minutes": 10, "href": "/cheatsheet"},
            {"type": "lessons", "title": "Study Section 1: Insurance Regulation", "sections": ["reg"], "minutes": 40},
            {"type": "quiz", "title": "Pass the Regulation quiz", "sections": ["reg"], "n": 20, "minutes": 20},
            {"type": "lessons", "title": "Study Section 2: General Insurance", "sections": ["general"], "minutes": 40},
            {"type": "quiz", "title": "Pass the General Insurance quiz", "sections": ["general"], "n": 20, "minutes": 20},
            {"type": "cards", "title": "Review all Regulation & General flashcards", "sections": ["reg", "general"], "minutes": 20},
        ],
    },
    {
        "day": 2,
        "title": "The biggest section",
        "focus": "Life Insurance Basics (24% of the exam)",
        "goal": "Master insurable interest, business uses, replacement and underwriting.",
        "tasks": [
            {"type": "lessons", "title": "Study Section 3: Life Insurance Basics", "sections": ["basics"], "minutes": 60},
            {"type": "quiz", "title": "Pass the Life Insurance Basics quiz", "sections": ["basics"], "n": 30, "minutes": 30},
            {"type": "cards", "title": "Review all Life Insurance Basics flashcards", "sections": ["basics"], "minutes": 15},
            {"type": "quiz", "title": "Day 1 recall: mixed Regulation & General quiz", "sections": ["reg", "general"], "n": 15, "minutes": 15},
            {"type": "review", "title": "Fix every question you've missed so far", "minutes": 15},
        ],
    },
    {
        "day": 3,
        "title": "Know your policies",
        "focus": "Term, whole life, universal, variable, group and credit (23%)",
        "goal": "Be able to match any client situation to the right type of policy.",
        "tasks": [
            {"type": "lessons", "title": "Study Section 4: Life Insurance Policies", "sections": ["policies"], "minutes": 50},
            {"type": "quiz", "title": "Pass the Policies quiz", "sections": ["policies"], "n": 25, "minutes": 25},
            {"type": "cards", "title": "Review all Policies flashcards", "sections": ["policies"], "minutes": 15},
            {"type": "quiz", "title": "Recall: mixed Days 1–2 quiz", "sections": ["reg", "general", "basics"], "n": 20, "minutes": 20},
            {"type": "review", "title": "Fix every question you've missed so far", "minutes": 15},
        ],
    },
    {
        "day": 4,
        "title": "The fine print",
        "focus": "Provisions, beneficiaries, settlement and nonforfeiture options, riders (23%)",
        "goal": "Memorize every Arizona time limit and know which option fits which goal.",
        "tasks": [
            {"type": "lessons", "title": "Study Section 5: Provisions, Options & Riders", "sections": ["provisions"], "minutes": 60},
            {"type": "quiz", "title": "Pass the Provisions quiz", "sections": ["provisions"], "n": 30, "minutes": 30},
            {"type": "cards", "title": "Review all Provisions flashcards", "sections": ["provisions"], "minutes": 20},
            {"type": "quiz", "title": "Recall: mixed Days 1–3 quiz", "sections": ["reg", "general", "basics", "policies"], "n": 25, "minutes": 25},
            {"type": "review", "title": "Fix every question you've missed so far", "minutes": 15},
        ],
    },
    {
        "day": 5,
        "title": "Annuities & taxes",
        "focus": "Annuities (10%) and federal tax (5%)",
        "goal": "Finish all content. After today you've seen everything on the exam.",
        "tasks": [
            {"type": "lessons", "title": "Study Section 6: Annuities", "sections": ["annuities"], "minutes": 40},
            {"type": "quiz", "title": "Pass the Annuities quiz", "sections": ["annuities"], "n": 20, "minutes": 20},
            {"type": "lessons", "title": "Study Section 7: Federal Tax", "sections": ["tax"], "minutes": 30},
            {"type": "quiz", "title": "Pass the Federal Tax quiz", "sections": ["tax"], "n": 15, "minutes": 15},
            {"type": "cards", "title": "Review all Annuities & Tax flashcards", "sections": ["annuities", "tax"], "minutes": 15},
            {"type": "quiz", "title": "Cumulative 50-question test (all sections)", "sections": [], "n": 50, "mode": "test", "minutes": 50},
        ],
    },
    {
        "day": 6,
        "title": "Exam simulation",
        "focus": "Full mock exam under real conditions",
        "goal": "Score 80%+ on a full mock exam, then close every gap.",
        "tasks": [
            {"type": "mock", "title": "Mock Exam #1: 100 questions, 2 hours", "minutes": 120},
            {"type": "review", "title": "Review and retry every missed question", "minutes": 30},
            {"type": "quiz", "title": "Weak-spot drill (your two lowest sections)", "weak": True, "n": 25, "minutes": 25},
            {"type": "read", "title": "Re-read the 'Commonly confused pairs' on the cheat sheet", "minutes": 10, "href": "/cheatsheet"},
        ],
    },
    {
        "day": 7,
        "title": "Ready to pass",
        "focus": "Final mock exam and confidence check",
        "goal": "Pass a second mock exam at 80%+. If you do, you're ready.",
        "tasks": [
            {"type": "mock", "title": "Mock Exam #2: beat 80%", "minutes": 120},
            {"type": "review", "title": "Review every miss from the final mock", "minutes": 20},
            {"type": "quiz", "title": "Lightning round: 25 random questions", "sections": [], "n": 25, "minutes": 15},
            {"type": "read", "title": "Read the exam-day tips", "minutes": 10, "href": "/tips"},
            {"type": "read", "title": "Final pass through the Arizona cheat sheet", "minutes": 15, "href": "/cheatsheet"},
        ],
    },
]


def _build():
    for d in DAYS:
        for i, t in enumerate(d["tasks"]):
            t["id"] = f"d{d['day']}t{i + 1}"
            t.setdefault("sections", [])
            if t["type"] in ("quiz", "mock"):
                t.setdefault("target", PASS_TARGET)
            secs = ",".join(t["sections"])
            if t["type"] == "lessons":
                t["href"] = f"/study/{t['sections'][0]}"
            elif t["type"] == "quiz":
                if t.get("weak"):
                    t["href"] = f"/quiz?mode=weak&n={t['n']}&task={t['id']}&target={t['target']}"
                else:
                    mode = t.get("mode", "practice")
                    t["href"] = f"/quiz?mode={mode}&n={t['n']}&sections={secs}&task={t['id']}&target={t['target']}"
            elif t["type"] == "cards":
                t["href"] = f"/flashcards?section={secs}&filter=all&task={t['id']}"
            elif t["type"] == "mock":
                t["href"] = f"/exam/start?task={t['id']}&target={t['target']}"
            elif t["type"] == "review":
                t["href"] = f"/quiz?mode=practice&source=missed&n=0&task={t['id']}&target=0"
    return DAYS


BOOTCAMP = _build()
