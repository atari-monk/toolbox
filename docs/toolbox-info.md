# [Toolbox](index.md) - Toolbox Info

## Table of Contents <a id="toc"></a>

- [Script](#script)

- [Usage Example](#usage)

## Script <a id="script"></a>

Pros:  
    - Simplest script to print aliases of cli tools available in package

Cons:  
    - Every time script is added code of the script changes

src/utils/toolbox_info.py

```py
import argparse

COMMANDS = {
    'toolbox-info': 'Show available toolbox commands',
    'proj-tree': 'Print the directory tree of current or chosen path',
    'yt-mp3': 'YouTube url to mp3'
}

def main():
    parser = argparse.ArgumentParser(description='Toolbox command overview')
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show command descriptions'
    )

    args = parser.parse_args()

    if args.verbose:
        print("Commands and descriptions:")
        for key, description in COMMANDS.items():
            print(f"  {key}: {description}")
    else:
        print("Commands:")
        for key in COMMANDS:
            print(f"  {key}")

if __name__ == "__main__":
    main()
```

[⬆ Table of Contents](#toc)

## Usage Example <a id="usage"></a>

Print the list of available toolbox commands (default, concise):

```sh
toolbox-info
```

Show commands **with descriptions** using the verbose flag (`--verbose` or `-v`):

```sh
toolbox-info --verbose
# short form:
toolbox-info -v
```

[⬆ Table of Contents](#toc)
