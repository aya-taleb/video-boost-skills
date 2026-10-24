# Competitors: what they do well, where they fall short, what we take

Checked 2026-10-23. Most pages below are written by one of the competitors, so prices and claims are their own; each line says whose page it is.

## Research and analytics tools

| Tool | Price (monthly) | Best at | Gaps |
|---|---|---|---|
| vidIQ | free (150 AI credits); Boost $39; Max $39 billed yearly (1of10's page, 2026-08-01) | keyword research, Daily Ideas from your channel, AI coach, Chrome overlay | coach advice is generic and pushes upgrades; credits run out; keyword-first, misses browse traffic; no outlier database (1of10's and OutlierKit's pages) |
| TubeBuddy | Pro $12, Legend $27 billed yearly (OutlierKit's page, verified 2026-06-23) | cheap SEO, thumbnail A/B tests, bulk edits | older keyword-first approach |
| 1of10 | free (60 credits); Basic $19; Pro $89 (1of10's own blog) | outlier videos 10x to 100x above their channel's average; titles, thumbnails and ideas from proven videos | not a keyword tool |
| ViewStats (MrBeast) | free; Pro $49 or $499 a year (creatoreconomytools, 2026) | outlier multiplier vs the channel's median of its last 10 videos; title and thumbnail change history | revenue estimates off by 300 to 500%; small channels not indexed; AI thumbnail remix drew attribution backlash |
| OutlierKit | from $49; Pro $99; Max $399 (its own page) | outliers, niche and viral idea reports, 16 titles ranked against breakout videos near your topic, API and Claude connector | does not write scripts or thumbnails |
| OpusClip | free; Starter $15; Pro $29 (quso.ai, a competitor, 2026-10-20) | clips long videos you own; virality score out of 100 split into Hook, Flow, Value, Trend | how the score is weighted is not explained; needs your own footage |
| Spotter Studio | closed to creators on 2025-10-22 (OutlierKit's page) | was AI ideation | gone |

## Faceless and AI video makers

| Tool | From (monthly) | Best at | Gaps |
|---|---|---|---|
| Revid | $39 | scripts, AI video, 70+ languages, auto-posting, API | credit use varies a lot; voice cloning only on $199 plan |
| AutoShorts.ai | $19 | autopilot series posting | 90 s max; still images by default; one series per plan |
| StoryShort | $39 | consistent characters, long-form on higher plans | credits |
| Faceless.video | $20 | autopilot posting | 15 videos at entry; premium models per scene |
| InVideo AI | $9 | prompt to video, timeline editor | stops at the file |
| Pictory, Fliki | $25 to $29 | article or voice to video, stock footage | stock-heavy look |

(All from easyviral.ai, a competitor, 2026-10-20.)

## The big gap in the market

- The makers push **volume on autopilot** (series, auto-posting, short caps, stills). That is exactly the "templated, mass-produced" pattern YouTube stopped paying for (clarified 2026-07-16; 16 AI channels removed in January to February 2026).
- The research tools stop at **insight**. None of them takes you from a trending idea to a finished, original, policy-checked video.
- Nobody shows the **reason** behind a score with dated sources, or the **exact cost** of each video.

## What we take (and where it goes)

| Idea | From | Goes into |
|---|---|---|
| Outlier multiplier: a video's views vs its channel's usual views | ViewStats, 1of10, OutlierKit | `trend-ideas` ranking, `similar-videos` table |
| Rank generated titles against real breakout titles near the topic | OutlierKit | `video-packaging` (10 to 16 candidates, top 3 kept) |
| Score split into parts (Hook, Flow, Value, Trend) | OpusClip | `video-score` stage scores |
| Ideas fitted to your own channel | vidIQ Daily Ideas | studio Ideas page (uses your categories and characters) |
| Test packaging after publishing | TubeBuddy, YouTube A/B | `publish-ruler` step 22 and results logging |
| Consistent characters | StoryShort | already in the studio (character looks) |

## What we do differently

- Human director in the loop (script room, review notes), never autopilot posting.
- Every rule and every idea has a dated source; no revenue estimates.
- Policy check before publishing (the ruler).
- Exact cost per video shown before and after.

## Sources
- [OutlierKit: YouTube tool pricing](https://outlierkit.com/resources/youtube-tool-pricing/) (verified 2026-06-23, OutlierKit's own page)
- [1of10: vidIQ review](https://1of10.com/blog/vidiq-review/) (2026-08-01, 1of10's own blog)
- [OutlierKit: vidIQ review](https://outlierkit.com/resources/vidiq-review/) (2026-07-01, updated 2026-09)
- [creatoreconomytools: ViewStats](https://creatoreconomytools.com/tool/viewstats) (2026)
- [quso.ai: OpusClip review](https://quso.ai/blog/opus-clip-review) (2026-10-20, a competitor)
- [easyviral.ai: Revid alternatives](https://easyviral.ai/blog/best-revid-ai-alternatives-2026) (2026-10-20, a competitor)
- [Tubefilter: inauthentic content clarification](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/) (2026-07-13)
- [The Next Web: AI slop purge](https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage)
