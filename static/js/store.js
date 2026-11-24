/* Progress storage: localStorage, synced to the server when logged in. */
(function () {
  const USER = window.USER || null;
  const ANON_KEY = "azlife_progress_v1";
  const KEY = USER ? "azlife_progress_v1_u_" + USER.username.toLowerCase() : ANON_KEY;

  const blank = () => ({
    answers: {},      // qid -> {r: right count, w: wrong count, last: bool, t: timestamp}
    lessons: {},      // "sid:index" -> signed timestamp (+ done, - not done)
    cards: {},        // cardId -> box (1-5)
    cardDue: {},      // cardId -> timestamp when due
    exams: [],        // {date, score, correct, total, seconds, bySection:{sid:[right,total]}}
    quizzes: 0,
    days: [],         // ISO dates studied
    flagged: {},      // qid -> signed timestamp (+ saved, - unsaved)
    watched: {},      // video slug -> timestamp watched
    boot: null,       // {start, examDate, tasks: {taskId: {best, last, date, manual, removed}}}
    bootTs: 0,        // last change to the plan
    resetAt: 0,
    updated: 0,
  });

  function readLocal(key) {
    try { const raw = localStorage.getItem(key); return raw ? JSON.parse(raw) : null; } catch (e) { return null; }
  }
  function writeLocal() {
    try { localStorage.setItem(KEY, JSON.stringify(mem)); } catch (e) { /* storage unavailable */ }
  }
  const hasProgress = d => d && (Object.keys(d.answers || {}).length || Object.keys(d.lessons || {}).length ||
    Object.keys(d.cards || {}).length || (d.exams || []).length || d.boot);

  let mem = null, version = 0, timer = null, inflight = false, needsReload = false, importedAnon = false;

  function load() {
    if (mem) return mem;
    let data;
    if (USER) {
      const local = readLocal(KEY);
      const server = window.SERVER_PROGRESS;
      if (local && local._dirty) data = local;                    // unsynced changes on this device
      else if (server) data = server;
      else if (local) data = local;
      if (!readLocal(KEY)) {                                      // first login on this device:
        const anon = readLocal(ANON_KEY);                         // bring this browser's guest progress along
        if (hasProgress(anon)) { data = anon; data._dirty = true; needsReload = !!server; importedAnon = true; }
      }
    } else {
      data = readLocal(ANON_KEY);
    }
    mem = Object.assign(blank(), data || {});
    if (USER) {
      writeLocal();
      if (mem._dirty) setTimeout(sync, 0);
    }
    return mem;
  }

  function save() {
    const s = load();
    s.updated = Date.now();
    if (USER) { s._dirty = true; version++; }
    writeLocal();
    if (USER) { clearTimeout(timer); timer = setTimeout(sync, 1200); }
  }

  function setStatus(t) {
    const el = document.getElementById("sync-status");
    if (el) { el.textContent = t; el.dataset.state = t; }
  }

  async function sync(keepalive) {
    if (!USER || !mem || !mem._dirty) return;
    if (inflight && !keepalive) { clearTimeout(timer); timer = setTimeout(sync, 800); return; }
    inflight = true;
    const sent = version;
    const body = Object.assign({}, mem); delete body._dirty;
    setStatus("Saving…");
    try {
      const res = await fetch("/api/progress", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body), credentials: "same-origin", keepalive: !!keepalive,
      });
      if (res.status === 401) { setStatus("Logged out"); return; }
      if (!res.ok) throw new Error(res.status);
      const merged = await res.json();
      if (version === sent) {
        mem = Object.assign(blank(), merged);
        mem._dirty = false;
        writeLocal();
        setStatus("Saved");
        if (importedAnon) { importedAnon = false; try { localStorage.removeItem(ANON_KEY); } catch (e) {} }
        if (needsReload) { needsReload = false; location.reload(); }
      } else {
        timer = setTimeout(sync, 300);   // more changes came in while saving; send again
      }
    } catch (e) {
      setStatus("Offline: will retry");
      clearTimeout(timer); timer = setTimeout(sync, 15000);
    } finally {
      inflight = false;
    }
  }
  window.addEventListener("pagehide", () => { if (mem && mem._dirty) sync(true); });
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden" && mem && mem._dirty) sync(true); });

  function today() {
    const d = new Date();
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }
  function touchDay() {
    const s = load();
    const t = today();
    if (!s.days.includes(t)) s.days.push(t);
  }
  function touchBoot() { load().bootTs = Date.now(); }

  const Store = {
    get: load,
    save,
    touchDay() { touchDay(); save(); },
    user: USER,
    async reset() {
      const stamp = Date.now();
      if (USER) {
        try {
          await fetch("/api/progress/reset", { method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ resetAt: stamp }), credentials: "same-origin" });
        } catch (e) { /* the reset marker below still wins on next sync */ }
      }
      mem = Object.assign(blank(), { resetAt: stamp, updated: stamp });
      writeLocal();
    },

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
    isFlagged(qid) { const v = load().flagged[qid]; return v === true || v > 0; },
    toggleFlag(qid) {
      const on = !Store.isFlagged(qid);
      load().flagged[qid] = on ? Date.now() : -Date.now();
      save();
      return on;
    },
    markLesson(sid, i, done) {
      load().lessons[sid + ":" + i] = done ? Date.now() : -Date.now();
      touchDay();
      save();
    },
    isWatched(slug) { return (load().watched || {})[slug] > 0; },
    markWatched(slug) {
      const s = load();
      if (!s.watched) s.watched = {};
      if (s.watched[slug] > 0) return;
      s.watched[slug] = Date.now();
      touchDay();
      save();
    },
    lessonDone(sid, i) { const v = load().lessons[sid + ":" + i]; return v === true || v > 0; },

    // Leitner spaced repetition. Box 1 = missed (review tomorrow), 2-4 = known,
    // 5 = mastered. A new card you know right away starts at box 3.
    gradeCard(id, knew) {
      const s = load();
      const box = s.cards[id] || 0;
      const nb = !knew ? 1 : box === 0 ? 3 : Math.min(5, box + 1);
      const days = [0, 0, 1, 3, 7, 14][nb];
      s.cards[id] = nb;
      s.cardDue[id] = Date.now() + days * 86400000;
      touchDay();
      save();
    },

    addExam(result) {
      load().exams.push(result);
      touchDay();
      save();
    },

    /* --- Bootcamp --- */
    startBoot(examDate) {
      const s = load();
      s.boot = { start: today(), examDate: examDate || null, tasks: {} };
      touchBoot();
      save();
    },
    setExamDate(d) {
      const s = load();
      if (!s.boot) return Store.startBoot(d);
      s.boot.examDate = d || null;
      touchBoot();
      save();
    },
    resetBoot() { load().boot = null; touchBoot(); save(); },
    recordTask(id, score, manual) {
      const s = load();
      if (!s.boot) s.boot = { start: today(), examDate: null, tasks: {} };
      if (!s.boot.tasks) s.boot.tasks = {};
      if (manual === false) {
        s.boot.tasks[id] = { removed: true, best: null, date: Date.now() };
      } else {
        const prev = s.boot.tasks[id];
        const t = prev && !prev.removed ? prev : { best: null };
        t.last = score;
        if (score !== null && score !== undefined) t.best = Math.max(t.best ?? -1, score);
        t.date = Date.now();
        if (manual) t.manual = true;
        delete t.removed;
        s.boot.tasks[id] = t;
        touchDay();
      }
      touchBoot();
      save();
    },
    today,
    flush() { return sync(); },

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

