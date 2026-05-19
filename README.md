# SKY-CRYPTO-FLASK ☁️🌙

### Simulasi Kriptografi Klasik Interaktif Berbasis Flask

CryptoSky adalah aplikasi web edukatif berbasis **Python Flask** yang dirancang untuk membantu pengguna memahami cara kerja algoritma kriptografi klasik secara visual, interaktif, dan modern.

Aplikasi ini tidak hanya melakukan proses enkripsi dan dekripsi, tetapi juga menampilkan proses matematika dan transformasi karakter secara **langkah demi langkah** sehingga lebih mudah dipahami oleh mahasiswa maupun pengguna awam.

CryptoSky menggunakan tema visual langit:

* ☀️ **Light Mode** → nuansa langit cerah dengan awan lembut
* 🌙 **Dark Mode** → nuansa malam dengan bulan dan bintang

---

# ✨ Fitur Utama

## 🔐 Algoritma Kriptografi

Aplikasi mendukung:

1. Caesar Cipher
2. Vigenère Cipher
3. Affine Cipher
4. Hill Cipher (2x2 & 3x3)
5. Playfair Cipher

---

# 🎓 Fitur Edukatif

## 📖 Penjelasan Langkah Demi Langkah

Setiap algoritma menampilkan:

* proses transformasi huruf,
* operasi modulo,
* perhitungan matematika,
* perubahan plaintext menjadi ciphertext,
* visualisasi hasil akhir.

---

## 🧮 Visualisasi Matriks Hill Cipher

Hill Cipher dilengkapi dengan:

* visualisasi matriks 2x2 dan 3x3,
* proses perkalian matriks,
* modulo 26,
* konversi huruf ↔ angka,
* penjelasan blok teks.

---

## 🟦 Playfair Cipher Interaktif

Playfair Cipher memiliki fitur interaktif:

* tabel 5x5 visual,
* highlight pasangan huruf,
* penjelasan rule:

  * same row,
  * same column,
  * rectangle swap,
* interaksi klik/tap langkah,
* highlight otomatis pada tabel.

Fitur ini mendukung:

* desktop,
* laptop,
* mobile/touchscreen.

---

# 🌗 Tampilan Modern CryptoSky

## ☀️ Light Mode

* nuansa langit biru cerah,
* awan bergerak lembut,
* tampilan clean dan nyaman.

## 🌙 Dark Mode

* nuansa malam elegan,
* bulan dan bintang,
* kontras nyaman untuk mata,
* seluruh card dan tabel menyesuaikan tema malam.

---

# 📱 Responsive & Mobile Friendly

CryptoSky dirancang agar tetap nyaman digunakan pada:

* desktop,
* laptop,
* tablet,
* smartphone.

Fitur interaktif tetap berjalan pada mode mobile, termasuk:

* tap highlight Playfair,
* copy hasil cipher,
* responsive matrix table,
* mobile navbar.

---

# 🛠️ Teknologi yang Digunakan

* Python 3
* Flask
* Jinja2
* Bootstrap 5
* HTML5
* CSS3
* Vanilla JavaScript
* Gunicorn

---

# 📂 Struktur Folder

```text
SKY-CRYPTO-FLASK/
├── app.py
├── requirements.txt
├── Procfile
├── README.md
├── .gitignore
│
├── cipher_modules/
│   ├── __init__.py
│   ├── caesar_cipher.py
│   ├── vigenere_cipher.py
│   ├── affine_cipher.py
│   ├── hill_cipher.py
│   └── playfair_cipher.py
│
├── templates/
│   ├── layout.html
│   ├── home.html
│   └── history.html
│
└── static/
    ├── style.css
    └── app.js
```

---

# ⚙️ Cara Menjalankan Secara Lokal

## 1. Clone Repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

## 2. Masuk ke Folder Project

```bash
cd SKY-CRYPTO-FLASK
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Jalankan Flask

```bash
python app.py
```

## 5. Buka Browser

```text
http://127.0.0.1:5000
```

---

# 🚀 Deployment

Project ini sudah dikonfigurasi menggunakan:

* `requirements.txt`
* `Procfile`
* `gunicorn`

sehingga siap dideploy ke platform seperti:

* Koyeb
* Railway
* Render
* Heroku

Deployment utama proyek ini menggunakan **Koyeb**.

---

# 🧪 Pengujian Aplikasi

Pengujian dilakukan pada:

* mode desktop,
* mode mobile,
* light mode,
* dark mode.

Pengujian mencakup:

* validasi input,
* encrypt/decrypt,
* responsive design,
* visualisasi matriks,
* interaksi Playfair,
* copy output,
* history,
* error handling.

---

# 📚 Tujuan Edukasi

Aplikasi ini dibuat bukan hanya untuk memenuhi tugas mata kuliah Kriptografi, tetapi juga untuk membantu pengguna memahami:

* konsep dasar kriptografi klasik,
* logika enkripsi dan dekripsi,
* operasi modulo,
* transformasi karakter,
* penggunaan matriks dalam kriptografi.

---

# 👨‍💻 Author

Roy Bakti Surya Medal
Mahasiswa Teknik Informatika, Fakultas Teknologi Informasi
