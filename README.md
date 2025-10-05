Dokumentasi Hegypt - AI Prompt Generator   

Hegypt - AI Prompt Generator 🚀
===============================

Dokumentasi Lengkap Aplikasi untuk Merancang, Menyimpan, dan Mengelola Prompt AI yang Ideal.

🖼️ Tampilan Aplikasi
---------------------

![Screenshot Aplikasi Hegypt](https://i.ibb.co/6P6XyL6/hegypt-ss.png)

✨ Fitur Utama
-------------

*   **Formulir Prompt Terstruktur**: Formulir metodis dengan field untuk Persona AI, Tujuan, Konteks, dan lainnya untuk memastikan prompt yang kaya detail.
*   **Manajemen Riwayat (CRUD)**: Simpan, lihat, edit, dan hapus prompt lama dengan mudah melalui halaman riwayat.
*   **Generator Teks Prompt Otomatis**: Menggabungkan semua input menjadi satu teks prompt yang koheren dan siap disalin.
*   **Akses Jaringan & Domain Kustom**: Didesain untuk bisa diakses melalui jaringan lokal menggunakan server WSGI **Waitress**.
*   **Peluncur Sekali Klik untuk Windows**: Dilengkapi script `.bat` yang mengotomatiskan seluruh proses startup dengan satu klik.

🛠️ Tech Stack & Arsitektur
---------------------------

Kategori

Teknologi

**Backend**

Python, Flask, Flask-SQLAlchemy

**Frontend**

HTML5, CSS3, JavaScript (Vanilla)

**Database**

MySQL (untuk pengembangan lokal)

**Server WSGI**

Waitress (Cross-platform, ideal untuk Windows)

**Reverse Proxy**

Nginx Proxy Manager (untuk manajemen domain, SSL, dan forwarding)

### Arsitektur Jaringan Lokal

Alur permintaan saat diakses melalui domain kustom:

    Pengguna --> https://hegypt.dix.my.id --> Nginx Proxy Manager --> http://IP_LOKAL_ANDA:5000 --> Server Waitress --> Aplikasi Flask

⚙️ Panduan Instalasi & Konfigurasi
----------------------------------

### 1\. Prasyarat

Pastikan Anda sudah menginstal perangkat lunak berikut di komputer Anda:

*   Python 3.8+
*   MySQL Server
*   Git

### 2\. Clone Repositori

Buka terminal dan jalankan perintah berikut:

    git clone https://github.com/username-anda/hegypt-app.git
    cd hegypt-app

### 3\. Setup Lingkungan & Dependensi

Buat dan aktifkan virtual environment, lalu install semua library yang dibutuhkan.

    # Buat virtual environment
    python -m venv myenv
    
    # Aktifkan di Windows
    .\myenv\Scripts\Activate.ps1
    
    # Install semua library dari requirements.txt
    pip install -r requirements.txt

### 4\. Setup Database MySQL

Masuk ke MySQL client Anda dan jalankan perintah SQL berikut untuk membuat database dan user:

    CREATE DATABASE hegypt;
    CREATE USER 'hegypt'@'localhost' IDENTIFIED BY 'hegypt';
    GRANT ALL PRIVILEGES ON hegypt.* TO 'hegypt'@'localhost';
    FLUSH PRIVILEGES;

### 5\. Inisialisasi Tabel Database

Jalankan skrip yang telah disediakan untuk membuat tabel `prompt_history` secara otomatis.

    python init_database.py

Anda akan melihat pesan konfirmasi: `>>> Database dan tabel 'prompt_history' berhasil dibuat! <<<`

🚀 Cara Penggunaan
------------------

1.  **Jalankan Aplikasi**: Cukup **double-click** file `start_hegypt.bat` atau shortcut desktop yang telah Anda buat.
2.  **Proses Otomatis**: Skrip akan membuka terminal, mengaktifkan lingkungan virtual, memulai server Waitress, dan membuka browser Anda ke alamat yang ditentukan.
3.  **Gunakan Hegypt**:
    *   Isi formulir di halaman utama untuk membuat prompt baru.
    *   Klik "Generate Prompt". Prompt akan ditampilkan dan otomatis tersimpan.
    *   Buka halaman "Lihat Riwayat" untuk mengelola (mengedit atau menghapus) prompt Anda.
4.  **Hentikan Server**: Untuk berhenti, kembali ke jendela terminal yang terbuka dan tekan `Ctrl + C`.

📜 Lisensi
----------

Proyek ini dilisensikan di bawah **MIT License**.

MIT License adalah lisensi perangkat lunak bebas permisif singkat yang berasal dari Massachusetts Institute of Technology (MIT). Sebagai lisensi permisif, ia hanya memberlakukan pembatasan yang sangat terbatas pada penggunaan kembali dan oleh karena itu memiliki kompatibilitas lisensi yang sangat baik.

Dibuat oleh Hendrik Mamarodia

[Lihat Proyek di GitHub](https://github.com/username-anda/hegypt-app)

conversi menjadi markdown untuk dokumentasi github, hasilkan txt file notepad agar saya salin   Dokumentasi Hegypt - AI Prompt Generator   

Hegypt - AI Prompt Generator 🚀
===============================

Dokumentasi Lengkap Aplikasi untuk Merancang, Menyimpan, dan Mengelola Prompt AI yang Ideal.

🖼️ Tampilan Aplikasi
---------------------

![Screenshot Aplikasi Hegypt](https://i.ibb.co/6P6XyL6/hegypt-ss.png)

✨ Fitur Utama
-------------

*   **Formulir Prompt Terstruktur**: Formulir metodis dengan field untuk Persona AI, Tujuan, Konteks, dan lainnya untuk memastikan prompt yang kaya detail.
*   **Manajemen Riwayat (CRUD)**: Simpan, lihat, edit, dan hapus prompt lama dengan mudah melalui halaman riwayat.
*   **Generator Teks Prompt Otomatis**: Menggabungkan semua input menjadi satu teks prompt yang koheren dan siap disalin.
*   **Akses Jaringan & Domain Kustom**: Didesain untuk bisa diakses melalui jaringan lokal menggunakan server WSGI **Waitress**.
*   **Peluncur Sekali Klik untuk Windows**: Dilengkapi script `.bat` yang mengotomatiskan seluruh proses startup dengan satu klik.

🛠️ Tech Stack & Arsitektur
---------------------------

Kategori

Teknologi

**Backend**

Python, Flask, Flask-SQLAlchemy

**Frontend**

HTML5, CSS3, JavaScript (Vanilla)

**Database**

MySQL (untuk pengembangan lokal)

**Server WSGI**

Waitress (Cross-platform, ideal untuk Windows)

**Reverse Proxy**

Nginx Proxy Manager (untuk manajemen domain, SSL, dan forwarding)

### Arsitektur Jaringan Lokal

Alur permintaan saat diakses melalui domain kustom:

    Pengguna --> https://hegypt.dix.my.id --> Nginx Proxy Manager --> http://IP_LOKAL_ANDA:5000 --> Server Waitress --> Aplikasi Flask

⚙️ Panduan Instalasi & Konfigurasi
----------------------------------

### 1\. Prasyarat

Pastikan Anda sudah menginstal perangkat lunak berikut di komputer Anda:

*   Python 3.8+
*   MySQL Server
*   Git

### 2\. Clone Repositori

Buka terminal dan jalankan perintah berikut:

    git clone https://github.com/username-anda/hegypt-app.git
    cd hegypt-app

### 3\. Setup Lingkungan & Dependensi

Buat dan aktifkan virtual environment, lalu install semua library yang dibutuhkan.

    # Buat virtual environment
    python -m venv myenv
    
    # Aktifkan di Windows
    .\myenv\Scripts\Activate.ps1
    
    # Install semua library dari requirements.txt
    pip install -r requirements.txt

### 4\. Setup Database MySQL

Masuk ke MySQL client Anda dan jalankan perintah SQL berikut untuk membuat database dan user:

    CREATE DATABASE hegypt;
    CREATE USER 'hegypt'@'localhost' IDENTIFIED BY 'hegypt';
    GRANT ALL PRIVILEGES ON hegypt.* TO 'hegypt'@'localhost';
    FLUSH PRIVILEGES;

### 5\. Inisialisasi Tabel Database

Jalankan skrip yang telah disediakan untuk membuat tabel `prompt_history` secara otomatis.

    python init_database.py

Anda akan melihat pesan konfirmasi: `>>> Database dan tabel 'prompt_history' berhasil dibuat! <<<`

🚀 Cara Penggunaan
------------------

1.  **Jalankan Aplikasi**: Cukup **double-click** file `start_hegypt.bat` atau shortcut desktop yang telah Anda buat.
2.  **Proses Otomatis**: Skrip akan membuka terminal, mengaktifkan lingkungan virtual, memulai server Waitress, dan membuka browser Anda ke alamat yang ditentukan.
3.  **Gunakan Hegypt**:
    *   Isi formulir di halaman utama untuk membuat prompt baru.
    *   Klik "Generate Prompt". Prompt akan ditampilkan dan otomatis tersimpan.
    *   Buka halaman "Lihat Riwayat" untuk mengelola (mengedit atau menghapus) prompt Anda.
4.  **Hentikan Server**: Untuk berhenti, kembali ke jendela terminal yang terbuka dan tekan `Ctrl + C`.

📜 Lisensi
----------

Proyek ini dilisensikan di bawah **MIT License**.

MIT License adalah lisensi perangkat lunak bebas permisif singkat yang berasal dari Massachusetts Institute of Technology (MIT). Sebagai lisensi permisif, ia hanya memberlakukan pembatasan yang sangat terbatas pada penggunaan kembali dan oleh karena itu memiliki kompatibilitas lisensi yang sangat baik.

Dibuat oleh Hendrik Mamarodia

[Lihat Proyek di GitHub](https://github.com/username-anda/hegypt-app)
