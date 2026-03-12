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