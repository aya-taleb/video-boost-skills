# video-boost-skills

Agent skills that find out what makes videos work right now, turn it into a checklist, and test your video against it.

Every rule comes from a source with a link and a date from the last 12 months. Defaults: US and English.

## Pick your goal

| I want to... | Ask | Skill |
|---|---|---|
| Know what works now for my topic | "Make a viral checklist for travel tips on TikTok and Reels" | `viral-checklist` |
| Test my video before posting | "Score this video against the checklist" | `video-score` |
| See how I stand against similar videos | "Compare my video with the top similar ones" | `similar-videos` |
| Get a title, description, hashtags and thumbnail ideas | "Package this video for YouTube" | `video-packaging` |
| Check everything before I hit publish | "Make my pre-publish checklist" | `publish-ruler` |
| Only research one platform | "What works on Reels for cooking videos?" | `tiktok-research`, `reels-research`, `shorts-research`, `youtube-research` |
| Check if sources are recent and right | "Check these sources" | `source-check` |

## The skills

| Skill | What it does |
|---|---|
| `viral-checklist` | Builds the checklist for one topic, platform, market and language. Runs the research skills and source-check. |
| `tiktok-research` | What works on TikTok for the topic now: top videos, patterns, mistakes, TikTok's own rules. |
| `reels-research` | The same for Instagram Reels. |
| `shorts-research` | The same for YouTube Shorts. Uses the free YouTube Data API if you add a key. |
| `youtube-research` | The same for long YouTube videos (over 3 minutes). |
| `source-check` | Checks every source: working link, date inside the window, right market and language, numbers that match the page. |
| `video-score` | Measures your video, checks every rule, and gives a readiness score, risks, top fixes and an estimate. |
| `similar-videos` | Finds the top similar videos and compares them with yours, fact by fact. |
| `video-packaging` | Writes 3 titles to test, the description with chapters, hashtags, thumbnail ideas, and the changes worth making. |
| `publish-ruler` | The ruler: YouTube's own upload steps and rules as a step-by-step pre-publish checklist, filled in for your video. |

## How to use

1. Copy the `skills` folder into your agent's skills folder (for Claude Code: `~/.claude/skills/` or `.claude/skills/` in your project).
2. Ask for a goal from the table above. Add a market or language if not US and English.

## What the score means

- **Readiness (0 to 100):** how well the video follows what is working now. Not a promise of views.
- **Chance to beat your usual views:** starts as a rough estimate (labeled uncalibrated). Log your real results in `results.csv` and after 20 videos it learns from your own channel.
- Items the tools cannot see (title, thumbnail, posting time) are marked "can't tell" and left out of the score. The report says how many.

## Needs

- Python 3.9 or newer and ffmpeg
- Optional: `pip install faster-whisper` for transcripts, `yt-dlp` to download your own videos from a link
- Optional: `YOUTUBE_API_KEY` for exact YouTube numbers

## Rules every skill follows

- No source older than the window (12 months, or 6 when you ask for recent).
- No numbers from memory.
- If there is no good recent source, the rule is left out and listed as a gap.
- Free and official sources only. No scraping, no logins.

## Example

`examples/book-summaries-youtube-US-en` has a full run on a 34-second test video: research notes, source report, checklist, score, similar videos, packaging and the pre-publish checklist.

## License

MIT
