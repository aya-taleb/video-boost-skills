---
name: video-packaging
description: Proposes everything around the video before it goes out - 3 titles to A/B test, the description (with chapters, credits and links), hashtags, thumbnail ideas, and a short list of changes to the video itself - each tied to a checklist rule, a similar-video finding or a platform rule. Use when the user asks for a title, description, hashtags, thumbnail ideas, how to package this video, or what to change before publishing.
---

# Video packaging

Writes the title, description and the rest, and lists the changes worth making to the video. Every proposal says why, so the user can judge it.

## Inputs

- The video (or its transcript and the `video-score` metrics)
- `checklist.json` from viral-checklist (if there is one)
- `similar-videos.json` from similar-videos (if there is one)
- Platform, market, language (defaults: youtube, US, en)
- The channel name and any links the user wants in the description

## What to write

1. **3 titles** for YouTube's A/B test. Each a different angle (for example: the promise, the number, the question). YouTube allows 100 characters; keep the main words in the first 60 or so so they show in search and on phones (check the current display length if the research found one; do not guess a number). No misleading clickbait: YouTube's spam policy bans titles that trick people into clicking. Say which rule or pattern each title follows.
2. **Description:**
   - First 2 lines: what the viewer gets, with the main words people search for. Write it for people, not for keyword stuffing (excessive tags in the description break YouTube's spam policy).
   - Chapters: first at 00:00, at least 3, ascending, each 10 seconds or longer (YouTube's chapter rules). Only for times that exist in the video.
   - Credits: the book and author, or the sources used for facts.
   - Links the user gave. Mark affiliate links as affiliate.
   - Disclosures: AI use if it applies, paid promotion if it applies.
3. **Hashtags:** 3 to 5 that are directly about the video. YouTube shows up to 3 above the title, ignores all hashtags past 60, and treats unrelated hashtags as misleading.
4. **Thumbnail ideas:** 3 concepts for the A/B test: what is in the frame, the words (5 or fewer), the face or character, the contrast. Do not promise anything the video does not show.
5. **Changes to the video:** up to 5, most important first. Each one names the failed checklist item or the similar-videos finding it fixes, and how much work it is (small, medium, large).

## Output

`packaging.md` with the 5 parts above, in that order, ready to paste into YouTube Studio.

## Rules

- Never invent a fact about the video's content. Only use what is in the transcript or on screen.
- Titles and thumbnails must match the video.
- Plain words, the user's tone. No hype words.
