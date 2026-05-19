from flask import Flask, render_template, request, redirect, url_for, flash
import datetime

# Import semua modul algoritma kriptografi
from cipher_modules import caesar_cipher, vigenere_cipher, affine_cipher, hill_cipher, playfair_cipher

app = Flask(__name__)
app.secret_key = 'cryptosky_super_secret_key_for_flash_messages'

# List Python sederhana untuk menyimpan riwayat selama aplikasi berjalan (di memory)
history_data = []

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/lab', methods=['GET', 'POST'])
def lab():
    result_data = None
    
    if request.method == 'POST':
        try:
            # Mengambil data dari form HTML
            algorithm = request.form.get('algorithm')
            mode = request.form.get('mode') # encrypt atau decrypt
            text = request.form.get('text', '')
            
            # Validasi input teks dasar
            if not text:
                flash('Silakan masukkan teks terlebih dahulu.', 'warning')
                return redirect(url_for('lab'))

            # Inisialisasi dictionary hasil
            process_result = {}

            # Pemilihan Algoritma
            if algorithm == 'caesar':
                key = request.form.get('caesar_key', '0')
                if mode == 'encrypt':
                    process_result = caesar_cipher.encrypt(text, key)
                else:
                    process_result = caesar_cipher.decrypt(text, key)
                    
            elif algorithm == 'vigenere':
                key = request.form.get('vigenere_key', '')
                if mode == 'encrypt':
                    process_result = vigenere_cipher.encrypt(text, key)
                else:
                    process_result = vigenere_cipher.decrypt(text, key)
                    
            elif algorithm == 'affine':
                key_a = request.form.get('affine_key_a', '1')
                key_b = request.form.get('affine_key_b', '0')
                if mode == 'encrypt':
                    process_result = affine_cipher.encrypt(text, key_a, key_b)
                else:
                    process_result = affine_cipher.decrypt(text, key_a, key_b)
                    
            elif algorithm == 'hill':
                key_matrix = request.form.get('hill_key_matrix', '')
                if mode == 'encrypt':
                    process_result = hill_cipher.encrypt(text, key_matrix)
                else:
                    process_result = hill_cipher.decrypt(text, key_matrix)
                    
            elif algorithm == 'playfair':
                key = request.form.get('playfair_key', '')
                if mode == 'encrypt':
                    process_result = playfair_cipher.encrypt(text, key)
                else:
                    process_result = playfair_cipher.decrypt(text, key)
            else:
                flash('Algoritma tidak dikenali.', 'danger')
                return redirect(url_for('index'))

            # Menangani jika ada error dari modul kriptografi
            if 'Error:' in process_result.get('result', ''):
                flash(process_result['result'], 'danger')
                return redirect(url_for('index'))

            process_result['algorithm'] = algorithm
            result_data = process_result
            
            # Simpan riwayat
            history_entry = {
                'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'algorithm': algorithm.capitalize(),
                'mode': mode.capitalize(),
                'input': text,
                'output': process_result.get('result', ''),
                'key': get_key_string(request.form, algorithm)
            }
            # Simpan di awal list agar yang terbaru muncul paling atas
            history_data.insert(0, history_entry)

        except Exception as e:
            flash(f"Terjadi kesalahan yang tidak terduga: {str(e)}", 'danger')

    return render_template('lab.html', result=result_data, request=request)

@app.route('/riwayat')
def history():
    return render_template('history.html', history=history_data)

# Fungsi helper untuk merapikan string key untuk history
def get_key_string(form, algo):
    if algo == 'caesar':
        return f"Shift: {form.get('caesar_key')}"
    elif algo == 'vigenere' or algo == 'playfair':
        return f"Keyword: {form.get(algo + '_key')}"
    elif algo == 'affine':
        return f"a: {form.get('affine_key_a')}, b: {form.get('affine_key_b')}"
    elif algo == 'hill':
        matrix = form.get('hill_key_matrix', '').replace('\n', ' | ')
        return f"Matrix: [{matrix}]"
    return ""

if __name__ == '__main__':
    app.run(debug=True)
