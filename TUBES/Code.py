import sys
import timeit
import matplotlib.pyplot as plt


# 1. KONFIGURASI SISTEM

sys.setrecursionlimit(5000)

# 2. IMPLEMENTASI ALGORITMA


def factorial_iterative(n):
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")

    # BASE CASE
    if n == 0 or n == 1:
        return 1

    # RECURSIVE CASE
    return n * factorial_recursive(n - 1)


# 3. MODUL BENCHMARKING

def run_benchmark():
    print()
    print("       BENCHMARK ALGORITMA FAKTORIAL: ITERATIF vs REKURSIF                  ")
    print()
    print(f"Recursion Limit: {sys.getrecursionlimit()}")
    print()

    test_cases = [10, 100, 500, 1000, 2000, 3500, 4500] #data yang di test

    results_iterative = [] #ini buat waktu si iterative
    results_recursive = [] #ini buat buat waktu si rekursive

    # Header tabel
    print("┌─────────────┬────────────────────┬────────────────────┬─────────────────┐")
    print("│   N Input   │  Iteratif (detik)  │  Rekursif (detik)  │  Ratio (R/I)    │")
    print("├─────────────┼────────────────────┼────────────────────┼─────────────────┤")

    setup = "from __main__ import factorial_iterative, factorial_recursive" #kita membwa fungsi fac_iterative, samaa factorial rekursive ke dalam kotak

    for n in test_cases: #ini biar inputnya lgsg masuk ke dalalm code tanpa input manual
        stmt_iter = f"factorial_iterative({n})" #berfungsi untuk menyiapkan teks perintah untuk fungsi itterative agar nanti bisa dibaca dan dieksekusi oleh timeit.
        stmt_rec = f"factorial_recursive({n})"# berfungsi untuk menyiapkan teks perintah untuk fungsi rekursif agar nanti bisa dibaca dan dieksekusi oleh timeit.

        # Jalankan Iteratif
        t_iter = timeit.timeit(stmt_iter, setup=setup, number=1000)# Eksekusi fungsi 1000 kali untuk mendapatkan total waktu yang akurat (stabil) agar perbandingan adil.
        results_iterative.append(t_iter)

        # Jalankan Rekursif
        t_rec = 0
        try:
            t_rec = timeit.timeit(stmt_rec, setup=setup, number=1000) # Eksekusi fungsi 1000 kali untuk mendapatkan total waktu yang akurat (stabil) agar perbandingan adil.
            results_recursive.append(t_rec)

            ratio = t_rec / t_iter if t_iter > 0 else 0
            print(f"│ {n:>10}  │ {t_iter:>17.6f}  │ {t_rec:>17.6f}  │ {ratio:>13.2f}x │")

        except RecursionError: #kita membuat program antisipasi error
            results_recursive.append(None)
            print(f"│ {n:>10}  │ {t_iter:>17.6f}  │ {' STACK OVERFLOW':>18} │ {'N/A':>15} │")
        except Exception as e:
            results_recursive.append(None) #Ini adalah cadangan lain. Siapa tahu errornya bukan karena rekursi (misalnya error memori RAM penuh atau error salah ketik).
            print(f"│ {n:>10}  │ {t_iter:>17.6f}  │ {' ERROR':>18} │ {'N/A':>15} │")

    print("└─────────────┴────────────────────┴────────────────────┴─────────────────┘")
    print()

    return test_cases, results_iterative, results_recursive

# 4. VISUALISASI HASIL
def plot_results(ns, times_iter, times_rec): # untuk membuat dan menampilkan grafik dari data hasil benchmarking.

    # Plot Iteratif
    plt.figure(figsize=(10, 6))  #menggambar garis untuk hasil Iteratif. Label Iteratif (O(1) Space) menunjukkan bahwa metode ini umumnya memiliki kompleksitas ruang (memori) yang konstan, yang merupakan keunggulannya.

    plt.plot(ns, times_iter, label='Iteratif ', marker='o', color='blue', linewidth=2)

    # Plot Rekursif (Filter data None akibat crash)
    valid_rec_indices = [i for i, t in enumerate(times_rec) if t is not None]
    valid_ns_rec = [ns[i] for i in valid_rec_indices]
    valid_times_rec = [times_rec[i] for i in valid_rec_indices] #menggunakan list comprehension untuk membuat daftar indeks (posisi) dari semua data waktu eksekusi rekursif (times_rec) yang tidak bernilai, enumerate(times_rec): Berfungsi untuk mengulang list times_rec sambil memberikan indeks (i) dan nilai (t) dari setiap elemen.


    if valid_ns_rec:
        plt.plot(valid_ns_rec, valid_times_rec, label='Rekursif ', marker='x', color='red', linestyle='--', linewidth=2)

    plt.xlabel('Ukuran Input (N)', fontsize=12)
    plt.ylabel('Waktu Eksekusi (detik per 1000 calls)', fontsize=12)
    plt.title('Performance Benchmark: Iterative vs Recursive', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)

    plt.tight_layout()
    plt.savefig('grafik_benchmark.png', dpi=150, bbox_inches='tight')
    print("Grafik disimpan sebagai 'grafik_benchmark.png'")
    plt.show()

if __name__ == "__main__":
    ns, t_iter, t_rec = run_benchmark()
    plot_results(ns, t_iter, t_rec)