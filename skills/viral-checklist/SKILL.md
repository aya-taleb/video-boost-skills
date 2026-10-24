---
name: viral-checklist
description: Builds a checklist of what makes videos work right now for one topic on TikTok, Instagram Reels, YouTube Shorts and/or long YouTube videos, for a market and language (US and English by default). Runs the platform research skills, checks every source with source-check (12 months max, 6 with recent), and merges the findings into rules with a reason, a way to check, a weight and a source. Use when the user asks for a viral checklist, what makes X videos go viral, best practices for X on TikTok/Reels/Shorts/YouTube, or before video-score.
---

# Viral checklist

Turns fresh, checked research into a checklist that a person (or `video-score`) can test a video against.

## Inputs

Ask only for what is missing. Defaults in brackets.

| Input | Default |
|---|---|
| topic | ask |
| platforms | tiktok, reels, shorts (add `youtube` for videos over 3 minutes) |
| market | US |
| language | en |
| window | 12 months (`recent` = 6 months) |
| format, if known | for example narrated animation, talking head, skit |

## Steps

1. **Research each platform** with its skill: `tiktok-research`, `reels-research`, `shorts-research`, `youtube-research`. They are independent, so run them at the same time when you can (for example as parallel subagents). Each writes `notes-<platform>.json`.
2. **Check sources** with `source-check` on every notes file. Read `source-report.md`. If a platform has big gaps, tell the user before going on.
3. **Merge into rules.** Group findings that say the same thing across platforms into one rule and list the platforms it applies to. Keep platform-only rules separate (for example Reels safe zones, YouTube end screens).
   For each rule fill the fields in `shared/checklist-format.md`:
   - `level`: `must` only for platform policy or `high` confidence evidence; `avoid` for mistakes; `should` for medium or high evidence that it helps; `nice` for low or mixed evidence.
   - `check`: how a person can tell, in one sentence. Use a `measure` (metric from `video-score`) whenever the rule can be measured.
   - `evidence`: the finding ids, so every rule traces back to dated sources.
   - When findings conflict (for example two "best lengths"), write the rule as a range and say there is a conflict.
4. **Add the topic's own risks**, from the research (for example: book summaries must use your own words and credit the author; travel prices change; health topics give no personal advice).
5. **Write two files:**
   - `checklist.json` (for `video-score`)
   - `checklist.md` (for people): grouped by stage (hook, story, length, pacing, visuals, text, audio, engagement, posting, policy), one line per rule with its level, and a Sources section with every link and its date.
   Set `valid_until` one month after today. Trends move fast; rebuild the checklist when it expires.
6. **Tell the user** in a few lines: how many rules, the 5 that matter most, the gaps, and the date it expires.

## Rules

- No rule without a dated source inside the window.
- No numbers from memory.
- Market and language stay what the user set. If the only evidence is global, the rule says "global".
- 15 to 40 rules is a good size. More than that and nobody uses it.
- Plain words everywhere.
