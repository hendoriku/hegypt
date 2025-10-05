@echo off
title Hegypt Server (Production Mode with Waitress)

echo =======================================================
echo  Memulai Aplikasi Hegypt untuk Jaringan Lokal...
echo =======================================================
echo.

REM Pindah ke direktori proyek Anda
cd /d D:\Data\Service\Hegypt

echo [1/4] Direktori Aktif: %cd%

REM Aktifkan virtual environment
echo [2/4] Mengaktifkan Virtual Environment (myenv)...
call myenv\Scripts\activate.bat

REM Siapkan aplikasi
echo [3/4] Menyiapkan Aplikasi Flask...

REM =======================================================
REM  BAGIAN TAMBAHAN: Buka browser ke domain publik Anda
REM =======================================================
echo [4/4] Membuka browser ke https://hegypt.dix.my.id ...
start https://hegypt.dix.my.id
REM =======================================================

REM Jalankan server menggunakan Waitress, bukan Flask
echo.
echo Memulai server Waitress di port 5000...
echo Server akan dapat diakses dari jaringan Anda.
echo Tekan Ctrl+C untuk berhenti.
echo.

waitress-serve --host 0.0.0.0 --port 5000 app:app