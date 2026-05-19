def process_vigenere(text, keyword, mode):
    result = []
    steps = []
    
    if not keyword.isalpha():
        return {"result": "Error: Keyword hanya boleh berisi huruf.", "steps": [], "formula": ""}
    
    keyword = keyword.upper()
    key_length = len(keyword)
    key_index = 0

    if mode == 'decrypt':
        fn_umum = "P_i = (C_i - K_i) mod 26"
        fn_impl = f"P_i = (C_i - K_i) mod 26"
        op = "-"
    else:
        fn_umum = "C_i = (P_i + K_i) mod 26"
        fn_impl = f"C_i = (P_i + K_i) mod 26"
        op = "+"
        
    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Rumus Vigenère Cipher</span>
        
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

        <div class="small dynamic-text-muted mb-2 text-start">
            <strong>P_i</strong> = huruf plaintext pada posisi ke-i <br>
            <strong>C_i</strong> = huruf ciphertext pada posisi ke-i <br>
            <strong>K_i</strong> = huruf keyword pada posisi ke-i setelah keyword ({keyword}) diulang <br>
            <strong>mod 26</strong> = operasi modulo pada alfabet A-Z
        </div>
    </div>
    """

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            
            # Posisi huruf (0-25)
            char_val = ord(char.upper()) - ord('A')
            
            # Nilai huruf dari keyword saat ini
            key_char = keyword[key_index % key_length]
            key_val = ord(key_char) - ord('A')
            
            if mode == 'encrypt':
                new_val = (char_val + key_val) % 26
                op_str = f"+ {key_val}"
            else:
                new_val = (char_val - key_val) % 26
                op_str = f"- {key_val}"
            
            new_char = chr(new_val + ord('A'))
            if not is_upper:
                new_char = new_char.lower()
                
            if mode == 'encrypt':
                step_calc = f"C_i = ({char_val} + {key_val}) mod 26 = {new_val} &rarr; {new_char.upper()}"
            else:
                step_calc = f"P_i = ({char_val} - {key_val}) mod 26 = {new_val} &rarr; {new_char.upper()}"

            step_html = f"""
            <div class="card mb-2 shadow-sm dynamic-card-border" style="background-color: var(--input-bg);">
                <div class="card-body py-2 px-3 d-flex align-items-center flex-wrap gap-2">
                    <div class="d-flex flex-column align-items-center me-1">
                        <span class="badge bg-primary mb-1" style="width: 35px;">{char}</span>
                        <span class="dynamic-text-muted" style="font-size: 0.7rem;">P_i = {char_val}</span>
                    </div>
                    <span class="font-monospace dynamic-text-muted">{op}</span>
                    <div class="d-flex flex-column align-items-center ms-1 me-1">
                        <span class="badge bg-info text-dark mb-1" style="width: 35px;">{key_char}</span>
                        <span class="dynamic-text-muted" style="font-size: 0.7rem;">K_i = {key_val}</span>
                    </div>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted small mx-1"></i>
                    <span class="font-monospace dynamic-text small">{step_calc}</span>
                </div>
            </div>
            """
            steps.append(step_html)
                
            result.append(new_char)
            key_index += 1 # Majukan index keyword hanya jika huruf
        else:
            # Jika bukan huruf (spasi/tanda baca), jangan diubah
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
    return process_vigenere(text, key, 'encrypt')

def decrypt(text, key):
    return process_vigenere(text, key, 'decrypt')
