/* 7-Day Bootcamp: task status, current day and "next best action". */
(function () {
  const B = {};
  const PLAN = () => window.BOOTCAMP || [];

  function lessonsDone(sid) {
    const m = SECTIONS.find(x => x.id === sid);
    if (!m) return true;
    for (let i = 0; i < m.lessons; i++) if (!Store.lessonDone(sid, i)) return false;
    return true;
  }

  /* Returns {done: bool, detail: string} */
  B.status = function (t) {
    const s = Store.get();
    const rec0 = s.boot && s.boot.tasks && s.boot.tasks[t.id];
    const rec = rec0 && !rec0.removed ? rec0 : null;
    switch (t.type) {
      case "lessons": {
        const m = SECTIONS.find(x => x.id === t.sections[0]);
        let n = 0;
        for (let i = 0; i < m.lessons; i++) if (Store.lessonDone(m.id, i)) n++;
        return { done: t.sections.every(lessonsDone), detail: n + "/" + m.lessons + " lessons" };
      }
      case "quiz":
      case "mock": {
        if (!rec || rec.best === null) return { done: false, detail: "Target " + t.target + "%" };
        const ok = rec.best >= t.target;
        return { done: ok, detail: (ok ? "Best " : "Best so far ") + rec.best + "% · need " + t.target + "%" , tried: true };
      }
      case "cards": {
        const pool = (window.CMETA || []).filter(c => t.sections.includes(c.section));
        const seen = pool.filter(c => s.cards[c.id]).length;
        return { done: pool.length > 0 && seen === pool.length, detail: seen + "/" + pool.length + " cards reviewed" };
      }
      case "review": {
        const missed = Object.values(s.answers).filter(a => a.last === false).length;
        if (rec) return { done: true, detail: "Done" };
        if (Object.keys(s.answers).length && !missed) return { done: true, detail: "Nothing missed 👏" };
        return { done: false, detail: missed + " missed question" + (missed === 1 ? "" : "s") + " to fix" };
      }
      case "read":
        return { done: !!rec, detail: rec ? "Done" : "Check off when finished" };
    }
    return { done: false, detail: "" };
  };

  B.dayProgress = function (d) {
    const st = d.tasks.map(B.status);
    const done = st.filter(x => x.done).length;
    return { done, total: d.tasks.length, complete: done === d.tasks.length,
      minutesLeft: d.tasks.reduce((m, t, i) => m + (st[i].done ? 0 : t.minutes), 0) };
  };

  B.overall = function () {
    let done = 0, total = 0;
    PLAN().forEach(d => { const p = B.dayProgress(d); done += p.done; total += p.total; });
    return { done, total, pct: total ? Math.round(done / total * 100) : 0 };
  };

  /* First day with unfinished work (or the last day if everything's done) */
  B.currentDay = function () {
    const plan = PLAN();
    return plan.find(d => !B.dayProgress(d).complete) || plan[plan.length - 1];
  };

  B.nextTask = function () {
    const d = B.currentDay();
    if (!d) return null;
    const t = d.tasks.find(t => !B.status(t).done);
    return t ? { day: d, task: t } : null;
  };

  B.started = () => !!Store.get().boot;

  B.calendarDay = function () {
    const b = Store.get().boot;
    if (!b) return 1;
    const start = new Date(b.start + "T00:00:00");
    const now = new Date(Store.today() + "T00:00:00");
    return Math.floor((now - start) / 86400000) + 1;
  };

  B.daysToExam = function () {
    const b = Store.get().boot;
    if (!b || !b.examDate) return null;
    const ex = new Date(b.examDate + "T00:00:00");
    const now = new Date(Store.today() + "T00:00:00");
    return Math.round((ex - now) / 86400000);
  };

  B.icon = { lessons: "📖", quiz: "✍️", cards: "🃏", mock: "⏱", review: "🔁", read: "👀" };
  B.verb = { lessons: "Study", quiz: "Start quiz", cards: "Review cards", mock: "Start exam", review: "Start review", read: "Open" };

  /* Lesson tasks jump straight to the first unfinished lesson */
  B.href = function (t) {
    if (t.type !== "lessons") return t.href;
    const m = SECTIONS.find(x => x.id === t.sections[0]);
    for (let i = 0; i < m.lessons; i++) if (!Store.lessonDone(m.id, i)) return "/study/" + m.id + "#l" + i;
    return t.href;
  };

  B.findTask = function (id) {
    for (const d of PLAN()) for (const t of d.tasks) if (t.id === id) return { day: d, task: t };
    return null;
  };

  window.Bootcamp = B;
})();
