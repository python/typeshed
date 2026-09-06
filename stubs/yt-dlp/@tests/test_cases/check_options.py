from yt_dlp import YoutubeDL, YoutubeDLOptions

options: YoutubeDLOptions = {"quiet": True, "extract_flat": True}
YoutubeDL(options)

YoutubeDL({"quiet": "yes"})  # type: ignore[arg-type]
