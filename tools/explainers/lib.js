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

/* Chrome: brand, note, progress, captions */
function chrome(t) {
  $("prog").style.width = (t / DURATION * 100) + "%";
  const out = 1 - seg(t, DURATION - 1.5, DURATION);
  $("brand").style.opacity = out;
  if ($("note")) $("note").style.opacity = (window.NOTE_WIN ? win(t, NOTE_WIN[0], NOTE_WIN[1]) : 0) * out;
  const cap = $("cap");
  const c = (window.CAPS || []).find(([a, b]) => t >= a - .4 && t <= b + .4);
  if (c) { cap.innerHTML = c[2]; cap.style.opacity = win(t, c[0] - .4, c[1] + .4, .4); }
  else cap.style.opacity = 0;
}

window.render = function (t) { chrome(t); scene(t); };
window.addEventListener("load", () => { prepPaths(); render(0); });
