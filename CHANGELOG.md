# Changelog

All notable changes to this project will be documented in this file.

## [3.1] - 2026 (Yuzuki)
**Security & Stability Improvements**

### Improved
- **Clean Installation**: Optimized `install.sh` to only copy necessary files, reducing storage usage and clutter.
- **Dependency Management**: Added `termux-tools` to ensure all external commands (like `xdg-open`) work correctly.
- **Environment Safety**: Added strict checks to warn users when running outside Termux.

### Safety
- **Auto-Backup**: The tool now automatically creates a backup of your `bash.bashrc` (`bash.bashrc.bak`) before applying any themes, preventing potential shell lockouts.

## [3.0] - 2025 (Shunkan)
**Rebuild 2**

### Added
- **Modular Structure**: Refactored the entire codebase into a modular architecture for better maintainability.
- **Dual Mode**: Added support for both **CLI** (Command Line Interface) and **Interactive** modes.
- **New Features**:
    - **Restore**: Ability to restore default settings.
    - **Update Tools**: Built-in feature to check and apply updates.
- **UI/UX**:
    - Redesigned interactive tools with a **simple and minimalist** aesthetic.
    - Added loading animations with random tips.
- **Documentation**: Added `theme-me.log` and `CHANGELOG.md`.

## [0.3.7] - 2024 (BETA)
**Rebuild 1**

### Added
- **Features**: Included options for changing **Themes**, **Fonts**, and **Backgrounds**.
- **Structure**: Initial rebuild attempt from the original version.

### Notes
- The project structure in this version was still disorganized compared to the current modular approach.

## [Initial Release] - 2020-2023
**Original Version**

### Added
- Basic script for Termux customization.
- Simple theme application.
