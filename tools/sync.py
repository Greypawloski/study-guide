#!/usr/bin/env python3
"""Build a narrated explainer video from cached narration audio.

  python3 tools/sync.py SLUG                 use the ElevenLabs audio in tools/explainers/audio/SLUG/
  python3 tools/sync.py SLUG --placeholder   use a free robot voice (espeak-ng) to test timing

Steps: read the script + per-segment audio and word timings → lay the segments
end to end and turn each cue phrase into a time → render the animation on that
timeline → mix the audio at the same times, level it to a consistent loudness →
mux into an MP4 and write matching WebVTT subtitles.

Output: tools/explainers/out/SLUG/{SLUG.mp4, SLUG.vtt, timeline.json}
Needs: python3, playwright + Chrome, ffmpeg (all available in the build workspace).
"""

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS / "explainers"
NARR, AUDIO, OUT = ROOT / "narration", ROOT / "audio", ROOT / "out"
PLACEHOLDER = ROOT / "audio_placeholder"

LEAD = 0.5          # silence before the first word
HOLD_AFTER_CUE = 2.2  # every cue's animation gets at least this long before the scene can change


def duration(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]).decode())


def placeholder_audio(slug, segs):
    """Free stand-in voice with evenly spaced character timings, for testing only."""
    out = PLACEHOLDER / slug
    out.mkdir(parents=True, exist_ok=True)
    for s in segs:
        wav, mp3 = out / f"{s['id']}.wav", out / f"{s['id']}.mp3"
        subprocess.run(["espeak-ng", "-s", "160", "-w", str(wav), s["text"]], check=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-ar", "44100", str(mp3)], check=True)
        wav.unlink()
        d = duration(mp3)
        n = len(s["text"])
        (out / f"{s['id']}.json").write_text(json.dumps({"fake": True, "text": s["text"], "alignment": {
            "characters": list(s["text"]),
            "character_start_times_seconds": [d * i / n for i in range(n)],
            "character_end_times_seconds": [d * (i + 1) / n for i in range(n)],
        }}))
    return out


def phrase_time(seg, meta, phrase):
    i = seg["text"].find(phrase)
    if i < 0:
        sys.exit(f"Cue phrase not found in segment '{seg['id']}': {phrase!r}")
    al = meta.get("alignment") or {}
    starts = al.get("character_start_times_seconds") or []
    chars = "".join(al.get("characters") or [])
    if chars != seg["text"]:           # alignment text differs slightly (normalization): search it directly
        j = chars.find(phrase)
        i = j if j >= 0 else round(i / max(1, len(seg["text"])) * len(chars))
    return starts[min(i, len(starts) - 1)] if starts else 0.0


def build_timeline(doc, cfg, adir):
    gap, tail = cfg.get("gap_seconds", .45), cfg.get("scene_tail_seconds", .6)
    t, cues, segs = LEAD, {}, []
    for s in doc["segments"]:
        meta = json.loads((adir / f"{s['id']}.json").read_text())
        mp3 = adir / f"{s['id']}.mp3"
        d = duration(mp3)
        start = t
        cues[s["id"]] = round(start - 0.25 if start > LEAD else 0, 3)   # scene arrives just before the first word
        last = start
        for name, phrase in s.get("cues", {}).items():
            ct = start + phrase_time(s, meta, phrase)
            cues[f"{s['id']}.{name}"] = round(ct, 3)
            last = max(last, ct)
        end = max(start + d + tail, last + HOLD_AFTER_CUE)
        segs.append({"id": s["id"], "start": start, "audio": str(mp3), "duration": d, "meta": meta, "text": s["text"]})
        t = end + gap
    total = round(t + 1.5, 3)
    cues["end"] = total
    return {"duration": total, "cues": cues}, segs


def write_vtt(segs, path, max_len=84):
    def ts(x):
        h, m, sec = int(x // 3600), int(x % 3600 // 60), x % 60
        return f"{h:02d}:{m:02d}:{sec:06.3f}"
    lines = ["WEBVTT", ""]
    cues = []
    for s in segs:
        text = s["text"]
        al = s["meta"].get("alignment") or {}
        st = al.get("character_start_times_seconds") or []
        en = al.get("character_end_times_seconds") or []
        chars = "".join(al.get("characters") or [])
        use_al = chars == text and st
        # split into sentences, then wrap long ones at commas/spaces
        pieces = []
        for m in re.finditer(r"[^.!?]+[.!?]?\s*", text):
            sent, base = m.group(0), m.start()
            while len(sent.strip()) > max_len:
                cut = sent.rfind(", ", 0, max_len)
                cut = cut + 2 if cut > 20 else sent.rfind(" ", 0, max_len) + 1
                pieces.append((base, sent[:cut]))
                base, sent = base + cut, sent[cut:]
            if sent.strip():
                pieces.append((base, sent))
        for base, p in pieces:
            a, b = base, base + len(p.rstrip()) - 1
            if use_al:
                t0, t1 = st[a], en[min(b, len(en) - 1)]
            else:
                t0, t1 = s["duration"] * a / len(text), s["duration"] * (b + 1) / len(text)
            cues.append([s["start"] + t0, s["start"] + t1 + .15, p.strip()])
    for i in range(len(cues) - 1):            # never overlap the next subtitle
        cues[i][1] = min(cues[i][1], cues[i + 1][0] - .02)
    for i, (a, b, p) in enumerate(cues, 1):
        lines += [str(i), f"{ts(a)} --> {ts(b)}", p, ""]
    path.write_text("\n".join(lines))


def main(argv):
    if not argv:
        sys.exit(__doc__)
    slug, fake = argv[0], "--placeholder" in argv
    doc = json.loads((NARR / f"{slug}.json").read_text())
    cfg = json.loads((NARR / "config.json").read_text())
    adir = placeholder_audio(slug, doc["segments"]) if fake else AUDIO / slug
    for s in doc["segments"]:
        if not (adir / f"{s['id']}.mp3").exists():
            sys.exit(f"Missing audio for {slug}/{s['id']}. Generate it first with tools/narrate.py.")

    timeline, segs = build_timeline(doc, cfg, adir)
    out = OUT / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "timeline.json").write_text(json.dumps(timeline, indent=2))
    print(f"Timeline: {timeline['duration']:.1f}s, {len(timeline['cues'])} cues")

    with tempfile.TemporaryDirectory() as tmp:
        silent = Path(tmp) / "video.mp4"
        subprocess.run([sys.executable, str(ROOT / "render.py"), str(ROOT / "videos" / f"{slug}.html"), str(silent),
                        "--timeline", str(out / "timeline.json")], check=True)
        # Place every segment at its start time, mix, level to a consistent loudness.
        inputs, filters = [], []
        for i, s in enumerate(segs):
            inputs += ["-i", s["audio"]]
            ms = int(round(s["start"] * 1000))
            filters.append(f"[{i + 1}:a]aresample=44100,adelay={ms}|{ms}[a{i}]")
        mix = "".join(f"[a{i}]" for i in range(len(segs)))
        lufs = cfg.get("loudness_lufs", -16)
        filters.append(f"{mix}amix=inputs={len(segs)}:normalize=0,loudnorm=I={lufs}:TP=-1.5:LRA=11,"
                       f"apad,atrim=0:{timeline['duration']}[aout]")
        final = out / f"{slug}.mp4"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(silent), *inputs,
                        "-filter_complex", ";".join(filters), "-map", "0:v", "-map", "[aout]",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "44100",
                        "-movflags", "+faststart", "-shortest", str(final)], check=True)
    write_vtt(segs, out / f"{slug}.vtt")
    print(f"Done: {final}  ({duration(final):.1f}s)")


if __name__ == "__main__":
    main(sys.argv[1:])
