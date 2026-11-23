# AZ Life Exam Prep

A study site for the Arizona Life Insurance Producer exam (Series 13-31): 100 questions, 2 hours, 70% to pass.

## Features

- **7-Day Pass Plan**: a guided bootcamp with daily tasks, 80% pass gates on quizzes, two mock exams, an exam-date countdown and a readiness checklist
- **Today's mission**: the dashboard always points to your next task
- **Lesson checkpoints**: 70 check questions after the lessons that complete each lesson when you pass
- **Study guide**: 30 lessons across the 7 official exam sections, each with key facts to memorize
- **Practice quizzes**: 318 questions with explanations. Pick topics, question count and mode (practice, test or timed)
- **Mock exam**: 100 questions weighted like the real exam, 2-hour timer, flagging, question navigator, section breakdown
- **Flashcards**: 124 cards with spaced repetition
- **Review**: missed and saved questions, weak-spot drills
- **Cheat sheet, glossary, exam-day tips, question of the day**
- **Progress dashboard**: readiness score, accuracy by section, streak, mock exam history (saved in the browser)

## Accounts

Users can register and log in; progress syncs across devices. Data lives in `data/app.db` (SQLite) and the session key in `data/secret_key`. Both are created automatically, git-ignored, and untouched by `git pull`. Back up `data/` to keep accounts.

## Run locally

```bash
pip install flask
python flask_app.py
```

## Deploy on PythonAnywhere

```bash
cd ~/mysite && git pull
```

Then click **Reload** on the Web tab.

## Editing content

- Lessons: `content/lessons.py`
- Questions: `content/questions.py` (write the correct answer first; choices are shuffled automatically)
- Flashcards: `content/flashcards.py`
- Lesson checkpoints: `content/checks.py`
- 7-day plan: `content/bootcamp.py`
