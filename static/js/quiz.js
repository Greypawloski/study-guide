/* Quiz and mock exam engine. */
(function () {
  const root = document.getElementById("quiz-app");
  const PAGE = root.dataset.mode;               // quiz | exam | daily
  const params = new URLSearchParams(location.search);
  const ALL = window.QUESTIONS;
  const $ = id => document.getElementById(id);

  /* ---------- Build the question set ---------- */
  let feedback = "instant";   // instant | end
  let seconds = 0;            // 0 = untimed
  let label = "Practice quiz";
  let set = [];

  function pick(pool, n) { return Store.shuffle(pool).slice(0, n || pool.length); }

  if (PAGE === "exam") {
    label = "Mock Exam · Arizona Life Producer";
    feedback = "end";
    seconds = 120 * 60;
    SECTIONS.forEach(sec => {
      set = set.concat(pick(ALL.filter(q => q.section === sec.id), sec.weight));
    });
    set = Store.shuffle(set);
  } else if (PAGE === "daily") {
    label = "Question of the day";
    set = ALL.slice();
  } else {
    const mode = params.get("mode") || "practice";
    const n = parseInt(params.get("n") || "10", 10);
    const secs = (params.get("sections") || "").split(",").filter(Boolean);
    const source = params.get("source") || "all";
    const s = Store.get();
    let pool = ALL.filter(q => !secs.length || secs.includes(q.section));

    if (mode === "weak") {
      label = "Weak-spot drill";
      const missed = pool.filter(q => s.answers[q.id] && s.answers[q.id].last === false);
      const stats = Store.sectionStats(ALL);
      const ranked = SECTIONS.slice().sort((a, b) => (stats[a.id].acc ?? 101) - (stats[b.id].acc ?? 101));
      const weakIds = ranked.slice(0, 2).map(x => x.id);
      const fill = pool.filter(q => weakIds.includes(q.section) && !(s.answers[q.id] && s.answers[q.id].last));
      const seen = new Set();
      set = Store.shuffle(missed).concat(Store.shuffle(fill)).filter(q => !seen.has(q.id) && seen.add(q.id)).slice(0, n);
      if (set.length < n) set = set.concat(pick(pool.filter(q => !seen.has(q.id)), n - set.length));
    } else {
      if (source === "unseen") pool = pool.filter(q => !s.answers[q.id]);
      if (source === "missed") pool = pool.filter(q => s.answers[q.id] && s.answers[q.id].last === false);
      if (source === "flagged") pool = pool.filter(q => Store.isFlagged(q.id));
      set = pick(pool, n);
      if (mode === "test" || mode === "timed") feedback = "end";
      if (mode === "timed") seconds = set.length * 72;
      label = (mode === "practice" ? "Practice" : mode === "timed" ? "Timed test" : "Test") +
        (secs.length === 1 ? " · " + Store.sectionTitle(secs[0]) : secs.length && secs.length < SECTIONS.length ? " · " + secs.length + " sections" : " · All sections");
    }
  }

  const TASK = params.get("task");
  const TARGET = parseInt(params.get("target") || "0", 10);

  if (!set.length) {
    if (TASK) {
      Store.recordTask(TASK, 100);
      $("question-card").innerHTML = '<h2>Nothing to review 👏</h2><p class="muted">You have no missed questions right now, so this task is complete.</p><a class="btn primary" href="/bootcamp">Back to my plan →</a>';
    } else
    $("question-card").innerHTML = '<h2>No questions match</h2><p class="muted">There are no questions for that filter yet. For example, "Missed" only shows questions you\'ve answered wrong.</p><a class="btn primary" href="/practice">Back to practice</a>';
    $("quiz-label").textContent = label;
    return;
  }

  /* Each item: question + shuffled choice order + user answer */
  const items = set.map(q => ({ q, order: Store.shuffle(q.choices.map((_, i) => i)), pick: null, checked: false, flag: false }));
  let cur = 0, finished = false, timerId = null, startTime = Date.now();
  const exam = feedback === "end";

  /* ---------- Rendering ---------- */
  function render() {
    const it = items[cur];
    $("quiz-label").textContent = label + " · Question " + (cur + 1) + " of " + items.length;
    $("quiz-progress").style.width = ((exam ? items.filter(x => x.pick !== null).length : cur + (it.checked ? 1 : 0)) / items.length * 100) + "%";
    $("q-section").textContent = Store.sectionTitle(it.q.section);
    $("q-text").textContent = it.q.q;
    const flagged = exam ? it.flag : Store.isFlagged(it.q.id);
    $("flag-btn").innerHTML = (flagged ? "★" : "☆") + " <span>" + (exam ? (flagged ? "Flagged" : "Flag") : (flagged ? "Saved" : "Save")) + "</span>";
    $("flag-btn").classList.toggle("on", flagged);

    const box = $("choices");
    box.innerHTML = "";
    it.order.forEach((ci, idx) => {
      const b = document.createElement("button");
      b.className = "choice";
      b.innerHTML = '<span class="letter">' + "ABCD"[idx] + "</span><span>" + Store.esc(it.q.choices[ci]) + "</span>";
      if (it.pick === ci) b.classList.add("picked");
      if (it.checked) {
        b.disabled = true;
        if (ci === it.q.answer) b.classList.add("correct");
        else if (it.pick === ci) b.classList.add("wrong");
      }
      b.onclick = () => choose(ci);
      box.appendChild(b);
    });

    const ex = $("explain");
    if (it.checked) {
      const ok = it.pick === it.q.answer;
      ex.hidden = false;
      ex.className = "explain " + (ok ? "ok" : "bad");
      ex.innerHTML = "<strong>" + (ok ? "Correct!" : "Not quite.") + "</strong> " +
        (ok ? "" : "The answer is <em>" + Store.esc(it.q.choices[it.q.answer]) + "</em>. ") + Store.esc(it.q.explain);
    } else ex.hidden = true;

    $("prev-btn").style.visibility = cur > 0 ? "visible" : "hidden";
    const last = cur === items.length - 1;
    if (exam) $("next-btn").textContent = last ? "Review & submit" : "Next →";
    else $("next-btn").textContent = !it.checked ? "Check answer" : last ? "See results" : "Next →";
    $("next-btn").disabled = !exam && !it.checked && it.pick === null;
    if (exam) drawNav();
  }

  function choose(ci) {
    const it = items[cur];
    if (it.checked || finished) return;
    it.pick = ci;
    if (!exam) {   // instant feedback
      it.checked = true;
      Store.recordAnswer(it.q.id, ci === it.q.answer);
    }
    render();
  }

  function next() {
    const it = items[cur];
    if (!exam && !it.checked) { if (it.pick !== null) choose(it.pick); return; }
    if (cur < items.length - 1) { cur++; render(); window.scrollTo({ top: 0, behavior: "smooth" }); }
    else if (exam) confirmSubmit();
    else finish();
  }

  /* ---------- Exam navigator ---------- */
  function drawNav() {
    const nav = $("qnav");
    nav.innerHTML = '<div class="qnav-legend"><span><i class="a"></i>Answered</span><span><i class="f"></i>Flagged</span><span><i class="u"></i>Unanswered</span></div><div class="qnav-grid">' +
      items.map((x, i) => '<button data-i="' + i + '" class="' + (x.pick !== null ? "a " : "") + (x.flag ? "f " : "") + (i === cur ? "cur" : "") + '">' + (i + 1) + "</button>").join("") + "</div>";
    nav.querySelectorAll("button[data-i]").forEach(b => b.onclick = () => { cur = +b.dataset.i; render(); });
  }

  function confirmSubmit(auto) {
    if (auto) return finish();
    const un = items.filter(x => x.pick === null).length;
    const fl = items.filter(x => x.flag).length;
    $("modal-title").textContent = "Submit your answers?";
    $("modal-body").textContent = (un ? un + " unanswered question" + (un > 1 ? "s" : "") + " will be marked wrong. " : "All questions answered. ") +
      (fl ? fl + " still flagged for review." : "");
    $("modal").hidden = false;
  }

  /* ---------- Timer ---------- */
  function startTimer() {
    if (!seconds) return;
    $("timer").hidden = false;
    const end = Date.now() + seconds * 1000;
    const tick = () => {
      const left = Math.max(0, Math.round((end - Date.now()) / 1000));
      const h = Math.floor(left / 3600), m = Math.floor(left % 3600 / 60), s = left % 60;
      $("timer-val").textContent = (h ? h + ":" + String(m).padStart(2, "0") : m) + ":" + String(s).padStart(2, "0");
      $("timer").classList.toggle("warn", left <= 300);
      if (!left) { clearInterval(timerId); finish(true); }
    };
    tick();
    timerId = setInterval(tick, 1000);
  }

  /* ---------- Results ---------- */
  function finish(timedOut) {
    if (finished) return;
    finished = true;
    clearInterval(timerId);
    $("modal").hidden = true;
    const used = Math.round((Date.now() - startTime) / 1000);
    if (exam) items.forEach(it => { if (!it.checked) { it.checked = true; Store.recordAnswer(it.q.id, it.pick === it.q.answer); } });

    const right = items.filter(x => x.pick === x.q.answer).length;
    const pct = Math.round(right / items.length * 100);
    const bySection = {};
    items.forEach(x => {
      const b = bySection[x.q.section] || (bySection[x.q.section] = [0, 0]);
      b[1]++; if (x.pick === x.q.answer) b[0]++;
    });
    if (PAGE === "exam") Store.addExam({ date: new Date().toISOString(), score: pct, correct: right, total: items.length, seconds: used, bySection });
    else { const s = Store.get(); s.quizzes = (s.quizzes || 0) + 1; Store.save(); }
    let taskBanner = "";
    if (TASK) {
      Store.recordTask(TASK, pct);
      const ok = pct >= TARGET;
      const nx = Bootcamp.nextTask();
      taskBanner = '<div class="task-banner card ' + (ok ? "ok" : "bad") + '"><div><strong>' +
        (ok ? "✓ Plan task complete" : "Not there yet: you need " + TARGET + "% to check this off") + "</strong><p>" +
        (ok ? (nx ? "Up next: " + Store.esc(nx.task.title) + "." : "You've finished the whole plan!") :
          "Read the explanations below for every miss, then retake it. New questions are drawn each time.") + "</p></div>" +
        (ok && nx ? '<a class="btn primary" href="' + Bootcamp.href(nx.task) + '">' + Bootcamp.verb[nx.task.type] + " →</a>" :
          ok ? '<a class="btn primary" href="/bootcamp">My plan →</a>' : '<a class="btn primary" href="' + location.pathname + location.search + '">Retake now</a>') +
        "</div>";
    }

    $("question-card").hidden = true;
    $("qnav").hidden = true;
    $("nav-toggle").hidden = true;
    $("timer").hidden = true;
    $("quiz-progress").style.width = "100%";
    $("quiz-label").textContent = label + " · Results";

    const pass = pct >= 70;
    const mm = Math.floor(used / 60), ss = used % 60;
    const rows = SECTIONS.filter(s => bySection[s.id]).map(s => {
      const [r, t] = bySection[s.id], p = Math.round(r / t * 100);
      return '<tr><td>' + s.icon + " " + s.title + '</td><td>' + r + "/" + t + '</td><td><div class="bar"><span class="bar-fill ' + (p >= 80 ? "good" : p >= 70 ? "ok" : "low") + '" style="width:' + p + '%"></span></div></td><td class="num">' + p + '%</td><td><a href="/study/' + s.id + '">Study</a></td></tr>';
    }).join("");
    const wrongCount = items.length - right;

    $("results").innerHTML = taskBanner +
      '<div class="result-hero card ' + (pass ? "pass" : "fail") + '">' +
        '<div class="ring big" style="--p:' + pct + '"><div class="ring-inner"><strong>' + pct + '%</strong><span>' + right + "/" + items.length + "</span></div></div>" +
        "<div><h1>" + (PAGE === "daily" ? (pct ? "Nice work!" : "Good to know for next time.") : pass ? "Passing score! 🎉" : "Not passing yet") + "</h1>" +
        "<p>" + (timedOut ? "Time ran out. " : "") + (PAGE === "daily" ? "Come back tomorrow for a new question." :
          (pass ? "You'd pass the real exam (70% needed). " : "The real exam needs 70%. ") + "Time used: " + mm + "m " + ss + "s.") + "</p>" +
        '<div class="btn-row">' +
          (wrongCount ? '<a class="btn primary" href="/quiz?mode=practice&source=missed&n=0">Retry what I missed</a>' : "") +
          (PAGE === "exam" ? '<a class="btn" href="/exam/start">New mock exam</a>' : '<a class="btn" href="' + location.pathname + location.search + '">Try another set</a>') +
          '<a class="btn ghost" href="/">Dashboard</a></div></div></div>' +
      (PAGE !== "daily" ? '<div class="card"><h2>By section</h2><table class="sec-table">' + rows + "</table></div>" : "") +
      '<div class="card"><div class="review-head"><h2>Review answers</h2><label class="inline"><input type="checkbox" id="wrong-only" ' + (wrongCount ? "checked" : "") + "> Show only missed</label></div><div id=\"review-list\"></div></div>";
    $("results").hidden = false;

    const drawReview = () => {
      const only = $("wrong-only").checked;
      $("review-list").innerHTML = items.map((x, i) => {
        const ok = x.pick === x.q.answer;
        if (only && ok) return "";
        return '<div class="rev ' + (ok ? "ok" : "bad") + '"><p class="rev-q"><b>' + (i + 1) + ".</b> " + Store.esc(x.q.q) + "</p>" +
          (ok ? "" : '<p class="rev-your">Your answer: ' + (x.pick === null ? "<em>blank</em>" : Store.esc(x.q.choices[x.pick])) + "</p>") +
          '<p class="rev-right">✓ ' + Store.esc(x.q.choices[x.q.answer]) + '</p><p class="rev-ex">' + Store.esc(x.q.explain) + "</p></div>";
      }).join("") || '<p class="muted">Nothing missed. Perfect score!</p>';
    };
    $("wrong-only").onchange = drawReview;
    drawReview();
    window.scrollTo({ top: 0 });
  }

  /* ---------- Events ---------- */
  $("next-btn").onclick = next;
  $("prev-btn").onclick = () => { if (cur > 0) { cur--; render(); } };
  $("flag-btn").onclick = () => {
    const it = items[cur];
    if (exam) it.flag = !it.flag; else Store.toggleFlag(it.q.id);
    render();
  };
  $("modal-cancel").onclick = () => $("modal").hidden = true;
  $("modal-ok").onclick = () => finish();
  if (exam) {
    $("nav-toggle").hidden = false;
    $("nav-toggle").onclick = () => { $("qnav").hidden = !$("qnav").hidden; };
    window.addEventListener("beforeunload", e => { if (!finished) { e.preventDefault(); e.returnValue = ""; } });
  }
  document.addEventListener("keydown", e => {
    if (finished || !$("modal").hidden) return;
    const k = parseInt(e.key, 10);
    if (k >= 1 && k <= 4 && items[cur].order[k - 1] !== undefined) choose(items[cur].order[k - 1]);
    if (e.key === "Enter") { e.preventDefault(); next(); }
    if (e.key === "ArrowLeft" && cur > 0) { cur--; render(); }
    if (e.key === "ArrowRight" && exam && cur < items.length - 1) { cur++; render(); }
  });

  render();
  startTimer();
})();
