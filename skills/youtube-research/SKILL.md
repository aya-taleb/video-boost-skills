---
name: youtube-research
description: Researches what is working in long YouTube videos (over 3 minutes) for one topic, market and language - top recent videos and channels, title and thumbnail patterns, hooks and retention, structure, end screens, mistakes, and YouTube's own rules (monetization and inauthentic content, AI disclosure, copyright) - using only sources from the last 12 months (6 with recent). Use when the user asks what works on YouTube for a topic, why long videos fail, or as part of viral-checklist with the youtube platform.
---

# YouTube long-form research

Same method, inputs and output format as `shorts-research` (read it first), for videos longer than 3 minutes. Output: `notes-youtube.json`.

## Where to look, in this order

1. **YouTube's own rules and tips (official):** YouTube Help pages (monetization policies and the inauthentic content clarification, altered or synthetic content, end screens, A/B testing of titles and thumbnails, the Intros metric), the YouTube Official Blog, Creator Insider interviews with YouTube staff. Use the latest version of each page and its date.
2. **Top recent videos and channels in the topic (data, example):** with `YOUTUBE_API_KEY`, run `shorts-research/scripts/top_shorts.py` with `--long` to get videos over 3 minutes. Otherwise search the web. Channel stats pages that show live numbers (for example OutlierKit or vidIQ channel pages) count as `data` with the date you read them; note which numbers are estimates.
3. **Studies and analysis:** retention benchmarks by length, hook studies, title and thumbnail studies, with sample size and dates. Say clearly when a benchmark comes from one company's own channel.
4. **Failures:** templated or mass-produced videos, misleading titles, slow intros, copyright risk for the topic (for book summaries: summarize ideas in your own words, keep quotes short, credit the author, do not read the book aloud).

## What to pull out

Title and thumbnail patterns; the first 30 seconds (what top videos do, and the Intros metric); length that fits the topic; structure (chapters, numbered takeaways, payoff); pace (how often the visual changes); narration and voice; on-screen text; examples and stories; calls to action and where they sit; end screens (last 5 to 20 seconds, video must be 25 seconds or longer); series and playlists; posting rhythm; monetization and policy rules; topic-specific risks.

Then run `source-check`.
