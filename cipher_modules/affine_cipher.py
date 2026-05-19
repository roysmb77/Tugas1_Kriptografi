# Fungsi untuk mencari GCD (Faktor Persekutuan Terbesar)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fungsi untuk mencari modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1

def process_affine(text, key_a, key_b, mode):
    result = []
    steps = []
    
    try:
        a = int(key_a)
        b = int(key_b)
    except ValueError:
        return {"result": "Error: Kunci 'a' dan 'b' harus berupa angka.", "steps": [], "formula": ""}

    # Validasi bahwa 'a' harus coprime dengan 26
    if gcd(a, 26) != 1:
        return {"result": f"Error: Kunci 'a' ({a}) tidak coprime dengan 26 (FPB bukan 1). Tidak bisa dienkripsi/dekripsi.", "steps": [], "formula": ""}

    if mode == 'encrypt':
        general_formula = "C &equiv; (mP + b) mod 26"
        formula_html = f"C &equiv; ({a}P + {b}) mod 26"
        legend = f"""
        <div class="small dynamic-text-muted mb-2 text-start">
            <strong>P</strong> = Plaintext <br>
            <strong>C</strong> = Ciphertext <br>
            <strong>m</strong> = nilai a ({a}) <br>
            <strong>b</strong> = nilai pergeseran ({b})
        </div>
        """
    else:
        a_inv = mod_inverse(a, 26)
        general_formula = "P &equiv; m⁻¹(C - b) mod 26"
        formula_html = f"P &equiv; {a_inv}(C - {b}) mod 26"
        legend = f"""
        <div class="small dynamic-text-muted mb-2 text-start">
            <strong>P</strong> = Plaintext <br>
            <strong>C</strong> = Ciphertext <br>
            <strong>m</strong> = nilai a ({a}) <br>
            <strong>b</strong> = nilai pergeseran ({b}) <br>
            <strong>m⁻¹</strong> = inverse modulo dari m <br>
            <strong>{a_inv}</strong> adalah inverse dari {a} modulo 26
        </div>
        """
        
    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Rumus Affine Cipher</span>
        
        <div class="mb-3">
            <label class="form-label fw-bold small mb-1 text-muted">Rumus Umum:</label>
            <div class="p-2 border dynamic-card-border rounded dynamic-bg-code font-monospace text-center">
                {general_formula}
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label fw-bold small mb-1 text-muted">Implementasi Saat Ini:</label>
            <div class="p-2 border dynamic-card-border rounded dynamic-bg-code font-monospace text-center">
                {formula_html}
            </div>
        </div>

        {legend}
    </div>
    """

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            
            if mode == 'encrypt':
                new_x = (a * x + b) % 26
                op_str = f"({a} &times; {x} + {b})"
            else:
                a_inv = mod_inverse(a, 26)
                new_x = (a_inv * (x - b)) % 26
                op_str = f"{a_inv} &times; ({x} - {b})"
            
            new_char = chr(new_x + base)
            
            step_html = f"""
            <div class="card mb-2 shadow-sm dynamic-card-border" style="background-color: var(--input-bg);">
                <div class="card-body py-2 px-3 d-flex align-items-center flex-wrap gap-2">
                    <span class="badge bg-primary fs-6" style="width: 35px;">{char}</span>
                    <span class="dynamic-text-muted small">({x})</span>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted small mx-1"></i>
                    <span class="font-monospace dynamic-text small">{op_str} mod 26</span>
                    <i class="fa-solid fa-equals dynamic-text-muted small mx-1"></i>
                    <strong class="dynamic-text-success">{new_x}</strong>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted small mx-1"></i>
                    <span class="badge bg-success fs-6" style="width: 35px;">{new_char}</span>
                </div>
            </div>
            """
            steps.append(step_html)
            
            result.append(new_char)
        else:
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

def encrypt(text, key_a, key_b):
    return process_affine(text, key_a, key_b, 'encrypt')

def decrypt(text, key_a, key_b):
    return process_affine(text, key_a, key_b, 'decrypt')
