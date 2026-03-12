# [Toolbox](index.md) - Yt to Mp3

Downloads yt video as mp3  

## Table of Contents <a id="toc"></a>

- [Yt to Mp3](#yt-mp3)

## Yt to Mp3 <a id="yt-mp3"></a>

Shell command  to download video as mp3

```sh
yt-dlp \
-f 251 \
-x --audio-format mp3 \
-c \
--restrict-filenames \
-o "%(id)s.%(ext)s" \
https://youtu.be/81EGRHFFnzM
```

Shell command  to download video

```sh
yt-dlp -f "bv*+ba/b" --merge-output-format mp4 -c --fragment-retries infinite --retries infinite URL
```

src/utils/yt_to_mp3.py  

```py
from yt_dlp import YoutubeDL
from typing import Any
import sys


def download_audio(url: str) -> None:
    ydl_opts: dict[str, Any] = {
        "format": "251",
        "outtmpl": "%(id)s.%(ext)s",
        "restrictfilenames": True,
        "continuedl": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:  # type: ignore[arg-type]
        ydl.download([url])


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python download.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]
    download_audio(url)


if __name__ == "__main__":
    main()
```

[⬆ Table of Contents](#toc)
