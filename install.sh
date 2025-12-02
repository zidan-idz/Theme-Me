#!/data/data/com.termux/files/usr/bin/bash
echo "[Theme-Me v3.0] Installing..."
# Install dependencies
pkg install python -y 
pkg install git -y
# Set permissions
chmod -R 755 data/
# Create symlink
INSTALL_DIR="$PREFIX/share/theme-me"
mkdir -p "$INSTALL_DIR"
cp -r . "$INSTALL_DIR/"

# Create executable wrapper
if [ ! -f "$PREFIX/bin/theme-me" ]; then
    echo '#!/data/data/com.termux/files/usr/bin/bash' > "$PREFIX/bin/theme-me"
    echo "cd $INSTALL_DIR && python run.py \"\$@\"" >> "$PREFIX/bin/theme-me"
    chmod +x "$PREFIX/bin/theme-me"
    echo "[Theme-Me v3.0] Installation complete! Run 'theme-me' to start."
else
    echo "[Theme-Me v3.0] Already installed. Run 'theme-me' to start."
fi
