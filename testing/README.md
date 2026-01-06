# Testing Directory

This directory contains test scripts and resources for verifying the functionality of **Theme-Me**.

##  Running Tests

You can run the full test suite using the runner script:

`ash
python run_tests.py
``n
##  Testing Online Fallback

To verify the online resource fallback mechanism:

1.  **Delete a local resource file** (e.g., a theme):
    `ash
    rm ../data/themes/infernal-reaper.txt
    ``n
2.  **Run the tool** trying to apply that resource:
    `ash
    python ../run.py --theme infernal-reaper
    ``n
3.  **Verify**:
    - The tool should warn that the local file is missing.
    - It should attempt to download from the online repository.
    - The theme should be applied successfully.

##  Directory Structure

- un_tests.py: Main test runner
- 	est_themes.py: Tests for theme application
- 	est_fonts.py: Tests for font application
- 	est_backgrounds.py: Tests for background application

##  Notes

- These tests are designed to run in a **Termux** environment.
- Some tests may fail on Windows/Linux due to missing Termux-specific commands (like 	ermux-reload-settings).
