/* Progress storage (browser localStorage) and shared helpers. */
(function () {
  const KEY = "azlife_progress_v1";

  const blank = () => ({
    answers: {},      // qid -> {r: right count, w: wrong count, last: bool, t: timestamp}
    lessons: {},      // "sid:index" -> true
    cards: {},        // cardId -> box (1-5)
    cardDue: {},      // cardId -> timestamp when due
    exams: [],        // {date, score, correct, total, seconds, bySection:{sid:[right,total]}}
    quizzes: 0,
    days: [],         // ISO dates studied
    flagged: {},      // qid -> true (saved for later)
    boot: null,       // {start: ISO date, examDate: "YYYY-MM-DD"|null, tasks: {taskId: {best, last, date, manual}}}
  });

  let mem = null;
  function load() {
    if (mem) return mem;
    try {
      const raw = localStorage.getItem(KEY);
      mem = Object.assign(blank(), raw ? JSON.parse(raw) : {});
    } catch (e) {
      mem = blank();
    }
    return mem;
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(mem)); } catch (e) { /* storage unavailable */ }
  }
  function today() {
    const d = new Date();
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }
  function touchDay() {
    const s = load();
    const t = today();
    if (!s.days.includes(t)) { s.days.push(t); save(); }
  }

  const Store = {
    get: load,
    save,
    touchDay,
    reset() { mem = blank(); save(); },

    recordAnswer(qid, correct) {
      const s = load();
      const a = s.answers[qid] || { r: 0, w: 0 };
      correct ? a.r++ : a.w++;
      a.last = correct;
      a.t = Date.now();
      s.answers[qid] = a;
      touchDay();
      save();
    },
    toggleFlag(qid) {
      const s = load();
      if (s.flagged[qid]) delete s.flagged[qid]; else s.flagged[qid] = true;
      save();
      return !!s.flagged[qid];
    },
    markLesson(sid, i, done) {
      const s = load();
      const k = sid + ":" + i;
      if (done) s.lessons[k] = true; else delete s.lessons[k];
      touchDay();
      save();
    },
    lessonDone(sid, i) { return !!load().lessons[sid + ":" + i]; },

    // Leitner spaced repetition: box 1 = daily ... box 5 = mastered
    gradeCard(id, knew) {
      const s = load();
      const box = s.cards[id] || 1;
      const nb = knew ? Math.min(5, box + 1) : 1;
      const days = [0, 0, 1, 3, 7, 14][nb];
      s.cards[id] = nb;
      s.cardDue[id] = Date.now() + days * 86400000;
      touchDay();
      save();
    },

    addExam(result) {
      const s = load();
      s.exams.push(result);
      touchDay();
      save();
    },

    /* --- Bootcamp --- */
    startBoot(examDate) {
      const s = load();
      s.boot = { start: today(), examDate: examDate || null, tasks: (s.boot && s.boot.tasks) || {} };
      save();
    },
    setExamDate(d) { const s = load(); if (!s.boot) Store.startBoot(d); else { s.boot.examDate = d || null; save(); } },
    resetBoot() { const s = load(); s.boot = null; save(); },
    recordTask(id, score, manual) {
      const s = load();
      if (!s.boot) s.boot = { start: today(), examDate: null, tasks: {} };
      const t = s.boot.tasks[id] || { best: null };
      if (manual === false) { delete s.boot.tasks[id]; save(); return; }
      t.last = score;
      t.best = score === null || score === undefined ? t.best : Math.max(t.best ?? -1, score);
      t.date = Date.now();
      if (manual) t.manual = true;
      s.boot.tasks[id] = t;
      touchDay();
      save();
    },
    today,

    /* --- Stats --- */
    sectionStats(questions) {
      const s = load();
      const out = {};
      (window.SECTIONS || []).forEach(sec => out[sec.id] = { seen: 0, total: 0, right: 0, wrong: 0, mastered: 0 });
      questions.forEach(q => {
        const o = out[q.section];
        if (!o) return;
        o.total++;
        const a = s.answers[q.id];
        if (a) {
          o.seen++;
          o.right += a.r;
          o.wrong += a.w;
          if (a.last) o.mastered++;
        }
      });
      Object.values(out).forEach(o => {
        const tries = o.right + o.wrong;
        o.acc = tries ? Math.round((o.right / tries) * 100) : null;
      });
      return out;
    },

    // Readiness = exam-weighted accuracy, scaled by how much of the bank you've covered.
    readiness(questions) {
      const stats = Store.sectionStats(questions);
      let num = 0, wsum = 0, seen = 0, total = 0;
      (window.SECTIONS || []).forEach(sec => {
        const o = stats[sec.id];
        seen += o.seen; total += o.total;
        if (o.acc !== null) { num += o.acc * sec.weight; wsum += sec.weight; }
      });
      if (!wsum) return { score: 0, accuracy: null, coverage: 0 };
      const accuracy = num / wsum;
      const coverage = total ? seen / total : 0;
      const confidence = Math.min(1, coverage / 0.6); // full confidence after ~60% of the bank
      return {
        score: Math.round(accuracy * confidence),
        accuracy: Math.round(accuracy),
        coverage: Math.round(coverage * 100),
      };
    },

    streak() {
      const days = new Set(load().days);
      let n = 0;
      const d = new Date();
      // allow today not yet studied
      const key = x => x.getFullYear() + "-" + String(x.getMonth() + 1).padStart(2, "0") + "-" + String(x.getDate()).padStart(2, "0");
      if (!days.has(key(d))) d.setDate(d.getDate() - 1);
      while (days.has(key(d))) { n++; d.setDate(d.getDate() - 1); }
      return n;
    },
  };

  /* Utilities */
  Store.shuffle = function (arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };
  Store.sectionTitle = function (id) {
    const s = (window.SECTIONS || []).find(x => x.id === id);
    return s ? s.title : id;
  };
  Store.esc = function (t) {
    const d = document.createElement("div");
    d.textContent = t;
    return d.innerHTML;
  };

  window.Store = Store;
})();
