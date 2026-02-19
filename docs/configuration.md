# [Story of Project Toolbox](index.md) - Project Configuration

## Table of Contents <a id="toc"></a>

- [Project Configuration](#project-configuration)
  - [Pyproject](#pyproject)
  - [Gitignore](#gitignore)

- [Info Script](#info)

- [Install](#install)

## Project Configuration <a id="project-configuration"></a>

### Pyproject <a id="pyproject"></a>

pyproject.toml

```toml
[project]
name = "toolbox"
version = "0.0.1"

[project.scripts]
toolbox-info = "utils.toolbox_info:main"

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
```

[⬆ Table of Contents](#toc)

### Gitignore <a id="gitignore"></a>

.gitignore

```text
__pycache__
toolbox.egg-info
.venv
build
```

[⬆ Table of Contents](#toc)

## Info Script <a id="info"></a>

src/utils/toolbox_info.py

```py
import argparse

COMMANDS = {
    'toolbox-info': 'Show available toolbox commands'
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

## Install <a id="install"></a>

Install scripts so they work globally on Ubuntu using **pipx**  
It covers both building and isolation, and you don’t need to manually create a venv.  

### **1️⃣ Ensure pipx is installed**

```bash
sudo apt install pipx
pipx ensurepath
```

> Close and reopen your terminal, or run `source ~/.bashrc` to update PATH.

---

### **2️⃣ Remove old pipx installs (optional, to avoid conflicts)**

```bash
pipx uninstall toolbox
```

> This clears any previous installations of your project.

---

### **3️⃣ Install your project via pipx**

Go to your project folder:

```bash
cd ~/atari-monk/atari-monk/project/toolbox
pipx install .
```

> This creates an isolated environment and installs all `[project.scripts]` (`toolbox-info`, etc.) into `~/.local/bin`.

---

### **4️⃣ Make sure `~/.local/bin` is in your PATH**

Check:

```bash
echo $PATH | tr ':' '\n' | grep '.local/bin'
```

* If nothing shows, add this line to `~/.bashrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload:

```bash
source ~/.bashrc
```

---

### **5️⃣ Test your scripts**

```bash
toolbox-info
```

They should now work **from any terminal**, both VS Code and normal Ubuntu terminal.

---

✅ **Optional tip:** If you have conflicts with system commands (like `zip`), consider renaming your script in `pyproject.toml` so pipx doesn’t clash.

```bash
cd ~/atari-monk/atari-monk/project/toolbox
pipx install --force .
```

### Dependencies

Dependencies must be stated in toml, for example

```toml
dependencies = [
    "some-lib-name"
]
```

and reinstall

---

If you want, I can also write a **one-liner** that does steps 2–4 automatically, cleaning old installs and making all scripts globally available.

[⬆ Table of Contents](#toc)