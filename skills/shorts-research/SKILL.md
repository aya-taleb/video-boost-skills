---
name: shorts-research
description: Researches what is working on YouTube Shorts right now for one topic, market and language - top recent Shorts (from the YouTube Data API when a key is set), their patterns, common mistakes, and YouTube's own rules (Shorts length, monetization and inauthentic content, AI disclosure, how Shorts are recommended) - using only sources from the last 12 months (6 with recent), each with a link and date. Use when the user asks what works on YouTube Shorts for a topic, why Shorts fail, or as part of viral-checklist.
---

# YouTube Shorts research

Finds what is working on YouTube Shorts for one topic, and what is not, with a source and date for every finding.

## Inputs

| Input | Default |
|---|---|
| topic | ask if missing |
| market (country) | US |
| language | en |
| window | 12 months (`recent` = 6 months) |

Write today's date at the top of your notes. Every date check uses it.

## Output

`notes-shorts.json` in the format in `shared/checklist-format.md`. Aim for 15 to 30 findings. List what you could not find under `gaps`.

## Where to look, in this order

1. **YouTube's own rules and tips (official).**
   - YouTube Help (support.google.com/youtube): Shorts length and format, monetization policies (inauthentic, repetitive and reused content), altered or synthetic content disclosure, fake engagement policy, made for kids rules.
   - The YouTube Official Blog (blog.youtube) and Creator Insider (YouTube's own creator channel) for how Shorts are recommended. Interviews with YouTube staff count as official when they are on a YouTube channel or quoted by a dated trade press article.
   - Find the latest version of each rule and its date. YouTube changed Shorts rules several times in 2025 and 2026.
2. **Recent top Shorts in the topic (data).** If `YOUTUBE_API_KEY` is set, run the helper:
   ```bash
   python3 <skill_path>/scripts/top_shorts.py --topic "travel tips" --region US --lang en --months 12 --max 25
   ```
   It searches recent videos in the topic, keeps the ones 3 minutes or shorter, and prints title, channel, views, likes, comments, length, and post date as JSON. Each search costs 100 units of the free daily quota of 10,000. Use the results as `example` sources (the link is the video). Look at the top 10: the hook, length, format, text on screen, sound, call to action. Open the video page if you need to see the first seconds.
   If there is no key, search the web for recent top Shorts in the topic instead, and keep only ones with a dated view count. Add "no YouTube API key" to `gaps`.
3. **Studies and analysis (data, analysis).** Recent studies with a sample size and dates (Shorts length, retention, Shorts to long-form subscribers). Mark creator surveys as surveys, not platform data.
4. **Failures (mistakes).** Reused clips without changes, templated AI videos (not paid by YouTube since the July 2026 clarification; find the current page), misleading thumbnails or titles, engagement bait, wrong made for kids setting. A mistake needs a reason and a source.

## What to pull out

Cover each of these, or list it as a gap:

- Hook: first 1 to 3 seconds of top Shorts in the topic
- Length that works now, and the current maximum length
- Loop: does the end lead back into the start
- Pacing, structure, payoff
- Text on screen and captions
- Sound: voice, music, YouTube audio library
- Calls to action: allowed ("subscribe, like, share" is fine) vs not (incentives for engagement)
- Shorts that lead to long videos (related video link)
- Monetization rules: inauthentic content, AI personas on health, finance and legal topics, reused content
- AI disclosure: when it is required (realistic content) and when it is not (clearly unrealistic, like animation)
- Topic-specific risks

## Rules

- Every finding needs a link and a publish date inside the window. A video example uses its post date.
- Market and language must match, or the finding is marked `"scope": "global"` (platform-wide announcements only).
- No numbers from memory. If you cannot find a current source, leave it out or add it to `gaps`.
- Keep claims short and specific, in plain words.

When done, run `source-check` on the notes, unless the user asked you not to.
