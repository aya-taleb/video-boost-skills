---
name: similar-videos
description: Finds the top videos most similar to yours (same topic, format, platform, market and language), collects their public facts (title, channel, date, length, views with source, chapters, description, hashtags), and compares them with your video side by side, so you see what the winners do that you don't. Use when the user says compare my video with similar ones, who are my competitors, what do the top videos on this do, or as part of video-score.
---

# Similar videos

A score against a checklist says how well you follow the rules. This skill says how you stand against the real videos you compete with.

## Inputs

| Input | Default |
|---|---|
| your video, and its title and description if it has them | ask |
| topic and format (for example "Atomic Habits, animated book summary") | from the video |
| platform | youtube |
| market, language | US, en |
| window | 12 months for "recent"; up to 3 older all-time leaders are allowed and marked `older` |

## Steps

1. **Find candidates.**
   - YouTube with `YOUTUBE_API_KEY`: `python3 ../shorts-research/scripts/top_shorts.py --topic "<topic>" --region US --lang en --months 12 [--long]`. Run it once more with `--months 120` to find older leaders.
   - Otherwise: search the web for the topic plus the format and the year, and open the video pages.
   - TikTok and Reels: public pages only, no logins, no scraping tools.
2. **Pick 5 to 10.** Same topic, or the same format on a close topic. Prefer videos from the last 12 months. Up to 3 older leaders, marked `older`. Drop videos in another language or made for another market (say why).
3. **Collect public facts for each,** from the video page or a dated stats page:
   title · channel · post date · length · views (with the source and the date you read it; leave empty if no page shows it) · chapters (count) · first 2 lines of the description · links in the description · hashtags · title pattern · thumbnail (describe it only if you can see it).
   Never guess a view count. Channel stats sites give estimates; say so.
4. **Do not download other people's videos.** Platform terms do not allow it. If the user wants pacing or hook details, ask them to watch the first 30 seconds and tell you, or to share screenshots.
5. **Compare.** One table: your video vs each similar video, one row per fact. Then:
   - **What they all do that you don't** (only patterns seen in 3 or more of them)
   - **Where you are different in a good way** (a gap you can own)
   - **What you could not compare** and why
6. Save `similar-videos.json` (the facts) and `similar-videos.md` (the table and findings). `video-packaging` and `video-score` read them.

## Rules

- Every fact has a link. Every view count has a source and a date.
- Patterns need 3 or more videos. One video is an example, not a pattern.
- Plain words. Short lines.
