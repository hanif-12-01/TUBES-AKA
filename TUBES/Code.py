"""
TUGAS BESAR ANALISIS DAN KOMPLEKSITAS ALGORITMA
Benchmark Algoritma Faktorial: Iteratif vs Rekursif
Studi Kasus: Permutasi Podium Formula 1
"""

# Import library yang dibutuhkan
import sys        # Untuk mengatur system settings (recursion limit)
import timeit     # Untuk mengukur waktu eksekusi code
import matplotlib.pyplot as plt  # Untuk membuat grafik


# ============================================================================
# 1. KONFIGURASI SISTEM
# ============================================================================

# Set batas maksimum kedalaman rekursi ke 5000
# Default Python hanya ~1000, kita naikkan agar rekursif bisa test N lebih besar
sys.setrecursionlimit(5000)


# ============================================================================
# 2. IMPLEMENTASI ALGORITMA
# ============================================================================

def factorial_iterative(n):
    """
    Menghitung n! dengan cara iteratif (pakai loop)
    
    Kompleksitas Waktu: O(n) - loop berjalan n kali
    Kompleksitas Ruang: O(1) - hanya pakai variabel result dan i
    """
    
    # Cek apakah input valid (harus non-negatif)
    # Faktorial tidak didefinisikan untuk bilangan negatif
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    
    # Inisialisasi result dengan 1
    # Kenapa 1? Karena 0! = 1 dan 1! = 1 (definisi matematis)
    result = 1
    
    # Loop dari 2 sampai n (inklusif)
    # Kenapa mulai dari 2? Karena result sudah 1, tidak perlu dikali 1 lagi
    # range(2, n+1) menghasilkan: 2, 3, 4, ..., n
    for i in range(2, n + 1):
        # Kalikan result dengan i
        # Contoh: 5! = 1 × 2 × 3 × 4 × 5
        result *= i
    
    # Return hasil akhir
    return result


def factorial_recursive(n):
    """
    Menghitung n! dengan cara rekursif (fungsi memanggil dirinya sendiri)
    
    Kompleksitas Waktu: O(n) - fungsi dipanggil n kali
    Kompleksitas Ruang: O(n) - call stack menyimpan n frame fungsi
    """
    
    # Cek apakah input valid (harus non-negatif)
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")

    # BASE CASE: kondisi untuk menghentikan rekursi
    # Jika n = 0 atau n = 1, langsung return 1
    # Ini penting! Tanpa base case, rekursi akan infinite loop
    if n == 0 or n == 1:
        return 1

    # RECURSIVE CASE: panggil fungsi lagi dengan n-1
    # Formula: n! = n × (n-1)!
    # Contoh: 5! = 5 × 4! = 5 × 4 × 3! = ... = 5 × 4 × 3 × 2 × 1
    return n * factorial_recursive(n - 1)


# ============================================================================
# 3. MODUL BENCHMARKING
# ============================================================================

