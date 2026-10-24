---
name: reels-research
description: Researches what is working on Instagram Reels right now for one topic, market and language - top recent Reels and their patterns, current trends, common mistakes, and Instagram's own rules and recommendations (originality, recommendation guidelines, ranking signals) - using only sources from the last 12 months (6 with recent), each with a link and date. Use when the user asks what works on Instagram Reels for a topic, why Reels fail, Reels trends for X, or as part of viral-checklist.
---

# Instagram Reels research

Finds what is working on Instagram Reels for one topic, and what is not, with a source and date for every finding.

## Inputs

| Input | Default |
|---|---|
| topic | ask if missing |
| market (country) | US |
| language | en |
| window | 12 months (`recent` = 6 months) |

Write today's date at the top of your notes. Every date check uses it.

## Output

`notes-reels.json` in the format in `shared/checklist-format.md`. Aim for 15 to 30 findings. List what you could not find under `gaps`.

## Where to look, in this order

1. **Instagram's own rules and tips (official).**
   - How Reels are ranked: Meta Transparency Center, "Explaining ranking" pages for Instagram Reels (transparency.meta.com/features/explaining-ranking). These pages list the signals Instagram uses.
   - Recommendation guidelines (what Instagram will not recommend) and original content rules: help.instagram.com and about.instagram.com/blog. Instagram has been changing how it treats reposted and unoriginal content; find the latest change and its date.
   - Instagram's creator channels: creators.instagram.com, the @creators account, and Adam Mosseri's announcements (usually reported by trade press on the same day; use the report's date and link to the original post if you can).
   - AI labels ("AI info") and branded content rules.
2. **Recent top Reels in the topic (examples).** Instagram has no public trending list. Search the web for recent viral Reels in the topic and market, with the year in the query. Keep only Reels where a dated page shows the view or like count. Note the hook, length, format, on-screen text, audio, and call to action.
3. **Studies and analysis (data, analysis).** Recent studies with a sample size and dates (for example Reels length, posting frequency, carousel vs Reels reach). Note who ran them and how many accounts or posts they looked at.
4. **Failures (mistakes).** Watermarks from other apps, reposted content, low resolution, text placed under the app buttons, engagement bait, and anything Instagram says it will not recommend. A mistake needs a reason and a source.

## What to pull out

Cover each of these, or list it as a gap:

- Hook: first 1 to 3 seconds of top Reels in the topic
- Length that works now (with the source's date)
- Shape and safe zones: 9:16, where text must not go (under the caption and buttons)
- Pacing, structure, payoff
- On-screen text, captions, cover image
- Audio: original audio, trending audio, voice over
- Sends (shares in DMs), saves, comments: which ones Instagram says matter, with the date it said so
- Calls to action that work and ones that count as engagement bait
- Posting frequency and hashtags (only with a dated source)
- Original content rules, reposts, watermarks, AI labels
- Topic-specific risks

## Rules

- Every finding needs a link and a publish date inside the window. No date, no finding.
- Market and language must match, or the finding is marked `"scope": "global"` (platform-wide announcements only).
- No numbers from memory. If you cannot find a current source, leave it out or add it to `gaps`.
- Do not use paid scraping tools or log in to Instagram to collect data. Public pages and official sources only.
- Keep claims short and specific, in plain words.

When done, run `source-check` on the notes, unless the user asked you not to.
