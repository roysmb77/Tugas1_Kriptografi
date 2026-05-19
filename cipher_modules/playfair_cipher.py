def generate_playfair_matrix(keyword):
    # Gabungkan I dan J dengan mengubah J menjadi I
    keyword = keyword.upper().replace("J", "I")
    matrix = []
    used_chars = set()
    
    # Masukkan karakter dari keyword (tanpa duplikat)
    for char in keyword:
        if char.isalpha() and char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
            
    # Masukkan sisa alfabet (tanpa J)
    for i in range(65, 91):
        char = chr(i)
        if char == 'J': continue
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
            
    # Ubah menjadi tabel 5x5
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return -1, -1

def process_playfair(text, keyword, mode):
    if not keyword.isalpha():
         return {"result": "Error: Keyword hanya boleh berisi huruf.", "steps": [], "formula": ""}

    matrix = generate_playfair_matrix(keyword)
    
    # Format teks (hanya huruf, J jadi I)
    clean_text = "".join([c.upper() for c in text if c.isalpha()]).replace("J", "I")
    
    # Buat pasangan huruf (bigram)
    pairs = []
    i = 0
    while i < len(clean_text):
        char1 = clean_text[i]
        # Jika ini huruf terakhir atau huruf berikutnya sama
        if i == len(clean_text) - 1:
            pairs.append(char1 + 'X')
            i += 1
        elif clean_text[i+1] == char1:
            pairs.append(char1 + 'X')
            i += 1
        else:
            pairs.append(char1 + clean_text[i+1])
            i += 2

    result = []
    steps = []
    
    # Visualisasi matriks
    table_rows = ""
    for r, row in enumerate(matrix):
        table_rows += "<tr>" + "".join([f"<td id='pf-cell-{r}-{c}' class='text-center align-middle fs-5 p-2 pf-cell'>{val}</td>" for c, val in enumerate(row)]) + "</tr>"
    
    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Tabel Playfair 5x5</span>
        <div class="table-responsive" style="max-width: 250px;">
            <table class="table table-bordered mb-0 playfair-table">
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
        <small class="dynamic-text-muted d-block mt-2">Huruf J digabung dengan I.</small>
        <div class="alert alert-info dynamic-bg-code dynamic-text border-0 py-2 px-3 small mt-2">
            <i class="fa-solid fa-lightbulb text-warning me-2"></i>
            Playfair Cipher mengenkripsi pasangan huruf (bigram) berdasarkan posisinya dalam tabel 5x5: baris yang sama, kolom yang sama, atau bentuk persegi.
        </div>
    </div>
    """

    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])
        
        if r1 == r2:
            # Baris sama
            if mode == 'encrypt':
                nc1 = (c1 + 1) % 5
                nc2 = (c2 + 1) % 5
                rule_desc = "Digeser ke kanan"
            else:
                nc1 = (c1 - 1) % 5
                nc2 = (c2 - 1) % 5
                rule_desc = "Digeser ke kiri"
            nr1, nr2 = r1, r2
            res_pair = matrix[r1][nc1] + matrix[r2][nc2]
            rule_badge = '<span class="badge bg-info text-dark">Satu Baris</span>'
            
        elif c1 == c2:
            # Kolom sama
            if mode == 'encrypt':
                nr1 = (r1 + 1) % 5
                nr2 = (r2 + 1) % 5
                rule_desc = "Digeser ke bawah"
            else:
                nr1 = (r1 - 1) % 5
                nr2 = (r2 - 1) % 5
                rule_desc = "Digeser ke atas"
            nc1, nc2 = c1, c2
            res_pair = matrix[nr1][c1] + matrix[nr2][c2]
            rule_badge = '<span class="badge bg-warning text-dark">Satu Kolom</span>'
            
        else:
            # Persegi (Rectangle)
            # Ambil sudut berlawanan pada baris yang sama
            nr1, nc1 = r1, c2
            nr2, nc2 = r2, c1
            res_pair = matrix[nr1][nc1] + matrix[nr2][nc2]
            rule_badge = '<span class="badge bg-danger">Bentuk Persegi</span>'
            rule_desc = "Tukar sudut pada baris yang sama"
            
        result.append(res_pair)
        
        step_html = f"""
        <div class="card mb-2 shadow-sm playfair-step dynamic-card-border" data-r1="{r1}" data-c1="{c1}" data-r2="{r2}" data-c2="{c2}" data-nr1="{nr1}" data-nc1="{nc1}" data-nr2="{nr2}" data-nc2="{nc2}" style="background-color: var(--input-bg); cursor: pointer; transition: all 0.2s ease;">
            <div class="card-body py-2 px-3 d-flex justify-content-between align-items-center flex-wrap gap-2">
                <div class="d-flex align-items-center gap-3">
                    <span class="badge bg-primary fs-5" style="width: 50px;">{pair}</span>
                    <i class="fa-solid fa-arrow-right dynamic-text-muted"></i>
                    <span class="badge bg-success fs-5" style="width: 50px;">{res_pair}</span>
                </div>
                <div class="text-md-end text-start">
                    <div class="mb-1">{rule_badge}</div>
                    <small class="dynamic-text-muted d-block" style="font-size: 0.8rem;">{rule_desc}</small>
                </div>
            </div>
        </div>
        """
        steps.append(step_html)

    return {
        "result": "".join(result),
        "steps": steps,
        "formula": formula
    }

def encrypt(text, keyword):
    return process_playfair(text, keyword, 'encrypt')

def decrypt(text, keyword):
    return process_playfair(text, keyword, 'decrypt')
