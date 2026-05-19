def parse_matrix(matrix_str):
    # Mengubah input text area menjadi list of lists (matriks)
    try:
        rows = matrix_str.strip().split('\n')
        matrix = []
        for row in rows:
            if not row.strip(): continue # Lewati baris kosong
            # Memisahkan berdasarkan koma dan menghapus spasi kosong
            vals = [int(val.strip()) for val in row.split(',') if val.strip()]
            if vals:
                matrix.append(vals)
            
        n = len(matrix)
        if n == 0: return None
        # Validasi bentuk matriks (harus n x n)
        for r in matrix:
            if len(r) != n:
                return None
        return matrix
    except Exception:
        return None

def determinant2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def determinant3x3(m):
    return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1]) -
            m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0]) +
            m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]))

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def cofactor_matrix3x3(m):
    # Menghitung matriks kofaktor untuk 3x3
    cofactor = []
    for r in range(3):
        row_cf = []
        for c in range(3):
            # submatriks 2x2
            sub = []
            for i in range(3):
                if i == r: continue
                sub_row = []
                for j in range(3):
                    if j == c: continue
                    sub_row.append(m[i][j])
                sub.append(sub_row)
            det_sub = determinant2x2(sub)
            sign = (-1)**(r+c)
            row_cf.append(sign * det_sub)
        cofactor.append(row_cf)
    return cofactor

def transpose(m):
    n = len(m)
    return [[m[j][i] for j in range(n)] for i in range(n)]

def inverse_matrix_mod26(m):
    n = len(m)
    if n == 2:
        det = determinant2x2(m)
    elif n == 3:
        det = determinant3x3(m)
    else:
        return None

    det = det % 26
    inv_det = mod_inverse(det, 26)
    
    if inv_det == -1:
        return None # Matriks tidak invertible mod 26

    # Adjugate matrix
    if n == 2:
        adj = [
            [m[1][1], -m[0][1]],
            [-m[1][0], m[0][0]]
        ]
    else:
        cf = cofactor_matrix3x3(m)
        adj = transpose(cf)
        
    # Kalikan adjugate dengan inv_det mod 26
    inv_m = []
    for r in range(n):
        row_inv = []
        for c in range(n):
            val = (adj[r][c] * inv_det) % 26
            row_inv.append(val)
        inv_m.append(row_inv)
        
    return inv_m

def process_hill(text, matrix_str, mode):
    matrix = parse_matrix(matrix_str)
    if matrix is None:
        return {"result": "Error: Format matriks tidak valid. Pastikan bentuknya merata (misal 2x2 atau 3x3) dipisah koma.", "steps": [], "formula": "", "matrix": matrix_str}
        
    n = len(matrix)
    if n not in [2, 3]:
        return {"result": "Error: Hanya mendukung matriks 2x2 dan 3x3.", "steps": [], "formula": "", "matrix": matrix_str}

    # Cek determinan untuk validasi kunci
    det = determinant2x2(matrix) if n == 2 else determinant3x3(matrix)
    if mod_inverse(det % 26, 26) == -1:
        return {"result": f"Error: Matriks tidak invertible modulo 26 (Determinan = {det}). Silakan gunakan matriks lain.", "steps": [], "formula": "", "matrix": matrix_str}

    active_matrix = matrix
    if mode == 'decrypt':
        active_matrix = inverse_matrix_mod26(matrix)
        if active_matrix is None:
            return {"result": "Error: Gagal mencari inverse matriks.", "steps": [], "formula": "", "matrix": matrix_str}

    # Mempersiapkan teks (hanya huruf, uppercase)
    clean_text = "".join([c.upper() for c in text if c.isalpha()])
    
    # Padding dengan 'X' jika panjang tidak kelipatan 'n'
    while len(clean_text) % n != 0:
        clean_text += 'X'

    result = []
    steps = []
    # Formula (Table HTML)
    table_rows = ""
    for row in active_matrix:
        table_rows += "<tr>" + "".join([f"<td class='text-center align-middle fs-5 p-2 pf-cell'>{val}</td>" for val in row]) + "</tr>"
    
    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Matriks Digunakan (Mod 26)</span>
        <div class="table-responsive" style="max-width: 250px;">
            <table class="table table-bordered mb-0 playfair-table hill-table">
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
        <div class="alert alert-info dynamic-bg-code dynamic-text border-0 py-2 px-3 small mt-2">
            <i class="fa-solid fa-lightbulb text-warning me-2"></i>
            Hill Cipher menggunakan perkalian matriks (aljabar linear) dengan vektor blok teks untuk menghasilkan ciphertext, lalu di-modulo 26.
        </div>
    </div>
    """
    
    for i in range(0, len(clean_text), n):
        block = clean_text[i:i+n]
        vec = [ord(c) - ord('A') for c in block]
        
        res_vec = []
        
        step_html = f"""
        <div class="card mb-3 shadow-sm dynamic-card-border" style="background-color: var(--input-bg);">
            <div class="card-header py-2 d-flex align-items-center dynamic-header-bg dynamic-card-border">
                <span class="me-2 dynamic-text-muted small">Blok Teks:</span>
                <span class="badge bg-primary fs-6 me-2">{block}</span> 
                <i class="fa-solid fa-arrow-right mx-2 dynamic-text-muted"></i> 
                <span class="font-monospace px-2 py-1 rounded dynamic-bg-code" style="color: var(--text-color);">{vec}</span>
            </div>
            <div class="card-body py-2 px-3">
        """
        
        # Perkalian matriks dengan vektor
        for r in range(n):
            sum_val = sum(active_matrix[r][c] * vec[c] for c in range(n))
            mod_val = sum_val % 26
            res_vec.append(mod_val)
            
            calc_str = " + ".join([f"({active_matrix[r][c]} &times; {vec[c]})" for c in range(n)])
            
            step_html += f"""
                <div class="mb-2 pb-2 dynamic-border-bottom last-border-none">
                    <div class="small dynamic-text-muted mb-1">Perhitungan Baris ke-{r+1}</div>
                    <div class="d-flex align-items-center flex-wrap gap-2 font-monospace dynamic-text" style="font-size: 0.95rem;">
                        <span class="text-nowrap">{calc_str} = <strong>{sum_val}</strong></span>
                        <i class="fa-solid fa-arrow-right dynamic-text-muted small"></i>
                        <span class="badge bg-secondary">Mod 26</span>
                        <i class="fa-solid fa-equals dynamic-text-muted small"></i>
                        <strong class="dynamic-text-success fs-5">{mod_val}</strong>
                        <i class="fa-solid fa-arrow-right dynamic-text-muted small"></i>
                        <span class="badge bg-success fs-6">{chr(mod_val + ord('A'))}</span>
                    </div>
                </div>
            """
            
        res_chars = "".join([chr(val + ord('A')) for val in res_vec])
        result.append(res_chars)
        
        step_html += f"""
            </div>
            <div class="card-footer py-2 text-end dynamic-footer-bg dynamic-card-border">
                <span class="dynamic-text-muted small me-2">Hasil Konversi Blok:</span> <span class="badge bg-success fs-6">{res_chars}</span>
            </div>
        </div>
        """
        steps.append(step_html)

    return {
        "result": "".join(result),
        "steps": steps,
        "formula": formula,
        "matrix": matrix_str
    }

def encrypt(text, matrix_str):
    return process_hill(text, matrix_str, 'encrypt')

def decrypt(text, matrix_str):
    return process_hill(text, matrix_str, 'decrypt')
