/* static/app.js */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Logika Theme Toggle (Light/Dark Mode)
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    const icon = themeToggle.querySelector('i');

    // Cek localStorage untuk preferensi sebelumnya
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-theme', savedTheme);
        updateIcon(savedTheme);
    }

    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        const processBtnIcon = document.getElementById('process-btn-icon');
        
        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateIcon(newTheme);
    });

    function updateIcon(theme) {
        const navLogoIcon = document.getElementById('nav-logo-icon');
        const emptyStateIcon = document.getElementById('empty-state-icon');
        const processBtnIcon = document.getElementById('process-btn-icon');
        const heroThemeIcon = document.getElementById('hero-theme-icon');
        
        if (theme === 'dark') {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
            themeToggle.classList.replace('btn-outline-dark', 'btn-outline-light');
            
            if (navLogoIcon) {
                navLogoIcon.classList.remove('fa-cloud-sun', 'text-primary');
                navLogoIcon.classList.add('fa-moon', 'text-warning');
            }
            if (emptyStateIcon) {
                emptyStateIcon.classList.remove('fa-cloud-sun', 'text-primary');
                emptyStateIcon.classList.add('fa-moon', 'text-warning');
            }
            if (processBtnIcon) {
                processBtnIcon.classList.remove('fa-cloud-sun');
                processBtnIcon.classList.add('fa-cloud-moon');
            }
            if (heroThemeIcon) {
            heroThemeIcon.classList.remove('fa-cloud-sun', 'text-primary');
            heroThemeIcon.classList.add('fa-cloud-moon', 'text-warning');
        }
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
            themeToggle.classList.replace('btn-outline-light', 'btn-outline-dark');
            
            if (navLogoIcon) {
                navLogoIcon.classList.remove('fa-moon', 'text-warning');
                navLogoIcon.classList.add('fa-cloud-sun', 'text-primary');
            }
            if (emptyStateIcon) {
                emptyStateIcon.classList.remove('fa-moon', 'text-warning');
                emptyStateIcon.classList.add('fa-cloud-sun', 'text-primary');
            }
            if (processBtnIcon) {
                processBtnIcon.classList.remove('fa-cloud-moon');
                processBtnIcon.classList.add('fa-cloud-sun');
            }
            if (heroThemeIcon) {
                heroThemeIcon.classList.remove('fa-cloud-moon', 'text-warning');
                heroThemeIcon.classList.add('fa-cloud-sun', 'text-primary');
            }
        }
    }

    // 2. Generate Bintang untuk Dark Mode
    const skyContainer = document.querySelector('.sky-container');
    if (skyContainer) {
        for (let i = 0; i < 80; i++) {
            const star = document.createElement('div');
            star.classList.add('star');
            
            // Random posisi
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            star.style.left = `${x}vw`;
            star.style.top = `${y}vh`;
            
            // Random ukuran
            const size = Math.random() * 3;
            star.style.width = `${size}px`;
            star.style.height = `${size}px`;
            
            // Random durasi kedip
            const duration = 2 + Math.random() * 4;
            star.style.animationDuration = `${duration}s`;
            
            // Random delay
            const delay = Math.random() * 4;
            star.style.animationDelay = `${delay}s`;
            
            skyContainer.appendChild(star);
        }
    }

    // 3. Logika Form Algoritma (Menampilkan input key yang sesuai)
    const algorithmRadios = document.querySelectorAll('input[name="algorithm"]');

    if (algorithmRadios.length > 0) {
        algorithmRadios.forEach(radio => {
            radio.addEventListener('change', updateKeyInputs);
        });

        updateKeyInputs();
    }

    function updateKeyInputs() {
        const selectedRadio = document.querySelector('input[name="algorithm"]:checked');
        const selected = selectedRadio ? selectedRadio.value : 'caesar';

        const keyGroups = document.querySelectorAll('.key-group');

        keyGroups.forEach(group => {
            group.style.display = 'none';
        });

        const activeGroup = document.getElementById(`key-group-${selected}`);
        if (activeGroup) {
            activeGroup.style.display = 'block';
        }
    }

    // =========================================
    // HILL CIPHER MATRIX GRID INPUT
    // =========================================

    const hillMatrixSize = document.querySelectorAll('input[name="hill_matrix_size"]');
    const hillMatrixGrid = document.getElementById('hill-matrix-grid');
    const hillMatrixHidden = document.getElementById('hill_key_matrix');

    function getSelectedMatrixSize() {
    const selected = document.querySelector('input[name="hill_matrix_size"]:checked');
    return selected ? parseInt(selected.value) : 2;
    }

    function getDefaultHillValues(size) {
        if (size === 3) {
            return [
                [6, 24, 1],
                [13, 16, 10],
                [20, 17, 15]
            ];
        }

        return [
            [3, 3],
            [2, 5]
        ];
    }

    function parseHillMatrixValue(value) {
        if (!value) return null;

        try {
            return value
                .trim()
                .split('\n')
                .map(row => row.split(',').map(num => num.trim()));
        } catch (error) {
            return null;
        }
    }

    function updateHiddenHillMatrix() {
        if (!hillMatrixGrid || !hillMatrixHidden || !hillMatrixSize) return;

        const size = getSelectedMatrixSize();
        const rows = [];

        for (let r = 0; r < size; r++) {
            const cols = [];

            for (let c = 0; c < size; c++) {
                const input = document.getElementById(`hill-cell-${r}-${c}`);
                cols.push(input ? input.value.trim() : '');
            }

            rows.push(cols.join(','));
        }

        hillMatrixHidden.value = rows.join('\n');
    }

    function renderHillMatrixGrid() {
        if (!hillMatrixSize || !hillMatrixGrid || !hillMatrixHidden) return;

        const size = getSelectedMatrixSize();

        hillMatrixGrid.innerHTML = '';
        hillMatrixGrid.classList.remove('hill-grid-2', 'hill-grid-3');
        hillMatrixGrid.classList.add(size === 3 ? 'hill-grid-3' : 'hill-grid-2');

        const oldMatrix = parseHillMatrixValue(hillMatrixHidden.value);
        const defaultMatrix = getDefaultHillValues(size);

        for (let r = 0; r < size; r++) {
            for (let c = 0; c < size; c++) {
                const input = document.createElement('input');

                input.type = 'number';
                input.className = 'hill-matrix-cell';
                input.id = `hill-cell-${r}-${c}`;
                input.placeholder = '0';

                if (
                    oldMatrix &&
                    oldMatrix.length === size &&
                    oldMatrix[r] &&
                    oldMatrix[r].length === size
                ) {
                    input.value = oldMatrix[r][c];
                } else {
                    input.value = defaultMatrix[r][c];
                }

                input.addEventListener('input', updateHiddenHillMatrix);

                hillMatrixGrid.appendChild(input);
            }
        }

        updateHiddenHillMatrix();
    }

    if (hillMatrixSize && hillMatrixGrid && hillMatrixHidden) {
        const currentMatrix = parseHillMatrixValue(hillMatrixHidden.value);

        if (currentMatrix && currentMatrix.length === 3) {
            const matrix3 = document.getElementById('matrix-3');
            if (matrix3) matrix3.checked = true;
        }

        renderHillMatrixGrid();
        hillMatrixSize.forEach(radio => {
            radio.addEventListener('change', renderHillMatrixGrid);
        });
    }

    // 4. Logika Interaktif Playfair Cipher (Highlight Tabel)
    const playfairSteps = document.querySelectorAll('.playfair-step');
    
    // Fungsi untuk menghapus semua highlight
    const clearHighlights = () => {
        const allCells = document.querySelectorAll('.pf-cell');
        allCells.forEach(c => {
            c.classList.remove('highlight-source', 'highlight-result', 'active-mobile-highlight');
            c.style.opacity = '1';
        });
        
        playfairSteps.forEach(s => s.classList.remove('active-step'));
    };

    // Fungsi untuk menambahkan highlight
    const applyHighlight = (stepCard) => {
        clearHighlights(); // bersihkan dulu sebelum highlight baru
        stepCard.classList.add('active-step');
        
        const r1 = stepCard.getAttribute('data-r1');
        const c1 = stepCard.getAttribute('data-c1');
        const r2 = stepCard.getAttribute('data-r2');
        const c2 = stepCard.getAttribute('data-c2');
        
        const nr1 = stepCard.getAttribute('data-nr1');
        const nc1 = stepCard.getAttribute('data-nc1');
        const nr2 = stepCard.getAttribute('data-nr2');
        const nc2 = stepCard.getAttribute('data-nc2');
        
        const cell1 = document.getElementById(`pf-cell-${r1}-${c1}`);
        const cell2 = document.getElementById(`pf-cell-${r2}-${c2}`);
        const resCell1 = document.getElementById(`pf-cell-${nr1}-${nc1}`);
        const resCell2 = document.getElementById(`pf-cell-${nr2}-${nc2}`);
        
        if (cell1) cell1.classList.add('highlight-source');
        if (cell2) cell2.classList.add('highlight-source');
        
        if (resCell1 && resCell1 !== cell1 && resCell1 !== cell2) resCell1.classList.add('highlight-result');
        if (resCell2 && resCell2 !== cell1 && resCell2 !== cell2) resCell2.classList.add('highlight-result');
        
        const allCells = document.querySelectorAll('.pf-cell');
        allCells.forEach(c => {
            if (!c.classList.contains('highlight-source') && !c.classList.contains('highlight-result')) {
                c.style.opacity = '0.4';
            }
        });
    };
    
    playfairSteps.forEach(stepCard => {
        // Desktop Hover Events
        stepCard.addEventListener('mouseenter', () => applyHighlight(stepCard));
        stepCard.addEventListener('mouseleave', clearHighlights);
        
        // Mobile Click/Touch Events
        const handleTouchClick = (e) => {
            e.preventDefault(); // Prevent double firing from touchstart and click
            if (stepCard.classList.contains('active-step')) {
                clearHighlights(); // Toggle off jika sudah aktif
            } else {
                applyHighlight(stepCard);
            }
        };
        
        stepCard.addEventListener('click', handleTouchClick);
        stepCard.addEventListener('touchstart', handleTouchClick, { passive: false });
    });

    // 5. Validasi Form Custom (Bahasa Indonesia)
    const cryptoForm = document.getElementById('crypto-form');
    if (cryptoForm) {
        cryptoForm.addEventListener('submit', function(e) {
            const textInput = document.getElementById('text-input').value.trim();
            const selectedAlgo = document.querySelector('input[name="algorithm"]:checked');
            const algoSelect = selectedAlgo ? selectedAlgo.value : 'caesar';

            if (!textInput) {
                e.preventDefault();
                alert('Pesan Error: Teks tidak boleh kosong.');
                return;
            }

            if (algoSelect === 'caesar') {
                const caesarKey = document.getElementById('caesar_key').value;
                if (!caesarKey) {
                    e.preventDefault();
                    alert('Pesan Error: Nilai shift (pergeseran) wajib diisi.');
                    return;
                }
            } else if (algoSelect === 'vigenere') {
                const vigenereKey = document.getElementById('vigenere_key').value.trim();
                if (!vigenereKey) {
                    e.preventDefault();
                    alert('Pesan Error: Keyword tidak boleh kosong.');
                    return;
                }
            } else if (algoSelect === 'affine') {
                const a = document.getElementById('affine_key_a').value;
                const b = document.getElementById('affine_key_b').value;
                if (!a || !b) {
                    e.preventDefault();
                    alert('Pesan Error: Kunci A dan Kunci B wajib diisi.');
                    return;
                }
            } else if (algoSelect === 'hill') {
                updateHiddenHillMatrix();

                const hillMatrix = document.getElementById('hill_key_matrix').value.trim();

                if (!hillMatrix) {
                    e.preventDefault();
                    alert('Pesan Error: Matriks kunci wajib diisi.');
                    return;
                }

                const matrixInputs = document.querySelectorAll('.hill-matrix-cell');
                const hasEmptyCell = Array.from(matrixInputs).some(input => input.value.trim() === '');

                if (hasEmptyCell) {
                    e.preventDefault();
                    alert('Pesan Error: Semua elemen matriks Hill wajib diisi.');
                    return;
                }
            } else if (algoSelect === 'playfair') {
                const playfairKey = document.getElementById('playfair_key').value.trim();
                if (!playfairKey) {
                    e.preventDefault();
                    alert('Pesan Error: Keyword tidak boleh kosong.');
                    return;
                }
            }
        });
    }

    // 6. Tombol Salin Hasil
    const btnCopy = document.getElementById('btn-copy');
    if (btnCopy) {
        btnCopy.addEventListener('click', () => {
            const outputText = document.getElementById('output-text');
            if (outputText) {
                // Menggunakan data-raw-result agar spasi dan format asli tidak hilang (fallback ke innerText)
                const textToCopy = outputText.getAttribute('data-raw-result') || outputText.innerText || outputText.textContent;
                
                const showSuccess = () => {
                    const originalHTML = btnCopy.innerHTML;
                    btnCopy.innerHTML = '<i class="fa-solid fa-check me-1"></i>Tersalin!';
                    btnCopy.classList.replace('btn-outline-success', 'btn-success');
                    
                    setTimeout(() => {
                        btnCopy.innerHTML = originalHTML;
                        btnCopy.classList.replace('btn-success', 'btn-outline-success');
                    }, 2000);
                };

                const fallbackCopyTextToClipboard = (text) => {
                    try {
                        const textArea = document.createElement("textarea");
                        textArea.value = text;
                        // Avoid scrolling to bottom
                        textArea.style.top = "0";
                        textArea.style.left = "0";
                        textArea.style.position = "fixed";
                        document.body.appendChild(textArea);
                        textArea.focus();
                        textArea.select();
                        document.execCommand('copy');
                        document.body.removeChild(textArea);
                        showSuccess();
                    } catch (err) {
                        alert('Gagal menyalin teks secara manual: ' + err);
                    }
                };

                // Coba gunakan Clipboard API modern jika tersedia
                if (navigator.clipboard && window.isSecureContext) {
                    navigator.clipboard.writeText(textToCopy).then(() => {
                        showSuccess();
                    }).catch(err => {
                        console.warn("Gagal menggunakan Clipboard API, mencoba fallback...", err);
                        fallbackCopyTextToClipboard(textToCopy);
                    });
                } else {
                    // Gunakan fallback untuk environment non-HTTPS atau jika clipboard tidak didukung
                    fallbackCopyTextToClipboard(textToCopy);
                }
            }
        });
    }
    // CLEAR FORM
    const clearFormBtn = document.getElementById('clear-form-btn');

    if (clearFormBtn) {

        clearFormBtn.addEventListener('click', () => {

            // TEXT INPUT
            const textInput = document.getElementById('text-input');

            if (textInput) {
                textInput.value = '';
            }

            // HILL MATRIX
            const matrixInputs = document.querySelectorAll('.hill-matrix-cell');

            matrixInputs.forEach(input => {
                input.value = '';
            });

            // OUTPUT
            const outputText = document.getElementById('output-text');

            if (outputText) {
                outputText.innerText = '';
            }
        });
    }
});
