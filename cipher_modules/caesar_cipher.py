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
        fn_umum = "P(x) = (C - k) mod 26"
        fn_impl = f"P(x) = (C - {key}) mod 26"
    else:
        fn_umum = "C(x) = (P + k) mod 26"
        fn_impl = f"C(x) = (P + {key}) mod 26"
        
    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Rumus Caesar Cipher</span>
        
        <div class="mb-3">
            <label class="form-label fw-bold small mb-1 text-muted">Rumus Umum:</label>
            <div class="p-2 border dynamic-card-border rounded dynamic-bg-code font-monospace text-center">
                {fn_umum}
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label fw-bold small mb-1 text-muted">Implementasi Saat Ini:</label>
            <div class="p-2 border dynamic-card-border rounded dynamic-bg-code font-monospace text-center">
                {fn_impl}
            </div>
        </div>

        <div class="small dynamic-text-muted mb-2">
            <strong>P</strong> = Plaintext <br>
            <strong>C</strong> = Ciphertext <br>
            <strong>k</strong> = Shift / Key
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
