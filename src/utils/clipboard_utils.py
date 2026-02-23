#!/usr/bin/env python3
"""
Clipboard helpers for Linux (Ubuntu) using xclip/xsel.
"""

import subprocess
import shutil

clip_cmd: str

if shutil.which("xclip"):
    clip_cmd = "xclip"
elif shutil.which("xsel"):
    clip_cmd = "xsel"
else:
    raise RuntimeError(
        "Either 'xclip' or 'xsel' must be installed for clipboard access.\n"
        "Install with: sudo apt install xclip"
    )


def copy_to_clipboard(text: str) -> None:
    """Copy text to the system clipboard."""
    if clip_cmd == "xclip":
        process = subprocess.Popen(
            ["xclip", "-selection", "clipboard"],
            stdin=subprocess.PIPE,
            close_fds=True,
        )
        process.communicate(input=text.encode("utf-8"))
    else:  # xsel
        process = subprocess.Popen(
            ["xsel", "--clipboard", "--input"],
            stdin=subprocess.PIPE,
            close_fds=True,
        )
        process.communicate(input=text.encode("utf-8"))


def paste_from_clipboard() -> str:
    """Get text from the system clipboard."""
    try:
        if clip_cmd == "xclip":
            return subprocess.check_output(
                ["xclip", "-selection", "clipboard", "-o"]
            ).decode("utf-8")
        else:  # xsel
            return subprocess.check_output(
                ["xsel", "--clipboard", "--output"]
            ).decode("utf-8")
    except subprocess.CalledProcessError:
        return ""


if __name__ == "__main__":
    # quick test
    sample = "Hello from clipboard_utils!"
    copy_to_clipboard(sample)
    print("Copied to clipboard:", paste_from_clipboard())
