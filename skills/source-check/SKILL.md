---
name: source-check
description: Checks research notes before they become rules - every finding needs a working link, a publish date inside the time window (12 months by default, 6 with recent), the right market and language (US and English by default), and numbers that match their source. Use after shorts-research, reels-research or tiktok-research, or when the user says check these sources, verify this research, or are these sources recent.
---

# Source check

Research is only useful if it is true now, for this market and this platform. This skill checks every finding in a research notes file and drops or downgrades what fails.

Input: one or more `notes-<platform>.json` files (format in `shared/checklist-format.md`), plus the settings they were made with: market, language, window in months.

Output: the same files, cleaned, plus `source-report.md` that lists what was dropped and why.

## Steps

For every finding, for every source in it:

1. **Open the link.** Use the web fetch tool. If the page will not load, try once more. If it still fails, mark the source `unreachable`.
2. **Find the publish date on the page.** Look for the article date, the post date, or "updated on". Use the date printed on the page, not the date in the search result. If there is no date anywhere, mark it `undated`. One exception: a platform's own live help or policy page (for example support.google.com/youtube, help.instagram.com, support.tiktok.com) shows the rule as it is today. Keep it with `"published": null, "accessed": "<today>", "type": "official"`.
3. **Check the window.** Today minus the window (12 months by default, 6 if the user asked for recent). A source older than that is `too_old`. An "updated on" date counts only if the part you quote was clearly part of the update.
4. **Check the scope.** Does the source talk about this platform? This market (country)? This language? A global platform announcement is fine and is marked `"scope": "global"`. A study of another country is `wrong_market` unless the finding says so.
5. **Check the claim against the page.** The claim and every number in it must be on the page. Read the sentence around it. Watch for:
   - a number from a different year or a different platform on the same page
   - "up to" or "as much as" turned into an average
   - a creator survey reported as if it were platform data
   - an ad (paid) result reported as organic
   If the page does not support the claim, mark it `not_supported` and write what the page actually says.
6. **Rate the source type.** `official` (the platform's own help pages, newsroom, blog, creator accounts, policy pages), `data` (a study or dataset that states its sample size and dates), `analysis` (an expert article), `example` (a video). Marketing pages that sell a tool count as `analysis` at best.

Then for every finding:

- No sources left: drop the finding.
- Only `example` sources: confidence `low`, and it can only become a `nice` rule.
- One `official` source, or two independent non-official sources that agree: confidence `high`.
- Otherwise: `medium`.
- Two sources that disagree: keep the finding, set confidence `medium` at most, and add a `conflict` note with both sides.

## Rules that never bend

- Never fill in a missing date with a guess.
- Never keep a number you could not find on the page.
- Never upgrade a source type to make a finding pass.
- If a whole platform ends up with fewer than 5 findings, say so in the report as a gap. Do not pad it with old or off-market sources.

## Report format (`source-report.md`)

```
Source check: tiktok, travel tips, US, en, last 12 months (checked 2026-10-23)

Kept: 21 findings (9 high, 8 medium, 4 low)
Dropped: 6
  tt-03  too_old         creatoracademy page last updated 2024-11-02
  tt-09  not_supported   page says "up to 34% more reach", note said "34% more reach"
  tt-12  wrong_market    study of UK creators only
Conflicts: 1
  tt-15  ideal length: 21-34 s (source A, 2026-05) vs 60 s+ (source B, 2026-08)
Gaps: no 2026 official data on posting times for the US
```

Plain words in the report. Short lines. No source is "trusted" just because it ranks high in search.
