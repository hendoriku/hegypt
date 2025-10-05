# app.py (Versi Final dengan Perbaikan Regenerasi Prompt)

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

# --- KONFIGURASI APLIKASI HEGYPT ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ini-adalah-kunci-rahasia-yang-sangat-aman-12345'
DB_USER, DB_PASS, DB_HOST, DB_NAME = 'hegypt', 'hegypt', 'localhost', 'hegypt'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- MODEL DATABASE (Tidak ada perubahan) ---
class PromptHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ai_persona = db.Column(db.String(200))
    core_objective = db.Column(db.Text, nullable=False)
    specific_task = db.Column(db.Text)
    context = db.Column(db.Text)
    audience = db.Column(db.String(200))
    tone_style = db.Column(db.String(200))
    output_structure = db.Column(db.String(200))
    constraints = db.Column(db.Text)
    example = db.Column(db.Text)
    generated_prompt = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# --- PERINTAH INISIALISASI DATABASE (Tidak ada perubahan) ---
@app.cli.command("init-db")
def init_db_command():
    """Membuat tabel database baru."""
    db.create_all()
    print("Database dan tabel berhasil diinisialisasi.")

# --- FUNGSI BANTU UNTUK MEMBUAT PROMPT ---
# Kita buat fungsi terpisah agar tidak duplikat kode
def build_prompt_text(form_data):
    prompt_parts = ["### PROMPT UTAMA ###"]
    if form_data.get('ai_persona'): prompt_parts.append(f"**Peran AI:** Kamu adalah seorang {form_data.get('ai_persona')}.")
    if form_data.get('core_objective'): prompt_parts.append(f"**Tujuan Utama:** {form_data.get('core_objective')}")
    if form_data.get('specific_task'): prompt_parts.append(f"**Tugas Spesifik:**\n{form_data.get('specific_task')}")
    
    context_section = []
    if form_data.get('context'): context_section.append(f"- Latar Belakang: {form_data.get('context')}")
    if form_data.get('audience'): context_section.append(f"- Audiens Target: Output ini ditujukan untuk {form_data.get('audience')}.")
    if context_section: prompt_parts.append("**Konteks dan Audiens:**\n" + "\n".join(context_section))

    format_section = []
    if form_data.get('tone_style'): format_section.append(f"- Gaya & Nada: Gunakan gaya bahasa yang {form_data.get('tone_style')}.")
    if form_data.get('output_structure'): format_section.append(f"- Struktur: Sajikan output dalam format berikut: {form_data.get('output_structure')}.")
    if format_section: prompt_parts.append("**Format dan Gaya Output:**\n" + "\n".join(format_section))

    if form_data.get('constraints'): prompt_parts.append(f"**Aturan dan Batasan Tegas:**\n{form_data.get('constraints')}")
    if form_data.get('example'): prompt_parts.append(f"**Contoh untuk Referensi:**\n---\n{form_data.get('example')}\n---")
    
    return "\n\n".join(prompt_parts)

# --- ROUTE HALAMAN UTAMA ---
@app.route('/', methods=['GET', 'POST'])
def index():
    generated_prompt = None
    if request.method == 'POST':
        form_data = {key: val for key, val in request.form.items()}
        generated_prompt = build_prompt_text(form_data)
        
        try:
            new_entry = PromptHistory(**form_data, generated_prompt=generated_prompt)
            db.session.add(new_entry)
            db.session.commit()
            flash('Prompt berhasil disimpan!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Gagal menyimpan prompt. Error: {e}', 'error')
    return render_template('index.html', generated_prompt=generated_prompt)

# --- ROUTE HALAMAN RIWAYAT (Tidak ada perubahan) ---
@app.route('/history')
def history():
    all_prompts = PromptHistory.query.order_by(PromptHistory.created_at.desc()).all()
    return render_template('history.html', prompts=all_prompts)


# --- ROUTE UNTUK MENGEDIT PROMPT (DENGAN PERBAIKAN) ---
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_prompt(id):
    prompt_to_edit = PromptHistory.query.get_or_404(id)

    if request.method == 'POST':
        prompt_to_edit.ai_persona = request.form.get('ai_persona')
        prompt_to_edit.core_objective = request.form.get('core_objective')
        prompt_to_edit.specific_task = request.form.get('specific_task')
        prompt_to_edit.context = request.form.get('context')
        prompt_to_edit.audience = request.form.get('audience')
        prompt_to_edit.tone_style = request.form.get('tone_style')
        prompt_to_edit.output_structure = request.form.get('output_structure')
        prompt_to_edit.constraints = request.form.get('constraints')
        prompt_to_edit.example = request.form.get('example')
        
        # --- LOGIKA REGENERASI PROMPT (INI BAGIAN PERBAIKANNYA) ---
        # Ambil semua data yang baru diupdate ke dalam sebuah dictionary
        updated_data = {
            'ai_persona': prompt_to_edit.ai_persona,
            'core_objective': prompt_to_edit.core_objective,
            'specific_task': prompt_to_edit.specific_task,
            'context': prompt_to_edit.context,
            'audience': prompt_to_edit.audience,
            'tone_style': prompt_to_edit.tone_style,
            'output_structure': prompt_to_edit.output_structure,
            'constraints': prompt_to_edit.constraints,
            'example': prompt_to_edit.example
        }
        # Panggil fungsi untuk membuat ulang teks prompt dan simpan
        prompt_to_edit.generated_prompt = build_prompt_text(updated_data)
        # -----------------------------------------------------------

        try:
            db.session.commit()
            flash('Prompt berhasil diperbarui!', 'success')
            return redirect(url_for('history'))
        except Exception as e:
            db.session.rollback()
            flash(f'Gagal memperbarui prompt. Error: {e}', 'error')
            return redirect(url_for('edit_prompt', id=id))

    return render_template('edit_prompt.html', prompt=prompt_to_edit)


# --- ROUTE UNTUK MENGHAPUS PROMPT (Tidak ada perubahan) ---
@app.route('/delete/<int:id>', methods=['POST'])
def delete_prompt(id):
    prompt_to_delete = PromptHistory.query.get_or_404(id)
    try:
        db.session.delete(prompt_to_delete)
        db.session.commit()
        flash('Prompt berhasil dihapus.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Gagal menghapus prompt. Error: {e}', 'error')
    
    return redirect(url_for('history'))

if __name__ == '__main__':
    app.run(debug=True)