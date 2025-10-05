// static/js/script.js

function copyPrompt() {
    // Ambil elemen textarea hasil
    const resultTextarea = document.getElementById('promptResult');
    
    // Pilih teks di dalamnya
    resultTextarea.select();
    resultTextarea.setSelectionRange(0, 99999); // Untuk mobile
    
    // Gunakan Clipboard API modern untuk menyalin teks
    navigator.clipboard.writeText(resultTextarea.value).then(() => {
        // Beri feedback visual ke user
        const copyButton = document.querySelector('.btn-copy');
        copyButton.innerText = 'Disalin!';
        setTimeout(() => {
            copyButton.innerText = 'Salin Prompt';
        }, 2000); // Kembalikan teks tombol setelah 2 detik
    }).catch(err => {
        console.error('Gagal menyalin teks: ', err);
    });
}