#!/usr/bin/env python3
"""Top recent YouTube videos for a topic, from the official YouTube Data API v3.

Shorts (3 minutes or less) by default; --long for videos over 3 minutes.
Needs YOUTUBE_API_KEY (free, from a Google Cloud project with "YouTube Data API v3" turned on).
Quota: about 101 units per run (search 100 + videos 1) out of 10,000 free per day.

Usage:
    python3 top_shorts.py --topic "travel tips" [--region US] [--lang en] [--months 12] [--max 25] [--long]
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.parse
import urllib.request

API = "https://www.googleapis.com/youtube/v3"


def get(path, **params):
    params["key"] = os.environ["YOUTUBE_API_KEY"]
    with urllib.request.urlopen(f"{API}/{path}?{urllib.parse.urlencode(params)}", timeout=30) as r:
        return json.load(r)


def seconds(iso):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    d, h, mi, s = (int(x or 0) for x in m.groups()) if m else (0, 0, 0, 0)
    return d * 86400 + h * 3600 + mi * 60 + s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--region", default="US")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--months", type=int, default=12)
    ap.add_argument("--max", type=int, default=25)
    ap.add_argument("--long", action="store_true", help="videos over 3 minutes instead of Shorts")
    a = ap.parse_args()
    if not os.environ.get("YOUTUBE_API_KEY"):
        sys.exit("Set YOUTUBE_API_KEY first. Without it, search the web for recent top videos instead.")
    after = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=30 * a.months)).strftime("%Y-%m-%dT%H:%M:%SZ")
    s = get("search", part="id", q=a.topic, type="video", order="viewCount", publishedAfter=after,
            regionCode=a.region, relevanceLanguage=a.lang, maxResults=50,
            videoDuration="any" if a.long else "short")
    ids = [i["id"]["videoId"] for i in s.get("items", [])]
    if not ids:
        print("[]"); return
    v = get("videos", part="snippet,statistics,contentDetails", id=",".join(ids))
    out = []
    for it in v.get("items", []):
        sec = seconds(it["contentDetails"]["duration"])
        if (sec > 180) != a.long:
            continue
        st = it.get("statistics", {})
        out.append({
            "url": f"https://www.youtube.com/watch?v={it['id']}",
            "title": it["snippet"]["title"],
            "channel": it["snippet"]["channelTitle"],
            "posted": it["snippet"]["publishedAt"][:10],
            "seconds": sec,
            "views": int(st.get("viewCount", 0)),
            "likes": int(st["likeCount"]) if "likeCount" in st else None,
            "comments": int(st["commentCount"]) if "commentCount" in st else None,
            "language": it["snippet"].get("defaultAudioLanguage") or it["snippet"].get("defaultLanguage"),
        })
    out.sort(key=lambda x: x["views"], reverse=True)
    print(json.dumps(out[: a.max], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
