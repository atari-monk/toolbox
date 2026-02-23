import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union, Mapping, Sequence, cast
from .clipboard_utils import copy_to_clipboard

# ------------------------
# ANSI colors for terminal
# ------------------------
RESET_COLOR = "\033[0m"
FOLDER_COLOR = "\033[94m"  # Blue
FILE_COLOR = "\033[92m"    # Green

# ------------------------
# Config
# ------------------------
CONFIG_FILE = Path(
    "/home/atari-monk/atari-monk/project/script/src/utils/tree.json"
)

@dataclass(frozen=True, slots=True)
class IgnoreConfig:
    folders: tuple[str, ...]
    files: tuple[str, ...]

@dataclass(frozen=True, slots=True)
class Config:
    ignore: IgnoreConfig

DEFAULT_CONFIG = Config(
    ignore=IgnoreConfig(folders=(), files=())
)

# ------------------------
# Load config
# ------------------------
def _only_strings(seq: Sequence[object]) -> tuple[str, ...]:
    return tuple(item for item in seq if isinstance(item, str))

def load_config() -> Config:
    if not CONFIG_FILE.exists():
        return DEFAULT_CONFIG
    try:
        with CONFIG_FILE.open("r", encoding="utf-8") as f:
            raw = json.load(f)

        if not isinstance(raw, Mapping):
            return DEFAULT_CONFIG

        data = cast(Mapping[str, object], raw)
        ignore_obj = data.get("ignore")
        if not isinstance(ignore_obj, Mapping):
            return DEFAULT_CONFIG

        ignore_map = cast(Mapping[str, object], ignore_obj)
        folders_obj = ignore_map.get("folders")
        files_obj = ignore_map.get("files")
        if not isinstance(folders_obj, Sequence) or not isinstance(files_obj, Sequence):
            return DEFAULT_CONFIG

        return Config(
            ignore=IgnoreConfig(
                folders=_only_strings(cast(Sequence[object], folders_obj)),
                files=_only_strings(cast(Sequence[object], files_obj)),
            )
        )
    except Exception as e:
        print(f"Error loading config.json: {e}")
        return DEFAULT_CONFIG

# ------------------------
# Tree logic
# ------------------------
def should_ignore(path: Path, config: Config) -> bool:
    name = path.name
    if path.is_dir():
        return name in config.ignore.folders
    return name in config.ignore.files

def build_tree(
    path: Path,
    config: Config,
    prefix: str = "",
    level: int = 0,
    max_level: Optional[int] = None,
    color: bool = True
) -> List[str]:
    if max_level is not None and level >= max_level:
        return []

    try:
        items: List[Path] = [p for p in path.iterdir() if not should_ignore(p, config)]
    except PermissionError:
        return [f"{prefix}└── [Permission denied]"]

    items.sort(key=lambda p: (p.is_file(), p.name.lower()))
    lines: List[str] = []

    for i, item in enumerate(items):
        last = i == len(items) - 1
        connector = "└── " if last else "├── "
        if color:
            name_display = f"{FOLDER_COLOR}{item.name}{RESET_COLOR}/" if item.is_dir() else f"{FILE_COLOR}{item.name}{RESET_COLOR}"
        else:
            name_display = f"{item.name}/" if item.is_dir() else item.name
        lines.append(f"{prefix}{connector}{name_display}")

        if item.is_dir():
            extension = "    " if last else "│   "
            lines.extend(build_tree(item, config, prefix + extension, level + 1, max_level, color=color))

    return lines

def generate_tree(
    path: Union[str, Path],
    config: Config,
    max_level: Optional[int] = None,
    color: bool = True
) -> str:
    root = Path(path).resolve()
    if not root.exists():
        return f"Error: {root} does not exist"

    if root.is_file():
        return root.name

    if color:
        root_name = f"{FOLDER_COLOR}{root.name}{RESET_COLOR}/"
    else:
        root_name = f"{root.name}/"

    lines: List[str] = [root_name]
    lines.extend(build_tree(root, config, max_level=max_level, color=color))
    return "\n".join(lines)

# ------------------------
# CLI
# ------------------------
def main() -> None:
    config = load_config()
    parser = argparse.ArgumentParser(description="Print directory tree")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("-l", "--level", type=int, help="Max depth")
    parser.add_argument("-c", "--clipboard", action="store_true")
    parser.add_argument("-s", "--show-ignore", action="store_true")
    args = parser.parse_args()

    if args.show_ignore:
        print(json.dumps(config.__dict__, indent=2, default=list))
        return

    output = generate_tree(args.path, config, args.level, color=not args.clipboard)

    if args.clipboard:
        copy_to_clipboard(output)
        print("Copied to clipboard")
    else:
        print(output)

if __name__ == "__main__":
    main()