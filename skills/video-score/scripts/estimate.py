#!/usr/bin/env python3
"""Turn a readiness score into a chance to beat your channel's usual views.

Without your own results this is a weak estimate: it starts from 50% (by definition, half of your videos beat
your median) and lets the readiness score move it at most 20 points either way. Checklist fit explains only part
of why a video does well, so the number is labeled "uncalibrated" until you log real results.

With 20 or more of your own videos in results.csv (columns: video,readiness,beat_median with 1 or 0),
it fits a simple logistic model on your data and reports "calibrated on N videos".

Usage:
    python3 estimate.py --readiness 72 [--results results.csv]
"""
import argparse
import csv
import json
import math
import os


def fit(rows):
    # One-feature logistic regression by plain gradient descent (no extra packages).
    xs = [(float(r["readiness"]) - 70) / 15 for r in rows]
    ys = [1.0 if str(r["beat_median"]).strip() in ("1", "true", "yes") else 0.0 for r in rows]
    a, b = 0.0, 0.0
    for _ in range(5000):
        ga = gb = 0.0
        for x, y in zip(xs, ys):
            p = 1 / (1 + math.exp(-(a + b * x)))
            ga += p - y
            gb += (p - y) * x
        a -= 0.05 * ga / len(xs)
        b -= 0.05 * gb / len(xs)
    return a, b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--readiness", type=float, required=True)
    ap.add_argument("--results")
    x = ap.parse_args()
    rows = []
    if x.results and os.path.exists(x.results):
        with open(x.results, newline="") as f:
            rows = [r for r in csv.DictReader(f) if r.get("readiness") and r.get("beat_median") not in (None, "")]
    if len(rows) >= 20:
        a, b = fit(rows)
        p = 1 / (1 + math.exp(-(a + b * (x.readiness - 70) / 15)))
        out = {"chance_to_beat_median": round(p * 100), "basis": f"calibrated on {len(rows)} of your videos", "confidence": "medium" if len(rows) < 60 else "high"}
    else:
        # Uncalibrated: 50% at readiness 70, ±20 points at most.
        p = 0.5 + 0.2 * math.tanh((x.readiness - 70) / 15)
        out = {"chance_to_beat_median": round(p * 100), "basis": f"uncalibrated ({len(rows)} of 20 videos logged)", "confidence": "low"}
    print(json.dumps(out))


if __name__ == "__main__":
    main()
