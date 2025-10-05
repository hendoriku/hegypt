# init_database.py

# 1. Impor objek 'app' dan 'db' dari file app.py kita
from app import app, db

# 2. Jalankan proses pembuatan tabel di dalam 'application context'
#    Ini penting agar SQLAlchemy tahu database mana yang harus digunakan
with app.app_context():
    db.create_all()

# 3. Beri pesan konfirmasi bahwa semuanya sudah selesai
print(">>> Database dan tabel 'prompt_history' berhasil dibuat! <<<")