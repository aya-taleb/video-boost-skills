---
name: trend-ideas
description: Give it a topic and it researches what is trending around it right now in your market and language, then recommends the top 10 video ideas ranked by viral potential, each with the evidence (real breakout videos with views, dates and outlier scores, plus dated news or trend sources) and why it fits now. Uses the YouTube Data API when YOUTUBE_API_KEY is set. Use when the user says give me video ideas for X, what should I make about X, what is trending in X, or top 10 viral ideas.
---

# Trend ideas: the top 10 videos to make next

Finds what is breaking out around a topic right now and turns it into 10 ranked video ideas. Every idea shows its evidence, so you can judge it.

## Inputs

| Input | Default |
|---|---|
| topic | ask |
| platform | YouTube (long videos); `shorts` for Shorts |
| market, language | US, en |
| window | last 90 days for trends (never more than 12 months) |
| your format and niche, if known | for example "animated narrator, book summaries"; used for fit |

## Steps

1. **Angles.** Write 6 to 10 search angles around the topic: sub-topics, famous books or people, problems people search, and fresh events. Use web search for news and trends from the last 90 days (dated sources only) to add angles that are new right now.
2. **Scan YouTube** (needs `YOUTUBE_API_KEY`):
   ```bash
   python3 <skill_path>/scripts/trend_scan.py --angles "angle one" "angle two" ... --region US --lang en --days 90 --long --out scan.json
   ```
   For each video: views per day, **outlier** (views vs the channel's median of its last 10 uploads; 3x or more is a breakout), views per subscriber, engagement. For each angle: demand (median views per day of the top 10), breakouts, breakouts from channels under 100K subscribers, and **rising** (are newer videos doing better than older ones in the window).
   Without a key: use web search for recent top videos with dated view counts, and say the ranking is rough.
3. **Clean the scan.** Drop videos that are off-topic (search returns loose matches, like a band with a similar name), in another language, or made for another market. Say how many you dropped.
4. **Find the themes that win.** Group the breakouts by what they promise (for example "fix your dopamine", "psychology of discipline"). Note the title patterns, lengths and formats that win, and the gaps: things people clearly want with few good videos.
5. **Write ideas.** For the best themes, write specific video ideas. Each idea:
   - working title (the winning pattern, never misleading)
   - the hook (first 10 seconds) and the promise
   - format and length (fit to the user's format if given)
   - why now: the evidence (2 to 4 breakout videos with links, views, date, outlier) and any dated trend or news source
   - risks: policy (no AI expert advice on health, money or law), copyright (books: own words, credit), saturation
6. **Rank.** Score each idea 0 to 100 and show the parts:
   | part | weight | from |
   |---|---|---|
   | demand | 30% | the theme's median views per day, scaled against the other themes |
   | breakouts | 25% | share of the theme's videos at 3x outlier or more |
   | open door | 15% | share of breakouts from channels under 100K subscribers (small channels can win) |
   | rising | 15% | newer videos beating older ones in the window |
   | fit | 15% | fits the user's format, characters and policies (your judgment, say why) |
   Call it **viral potential**, never a promise.
7. **Output** `ideas.md` (ranked list, one block per idea, sources at the end) and `ideas.json`.

## Rules

- Evidence comes only from the scan or from dated sources inside the window. No views from memory.
- Never copy a competitor's title word for word. Learn the pattern, write your own.
- Prefer ideas where small channels break out (an open door) over ideas owned by giant channels.
- Plain words.
