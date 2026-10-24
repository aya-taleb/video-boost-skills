---
name: publish-ruler
description: The ruler. Reads YouTube's own upload steps and policies (live help pages) and builds a step-by-step pre-publish checklist in the same order as the YouTube Studio upload flow - details, audience, disclosures, chapters, captions, end screen, ad suitability, Checks, visibility - then fills it in for one video with done, to do, or blocked. Use when the user says pre-publish checklist, is this ready to upload, check before publishing, or what do I need to set in YouTube Studio.
---

# Publish ruler

A step-by-step list of everything to set and check before a YouTube video goes public, built from YouTube's own pages, in the order YouTube Studio shows them.

## Step 1: Refresh the rules

YouTube changes these pages often. Open each one (web fetch) and note anything new. These are live official pages: record the date you read them.

| Rule | Page |
|---|---|
| Upload steps and limits | support.google.com/youtube/answer/57407 |
| Custom thumbnails | support.google.com/youtube/answer/72431 |
| Hashtags | support.google.com/youtube/answer/6390658 |
| Tags | support.google.com/youtube/answer/146402 |
| Chapters | support.google.com/youtube/answer/9884579 |
| End screens | support.google.com/youtube/answer/6388789 |
| AI and altered content disclosure | support.google.com/youtube/answer/14328491 |
| Spam, deceptive practices and scams | support.google.com/youtube/answer/2801973 |
| Fake engagement | support.google.com/youtube/answer/3399767 |
| Advertiser-friendly guidelines | support.google.com/youtube/answer/6162278 |
| Monetization policies (inauthentic content) | search "YouTube channel monetization policies" on support.google.com |
| Made for kids | search "Determine if your content is made for kids" on support.google.com |

If a page has changed a rule below, use the page, update the rule, and say so in the report.

## Step 2: The checklist, in upload order

Each line: what to set or check · the rule · how to verify.

**A. Before you upload**
1. Final file: 16:9 for a video (9:16 for a Short), the length you planned, sound on, no stray black frames or long silences (use `video-score` metrics).
2. Rights: you own or have the rights to every picture, clip, sound and music in it. Book or other works are summarized in your own words with short quotes only.
3. Policy pass: no AI expert persona giving health, legal or money advice; not a templated copy of your other videos.

**B. Details**
4. Title: 100 characters or fewer, matches the video, not misleading.
5. Description: 5,000 characters or fewer; first lines say what the viewer gets; no lists of keywords or excessive tags (spam policy).
6. Thumbnail: JPG or PNG, 16:9, at least 640 px wide (3840x2160 recommended), 50 MB or less on desktop; follows the Community Guidelines; matches the video. Custom thumbnails need a verified account.
7. Playlist: add it to the right series playlist.
8. Audience: answer "made for kids" honestly (required by law, COPPA). Made for kids turns off comments, end screens, cards, notifications and more.
9. Age restriction: only if the content needs it.

**C. Show more**
10. Paid promotion: tick it if anyone paid or gave something for a mention.
11. Altered content: "yes" only if it looks realistic (real people, real events, realistic scenes, AI music as the main focus). Clearly animated content does not need it.
12. Chapters: in the description, first at 00:00, at least 3, ascending, each 10 seconds or longer.
13. Tags: a few, directly related; they play a minimal role in discovery.
14. Hashtags: 3 to 5, related; up to 3 show above the title; more than 60 and all are ignored.
15. Language, caption certification, category, comments: set them.

**D. Video elements**
16. Captions: upload or check the auto captions (names and numbers spelled right).
17. End screen: the video must be 25 seconds or longer; it runs in the last 5 to 20 seconds; up to 4 elements; leave room for it in the edit.
18. Cards: link the related video at the right moment.

**E. Monetization (YouTube Partner Program only)**
19. Self-certify ad suitability honestly against the advertiser-friendly topics (language, violence, adult content, shocking, harmful acts, hate, drugs, firearms, controversial issues, sensitive events, dishonest behavior, content for kids, incendiary, tobacco). Titles, thumbnails, descriptions and tags count too.

**F. Checks**
20. Wait for the copyright check. Fix or dispute any claim before going public.

**G. Visibility**
21. Upload as private or unlisted first, watch it once on a phone, then schedule or publish.
22. After publishing: set up the title and thumbnail A/B test (up to 3), pin a comment, and log the results for `video-score` after 7 days.

## Step 3: Fill it in for the video

For each line write `done`, `to do` (with the exact action), `blocked` (with why), or `n/a`. Use `video-score` metrics and `video-packaging` output when they exist. Anything that can only be set inside YouTube Studio is `to do` until the user confirms it.

## Output

`prepublish.md`: the filled checklist, the rule changes found in Step 1, and the list of pages with the date read.
