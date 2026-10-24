#!/usr/bin/env python3
"""Measure a video so it can be scored against a checklist.

Prints metrics as JSON and saves frames to look at (the hook frames and one frame every few seconds).
Needs ffmpeg and ffprobe. Transcription is optional: pass --transcript FILE (plain text or JSON with words),
or install faster-whisper (pip install faster-whisper) and it runs automatically.

Usage:
    python3 inspect_video.py VIDEO --out DIR [--every 3] [--transcript FILE] [--no-whisper]
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout + r.stderr


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"ffprobe could not read {path}: {out.stderr[:300]}")
    return json.loads(out.stdout)


def scene_cuts(path, threshold=22.0, rate=5):
    """Find cuts by comparing small grey frames taken 5 times a second.
    Works for hard cuts and for short crossfades (which per-frame scene scores miss)."""
    raw = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-vf", f"fps={rate},scale=64:36,format=gray", "-f", "rawvideo", "-"],
                         capture_output=True).stdout
    size = 64 * 36
    n = len(raw) // size
    diffs = []
    for i in range(1, n):
        a, b = raw[(i - 1) * size:i * size], raw[i * size:(i + 1) * size]
        diffs.append((i / rate, sum(abs(x - y) for x, y in zip(a, b)) / size))
    cuts = []
    for t, d in diffs:
        if d >= threshold and (not cuts or t - cuts[-1] > 0.6):
            cuts.append(round(t, 2))
    return cuts


def silences(path, noise="-40dB", dur=0.3):
    log = run(["ffmpeg", "-hide_banner", "-i", path, "-af", f"silencedetect=noise={noise}:d={dur}", "-vn", "-f", "null", "-"])
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", log)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    return list(zip(starts, ends + [None] * (len(starts) - len(ends))))


def loudness(path):
    log = run(["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128=peak=true", "-vn", "-f", "null", "-"])
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", log)
    tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", log)
    return (float(i[-1]) if i else None, float(tp[-1]) if tp else None)


def frames(path, out_dir, times):
    os.makedirs(out_dir, exist_ok=True)
    saved = []
    for t in times:
        f = os.path.join(out_dir, f"frame_{t:07.2f}s.jpg")
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(t), "-i", path, "-frames:v", "1", "-vf", "scale=960:-2", f])
        if os.path.exists(f):
            saved.append(f)
    return saved


def transcribe(path, transcript, use_whisper):
    if transcript:
        text = open(transcript, encoding="utf-8").read()
        try:
            data = json.loads(text)
            words = data.get("words") or []
            return {"text": data.get("text") or " ".join(w["text"] for w in words), "words": words, "source": "file"}
        except json.JSONDecodeError:
            return {"text": text.strip(), "words": [], "source": "file"}
    if not use_whisper:
        return None
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return None
    model = WhisperModel("small", compute_type="int8")
    segs, _ = model.transcribe(path, word_timestamps=True)
    words, text = [], []
    for s in segs:
        text.append(s.text.strip())
        for w in s.words or []:
            words.append({"text": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
    return {"text": " ".join(text), "words": words, "source": "faster-whisper small"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--out", default="video-score-out")
    ap.add_argument("--every", type=float, default=3.0, help="seconds between review frames")
    ap.add_argument("--transcript")
    ap.add_argument("--no-whisper", action="store_true")
    a = ap.parse_args()

    p = probe(a.video)
    v = next((s for s in p["streams"] if s["codec_type"] == "video"), None)
    au = next((s for s in p["streams"] if s["codec_type"] == "audio"), None)
    if not v:
        sys.exit("No video stream found.")
    dur = float(p["format"]["duration"])
    w, h = int(v["width"]), int(v["height"])
    num, den = (v.get("avg_frame_rate") or "0/1").split("/")
    fps = round(float(num) / float(den), 2) if float(den) else None

    cuts = scene_cuts(a.video)
    shot_edges = [0.0] + cuts + [dur]
    shot_lengths = [round(shot_edges[i + 1] - shot_edges[i], 2) for i in range(len(shot_edges) - 1)]

    sil = silences(a.video) if au else []
    # First sound: the end of a silence that starts at 0, else 0.
    first_sound = 0.0
    for s, e in sil:
        if s <= 0.05 and e:
            first_sound = round(e, 2)
            break
    lufs, peak = loudness(a.video) if au else (None, None)

    hook_times = [0.0, 0.5, 1.0, 2.0, 3.0]
    review_times = [round(t, 2) for t in [x * a.every for x in range(1, int(dur / a.every) + 1)] if t < dur - 0.2]
    out_frames = os.path.join(a.out, "frames")
    hook = frames(a.video, out_frames, hook_times)
    review = frames(a.video, out_frames, [t for t in review_times if t not in hook_times])
    last = frames(a.video, out_frames, [max(0.0, round(dur - 0.5, 2))])

    tr = transcribe(a.video, a.transcript, not a.no_whisper)
    first_word = None
    wpm = None
    if tr and tr["words"]:
        first_word = tr["words"][0].get("start")
        spoken = (tr["words"][-1].get("end") or dur) - (first_word or 0)
        wpm = round(len(tr["words"]) / max(spoken, 1) * 60)

    m = {
        "file": os.path.abspath(a.video),
        "duration_s": round(dur, 2),
        "width": w, "height": h,
        "aspect": "9:16" if h > w and abs(w / h - 9 / 16) < 0.03 else "16:9" if abs(w / h - 16 / 9) < 0.03 else "1:1" if w == h else f"{w}:{h}",
        "vertical": h > w,
        "fps": fps,
        "has_audio": bool(au),
        "cuts": len(cuts),
        "cut_times_s": cuts,
        "cuts_per_minute": round(len(cuts) / dur * 60, 1) if dur else 0,
        "longest_shot_s": max(shot_lengths) if shot_lengths else round(dur, 2),
        "first_cut_s": cuts[0] if cuts else None,
        "first_sound_s": first_sound,
        "first_word_s": first_word,
        "words_per_minute": wpm,
        "silences_over_1s": [[round(s, 2), round(e, 2) if e else None] for s, e in sil if e and e - s >= 1.0],
        "loudness_lufs": lufs,
        "true_peak_dbfs": peak,
        "transcript": tr,
        "frames": {"hook": hook, "review": review, "last": last},
    }
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "metrics.json"), "w") as f:
        json.dump(m, f, indent=2)
    print(json.dumps({k: v for k, v in m.items() if k not in ("transcript",)}, indent=2))


if __name__ == "__main__":
    main()
