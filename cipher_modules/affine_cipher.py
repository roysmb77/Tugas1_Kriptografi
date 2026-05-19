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
        general_formula = "C &equiv; mP + b (mod 26)"
        formula_html = f"E(x) = ({a}*x + {b}) mod 26"
        legend = ""
    else:
        a_inv = mod_inverse(a, 26)
        general_formula = "P &equiv; m⁻¹ (C - b) (mod 26)"
        formula_html = f"D(x) = {a_inv} * (x - {b}) mod 26"
        legend = f"<div class='small dynamic-text-muted mt-2 text-start'><strong>m⁻¹</strong> adalah inverse modulo dari <strong>m</strong><br><strong>{a_inv}</strong> adalah inverse dari <strong>{a}</strong> modulo 26.</div>"
        
    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Rumus Affine Cipher</span>
        <div class="p-2 border dynamic-card-border rounded dynamic-bg-code fs-6 mb-2" style="max-width: 450px;">
            <div class="text-start dynamic-text-muted mb-1 small">Rumus Umum:</div>
            <div class="font-monospace fw-bold text-center mb-2">{general_formula}</div>
            <div class="text-start dynamic-text-muted mb-1 small">Implementasi:</div>
            <div class="font-monospace fw-bold text-center">{formula_html}</div>
            {legend}
        </div>
        <div class="alert alert-info dynamic-bg-code dynamic-text border-0 py-2 px-3 small">
            <i class="fa-solid fa-lightbulb text-warning me-2"></i>
            Affine Cipher menggabungkan teknik perkalian (dengan <strong>m</strong>/a) dan pergeseran (dengan <strong>b</strong>).
        </div>
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
