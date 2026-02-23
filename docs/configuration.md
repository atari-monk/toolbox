# [Project Toolbox](index.md) - Configuration

## Table of Contents <a id="toc"></a>

- [Pyproject](#pyproject)

- [Gitignore](#gitignore)

- [Strict Type Checking](#pylance)

- [Install](#install)

## Pyproject <a id="pyproject"></a>

Needs to be updated with every new script.  

pyproject.toml

```toml
[project]
name = "toolbox"
version = "0.0.1"

[project.scripts]
toolbox-info = "utils.toolbox_info:main"
proj-tree = "utils.proj_tree:main"

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
```

[⬆ Table of Contents](#toc)

## Gitignore <a id="gitignore"></a>

.gitignore

```text
__pycache__
toolbox.egg-info
.venv
build
```

[⬆ Table of Contents](#toc)

## Strict Type Checking <a id="pylance"></a>

Python project using Pylance with strict type checking.  

### **.vscode/settings.json**

```json
{
  // Python interpreter to use
  "python.pythonPath": ".venv/bin/python3.12",

  // Enable Pylance as the language server
  "python.languageServer": "Pylance",

  // Exclude folders like virtual environments or build artifacts
  "files.exclude": {
    "**/__pycache__": true,
    "**/.venv": true,
    "**/.pytest_cache": true
  }
}
```

### **pyrightconfig.json**

```json
{
  // Strict type checking
  "typeCheckingMode": "strict",

  // Folders to exclude from type checking
  "exclude": ["**/tests", "**/.venv", "**/__pycache__"],

  // Report issues for optional member access
  "reportOptionalMemberAccess": true,

  // Report missing imports
  "reportMissingImports": true,

  // Ignore private usage warnings
  "reportPrivateUsage": false
}
```

### ✅ **How it works**

1. **VS Code `.vscode/settings.json`**:

   * Configures Pylance in the editor.
   * Enables strict type checking while controlling warning vs error levels.

2. **`pyrightconfig.json`**:

   * Ensures the same type checking rules are enforced outside VS Code (CI pipelines, command line, other editors using Pyright).

3. **Consistency**:

   * Both files ensure your project always uses the same type checking rules.
   * Excludes virtual environments, cache folders, and test folders from unnecessary checks.

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