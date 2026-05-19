# SKY-CRYPTO-FLASK
Aplikasi Web Simulasi Kriptografi Klasik berbasis Flask dengan tema "CryptoSky".

## Deskripsi
Proyek ini adalah tugas mata kuliah Kriptografi untuk membuat simulasi lima algoritma kriptografi klasik (Caesar, Vigenère, Affine, Hill, dan Playfair). Aplikasi ini dibangun dengan framework web Python Flask, tanpa database, dan menampilkan proses perhitungan algoritma langkah demi langkah untuk tujuan edukasi. Tampilan dibalut dengan tema yang memukau "CryptoSky" yang mendukung *Light Mode* dan *Dark Mode*.

## Fitur
- Enkripsi dan Dekripsi menggunakan 5 algoritma klasik.
- Tampilan proses (langkah demi langkah), rumus, dan matriks.
- Tema CryptoSky (awan bergerak, bintang di malam hari) dengan dukungan Mode Terang dan Gelap.
- Riwayat (History) sesi enkripsi dan dekripsi.
- Responsive design dan *glassmorphism* menggunakan Bootstrap 5 dan Vanilla CSS/JS.

## Algoritma
1. **Caesar Cipher**: Menggeser setiap huruf alfabet berdasarkan nilai *key* numerik tertentu.
2. **Vigenère Cipher**: Menggunakan *keyword* berulang untuk menentukan seberapa jauh pergeseran masing-masing huruf (kombinasi banyak Caesar cipher).
3. **Affine Cipher**: Menggabungkan perkalian (dengan nilai coprime $a$) dan penambahan (dengan nilai $b$) lalu modulo 26.
4. **Hill Cipher**: Menggunakan perkalian matriks (2x2 atau 3x3) dengan blok teks plaintext untuk menyandikan teks.
5. **Playfair Cipher**: Mengenkripsi teks dengan menggunakan tabel huruf 5x5 berpasangan (bigram) dan aturan pergeseran khusus.

## Teknologi
- Python 3.x
- Flask (Web Framework)
- Bootstrap 5 (CSS Framework)
- Vanilla JavaScript & CSS3 (Animasi dan Interaksi)

## Struktur Folder
```text
SKY-CRYPTO-FLASK/
├── app.py                   # File utama Flask web server
├── requirements.txt         # Daftar dependensi Python
├── Procfile                 # File konfigurasi untuk deployment
├── README.md                # Dokumentasi proyek
├── .gitignore               # Daftar file yang diabaikan Git
├── cipher_modules/          # Modul logika algoritma kriptografi
│   ├── __init__.py
│   ├── caesar_cipher.py
│   ├── vigenere_cipher.py
│   ├── affine_cipher.py
│   ├── hill_cipher.py
│   └── playfair_cipher.py
├── templates/               # File HTML (Jinja2)
│   ├── layout.html
│   ├── home.html
│   └── history.html
└── static/                  # File statis (CSS, JS)
    ├── style.css
    └── app.js
```

## Cara Instalasi Lokal
1. Pastikan Anda memiliki **Python 3.x** terinstal.
2. Buka terminal/command prompt.
3. Masuk ke direktori proyek:
   ```bash
   cd SKY-CRYPTO-FLASK
   ```
4. (Opsional namun disarankan) Buat dan aktifkan *virtual environment*:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install *dependencies*:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan
1. Di terminal Anda, jalankan aplikasi Flask:
   ```bash
   python app.py
   ```
2. Buka browser dan akses alamat: `http://localhost:5000`

## Cara Deploy
Aplikasi ini sudah dilengkapi dengan `Procfile` dan `requirements.txt` sehingga siap untuk dideploy di platform PaaS seperti **Render**, **Heroku**, atau **Railway**.
- Cukup hubungkan repository GitHub Anda dengan platform terkait.
- Platform akan otomatis mendeteksi sebagai aplikasi Python, menginstal `requirements.txt`, dan menjalankan perintah di `Procfile`.

---
*Dibuat untuk keperluan tugas kuliah Kriptografi.*
