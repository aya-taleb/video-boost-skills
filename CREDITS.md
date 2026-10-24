# Credits

Everything in this repo was written by Aya Taleb. No text or code was copied from another
project, so there is no upstream license to carry.

## Ideas we learned from (thank you)

These tools showed good ideas. We wrote our own version from scratch. See
`docs/COMPETITORS.md` for what each one does well and where it falls short.

- **OpusClip**: splitting one virality score into stages (Hook, Flow, Value, Trend). Our
  `video-score` gives stage scores too.
- **ViewStats** and **1of10**: the outlier score, a video's views against its channel's usual
  views. Used in `trend-ideas` and `similar-videos`.
- **OutlierKit**: ranking title ideas against breakout videos near the topic. Used in
  `video-packaging`.

## Works well with

Jake Schincariol's free MIT packs
[chatgpt-youtube-agent-skill](https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill) and
[instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) do things this
pack doesn't. We recommend them; we don't copy or ship them. `video-score` can run his
`hookscore.py` if you installed his pack yourself.

## Tools the skills call (not shipped here)

- [ffmpeg and ffprobe](https://ffmpeg.org/), installed by you, for measuring videos.
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (MIT), optional, for transcripts.
- [YouTube Data API v3](https://developers.google.com/youtube/v3), optional, with your own free key.
