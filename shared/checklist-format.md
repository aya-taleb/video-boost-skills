# Checklist format

Every skill in this repo reads and writes the same two files, so they work together and you can edit them by hand.

## 1. Research notes (`notes-<platform>.json`)

Written by `shorts-research`, `reels-research` and `tiktok-research`. Checked by `source-check`.

```json
{
  "platform": "tiktok",
  "topic": "travel tips",
  "market": "US",
  "language": "en",
  "window_months": 12,
  "researched_on": "2026-10-23",
  "findings": [
    {
      "id": "tt-07",
      "kind": "winner_pattern",
      "claim": "Top travel tip videos show the place in the first second, before any talking.",
      "detail": "8 of the 10 most-viewed examples open on the destination, not a face.",
      "examples": [{ "url": "https://...", "views": 2400000, "posted": "2026-08-02" }],
      "sources": [{ "url": "https://...", "publisher": "TikTok Newsroom", "published": "2026-06-11", "type": "official" }],
      "scope": "US",
      "confidence": "high"
    }
  ],
  "gaps": ["No 2026 data on caption length for this topic in the US."]
}
```

`kind` is one of:

| kind | What it means |
|---|---|
| `official_rule` | The platform says so in its own help pages, policy or creator channels |
| `official_tip` | The platform recommends it, but it is not a rule |
| `winner_pattern` | Seen in recent top videos in this topic |
| `data_study` | A study with a sample size and a date |
| `mistake` | Something that drags videos down, with a reason |
| `trend` | A current format, sound or hashtag, with the date it was seen |

`source type` is one of `official`, `data` (study or dataset with a sample), `analysis` (expert article), `example` (the video itself).

`confidence`:
- `high`: official source, or two independent sources agree
- `medium`: one good source
- `low`: one weak source or examples only. Low items never become `must` rules.

## 2. The checklist (`checklist.json` and `checklist.md`)

Written by `viral-checklist`. Read by `video-score`.

```json
{
  "topic": "travel tips",
  "platforms": ["tiktok", "reels", "shorts"],
  "market": "US",
  "language": "en",
  "made_on": "2026-10-23",
  "valid_until": "2026-11-23",
  "items": [
    {
      "id": "hook-01",
      "platforms": ["tiktok", "reels", "shorts"],
      "stage": "hook",
      "level": "must",
      "rule": "Show the payoff (the place, the result, the surprise) in the first second.",
      "why": "Viewers decide in the first seconds whether to keep watching.",
      "check": "Frame at 0.0 s and 1.0 s shows the subject of the video, not a logo or a blank card.",
      "measure": { "metric": "first_frame_has_subject", "pass": true },
      "weight": 3,
      "evidence": ["tt-07", "sh-02"],
      "confidence": "high"
    }
  ]
}
```

`stage`: `hook`, `story`, `length`, `pacing`, `visuals`, `text`, `audio`, `engagement`, `posting`, `policy`.

`level`:
- `must`: breaking it is a real risk (policy, or strong evidence)
- `should`: strong evidence it helps
- `avoid`: a known mistake; the check passes when the video does NOT do it
- `nice`: small or mixed evidence

`weight`: 3 for must and avoid, 2 for should, 1 for nice (change it if your data says otherwise).

`measure` is optional. When a rule can be measured by the script in `video-score` (length, shape, first words, cuts per minute, loudness, captions), name the metric so the score is exact, not a guess. The metric names are listed in `skills/video-score/SKILL.md`.

## Source rules (all skills)

- Every finding has at least one source with a link and a publish date.
- Default window: the last 12 months. With `--recent`, the last 6 months. Older sources are dropped, even if they look right.
- Default market and language: US and English. A global source is allowed and marked `"scope": "global"`.
- A number (views, percent, seconds) must come from a source that shows it. No number from memory.
- When sources disagree, keep both and say so. Do not pick the one you like.
