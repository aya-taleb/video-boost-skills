#!/usr/bin/env python3
"""Scan YouTube for what is breaking out right now around a topic (official YouTube Data API v3).

For each search angle it finds recent videos by views, then measures each one:
  views_per_day   views divided by days since posting
  outlier         views divided by the channel's median views of its last 10 uploads (the ViewStats / 1of10 idea)
  views_per_sub   views divided by channel subscribers
  engagement      (likes + comments) / views
and summarizes each angle (demand, breakouts, how many breakouts come from small channels, rising or not).

Needs YOUTUBE_API_KEY. Quota: about 100 units per angle plus about 3 per channel (free daily quota: 10,000).

Usage:
    python3 trend_scan.py --angles "atomic habits" "habit stacking" --region US --lang en --days 90 [--shorts | --long] [--out scan.json]
"""
import argparse
import datetime as dt
import json
import os
import re
import statistics
import sys
import urllib.parse
import urllib.request

API = "https://www.googleapis.com/youtube/v3"
used = 0


def get(path, cost, **params):
    global used
    used += cost
    params["key"] = os.environ["YOUTUBE_API_KEY"]
    with urllib.request.urlopen(f"{API}/{path}?{urllib.parse.urlencode(params)}", timeout=30) as r:
        return json.load(r)


def seconds(iso):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    d, h, mi, s = (int(x or 0) for x in m.groups()) if m else (0, 0, 0, 0)
    return d * 86400 + h * 3600 + mi * 60 + s


LATIN = {"en", "es", "fr", "de", "it", "pt", "nl", "tr", "id", "pl", "sv"}


def key_words(angle):
    words = [w for w in re.findall(r"[\w']+", angle.lower()) if len(w) >= 4]
    return words or [angle.lower()]


