"""Unit tests for the Python tools. Run: python3 -m unittest discover -s tests -v

No network: the YouTube API helpers are tested only on their pure parts.
The video test runs only when ffmpeg and ffprobe are installed.
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load(rel):
    path = os.path.join(ROOT, rel)
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


TREND = load("skills/trend-ideas/scripts/trend_scan.py")
SHORTS = load("skills/shorts-research/scripts/top_shorts.py")
ESTIMATE = os.path.join(ROOT, "skills/video-score/scripts/estimate.py")
INSPECT = os.path.join(ROOT, "skills/video-score/scripts/inspect_video.py")


def run_estimate(*args):
    out = subprocess.run([sys.executable, "-I", ESTIMATE] + list(args),
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


class Durations(unittest.TestCase):
    def test_iso_durations(self):
        for mod in (TREND, SHORTS):
            self.assertEqual(mod.seconds("PT1M5S"), 65)
            self.assertEqual(mod.seconds("PT2H"), 7200)
            self.assertEqual(mod.seconds("P1DT1S"), 86401)
            self.assertEqual(mod.seconds("PT45S"), 45)

    def test_missing_duration_is_zero(self):
        for mod in (TREND, SHORTS):
            self.assertEqual(mod.seconds(""), 0)
            self.assertEqual(mod.seconds(None), 0)


class KeyWords(unittest.TestCase):
    def test_short_words_dropped(self):
        self.assertEqual(TREND.key_words("how to build atomic habits"), ["build", "atomic", "habits"])

    def test_falls_back_to_whole_angle(self):
        self.assertEqual(TREND.key_words("AI"), ["ai"])


class Estimate(unittest.TestCase):
    def test_uncalibrated_starts_at_half(self):
        out = run_estimate("--readiness", "70")
        self.assertEqual(out["chance_to_beat_median"], 50)
        self.assertEqual(out["confidence"], "low")
        self.assertIn("uncalibrated", out["basis"])

    def test_uncalibrated_moves_at_most_20_points(self):
        self.assertLessEqual(run_estimate("--readiness", "100")["chance_to_beat_median"], 70)
        self.assertGreaterEqual(run_estimate("--readiness", "0")["chance_to_beat_median"], 30)

    def test_fewer_than_20_results_stay_uncalibrated(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "results.csv")
            with open(path, "w") as fh:
                fh.write("video,readiness,beat_median\n")
                for i in range(19):
                    fh.write("v%d,%d,%d\n" % (i, 60 + i, i % 2))
            out = run_estimate("--readiness", "80", "--results", path)
            self.assertIn("19 of 20", out["basis"])

    def test_calibrates_on_own_results(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "results.csv")
            with open(path, "w") as fh:
                fh.write("video,readiness,beat_median\n")
                for i in range(24):
                    readiness = 40 + i * 2
                    fh.write("v%d,%d,%d\n" % (i, readiness, 1 if readiness >= 64 else 0))
            high = run_estimate("--readiness", "90", "--results", path)
            low = run_estimate("--readiness", "45", "--results", path)
            self.assertIn("calibrated on 24", high["basis"])
            self.assertGreater(high["chance_to_beat_median"], low["chance_to_beat_median"])


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "needs ffmpeg")
class InspectVideo(unittest.TestCase):
    def test_measures_a_two_shot_clip(self):
        with tempfile.TemporaryDirectory() as d:
            clip = os.path.join(d, "clip.mp4")
            # 2 s of black, then 2 s of white, vertical 9:16, with a tone for audio.
            subprocess.run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-f", "lavfi", "-i", "color=c=black:s=360x640:d=2:r=25",
                "-f", "lavfi", "-i", "color=c=white:s=360x640:d=2:r=25",
                "-f", "lavfi", "-i", "sine=frequency=440:duration=4",
                "-filter_complex", "[0:v][1:v]concat=n=2:v=1:a=0[v]",
                "-map", "[v]", "-map", "2:a", "-shortest",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", clip,
            ], check=True)
            out = os.path.join(d, "out")
            subprocess.run([sys.executable, "-I", INSPECT, clip, "--out", out, "--no-whisper"],
                           capture_output=True, text=True, check=True)
            with open(os.path.join(out, "metrics.json")) as fh:
                m = json.load(fh)
            self.assertAlmostEqual(m["duration_s"], 4.0, delta=0.2)
            self.assertTrue(m["vertical"])
            self.assertEqual(m["aspect"], "9:16")
            self.assertEqual(m["cuts"], 1)
            self.assertAlmostEqual(m["first_cut_s"], 2.0, delta=0.3)
            self.assertTrue(m["has_audio"])
            self.assertTrue(m["frames"]["hook"])


if __name__ == "__main__":
    unittest.main()
