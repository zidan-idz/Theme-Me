#!/bin/bash

echo -e "\033[92m[Theme-Me v3.0] Installing..."

# Install dependencies
pkg install python -y

# Ensure data directory permissions
chmod -R 755 data/

# Run the download script if resources are missing (optional, but good for first run if cloned without data)
# But since we want offline, we assume data is there.
# If not, we can try to run it.
if [ ! -d "data/fonts" ] || [ ! -d "data/backgrounds" ]; then
    echo -e "\033[93m[Warning] Offline resources missing. Please ensure data folder is populated."
fi

echo -e "\033[92m[Success] Installation complete!"
echo -e "\033[96mPlease see README.md for more information."