def run_benchmark():
    """
    Fungsi untuk menjalankan benchmark dan membandingkan performa
    iteratif vs rekursif
    """
    
    # Print header kosong untuk spacing
    print()
    
    # Print judul benchmark
    print("       BENCHMARK ALGORITMA FAKTORIAL: ITERATIF vs REKURSIF                  ")
    print("                 Studi Kasus: Permutasi Podium Formula 1                    ")
    
    # Print spacing
    print()
    
    # Print recursion limit yang sudah di-set
    # sys.getrecursionlimit() mengambil nilai limit yang aktif
    print(f"Recursion Limit: {sys.getrecursionlimit()}")
    print()

    # Test cases: list ukuran input yang akan di-test
    # 10      = baseline (sangat cepat)
    # 100     = ukuran kecil
    # 500     = ukuran medium-small
    # 1000    = ukuran medium
    # 2000    = ukuran medium-large
    # 3500    = ukuran besar
    # 4500    = breaking point (rekursif akan crash)
    test_cases = [10, 100, 500, 1000, 2000, 3500, 4500]

    # Buat list kosong untuk menyimpan hasil waktu eksekusi
    results_iterative = []  # Untuk hasil iteratif
    results_recursive = []  # Untuk hasil rekursif

    # Print header tabel menggunakan Unicode box-drawing characters
    # ┌ └ ┐ ┘ = sudut box
    # ─ = garis horizontal
    # │ = garis vertikal
    # ├ ┤ ┬ ┴ ┼ = junction
    print("┌─────────────┬────────────────────┬────────────────────┬─────────────────┐")
    print("│   N Input   │  Iteratif (detik)  │  Rekursif (detik)  │  Ratio (R/I)    │")
    print("├─────────────┼────────────────────┼────────────────────┼─────────────────┤")

    # Setup untuk timeit
    # timeit berjalan di namespace terpisah, jadi perlu import fungsi
    # "from __main__ import ..." = import dari file ini sendiri
    setup = "from __main__ import factorial_iterative, factorial_recursive"

    # Loop untuk setiap test case
    for n in test_cases:
        # Buat statement yang akan dieksekusi oleh timeit
        # f-string untuk memasukkan nilai n ke dalam string
        stmt_iter = f"factorial_iterative({n})"   # Contoh: "factorial_iterative(10)"
        stmt_rec = f"factorial_recursive({n})"    # Contoh: "factorial_recursive(10)"

        # === BENCHMARK ITERATIF ===
        
        # timeit.timeit(stmt, setup, number) menjalankan stmt sebanyak number kali
        # Return: total waktu eksekusi dalam detik (float)
        # Kenapa 1000x? Agar hasil lebih akurat dan mengurangi noise
        t_iter = timeit.timeit(stmt_iter, setup=setup, number=1000)
        
        # Simpan hasil ke list
        results_iterative.append(t_iter)

        # === BENCHMARK REKURSIF ===
        
        # Pakai try-except karena rekursif bisa crash (RecursionError)
        try:
            # Jalankan benchmark rekursif (sama seperti iteratif)
            t_rec = timeit.timeit(stmt_rec, setup=setup, number=1000)
            
            # Simpan hasil ke list
            results_recursive.append(t_rec)

            # Hitung ratio: berapa kali lebih lambat rekursif dibanding iteratif
            # Contoh: ratio = 1.5 artinya rekursif 1.5x lebih lambat
            # if t_iter > 0 untuk menghindari division by zero
            ratio = t_rec / t_iter if t_iter > 0 else 0
            
            # Print hasil dalam format tabel yang rapi
            # {:>10}   = right-align dengan lebar 10 karakter
            # {:.6f}   = float dengan 6 digit desimal
            # {:.2f}x  = ratio dengan 2 desimal + tanda 'x'
            print(f"│ {n:>10}  │ {t_iter:>17.6f}  │ {t_rec:>17.6f}  │ {ratio:>13.2f}x │")

        except RecursionError:
            # Tangkap RecursionError (stack overflow)
            # Ini terjadi ketika rekursi terlalu dalam
            
            # Simpan None untuk menandakan error
            results_recursive.append(None)
            
            # Print "STACK OVERFLOW" di kolom rekursif
            print(f"│ {n:>10}  │ {t_iter:>17.6f}  │ {' STACK OVERFLOW':>18} │ {'N/A':>15} │")
            
        except Exception as e:
            # Tangkap error lainnya (safety net)
            # except Exception akan catch semua error selain RecursionError
            
            # Simpan None
            results_recursive.append(None)
            
            # Ambil 15 karakter pertama dari error message
            # [:15] untuk truncate agar fit di kolom tabel
            error_msg = str(e)[:15]
            
            # Print error message di kolom rekursif
            print(f"│ {n:>10}  │ {t_iter:>17.6f}  │ {error_msg:>18} │ {'N/A':>15} │")

    # Print footer tabel (penutup)
    print("└─────────────┴────────────────────┴────────────────────┴─────────────────┘")
    print()

    # Return 3 data untuk digunakan oleh plot_results()
    # test_cases = list ukuran input [10, 100, ...]
    # results_iterative = list waktu iteratif
    # results_recursive = list waktu rekursif (bisa ada None)
    return test_cases, results_iterative, results_recursive


# ============================================================================
# 4. VISUALISASI HASIL
# ============================================================================

