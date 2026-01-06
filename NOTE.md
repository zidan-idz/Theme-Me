# CATATAN PRIBADI: PROJECT THEME-ME
*(Baca ini kalau lupa cara kerja kodenya)*

Dokumen ini buat pengingat diri sendiri di masa depan tentang gimana struktur dan logika proyek ini bekerja. Jangan dihapus.

---

## 📑 Daftar Isi
1.  [Peta Folder (Apa ada di mana?)](#1-peta-folder-apa-ada-di-mana)
2.  [Alur Kerja Sistem (Gimana codingannya jalan)](#2-alur-kerja-sistem-gimana-codingannya-jalan)
3.  [Cheat Sheet: Nambah Fitur](#3-cheat-sheet-nambah-fitur)
    *   [Cara Tambah Tema Baru](#cara-tambah-tema-baru)
    *   [Cara Update Versi](#cara-update-versi)
4.  [Ingat Soal Keamanan! (Penting)](#4-ingat-soal-keamanan-penting)
5.  [Kalo Error (Debugging)](#5-kalo-error-debugging)
6.  [Soal Install Script](#6-soal-install-script)

---

## 1. Peta Folder (Apa ada di mana?)

Ini struktur intinya biar gak bingung nyari file:

*   **`run.py`**: Ini **pintu masuk**. Kalo mau nambah argumen perintah baru (CLI), edit di sini.
*   **`install.sh`**: Script buat mindahin file ke HP user.
*   **`core/`**: Jantungnya program.
    *   `handler.py`: **File paling krusial**. Semua logika ganti tema, backup file, copy-copy file ada di sini.
    *   `utils.py`: Isinya helper kayak animasi loading, cek termux, warna teks.
    *   `constants.py`: Konfigurasi statis. **Ganti versi di sini**.
    *   `ui.py`: Urusan tampilan menu ASCII art.
*   **`data/`**: Gudang aset.
    *   `themes.json`: Daftar tema (ID, Nama, Path).

---

## 2. Alur Kerja Sistem (Gimana codingannya jalan)

1.  User jalanin `theme-me`.
2.  Script ngecek: "Ini di Termux gak?" (`check_termux` di `utils.py`).
3.  Kalo user pilih tema (misal ID: `cyberpunk`):
    *   Code bakal lari ke `handler.apply_theme()`.
    *   **STEP 1**: Cek file `themes.json` buat nyari path file ASCII art-nya.
    *   **STEP 2 (PENTING)**: Code bakal ngecek `bash.bashrc` di folder `usr/etc`.
    *   **STEP 3**: Sebelum diapa-apain, code bakal **BACKUP** dulu jadi `bash.bashrc.bak`.
    *   **STEP 4**: Code bikin file baru namanya `theme.py` di folder sistem, isinya script Python buat nampilin logo.
    *   **STEP 5**: Code ngubah `bash.bashrc` biar setiap buka terminal dia jalanin `python theme.py`.

---

## 3. Cheat Sheet: Nambah Fitur

### Cara Tambah Tema Baru
Gak perlu ngoding Python.
1.  Bikin file ASCII art (misal `hacker.txt`) taruh di `data/themes/`.
2.  Buka `data/themes.json`.
3.  Copy-paste format ini:
    ```json
    {
      "id": "hacker",
      "name": "Hacker Mode",
      "path": "data/themes/hacker.txt"
    }
    ```

### Cara Update Versi
Kalo udah update fitur dan mau rilis:
1.  Buka `core/constants.py` -> Ganti `VERSION` dan `VERSION_TAG`.
2.  Buka `install.sh` -> Ganti echo versi di bawah.
3.  Update `CHANGELOG.md` biar gak lupa apa yang diubah.

---

## 4. Ingat Soal Keamanan! (Penting)

Di versi 3.1 (Yuzuki), gue udah nambahin sistem pengaman biar gak ngerusak HP orang.

1.  **Backup Otomatis**: Code `handler.py` udah diprogram buat SELALU backup `bash.bashrc` sebelum nimpa file itu. Jadi kalo corrupt, tinggal balikin backupnya.
2.  **Install Bersih**: Script `install.sh` cuma nyalin folder `core`, `data`, dan `run.py`. Folder sampah kayak `.git` atau `testing` gak bakal ikut keinstall di HP.

---

## 5. Kalo Error (Debugging)

Kalo pas testing code ternyata error dan Termux gak bisa dibuka:

**Solusi Darurat:**
1.  Masuk **Fail-safe Mode** Termux.
2.  Jalanin perintah ini buat balikin kondisi semula:
    ```bash
    cp ../usr/etc/bash.bashrc.bak ../usr/etc/bash.bashrc
    rm ../usr/etc/theme.py
    ```

**Masalah umum lain:**
*   *Permission Denied?* -> Cek `chmod` di `install.sh` atau jalanin `termux-setup-storage`.
*   *Module not found?* -> Pastiin di `install.sh` udah ada `pkg install python`.

---

## 6. Soal Install Script

File `install.sh` itu intinya cuma mindahin isi folder proyek ini ke `$PREFIX/share/theme-me` terus bikin shortcut di `$PREFIX/bin`. 

Kalo nambah folder baru di root (misal folder `icons/`), JANGAN LUPA update `install.sh` buat copy folder itu juga:
`cp -r icons "$INSTALL_DIR/"`