/* Mark a video watched once 90% has played. */
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("video[data-slug]").forEach(v => {
    const slug = v.dataset.slug;
    const tag = v.closest("figure") && v.closest("figure").querySelector(".watched-tag");
    if (tag && Store.isWatched(slug)) tag.hidden = false;
    v.addEventListener("timeupdate", () => {
      if (v.duration && v.currentTime / v.duration >= .9 && !Store.isWatched(slug)) {
        Store.markWatched(slug);
        if (tag) tag.hidden = false;
      }
    });
  });
});

/* Subtitles toggle and playback speed (works the same on iPhone, Android and desktop). */
document.addEventListener("DOMContentLoaded", () => {
  const SPEEDS = [1, 1.25, 1.5, 1.75, 0.75];
  let ccOn = false, speed = 1;
  try { ccOn = localStorage.getItem("azlife_cc") === "1"; speed = parseFloat(localStorage.getItem("azlife_speed")) || 1; } catch (e) {}
  const videos = () => document.querySelectorAll("video[data-slug]");
  function apply() {
    videos().forEach(v => {
      v.playbackRate = speed;
      v.defaultPlaybackRate = speed;
      if (v.textTracks && v.textTracks[0]) v.textTracks[0].mode = ccOn ? "showing" : "hidden";
    });
    document.querySelectorAll("[data-cc]").forEach(b => b.setAttribute("aria-pressed", ccOn ? "true" : "false"));
    document.querySelectorAll("[data-speed]").forEach(b => b.textContent = speed + "×");
  }
  document.querySelectorAll("[data-cc]").forEach(b => b.addEventListener("click", () => {
    ccOn = !ccOn; try { localStorage.setItem("azlife_cc", ccOn ? "1" : "0"); } catch (e) {} apply();
  }));
  document.querySelectorAll("[data-speed]").forEach(b => b.addEventListener("click", () => {
    speed = SPEEDS[(SPEEDS.indexOf(speed) + 1) % SPEEDS.length]; try { localStorage.setItem("azlife_speed", speed); } catch (e) {} apply();
  }));
  videos().forEach(v => v.addEventListener("loadedmetadata", apply));
  apply();
});
