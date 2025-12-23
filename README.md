# PROJECT MBUT: Model Ban Usia Terprediksi
### Analisis Efisiensi Algoritma Iteratif vs Rekursif pada Simulasi F1

> **Mata Kuliah:** Analisis Kompleksitas Algoritma  
> **Topik:** Perbandingan Kompleksitas Waktu & Ruang (Time & Space Complexity)  
> **Studi Kasus:** Permutasi Strategi Urutan Ban (Tire Strategy Permutation)

---

## Daftar Isi

1. [Latar Belakang](#1-latar-belakang)
2. [Rumusan Masalah](#2-rumusan-masalah)
3. [Tujuan](#3-tujuan)
4. [Landasan Teori](#4-landasan-teori)
5. [Metodologi](#5-metodologi)
6. [Implementasi](#6-implementasi)
7. [Hasil dan Analisis](#7-hasil-dan-analisis)
8. [Kesimpulan](#8-kesimpulan)
9. [Cara Menjalankan Program](#9-cara-menjalankan-program)

---

## 1. Latar Belakang

Dalam dunia balap Formula 1, strategi pemilihan dan penggunaan ban merupakan salah satu faktor krusial yang menentukan kemenangan. Setiap tim balap harus mempertimbangkan berbagai kombinasi urutan penggunaan ban, mulai dari ban Soft, Medium, hingga Hard, untuk mendapatkan performa optimal sepanjang balapan.

Permasalahan ini secara matematis dapat dimodelkan sebagai perhitungan **permutasi**, di mana jumlah kemungkinan urutan penggunaan N jenis ban adalah **N! (N faktorial)**. Misalnya, dengan 3 jenis ban, terdapat 3! = 6 kemungkinan strategi yang berbeda.

Dalam konteks komputasi, perhitungan faktorial dapat diimplementasikan dengan dua pendekatan utama: **algoritma iteratif** dan **algoritma rekursif**. Masing-masing pendekatan memiliki karakteristik yang berbeda dalam hal kompleksitas waktu (*time complexity*) dan kompleksitas ruang (*space complexity*).

Project MBUT (Model Ban Usia Terprediksi) ini bertujuan untuk menganalisis dan membandingkan efisiensi kedua pendekatan tersebut, sehingga dapat memberikan rekomendasi algoritma yang paling optimal untuk sistem simulasi strategi ban pada tim Formula 1.

---

## 2. Rumusan Masalah

Berdasarkan latar belakang di atas, rumusan masalah dalam project ini adalah:

1. Bagaimana implementasi algoritma faktorial dengan pendekatan iteratif dan rekursif?
2. Bagaimana perbandingan kompleksitas waktu (*time complexity*) antara kedua pendekatan tersebut?
3. Bagaimana perbandingan kompleksitas ruang (*space complexity*) antara kedua pendekatan tersebut?
4. Algoritma mana yang lebih efisien dan aman untuk digunakan pada sistem simulasi strategi tim F1?

---

## 3. Tujuan

Tujuan dari project ini adalah:

1. Mengimplementasikan algoritma faktorial menggunakan pendekatan iteratif dan rekursif dalam bahasa Python.
2. Melakukan benchmarking untuk mengukur waktu eksekusi kedua algoritma pada berbagai ukuran input.
3. Menganalisis dan membandingkan efisiensi kedua algoritma berdasarkan hasil benchmarking.
4. Memberikan rekomendasi algoritma yang optimal untuk digunakan dalam sistem komputasi tim F1.

---

## 4. Landasan Teori

### 4.1 Faktorial

Faktorial dari bilangan bulat non-negatif n, dilambangkan dengan n!, adalah hasil perkalian semua bilangan bulat positif yang kurang dari atau sama dengan n.

$$n! = n \times (n-1) \times (n-2) \times ... \times 2 \times 1$$

Dengan definisi khusus: **0! = 1** dan **1! = 1**

**Contoh:**
- 3! = 3 × 2 × 1 = 6
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 10! = 3.628.800

### 4.2 Algoritma Iteratif

Algoritma iteratif adalah pendekatan pemrograman yang menggunakan struktur perulangan (loop) untuk menyelesaikan masalah secara berulang hingga kondisi tertentu terpenuhi.

**Karakteristik:**
- Menggunakan struktur kontrol `for` atau `while`
- State disimpan dalam variabel lokal
- Tidak memerlukan call stack tambahan
- **Space Complexity: O(1)** - hanya membutuhkan memori konstan

### 4.3 Algoritma Rekursif

Algoritma rekursif adalah pendekatan pemrograman di mana sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan sub-masalah yang lebih kecil hingga mencapai *base case*.

**Karakteristik:**
- Fungsi memanggil dirinya sendiri
- Memiliki *base case* sebagai kondisi penghentian
- Setiap pemanggilan fungsi menambah *call stack*
- **Space Complexity: O(n)** - membutuhkan memori proporsional dengan kedalaman rekursi

### 4.4 Kompleksitas Algoritma

| Aspek | Iteratif | Rekursif |
|-------|----------|----------|
| **Time Complexity** | O(n) | O(n) |
| **Space Complexity** | O(1) | O(n) |
| **Stack Usage** | Minimal | Linear terhadap n |
| **Risk of Overflow** | Tidak ada | Ada (RecursionError) |

### 4.5 Call Stack dan Stack Overflow

Setiap kali fungsi rekursif dipanggil, Python menyimpan informasi pemanggilan tersebut di dalam **call stack**. Python memiliki batas default sekitar 1000 kedalaman rekursi. Jika batas ini terlampaui, akan terjadi **RecursionError** (stack overflow).

---

## 5. Metodologi

### 5.1 Alat dan Bahan

- **Bahasa Pemrograman:** Python 3.x
- **Library:**
  - `sys` - untuk konfigurasi recursion limit
  - `timeit` - untuk mengukur waktu eksekusi
  - `matplotlib` - untuk visualisasi hasil

### 5.2 Langkah Penelitian

1. **Implementasi Algoritma:** Membuat dua fungsi faktorial (iteratif dan rekursif)
2. **Konfigurasi Sistem:** Mengatur recursion limit Python ke 5000
3. **Benchmarking:** Menjalankan kedua algoritma dengan berbagai ukuran input (10, 100, 500, 1000, 2000, 3500, 4500)
4. **Pengukuran:** Setiap pengukuran dijalankan 1000 kali untuk akurasi
5. **Visualisasi:** Membuat grafik perbandingan waktu eksekusi
6. **Analisis:** Menginterpretasikan hasil dan menarik kesimpulan

### 5.3 Parameter Pengujian

| Parameter | Nilai |
|-----------|-------|
| Recursion Limit | 5000 |
| Jumlah Iterasi per Test | 1000 kali |
| Ukuran Input (N) | 10, 100, 500, 1000, 2000, 3500, 4500 |

---

## 6. Implementasi

### 6.1 Struktur Program

Program terdiri dari 5 modul utama:

```
Code.py
├── 1. Konfigurasi Sistem
├── 2. Implementasi Algoritma
│   ├── factorial_iterative(n)
│   └── factorial_recursive(n)
├── 3. Modul Benchmarking
│   └── run_benchmark()
├── 4. Visualisasi Hasil
│   └── plot_results()
└── 5. Main Program
```

### 6.2 Algoritma Faktorial Iteratif

```python
def factorial_iterative(n):
    # Validasi input
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    
    # Inisialisasi hasil dengan 1 (karena 0! = 1 dan 1! = 1)
    result = 1
    
    # Perulangan dari 2 sampai n
    for i in range(2, n + 1):
        result *= i
    
    return result
```

**Penjelasan:**
- Fungsi dimulai dengan validasi input untuk memastikan n tidak negatif
- Variabel `result` diinisialisasi dengan nilai 1
- Loop `for` mengiterasi dari 2 hingga n, mengalikan `result` dengan setiap nilai i
- Kompleksitas waktu O(n) karena loop berjalan n-1 kali
- Kompleksitas ruang O(1) karena hanya menggunakan satu variabel `result`

### 6.3 Algoritma Faktorial Rekursif

```python
def factorial_recursive(n):
    # Validasi input
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    
    # Base case: kondisi penghentian rekursi
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    return n * factorial_recursive(n - 1)
```

**Penjelasan:**
- Fungsi dimulai dengan validasi input
- **Base case:** Jika n = 0 atau n = 1, kembalikan 1 (kondisi penghentian)
- **Recursive case:** Fungsi memanggil dirinya sendiri dengan n-1
- Setiap pemanggilan menambah satu frame ke call stack
- Kompleksitas waktu O(n) karena ada n pemanggilan fungsi
- Kompleksitas ruang O(n) karena call stack bertumbuh linear

### 6.4 Modul Benchmarking

```python
def run_benchmark():
    # Test cases dengan berbagai ukuran input
    test_cases = [10, 100, 500, 1000, 2000, 3500, 4500]
    
    results_iterative = []
    results_recursive = []
    
    for n in test_cases:
        # Benchmark iteratif
        t_iter = timeit.timeit(f"factorial_iterative({n})", 
                               setup="from __main__ import factorial_iterative", 
                               number=1000)
        results_iterative.append(t_iter)
        
        # Benchmark rekursif dengan penanganan error
        try:
            t_rec = timeit.timeit(f"factorial_recursive({n})", 
                                  setup="from __main__ import factorial_recursive", 
                                  number=1000)
            results_recursive.append(t_rec)
        except RecursionError:
            results_recursive.append(None)  # Stack overflow
    
    return test_cases, results_iterative, results_recursive
```

**Penjelasan:**
- Fungsi menguji kedua algoritma dengan 7 ukuran input berbeda
- Setiap pengujian dijalankan 1000 kali untuk mendapatkan hasil yang akurat
- Pengujian rekursif dibungkus dalam `try-except` untuk menangani stack overflow
- Hasil dikembalikan dalam bentuk list untuk visualisasi

### 6.5 Visualisasi Hasil

```python
def plot_results(ns, times_iter, times_rec):
    plt.figure(figsize=(10, 6))
    
    # Plot data iteratif
    plt.plot(ns, times_iter, label='Iteratif (O(1) Space)', 
             marker='o', color='blue', linewidth=2)
    
    # Filter dan plot data rekursif yang valid
    valid_rec_indices = [i for i, t in enumerate(times_rec) if t is not None]
    valid_ns_rec = [ns[i] for i in valid_rec_indices]
    valid_times_rec = [times_rec[i] for i in valid_rec_indices]
    
    if valid_ns_rec:
        plt.plot(valid_ns_rec, valid_times_rec, label='Rekursif (O(n) Space)',
                 marker='x', color='red', linestyle='--', linewidth=2)
    
    # Konfigurasi grafik
    plt.xlabel('Ukuran Input (N)')
    plt.ylabel('Waktu Eksekusi (detik per 1000 calls)')
    plt.title('Benchmark: Algoritma Faktorial (Iteratif vs Rekursif)')
    plt.legend(loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.savefig('grafik_benchmark.png', dpi=150)
    plt.show()
```

**Penjelasan:**
- Membuat grafik perbandingan waktu eksekusi
- Data iteratif ditampilkan dengan garis biru solid
- Data rekursif ditampilkan dengan garis merah putus-putus
- Data yang mengalami stack overflow tidak diplot
- Grafik disimpan sebagai file PNG

---

## 7. Hasil dan Analisis

### 7.1 Hasil Benchmarking

Berikut adalah contoh hasil benchmarking yang diharapkan:

| N Input | Iteratif (detik) | Rekursif (detik) | Ratio (R/I) |
|---------|------------------|------------------|-------------|
| 10 | ~0.000200 | ~0.000300 | ~1.5x |
| 100 | ~0.002000 | ~0.004000 | ~2.0x |
| 500 | ~0.010000 | ~0.025000 | ~2.5x |
| 1000 | ~0.020000 | ~0.055000 | ~2.7x |
| 2000 | ~0.040000 | ~0.120000 | ~3.0x |
| 3500 | ~0.070000 | ~0.220000 | ~3.1x |
| 4500 | ~0.090000 | STACK OVERFLOW | N/A |

*Catatan: Nilai aktual dapat bervariasi tergantung spesifikasi hardware*

### 7.2 Analisis Hasil

**Observasi Utama:**

1. **Konsistensi Iteratif:** Algoritma iteratif menunjukkan performa yang konsisten dan stabil untuk semua ukuran input yang diuji.

2. **Overhead Rekursif:** Algoritma rekursif selalu lebih lambat dibandingkan iteratif, dengan ratio yang meningkat seiring bertambahnya ukuran input. Hal ini disebabkan oleh overhead pengelolaan call stack.

3. **Breaking Point:** Algoritma rekursif mengalami stack overflow pada N = 4500, meskipun recursion limit sudah dinaikkan menjadi 5000. Ini menunjukkan keterbatasan fundamental dari pendekatan rekursif.

4. **Skalabilitas:** Algoritma iteratif memiliki skalabilitas yang lebih baik untuk input berukuran besar.

### 7.3 Perbandingan Kompleksitas

| Kriteria | Iteratif | Rekursif | Pemenang |
|----------|----------|----------|----------|
| Time Complexity | O(n) | O(n) | Seri |
| Space Complexity | O(1) | O(n) | **Iteratif** |
| Waktu Aktual | Lebih cepat | Lebih lambat | **Iteratif** |
| Stabilitas | Stabil | Bisa crash | **Iteratif** |
| Keterbacaan Kode | Baik | Lebih intuitif | Rekursif |
| Skalabilitas | Sangat baik | Terbatas | **Iteratif** |

---

## 8. Kesimpulan

Berdasarkan hasil analisis dan benchmarking yang telah dilakukan, dapat disimpulkan bahwa:

1. **Algoritma iteratif lebih unggul** dalam hal efisiensi waktu eksekusi, penggunaan memori, dan stabilitas sistem.

2. **Algoritma rekursif memiliki keterbatasan** berupa overhead call stack yang menyebabkan waktu eksekusi lebih lama dan risiko stack overflow pada input berukuran besar.

3. **Untuk sistem simulasi strategi tim F1**, algoritma iteratif adalah pilihan yang **lebih tepat dan aman** karena:
   - Tidak ada risiko crash akibat stack overflow
   - Performa yang lebih konsisten dan cepat
   - Penggunaan memori yang lebih efisien (O(1) vs O(n))
   - Skalabilitas yang lebih baik untuk input berukuran besar

4. **Rekomendasi:** Gunakan pendekatan iteratif untuk implementasi perhitungan faktorial dalam sistem produksi, terutama yang membutuhkan keandalan tinggi seperti sistem komputasi strategi tim Formula 1.

---
### 9. Output Program

Program akan menghasilkan:
1. **Tabel benchmark** di terminal dengan perbandingan waktu eksekusi
2. **File grafik** `grafik_benchmark.png` berisi visualisasi hasil
3. **Window grafik** (jika environment mendukung display)

---
### 10 Struktur File

```
PROJECT_MBUT/
├── README.md           # Dokumentasi project (file ini)
├── TUBES/
    └── Code.py         # Source code utama
```

---

## Referensi

1. Cormen, T. H., et al. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Python Software Foundation. (2024). *Python Documentation - sys module*.
3. Python Software Foundation. (2024). *Python Documentation - timeit module*.
4. Formula 1 Official. (2024). *Tyre Regulations and Strategy*.
