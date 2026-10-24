---
name: tiktok-research
description: Researches what is working on TikTok right now for one topic, market and language - top recent videos and their patterns, current trends, common mistakes, and TikTok's own rules and recommendations - using only sources from the last 12 months (6 with recent), each with a link and date. Use when the user asks what works on TikTok for a topic, why TikTok videos fail, TikTok trends for X, or as part of viral-checklist.
---

# TikTok research

Finds what is working on TikTok for one topic, and what is not, with a source and date for every finding.

## Inputs

| Input | Default |
|---|---|
| topic | ask if missing |
| market (country) | US |
| language | en |
| window | 12 months (`recent` = 6 months) |

Write today's date at the top of your notes. Every date check uses it.

## Output

`notes-tiktok.json` in the format in `shared/checklist-format.md`. Aim for 15 to 30 findings. Fewer is fine if that is all the good evidence there is. List what you could not find under `gaps`.

## Where to look, in this order

1. **TikTok's own rules and tips (official).** These beat everything else.
   - Community Guidelines, including the For You feed eligibility standards (what TikTok will not recommend): tiktok.com/community-guidelines
   - How TikTok recommends videos: support.tiktok.com (search "how TikTok recommends content")
   - Creator help and Creator Academy pages, the TikTok Newsroom (newsroom.tiktok.com), and TikTok's yearly trend reports ("What's Next")
   - AI content labels and rules (search "TikTok AI-generated content label")
   Check the date on every page. Rules change often.
2. **What is trending now (official data).** TikTok Creative Center (ads.tiktok.com/business/creativecenter) shows trending hashtags, songs, creators and videos by country and time range. Set the country to the market. If the page will not load in your tools, say so in `gaps` and do not guess what it shows.
3. **Recent top videos in the topic (examples).** Search the web for recent viral or top videos in the topic and market, with the year in the query (for example "travel tips TikTok viral 2026"). Keep only videos where you can see the post date and a view count from the page or a dated article. Note for each: the hook (first 1 to 3 seconds), length, format (talking head, voice over, text on screen, skit, list), on-screen text, sound (trending sound, original voice, music), and call to action.
4. **Studies and analysis (data, analysis).** Recent studies with a sample size (for example from social media management or analytics companies), and articles from reputable trade press. Prefer studies that say how many videos or accounts they looked at, which country, and which months.
5. **Failures (mistakes).** Search for why videos in this topic flop, TikTok shadowban myths vs facts, and content TikTok does not recommend. A mistake needs a reason and a source, not just an opinion.

## What to pull out

Cover each of these, or list it as a gap:

- Hook: what happens in the first 1 to 3 seconds of top videos
- Length that works for this topic now (with the source's date)
- Structure and pacing: cuts, list format, story, payoff at the end
- On-screen text and captions
- Sound: original audio vs trending sounds, voice over, music
- Visual style, faces vs no faces, real footage vs animation
- Calls to action that work (follow, comment, save, share) and ones that hurt
- Posting: frequency, times (only with a dated US source), hashtags (how many, which kind)
- What TikTok will not recommend (For You feed rules), AI labels, copyright and unoriginal content
- Topic-specific risks (for travel: safety claims, prices that change; for health: no advice)

## Rules

- Every finding needs a link and a publish date inside the window. No date, no finding.
- Market and language must match, or the finding is marked `"scope": "global"` (only for platform-wide announcements).
- No numbers from memory. If you know something but cannot find a current source, leave it out or put it in `gaps`.
- Ads results (TikTok's ad studies) are about paid ads. Mark them clearly. Do not present them as organic.
- Keep claims short and specific. "Hooks matter" is useless; "Top 10 travel tip videos this summer all show the destination in frame 1" is useful.
- Write the notes in plain words.

When done, run `source-check` on the notes, unless the user asked you not to.
