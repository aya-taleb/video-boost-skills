# video-boost-skills

Find out what makes videos work right now for your topic, turn it into a checklist, and test your own video against it before you post.

Every rule comes from a source with a link and a date from the last 12 months. Defaults: US and English.

## What do you want to do?

| I want to... | Ask | Skill |
|---|---|---|
| Find the next videos to make | "Give me the top 10 video ideas for habits and self-improvement" | `trend-ideas` |
| Know what works now for my topic | "Make a viral checklist for travel tips on TikTok and Reels" | `viral-checklist` |
| Test my video before posting | "Score this video against the checklist" | `video-score` |
| See how I stand against similar videos | "Compare my video with the top similar ones" | `similar-videos` |
| Get a title, description, hashtags and thumbnail ideas | "Package this video for YouTube" | `video-packaging` |
| Check everything before I hit publish | "Make my pre-publish checklist" | `publish-ruler` |
| Only research one platform | "What works on Reels for cooking videos?" | `tiktok-research`, `reels-research`, `shorts-research`, `youtube-research` |
| Check if sources are recent and right | "Check these sources" | `source-check` |

## Install

/plugin marketplace add aya-taleb/video-boost-skills
/plugin install video-boost-skills@video-boost-skills

In the Claude app: Customize, Plugins, Add, Add marketplace, Add from a repository, then pick `aya-taleb/video-boost-skills`.

## Start here

Run `/trend-ideas` with your topic, for example "top 10 video ideas for habits and self-improvement".
Pick an idea, make the video, then run `/viral-checklist` for that topic and platform and `/video-score` on your file.
Finish with `/video-packaging` and `/publish-ruler` before you upload.

## What the score means

- **Readiness (0 to 100):** how well the video follows what is working now. Not a promise of views.
- **Chance to beat your usual views:** starts as a rough estimate (labeled uncalibrated). Log your real results in `results.csv` and after 20 videos it learns from your own channel.
- Items the tools cannot see (title, thumbnail, posting time) are marked "can't tell" and left out of the score. The report says how many.

## Needs

- Python 3.9 or newer and ffmpeg
- Optional: `pip install faster-whisper` for transcripts
- Optional: `YOUTUBE_API_KEY` (free, from a Google Cloud project with YouTube Data API v3 turned on) for exact YouTube numbers

## Good to know

- **Recent sources only.** Nothing older than the window (12 months, or 6 when you ask for recent). If there is no good recent source, the rule is left out and listed as a gap.
- **No numbers from memory.** Every number has a link and a date.
- **Free and official sources only.** No scraping and no logins.
- **Your own files only.** Nothing here downloads from YouTube, TikTok or Instagram, not even your own videos. Get your file from YouTube Studio (Content, the video's menu, Download), or use the original from your phone or editor.
- **A score is not a promise.** Readiness says how well a video follows what works now, not how many views it will get.

## Works well with

These free MIT packs by Jake Schincariol do things we don't, and our checklists fit right in:

| Pack | Use it for |
|---|---|
| [chatgpt-youtube-agent-skill](https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill) | scoring your hook before you record (`yt-script`), reading your retention export to find the second people left (`yt-retention`), finding Shorts inside a long video (`yt-shorts`) |
| [instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) | Reels hooks, captions, and the humanizer that cleans AI-sounding text |

What this pack adds on top: dated research with a source check, the platform rules as a pre-publish ruler, measuring the actual video file, and ranked ideas from a live YouTube breakout scan.

## Learned from other tools

See `docs/COMPETITORS.md`: what vidIQ, TubeBuddy, 1of10, ViewStats, OutlierKit, OpusClip and the faceless video makers do well, where they fall short, and what we took.

## Example

`examples/book-summaries-youtube-US-en` has a full run on a 34-second test video: research notes, source report, checklist, score, similar videos, packaging and the pre-publish checklist.

## Credits

Made by Aya Taleb (github.com/aya-taleb). Written from scratch, with ideas learned from OpusClip, ViewStats, 1of10 and OutlierKit. This repo is not made by or affiliated with any of them. See CREDITS.md. MIT.
