#### English
Read in Other Language: [Indonesia](#Indonesia)

Hegypt - Ideal AI Prompt Generator 🚀
=====================================

**Hegypt** is a web application designed to tackle one of the biggest challenges in AI interaction: **crafting the perfect prompt**. This application acts as your personal assistant, guiding you through a structured form to design, save, manage, and reuse ideal prompts for various technical and creative needs.

This project is a complete solution, from brainstorming a prompt in a local environment to making it accessible over the network with a custom domain via a reverse proxy.

✨ Key Features
--------------

*   **Structured Prompt Form**: A methodically designed form with fields for AI Persona, Core Objective, Context, Output Format, and Rules to ensure every generated prompt is rich in detail.
*   **History Management (CRUD)**: Save every prompt you create to a database. Easily review, **Edit**, **Update**, and **Delete** old prompts through the history page.
*   **Automatic Prompt Text Generation**: Intelligently combines all inputs from the form into a single, coherent prompt text ready to be copied.
*   **Network & Custom Domain Accessibility**: Designed to be accessible over a local network using the **Waitress** WSGI server and can be pointed to from a public domain (e.g., `hegypt.dix.my.id`) using **Nginx Proxy Manager**.
*   **One-Click Windows Launcher**: Comes with a `.bat` script that automates the entire startup process—activating the virtual environment and starting the server—with a single click from a desktop shortcut.

🛠️ Tech Stack & Architecture
-----------------------------

**Category**: Technology

**Backend**: Python, Flask, Flask-SQLAlchemy

**Frontend**: HTML5, CSS3, JavaScript (Vanilla)

**Database**: MySQL (for local development)

**WSGI Server**: Waitress (Cross-platform, ideal for Windows & local networks)

**Reverse Proxy**: Nginx Proxy Manager (for domain management, SSL, and forwarding)

### Local Network Architecture

The request flow when accessed via a domain:

    User --> https://hegypt.dix.my.id --> Nginx Proxy Manager --> http://YOUR_LOCAL_IP:5000 --> Waitress Server --> Flask Application

⚙️ Local Installation & Setup
-----------------------------

### 1\. Prerequisites

*   Python 3.8+
*   MySQL Server
*   Git

### 2\. Clone the Repository

    git clone https://github.com/your-username/hegypt-app.git
    cd hegypt-app

### 3\. Setup Virtual Environment & Dependencies

    # Create virtual environment
    python -m venv myenv
    
    # Activate on Windows
    .\myenv\Scripts\Activate.ps1
    
    # Install all libraries from requirements.txt
    pip install -r requirements.txt

### 4\. Setup MySQL Database

Log in to your MySQL client and run the following SQL commands:

    CREATE DATABASE hegypt;
    CREATE USER 'hegypt'@'localhost' IDENTIFIED BY 'hegypt';
    GRANT ALL PRIVILEGES ON hegypt.* TO 'hegypt'@'localhost';
    FLUSH PRIVILEGES;

### 5\. Initialize Database Tables

Run the provided script to automatically create the `prompt_history` table.

    python init_database.py

You will see a confirmation message: `>>> Database dan tabel 'prompt_history' berhasil dibuat! <<<`

🚀 Usage
--------

1.  **Run the Application**: Simply **double-click** the `start_hegypt.bat` file or the desktop shortcut you created.
2.  **Automated Process**: The script will open a terminal, activate the virtual environment, start the Waitress server, and open your browser to the specified address.
3.  **Use Hegypt**:
    *   Fill out the form on the main page to create a new prompt.
    *   Click "Generate Prompt." The prompt will be displayed and automatically saved.
    *   Go to the "View History" page to manage (edit or delete) your prompts.
4.  **Stop the Server**: To stop, return to the open terminal window and press `Ctrl + C`.

📜 License
----------

This project is distributed under the **MIT License**.

👤 Contact
----------

**Your Name** - [GitHub Profile](https://github.com/hendoriku)

Project Link: [https://github.com/hendoriku/hegypt](https://github.com/hendoriku/hegypt)

* * *
#### Indonesia
Baca dalam bahasa lain: [English](#English)

Hegypt - Ideal AI Prompt Generator 🚀
=====================================

**Hegypt** adalah aplikasi web yang dirancang untuk mengatasi salah satu tantangan terbesar saat berinteraksi dengan AI: **membuat \*prompt\* yang sempurna**. Aplikasi ini berfungsi sebagai asisten pribadi Anda, memandu Anda melalui formulir terstruktur untuk merancang, menyimpan, mengelola, dan menggunakan kembali \*prompt\* yang ideal untuk berbagai kebutuhan teknis dan kreatif.

Proyek ini adalah solusi lengkap, dari pembuatan ide \*prompt\* di lingkungan lokal hingga siap diakses melalui jaringan dengan domain kustom menggunakan \*reverse proxy\*.

✨ Fitur Utama
-------------

*   **Formulir Prompt Terstruktur**: Formulir yang dirancang secara metodis dengan \*field\* untuk Persona AI, Tujuan Utama, Konteks, Format Output, dan Aturan untuk memastikan setiap \*prompt\* yang dihasilkan kaya akan detail.
*   **Manajemen Riwayat (CRUD)**: Simpan setiap \*prompt\* yang Anda buat ke database. Lihat kembali, **Edit**, **Perbarui**, dan **Hapus** \*prompt\* lama dengan mudah melalui halaman riwayat.
*   **Generator Teks Prompt Otomatis**: Secara cerdas menggabungkan semua input dari formulir menjadi satu teks \*prompt\* yang koheren dan siap disalin.
*   **Akses Jaringan & Domain Kustom**: Didesain untuk bisa diakses melalui jaringan lokal menggunakan server WSGI **Waitress** dan dapat di-pointing dari domain publik (misal: `hegypt.dix.my.id`) menggunakan **Nginx Proxy Manager**.
*   **Peluncur Sekali Klik untuk Windows**: Dilengkapi dengan \*script\* `.bat` yang mengotomatiskan seluruh proses—aktivasi \*virtual environment\* dan memulai server—hanya dengan satu kali klik dari \*shortcut\* desktop.

🛠️ Tech Stack & Arsitektur
---------------------------

**Kategori**: Teknologi

**Backend**: Python, Flask, Flask-SQLAlchemy

**Frontend**: HTML5, CSS3, JavaScript (Vanilla)

**Database**: MySQL (untuk pengembangan lokal)

**Server WSGI**: Waitress (Cross-platform, ideal untuk Windows & jaringan lokal)

**Reverse Proxy**: Nginx Proxy Manager (untuk manajemen domain, SSL, dan forwarding)

### Arsitektur Jaringan Lokal

Alur permintaan saat diakses melalui domain:

    Pengguna --> https://hegypt.dix.my.id --> Nginx Proxy Manager --> http://IP_LOKAL_ANDA:5000 --> Server Waitress --> Aplikasi Flask

⚙️ Instalasi & Konfigurasi Lokal
--------------------------------

### 1\. Prasyarat

*   Python 3.8+
*   MySQL Server
*   Git

### 2\. Clone Repositori

    git clone https://github.com/username-anda/hegypt-app.git
    cd hegypt-app

### 3\. Setup Lingkungan & Dependensi

    # Buat virtual environment
    python -m venv myenv
    
    # Aktifkan di Windows
    .\myenv\Scripts\Activate.ps1
    
    # Install semua library dari requirements.txt
    pip install -r requirements.txt

### 4\. Setup Database MySQL

Masuk ke MySQL client Anda dan jalankan perintah SQL berikut:

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

1.  **Jalankan Aplikasi**: Cukup **double-click** file `start_hegypt.bat` atau \*shortcut\* desktop yang telah Anda buat.
2.  **Proses Otomatis**: Skrip akan membuka terminal, mengaktifkan lingkungan virtual, memulai server Waitress, dan membuka browser Anda ke alamat yang ditentukan.
3.  **Gunakan Hegypt**:
    *   Isi formulir di halaman utama untuk membuat prompt baru.
    *   Klik "Generate Prompt". Prompt akan ditampilkan dan otomatis tersimpan.
    *   Buka halaman "Lihat Riwayat" untuk mengelola (mengedit atau menghapus) prompt Anda.
4.  **Hentikan Server**: Untuk berhenti, kembali ke jendela terminal yang terbuka dan tekan `Ctrl + C`.

📜 Lisensi
----------

Proyek ini dilisensikan di bawah **Lisensi MIT**.

👤 Kontak
---------

**Nama Anda** - [Profil GitHub](https://github.com/hendoriku)

Link Proyek: [https://github.com/hendoriku/hegypt](https://github.com/hendoriku/hegypt)
