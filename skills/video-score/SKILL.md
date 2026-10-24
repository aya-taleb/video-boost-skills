---
name: video-score
description: Tests a video against a checklist made by viral-checklist and gives a readiness score (0 to 100), the risks that could hold it back, the top fixes, and an estimated chance to beat the channel's usual views (labeled uncalibrated until real results are logged). Use when the user says test this video, score my video, will this go viral, check this video against the checklist, or before publishing.
---

# Video score

Measures a video, looks at it, and checks every checklist item. The result is honest: a readiness score is how well the video follows what works now, not a promise of views.

## Inputs

- The video: a local file, or a URL of a video the user owns or has the right to download (download with `yt-dlp` if installed; do not download other people's videos to repost or reuse).
- A checklist (`checklist.json` from viral-checklist). If there is none, ask for the topic, platform, market and language, and run viral-checklist first. Do not score against a made-up checklist.
- Optional: a transcript file, and `results.csv` with the user's past results (see Estimate).

## Steps

1. **Measure.**
   ```bash
   python3 <skill_path>/scripts/inspect_video.py VIDEO --out score-out --every 3 [--transcript FILE]
   ```
   It writes `score-out/metrics.json` and frames: the hook (0, 0.5, 1, 2, 3 s), one every 3 seconds, and the last frame. Transcription uses `--transcript` if given, otherwise faster-whisper if installed, otherwise none (say so in the report).

   Metrics you can use in checklist `measure` fields:

   | metric | meaning |
   |---|---|
   | `duration_s` | length in seconds |
   | `aspect`, `vertical` | `9:16`, `16:9`, `1:1`; true when taller than wide |
   | `cuts_per_minute`, `longest_shot_s`, `first_cut_s` | visual changes, found by comparing frames 5 times a second (crossfades count; changes between two very similar frames can be missed) |
   | `first_sound_s`, `first_word_s`, `words_per_minute` | when sound and speech start, speaking pace (needs word timings) |
   | `silences_over_1s` | quiet gaps |
   | `loudness_lufs`, `true_peak_dbfs` | loudness and peak (use the platform's current loudness guidance from the checklist, if the research found one) |

2. **Look.** Open the hook frames, the review frames and the last frame with the image reader. Read the transcript. Note what is on screen: subject in frame 1, text on screen and whether it is readable, captions, faces, brand or credit, end screen space, anything off (garbled text in pictures, watermarks, borders).

3. **Score every checklist item.** For each item write one line:
   - `pass`, `partial`, `fail`, or `cant_tell` (when the video or tools cannot show it, like posting time or the title and thumbnail, unless the user gave them)
   - the evidence: the metric value, the frame time, or the transcript words
   - for `partial` and `fail`: the fix, in one plain sentence
   `avoid` items pass when the video does NOT do the thing.
   Measured items use the metric, not your opinion.

4. **Readiness score.**
   `readiness = 100 × sum(weight × points) / sum(weight)`, with pass = 1, partial = 0.5, fail = 0, and `cant_tell` items left out of both sums. Report how many items were `cant_tell`, because many unknowns make the score less reliable.

5. **Risks.** List every failed `must` item and every failed `avoid` item as a risk, most serious first. Policy risks (monetization, copyright, AI labels, made for kids) always go on top.

6. **Estimate.**
   ```bash
   python3 <skill_path>/scripts/estimate.py --readiness 74 [--results results.csv]
   ```
   It returns the chance (in percent) that the video beats the channel's median views. Without 20 logged results it is **uncalibrated**: it starts at 50% and the readiness moves it at most 20 points. Always print the basis and confidence next to the number. After the video has been out for 7 days, add a row to `results.csv` (`video,readiness,beat_median`) so future estimates learn from real results.

## After the score

- Run `similar-videos` to see how the video stands against the top similar ones (not only against the checklist).
- Run `video-packaging` for titles, description and changes, and `publish-ruler` for the pre-publish checklist.

## Report format

```
Video score: POC4-atomic-habits-takeaway-1.mp4 (34.5 s, 16:9)
Checklist: book summaries · YouTube long-form · US · en · made 2026-10-23

Readiness: 74 / 100   (20 items scored, 4 can't tell)
Chance to beat your median views: 59%  (uncalibrated, low confidence)

Risks
1. ...

Top 3 fixes
1. ...

All items
pass     hook-01  Payoff in the first second ... (frame 0.0 s: Zaid at a huge staircase)
partial  pace-02  New visual every 3 to 6 s ... (longest shot 7.0 s at 9.8 to 16.8 s)
...
```

Plain words. Short lines. Never round a score up to make the video look better.
