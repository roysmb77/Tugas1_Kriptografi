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
        
        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateIcon(newTheme);
    });

    function updateIcon(theme) {
        const navLogoIcon = document.getElementById('nav-logo-icon');
        const emptyStateIcon = document.getElementById('empty-state-icon');
        
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
    const algoSelect = document.getElementById('algorithm-select');
    if (algoSelect) {
        algoSelect.addEventListener('change', updateKeyInputs);
        // Panggil sekali saat dimuat untuk mengatur tampilan awal
        updateKeyInputs();
    }

    function updateKeyInputs() {
        const selected = algoSelect.value;
        const keyGroups = document.querySelectorAll('.key-group');
        
        // Sembunyikan semua terlebih dahulu
        keyGroups.forEach(group => {
            group.style.display = 'none';
        });

        // Tampilkan yang sesuai dengan pilihan
        const activeGroup = document.getElementById(`key-group-${selected}`);
        if (activeGroup) {
            activeGroup.style.display = 'block';
        }
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
            const algoSelect = document.getElementById('algorithm-select').value;
            
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
                const hillMatrix = document.getElementById('hill_key_matrix').value.trim();
                if (!hillMatrix) {
                    e.preventDefault();
                    alert('Pesan Error: Matriks kunci wajib diisi.');
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
                const textToCopy = outputText.innerText || outputText.textContent;
                navigator.clipboard.writeText(textToCopy).then(() => {
                    const originalHTML = btnCopy.innerHTML;
                    btnCopy.innerHTML = '<i class="fa-solid fa-check me-1"></i>Tersalin!';
                    btnCopy.classList.replace('btn-outline-success', 'btn-success');
                    
                    setTimeout(() => {
                        btnCopy.innerHTML = originalHTML;
                        btnCopy.classList.replace('btn-success', 'btn-outline-success');
                    }, 2000);
                }).catch(err => {
                    alert('Gagal menyalin teks: ' + err);
                });
            }
        });
    }
});
