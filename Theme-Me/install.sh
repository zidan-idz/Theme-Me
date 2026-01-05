#!/data/data/com.termux/files/usr/bin/bash

# Pastikan lingkungan kompatibel (Termux) atau PREFIX sudah diset
if [ -z "$PREFIX" ]; then
    echo "[Warning] PREFIX is not set. This script is designed for Termux."
    echo "If you are testing, proceed with caution."
fi

echo "[Theme-Me v3.1] Installing..."

# Instal dependensi
echo "Installing dependencies..."
pkg install python git termux-tools -y

# Atur izin akses
chmod -R 755 data/

INSTALL_DIR="$PREFIX/share/theme-me"
mkdir -p "$INSTALL_DIR"

# Strategi instalasi bersih - Hanya salin file yang diperlukan
echo "Copying files to $INSTALL_DIR..."
cp run.py "$INSTALL_DIR/"
cp -r core "$INSTALL_DIR/"
cp -r data "$INSTALL_DIR/"

# Salin file opsional (jika ada)
if [ -d "docs" ]; then cp -r docs "$INSTALL_DIR/"; fi
if [ -f "since.txt" ]; then cp since.txt "$INSTALL_DIR/"; fi
if [ -f "LICENSE" ]; then cp LICENSE "$INSTALL_DIR/"; fi
if [ -f "README.md" ]; then cp README.md "$INSTALL_DIR/"; fi
if [ -f "CHANGELOG.md" ]; then cp CHANGELOG.md "$INSTALL_DIR/"; fi

# Hapus sampah (seperti pycache) dari direktori tujuan
find "$INSTALL_DIR" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null

# Buat wrapper eksekusi
if [ ! -f "$PREFIX/bin/theme-me" ]; then
    echo '#!/data/data/com.termux/files/usr/bin/bash' > "$PREFIX/bin/theme-me"
    echo "cd \"$INSTALL_DIR\" && python run.py \"\$@\"" >> "$PREFIX/bin/theme-me"
    chmod +x "$PREFIX/bin/theme-me"
    echo "[Theme-Me v3.1] Installation complete! Run 'theme-me' to start."
else
    echo "[Theme-Me v3.1] Already installed. Run 'theme-me' to start."
fi