def plot_results(ns, times_iter, times_rec):
    """
    Membuat grafik perbandingan waktu eksekusi
    
    Args:
        ns: list ukuran input yang di-test
        times_iter: list waktu eksekusi iteratif
        times_rec: list waktu eksekusi rekursif (bisa ada None)
    """
    
    # Buat figure (kanvas kosong) dengan ukuran 10 inch × 6 inch
    plt.figure(figsize=(10, 6))

    # === PLOT ITERATIF ===
    
    # Plot garis untuk data iteratif
    plt.plot(
        ns,                              # Data X-axis (ukuran input)
        times_iter,                      # Data Y-axis (waktu eksekusi)
        label='Iteratif (O(1) Space)',   # Label untuk legend
        marker='o',                      # Marker bulat di setiap data point
        color='blue',                    # Warna garis biru
        linewidth=2                      # Ketebalan garis 2 pixel
    )

    # === PLOT REKURSIF ===
    
    # Filter data rekursif yang valid (tidak None karena crash)
    # List comprehension untuk ambil index dimana times_rec[i] bukan None
    valid_rec_indices = [i for i, t in enumerate(times_rec) if t is not None]
    
    # Ambil nilai N yang valid (hanya yang rekursif tidak crash)
    # Contoh: jika N=4500 crash, maka tidak dimasukkan
    valid_ns_rec = [ns[i] for i in valid_rec_indices]
    
    # Ambil waktu eksekusi rekursif yang valid
    valid_times_rec = [times_rec[i] for i in valid_rec_indices]

    # Plot rekursif jika ada data yang valid
    # if valid_ns_rec = cek apakah list tidak kosong
    if valid_ns_rec:
        plt.plot(
            valid_ns_rec,                    # Data X-axis (hanya yang valid)
            valid_times_rec,                 # Data Y-axis (hanya yang valid)
            label='Rekursif (O(n) Space)',   # Label untuk legend
            marker='x',                      # Marker X di setiap data point
            color='red',                     # Warna garis merah
            linestyle='--',                  # Garis putus-putus (dashed)
            linewidth=2                      # Ketebalan garis 2 pixel
        )

    # === KONFIGURASI GRAFIK ===
    
    # Set label untuk sumbu X
    plt.xlabel('Ukuran Input (N)', fontsize=12)
    
    # Set label untuk sumbu Y
    plt.ylabel('Waktu Eksekusi (detik per 1000 calls)', fontsize=12)
    
    # Set judul grafik (2 baris dengan \n)
    plt.title(
        'Benchmark: Algoritma Faktorial (Iteratif vs Rekursif)\n' +
        'Studi Kasus: Permutasi Podium Formula 1', 
        fontsize=14,           # Ukuran font 14
        fontweight='bold'      # Text tebal (bold)
    )
    
    # Tampilkan legend di pojok kiri atas
    # Legend menampilkan label dari setiap garis
    plt.legend(loc='upper left')
    
    # Tampilkan grid (garis bantu)
    plt.grid(
        True,              # Aktifkan grid
        linestyle=':',     # Garis titik-titik
        alpha=0.7          # Transparansi 70% (0.0-1.0)
    )

    # === SAVE DAN SHOW ===
    
    # Adjust layout agar tidak ada elemen yang terpotong
    plt.tight_layout()
    
    # Save grafik sebagai file PNG
    plt.savefig(
        'grafik_benchmark.png',   # Nama file output
        dpi=150,                  # Resolusi 150 dots per inch (kualitas medium-high)
        bbox_inches='tight'       # Crop whitespace di pinggir
    )
    
    # Print konfirmasi bahwa grafik sudah tersimpan
    print("✅ Grafik disimpan sebagai 'grafik_benchmark.png'")
    
    # Tampilkan grafik di window (jika ada display)
    # Di beberapa environment (server, headless), ini akan skip otomatis
    plt.show()


# ============================================================================
# 5. MAIN PROGRAM
# ============================================================================

# if __name__ == "__main__":
# Artinya: code di bawah hanya jalan kalau file ini di-run langsung
# Tidak jalan kalau file ini di-import sebagai module
if __name__ == "__main__":
    
    # Print garis header (80 karakter tanda '=')
    print("="*80)
    
    # Print judul program
    print("     TUGAS BESAR ANALISIS DAN KOMPLEKSITAS ALGORITMA")
    print("     Perbandingan Efisiensi Algoritma Iteratif vs Rekursif")
    
    # Print garis header
    print("="*80)
    
    # Jalankan benchmark dan simpan hasilnya
    # ns = list ukuran input
    # t_iter = list waktu iteratif
    # t_rec = list waktu rekursif
    ns, t_iter, t_rec = run_benchmark()
    
    # Buat visualisasi grafik dari hasil benchmark
    plot_results(ns, t_iter, t_rec)
    
    # Print newline + garis footer
    print("\n" + "="*80)
    
    # Print penutup
    print("     BENCHMARK SELESAI")
    
    # Print garis footer
    print("="*80)
