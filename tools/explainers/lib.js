/* Shared helpers for explainer animations. Each video defines DURATION, CAPS and scene(t). */
const $ = id => document.getElementById(id);
const clamp = x => Math.max(0, Math.min(1, x));
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const easeOut = x => 1 - Math.pow(1 - x, 3);
const seg = (t, a, b) => ease(clamp((t - a) / (b - a)));
const segO = (t, a, b) => easeOut(clamp((t - a) / (b - a)));
const win = (t, a, b, f = .6) => Math.min(seg(t, a, a + f), 1 - seg(t, b - f, b));
const money = n => "$" + Math.round(n).toLocaleString("en-US");
const lerp = (a, b, p) => a + (b - a) * p;

function pop(el, t, a, dy = 30) {
  if (typeof el === "string") el = $(el);
  const p = segO(t, a, a + .6);
  el.style.opacity = p;
  el.style.transform = `translateY(${(1 - p) * dy}px)`;
  return p;
}
function popX(el, t, a, dx = 40) {
  if (typeof el === "string") el = $(el);
  const p = segO(t, a, a + .6);
  el.style.opacity = p;
  el.style.transform = `translateX(${(1 - p) * dx}px)`;
  return p;
}
function popS(el, t, a) {
  if (typeof el === "string") el = $(el);
  const p = segO(t, a, a + .5);
  el.style.opacity = p;
  el.style.transform = `scale(${.85 + .15 * p})`;
  return p;
}
function show(el, v) { if (typeof el === "string") el = $(el); el.style.opacity = v; }
function sceneWin(id, t, a, b, f) { $(id).style.opacity = win(t, a, b, f); }

/* SVG path drawing */
function prepPaths() {
  document.querySelectorAll("path.ln, line.ln, polyline.ln").forEach(p => {
    const L = p.getTotalLength();
    p.style.strokeDasharray = L;
    p.dataset.len = L;
    p.style.strokeDashoffset = L;
  });
}
function draw(el, t, a, b) {
  if (typeof el === "string") el = $(el);
  const L = +el.dataset.len, d = seg(t, a, b);
  el.style.strokeDashoffset = L * (1 - d);
  el.style.opacity = d > 0 ? 1 : 0;
}

/* Narration support.
   tools/sync.py injects window.TIMELINE = {duration, anchors: [[narratedTime, originalTime], ...]}.
   warp() maps narrated time back to the original silent timeline: between two anchors the
   original plays at normal speed, then holds on the settled frame while the narrator is still
   talking, and the final second before the next anchor (scene fades, set-up moves) plays just
   before the next cue. If the narration is faster than the original, that stretch speeds up. */
const TL = window.TIMELINE || null;
const LEAD_IN = 1.0;
function warp(t) {
  const A = TL.anchors;
  if (t <= A[0][0]) return A[0][1];
  for (let i = 0; i < A.length - 1; i++) {
    const [n0, o0] = A[i], [n1, o1] = A[i + 1];
    if (t > n1) continue;
    const dn = n1 - n0, dO = o1 - o0;
    if (dn <= dO || dO <= LEAD_IN) return o0 + (t - n0) * (dO / Math.max(dn, 1e-6));
    const k = t - n0;
    if (k <= dO - LEAD_IN) return o0 + k;          // play
    if (t >= n1 - LEAD_IN) return o1 - (n1 - t);    // lead-in to the next cue
    return o1 - LEAD_IN;                            // hold
  }
  return A[A.length - 1][1] + (t - A[A.length - 1][0]);
}

/* Chrome: brand, note, progress, captions */
function chrome(t, tw) {
  const total = TL ? TL.duration : DURATION;
  $("prog").style.width = (t / total * 100) + "%";
  const out = 1 - seg(t, total - 1.5, total);
  $("brand").style.opacity = out;
  if ($("note")) $("note").style.opacity = (window.NOTE_WIN ? win(tw, NOTE_WIN[0], NOTE_WIN[1]) : 0) * out;
  const cap = $("cap");
  // Narrated videos use subtitles instead of burned-in captions.
  const c = TL ? null : (window.CAPS || []).find(([a, b]) => tw >= a - .4 && tw <= b + .4);
  if (c) { cap.innerHTML = c[2]; cap.style.opacity = win(tw, c[0] - .4, c[1] + .4, .4); }
  else cap.style.opacity = 0;
}

window.render = function (t) { const tw = TL ? warp(t) : t; chrome(t, tw); scene(tw); };
window.addEventListener("load", () => { prepPaths(); render(0); });
