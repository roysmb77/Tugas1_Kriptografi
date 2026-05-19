def process_caesar(text, key, mode):
    result = []
    steps = []
    
    # Memastikan key adalah integer (nilai pergeseran)
    try:
        shift = int(key) % 26
    except ValueError:
        return {"result": "Error: Keyword (nilai pergeseran) harus berupa angka.", "steps": [], "formula": ""}

    if mode == 'decrypt':
        shift = -shift
        op = "-"
        fn = "D(x) / P(x)"
    else:
        op = "+"
        fn = "E(x) / C(x)"
        
    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Rumus Caesar Cipher</span>
        <div class="p-2 border dynamic-card-border rounded dynamic-bg-code font-monospace fs-5 text-center mb-2" style="max-width: 350px;">
            {fn} = (P {op} k) mod 26
        </div>
        <div class="small dynamic-text-muted mb-2">
            <strong>P</strong> = Plaintext (huruf asal) <br>
            <strong>C</strong> = Ciphertext (huruf hasil) <br>
            <strong>k</strong> = Key / Nilai Shift ({key})
        </div>
        <div class="alert alert-info dynamic-bg-code dynamic-text border-0 py-2 px-3 small">
            <i class="fa-solid fa-lightbulb text-warning me-2"></i>
            Caesar Cipher bekerja dengan menggeser huruf plaintext secara alfabetis sebanyak nilai key (k) menggunakan operasi matematika modulo 26.
        </div>
    </div>
    """

    for char in text:
        if char.isalpha():
            # Tentukan nilai dasar ASCII (65 untuk 'A', 97 untuk 'a')
            base = ord('A') if char.isupper() else ord('a')
            
            # Hitung posisi huruf saat ini (0-25)
            x = ord(char) - base
            
            # Terapkan pergeseran dan modulo 26
            new_x = (x + shift) % 26
            
            # Ubah kembali ke karakter ASCII
            new_char = chr(new_x + base)
            result.append(new_char)
            
            # Simpan langkah perhitungan untuk edukasi
            op_str = f"+ {key}" if mode == 'encrypt' else f"- {key}"
            
            step_html = f"""
            <div class="card mb-2 shadow-sm dynamic-card-border" style="background-color: var(--input-bg);">
                <div class="card-body py-2 px-3 d-flex align-items-center flex-wrap gap-2">
                    <span class="badge bg-primary fs-6" style="width: 35px;">{char}</span>
                    <span class="dynamic-text-muted small">({x})</span>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted small mx-1"></i>
                    <span class="font-monospace dynamic-text small">({x} {op_str}) mod 26</span>
                    <i class="fa-solid fa-equals dynamic-text-muted small mx-1"></i>
                    <strong class="dynamic-text-success">{new_x}</strong>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted small mx-1"></i>
                    <span class="badge bg-success fs-6" style="width: 35px;">{new_char}</span>
                </div>
            </div>
            """
            steps.append(step_html)
        else:
            # Jika bukan huruf, jangan diubah (contoh: spasi, koma)
            result.append(char)
            step_html = f"""
            <div class="card mb-2 shadow-sm dynamic-card-border" style="background-color: var(--input-bg); opacity: 0.8;">
                <div class="card-body py-2 px-3 d-flex align-items-center gap-2">
                    <span class="badge bg-secondary fs-6" style="width: 35px;">{char}</span>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted small mx-1"></i>
                    <span class="dynamic-text-muted small">Tidak diubah (Bukan Huruf)</span>
                </div>
            </div>
            """
            steps.append(step_html)

    return {
        "result": "".join(result),
        "steps": steps,
        "formula": formula
    }

def encrypt(text, key):
    return process_caesar(text, key, 'encrypt')

def decrypt(text, key):
    return process_caesar(text, key, 'decrypt')
