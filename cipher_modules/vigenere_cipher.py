def process_vigenere(text, keyword, mode):
    result = []
    steps = []
    
    if not keyword.isalpha():
        return {"result": "Error: Keyword hanya boleh berisi huruf.", "steps": [], "formula": ""}
    
    keyword = keyword.upper()
    key_length = len(keyword)
    key_index = 0

    if mode == 'decrypt':
        op = "-"
        fn = "D(x) / P(x)"
    else:
        op = "+"
        fn = "E(x) / C(x)"
        
    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Rumus Vigenère Cipher</span>
        <div class="p-2 border dynamic-card-border rounded dynamic-bg-code font-monospace fs-5 text-center mb-2" style="max-width: 350px;">
            {fn} = (P {op} K) mod 26
        </div>
        <div class="small dynamic-text-muted mb-2">
            <strong>P</strong> = Plaintext (huruf asal) <br>
            <strong>C</strong> = Ciphertext (huruf hasil) <br>
            <strong>K</strong> = Keyword
        </div>
        <div class="alert alert-info dynamic-bg-code dynamic-text border-0 py-2 px-3 small">
            <i class="fa-solid fa-lightbulb text-warning me-2"></i>
            Vigenère Cipher menggunakan kombinasi huruf plaintext dan keyword untuk menghasilkan ciphertext dengan operasi matematika modulo 26 berulang.
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
                
            step_html = f"""
            <div class="card mb-2 shadow-sm dynamic-card-border" style="background-color: var(--input-bg);">
                <div class="card-body py-2 px-3 d-flex align-items-center flex-wrap gap-2">
                    <div class="d-flex flex-column align-items-center me-1">
                        <span class="badge bg-primary mb-1" style="width: 35px;">{char}</span>
                        <span class="dynamic-text-muted" style="font-size: 0.7rem;">P=({char_val})</span>
                    </div>
                    <span class="font-monospace dynamic-text-muted">{op}</span>
                    <div class="d-flex flex-column align-items-center ms-1 me-1">
                        <span class="badge bg-info text-dark mb-1" style="width: 35px;">{key_char}</span>
                        <span class="dynamic-text-muted" style="font-size: 0.7rem;">K=({key_val})</span>
                    </div>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted small mx-1"></i>
                    <span class="font-monospace dynamic-text small">({char_val} {op_str}) mod 26</span>
                    <i class="fa-solid fa-equals dynamic-text-muted small mx-1"></i>
                    <strong class="dynamic-text-success">{new_val}</strong>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted small mx-1"></i>
                    <span class="badge bg-success fs-6" style="width: 35px;">{new_char}</span>
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
