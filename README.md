# AZ Life Exam Prep

A study site for the Arizona Life Insurance Producer exam (Series 13-31): 100 questions, 2 hours, 70% to pass.

## Features

- **Study guide**: 30 lessons across the 7 official exam sections, each with key facts to memorize
- **Practice quizzes**: 248 questions with explanations. Pick topics, question count and mode (practice, test or timed)
- **Mock exam**: 100 questions weighted like the real exam, 2-hour timer, flagging, question navigator, section breakdown
- **Flashcards**: 124 cards with spaced repetition
- **Review**: missed and saved questions, weak-spot drills
- **Cheat sheet, glossary, exam-day tips, question of the day**
- **Progress dashboard**: readiness score, accuracy by section, streak, mock exam history (saved in the browser)

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