def videos(ids):
    out = []
    for i in range(0, len(ids), 50):
        out += get("videos", 1, part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50])).get("items", [])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--angles", nargs="+", required=True)
    ap.add_argument("--region", default="US")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--days", type=int, default=90)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--shorts", action="store_true")
    g.add_argument("--long", action="store_true")
    ap.add_argument("--channels", type=int, default=40, help="max channels to measure for the outlier score")
    ap.add_argument("--loose", action="store_true", help="keep videos whose title does not contain any word of the angle")
    ap.add_argument("--out")
    a = ap.parse_args()
    if not os.environ.get("YOUTUBE_API_KEY"):
        sys.exit("Set YOUTUBE_API_KEY first.")
    now = dt.datetime.now(dt.timezone.utc)
    after = (now - dt.timedelta(days=a.days)).strftime("%Y-%m-%dT%H:%M:%SZ")

    found = {}
    for angle in a.angles:
        s = get("search", 100, part="id", q=angle, type="video", order="viewCount", publishedAfter=after,
                regionCode=a.region, relevanceLanguage=a.lang, maxResults=50,
                videoDuration="short" if a.shorts else "any")
        for it in s.get("items", []):
            found.setdefault(it["id"]["videoId"], set()).add(angle)

    vids = []
    for it in videos(list(found)):
        sec = seconds(it["contentDetails"]["duration"])
        if a.shorts and sec > 180 or a.long and sec <= 180:
            continue
        lang = (it["snippet"].get("defaultAudioLanguage") or it["snippet"].get("defaultLanguage") or "").lower()
        if lang and not lang.startswith(a.lang.lower()):
            continue
        title = it["snippet"]["title"]
        # The language field is often empty or wrong. For Latin-script languages, drop titles mostly in another script.
        letters = [ch for ch in title if ch.isalpha()]
        if a.lang.lower() in LATIN and letters and sum(ord(ch) > 0x24F for ch in letters) / len(letters) > 0.3:
            continue
        # Search also returns loose matches (a band called "Atomic Habitz"); keep titles that contain a word of the angle.
        if not a.loose and not any(w in title.lower() for ang in found[it["id"]] for w in key_words(ang)):
            continue
        st = it.get("statistics", {})
        views = int(st.get("viewCount", 0))
        posted = dt.datetime.fromisoformat(it["snippet"]["publishedAt"].replace("Z", "+00:00"))
        days = max((now - posted).total_seconds() / 86400, 0.5)
        likes, comments = int(st.get("likeCount", 0)), int(st.get("commentCount", 0))
        vids.append({
            "id": it["id"], "url": f"https://www.youtube.com/watch?v={it['id']}",
            "title": it["snippet"]["title"], "channel": it["snippet"]["channelTitle"], "channel_id": it["snippet"]["channelId"],
            "posted": it["snippet"]["publishedAt"][:10], "age_days": round(days, 1), "seconds": sec,
            "views": views, "views_per_day": round(views / days), "engagement": round((likes + comments) / views, 4) if views else 0,
            "angles": sorted(found[it["id"]]),
        })

    # Channel size, then the channel's usual views (median of its last 10 uploads) for the biggest videos' channels.
    ch_ids = list({v["channel_id"] for v in vids})
    chans = {}
    for i in range(0, len(ch_ids), 50):
        for c in get("channels", 1, part="statistics,contentDetails", id=",".join(ch_ids[i:i + 50])).get("items", []):
            chans[c["id"]] = {"subs": int(c["statistics"].get("subscriberCount", 0) or 0), "uploads": c["contentDetails"]["relatedPlaylists"]["uploads"]}
    ranked = sorted(vids, key=lambda v: v["views_per_day"], reverse=True)
    measured = []
    for v in ranked:
        cid = v["channel_id"]
        if cid in measured or len(measured) >= a.channels or cid not in chans:
            continue
        measured.append(cid)
        try:
            pl = get("playlistItems", 1, part="contentDetails", playlistId=chans[cid]["uploads"], maxResults=11)
            ids = [p["contentDetails"]["videoId"] for p in pl.get("items", [])]
            vs = [int(x.get("statistics", {}).get("viewCount", 0)) for x in videos(ids)]
            chans[cid]["median_views"] = statistics.median(vs[:10]) if vs else None
        except Exception as e:  # a private uploads list, for example
            chans[cid]["median_views"] = None
    for v in vids:
        c = chans.get(v["channel_id"], {})
        v["channel_subs"] = c.get("subs")
        v["views_per_sub"] = round(v["views"] / c["subs"], 2) if c.get("subs") else None
        med = c.get("median_views")
        v["outlier"] = round(v["views"] / med, 1) if med else None

    summary = []
    for angle in a.angles:
        vs = sorted([v for v in vids if angle in v["angles"]], key=lambda v: v["views_per_day"], reverse=True)
        top = vs[:10]
        breakouts = [v for v in vs if (v["outlier"] or 0) >= 3]
        young = [v["views_per_day"] for v in vs if v["age_days"] <= a.days / 3]
        old = [v["views_per_day"] for v in vs if v["age_days"] > a.days / 3]
        summary.append({
            "angle": angle, "videos": len(vs),
            "median_views_per_day_top10": round(statistics.median([v["views_per_day"] for v in top])) if top else 0,
            "breakouts_3x": len(breakouts),
            "breakouts_from_small_channels": len([v for v in breakouts if (v["channel_subs"] or 0) < 100_000]),
            "rising": round(statistics.median(young) / statistics.median(old), 2) if young and old and statistics.median(old) else None,
            "top": [{k: v[k] for k in ("title", "channel", "url", "posted", "views", "views_per_day", "outlier", "channel_subs", "seconds")} for v in top[:5]],
        })
    out = {"scanned_on": now.strftime("%Y-%m-%d"), "region": a.region, "language": a.lang, "window_days": a.days,
           "format": "shorts" if a.shorts else "long" if a.long else "any", "quota_used": used, "angles": summary, "videos": vids}
    text = json.dumps(out, indent=2, ensure_ascii=False)
    if a.out:
        open(a.out, "w").write(text)
        print(json.dumps({"saved": a.out, "quota_used": used, "angles": [{k: s[k] for k in ("angle", "videos", "median_views_per_day_top10", "breakouts_3x", "breakouts_from_small_channels", "rising")} for s in summary]}, indent=2))
    else:
        print(text)


if __name__ == "__main__":
    main()
