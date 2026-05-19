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
        
    if mode == 'encrypt':
        general_formula = "C = K &times; P mod 26"
        impl_prefix = "C = "
        impl_suffix = " &times; P mod 26"
    else:
        general_formula = "P = K⁻¹ &times; C mod 26"
        impl_prefix = "P = "
        impl_suffix = " &times; C mod 26"

    formula = f"""
    <div class="mb-2">
        <span class="badge bg-primary mb-2">Rumus Hill Cipher</span>
        
        <div class="mb-3">
            <label class="form-label fw-bold small mb-1 text-muted">Rumus Umum:</label>
            <div class="p-2 border dynamic-card-border rounded dynamic-bg-code font-monospace text-center">
                {general_formula}
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label fw-bold small mb-1 text-muted">Implementasi Saat Ini:</label>
            <div class="p-2 border dynamic-card-border rounded dynamic-bg-code font-monospace d-flex align-items-center justify-content-center gap-2">
                <span>{impl_prefix}</span>
                <div class="table-responsive" style="max-width: 250px; margin-bottom: 0;">
                    <table class="table table-bordered mb-0 playfair-table hill-table" style="background-color: transparent;">
                        <tbody>
                            {table_rows}
                        </tbody>
                    </table>
                </div>
                <span>{impl_suffix}</span>
            </div>
        </div>

        <div class="small dynamic-text-muted mb-2 text-start">
            <strong>P</strong> = vektor plaintext <br>
            <strong>C</strong> = vektor ciphertext <br>
            <strong>K</strong> = matriks kunci <br>
            <strong>K⁻¹</strong> = inverse matriks modulo 26
        </div>
    </div>
    """
    
    for i in range(0, len(clean_text), n):
        block = clean_text[i:i+n]
        vec = [ord(c) - ord('A') for c in block]
        
        res_vec = []
        raw_res_vec = []
        
        for r in range(n):
            sum_val = sum(active_matrix[r][c] * vec[c] for c in range(n))
            raw_res_vec.append(sum_val)
            res_vec.append(sum_val % 26)
            
        res_chars = "".join([chr(val + ord('A')) for val in res_vec])
        result.append(res_chars)

        matrix_html = "<table class='math-matrix'>" + "".join(["<tr>" + "".join([f"<td>{val}</td>" for val in row]) + "</tr>" for row in active_matrix]) + "</table>"
        vec_html = "<table class='math-matrix'>" + "".join([f"<tr><td>{v}</td></tr>" for v in vec]) + "</table>"
        raw_res_html = "<table class='math-matrix'>" + "".join([f"<tr><td>{v}</td></tr>" for v in raw_res_vec]) + "</table>"
        res_html = "<table class='math-matrix'>" + "".join([f"<tr><td>{v}</td></tr>" for v in res_vec]) + "</table>"

        matrix_label = "Matriks Kunci" if mode == 'encrypt' else "Inverse Matriks Kunci"

        step_html = f"""
        <div class="card mb-3 shadow-sm dynamic-card-border" style="background-color: var(--input-bg);">
            <div class="card-header py-2 d-flex justify-content-between align-items-center dynamic-header-bg dynamic-card-border">
                <div>
                    <span class="badge bg-primary fs-6">Blok {i//n + 1}</span> 
                </div>
            </div>
            <div class="card-body py-3 px-3">
                <div class="math-matrix-container overflow-x-auto">
                  <div class="d-flex align-items-center justify-content-center flex-nowrap" style="min-width: max-content;">
                     <div class="matrix-wrapper text-center mx-2" style="transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                        <div class="small dynamic-text-muted mb-1">{matrix_label}</div>
                        {matrix_html}
                     </div>
                     <div class="fs-4 mx-2 dynamic-text">&times;</div>
                     <div class="matrix-wrapper text-center mx-2" style="transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                        <div class="small dynamic-text-muted mb-1">Vektor</div>
                        {vec_html}
                     </div>
                     <div class="fs-4 mx-2 dynamic-text">=</div>
                     <div class="matrix-wrapper text-center mx-2" style="transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                        <div class="small dynamic-text-muted mb-1">Hasil Kali</div>
                        {raw_res_html}
                     </div>
                     <div class="fs-6 mx-2 dynamic-text-muted">mod 26</div>
                     <div class="fs-4 mx-2 dynamic-text">=</div>
                     <div class="matrix-wrapper text-center mx-2" style="transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                        <div class="small dynamic-text-muted mb-1">Hasil</div>
                        {res_html}
                     </div>
                  </div>
                </div>
                <div class="text-center mt-3 fw-bold fs-5 text-primary" style="letter-spacing: 2px;">
                    {block} <i class="fa-solid fa-arrow-right mx-3 dynamic-text-muted"></i> {res_chars}
                </div>
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
