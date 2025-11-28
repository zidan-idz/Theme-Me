<div align="center">
  <img src="docs/logo.png" width="700" title="logo" alt="Theme-Me">
</div>

<div align="center">

[![Author](https://img.shields.io/badge/Author-Zidan%20IDz-%23FF0000?style=for-the-badge&logo=github)](https://github.com/zidan-idz)
[![Version](https://img.shields.io/badge/Version-3.0%20(Stable)-%23FF0000?style=for-the-badge)](https://github.com/zidan-idz/Theme-Me/releases)
[![Language](https://img.shields.io/badge/Language-Python-%23FF0000?style=for-the-badge&logo=python)](https://www.python.org/)
[![Environment](https://img.shields.io/badge/Environment-Termux-%23FF0000?style=for-the-badge&logo=termux)](https://termux.com/)

</div>

---

## 📖 Description
**Theme-Me** is a simple customization tool designed specifically for **Termux**. It allows you to completely transform your terminal's appearance with custom themes, fonts, and color schemes (backgrounds).

### ✨ Key Features
*   🎨 **20+ Unique Themes** - each with custom ASCII art
*   🔤 **20+ Unique Fonts** - enhance your terminal readability
*   🌈 **20+ Color Schemes** - from dark modes to vibrant palettes
*   🧭 **Dual Mode** - interactive menu & CLI arguments
*   ♻️ **Restore Defaults** - revert Termux back to its original look
*   🔄 **Update Tool** - check and apply the latest updates
*   ⚡ **Offline Support** - works fully offline after initial setup

---

## 📦 Installation
```bash
# Update packages
pkg update && pkg upgrade -y

# Install Git
pkg install git -y

# Clone the repository
git clone https://github.com/zidan-idz/Theme-Me

# Enter directory
cd Theme-Me

# Run installation
bash install.sh

```

---

## 🖥️ Interactive Mode
To enter the interactive menu.
```bash
# Start the tool with Interactive Mode
python run.py
```

Once inside, simply choose the number of the action you want to perform.  
**For example:** Enter `1` to change the theme. After selecting it, a list of themes will appear along with their IDs, Example `Onic`.  
Just **copy the ID** of the theme you want, paste it, and confirm.  
Wait a moment and your theme will be applied instantly! ✨

The same process applies to **fonts** and **backgrounds**:  
*pick the menu number → choose an ID → done.*

---

## ⚡ CLI Mode (Command Line Interface)
For advanced users, **Theme-Me** supports command-line arguments for quick actions.

| Argument | Description | Example |
| :--- | :--- | :--- |
| `--theme <name/id>` | Apply a specific theme | `python run.py --theme "Onic"` |
| `--font <name/id>` | Apply a specific font | `python run.py --font "FiraCode"` |
| `--background <name/id>` | Apply a specific background | `python run.py --background "Dracula"` |
| `--list <type>` | List available options | `python run.py --list theme` |
| `--preview <id>` | Preview a theme in browser | `python run.py --preview 1` |
| `--restore` | Restore default settings | `python run.py --restore` |
| `--about` | Show about information | `python run.py --about` |
| `--version` | Show version information | `python run.py --version` |

---

## 📸 Screenshots
<div align="center">
  <img src="docs/img1.png" width="48%" title="Main Menu" alt="Main Menu">
  <img src="docs/img2.png" width="48%" title="Theme Menu" alt="Theme Menu">
  <img src="docs/img3.png" width="48%" title="Font Menu" alt="Font Menu">
  <img src="docs/img4.png" width="48%" title="Background Menu" alt="Background Menu">
</div>

---

## ⚠️ Disclaimer
This tool modifies Termux configuration files. While it includes a restore feature, **please use at your own risk**. The author is not responsible for any data loss or system issues that may occur from using this tool.

**Recommendations:**
- Backup your Termux configuration before using this tool
- Test on a non-critical Termux installation first
- Use the "Restore Defaults" feature if you encounter any issues

## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/zidan-idz">Zidan IDz</a>
</div>
