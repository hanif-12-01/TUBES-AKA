# 📘 DOKUMENTASI CODE.PY
## Tugas Besar Analisis dan Kompleksitas Algoritma

---

## 📋 Deskripsi Program

Program ini merupakan **benchmark perbandingan algoritma faktorial** yang membandingkan dua pendekatan:
1. **Algoritma Iteratif** (menggunakan loop)
2. **Algoritma Rekursif** (fungsi memanggil dirinya sendiri)

Program mengukur waktu eksekusi kedua algoritma dan menampilkan hasil dalam bentuk tabel serta visualisasi grafik.

---

## 📁 Struktur Program

```
Code.py
├── 1. KONFIGURASI SISTEM
├── 2. IMPLEMENTASI ALGORITMA
│   ├── factorial_iterative(n)
│   └── factorial_recursive(n)
├── 3. MODUL BENCHMARKING
│   └── run_benchmark()
└── 4. VISUALISASI HASIL
    └── plot_results()
```

---

## 🔧 Konfigurasi Sistem

```python
sys.setrecursionlimit(5000)
```

**Penjelasan:**
- Python memiliki batas rekursi default sekitar 1000
- Limit dinaikkan menjadi 5000 agar algoritma rekursif dapat menghitung faktorial hingga N = 4500 tanpa error `RecursionError`

---

## 📐 Implementasi Algoritma

### 1. Algoritma Iteratif

```python
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

| Aspek | Keterangan |
|-------|------------|
| **Cara Kerja** | Menggunakan loop `for` untuk mengalikan angka dari 2 hingga n |
| **Kompleksitas Waktu** | O(n) |
| **Kompleksitas Ruang** | O(1) - hanya menyimpan variabel `result` |
| **Kelebihan** | Efisien dalam penggunaan memori, tidak ada overhead call stack |
| **Kekurangan** | Kode mungkin kurang intuitif untuk konsep matematis |

---

### 2. Algoritma Rekursif

```python
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif")
    
    # BASE CASE
    if n == 0 or n == 1:
        return 1
    
    # RECURSIVE CASE
    return n * factorial_recursive(n - 1)
```

| Aspek | Keterangan |
|-------|------------|
| **Cara Kerja** | Fungsi memanggil dirinya sendiri dengan nilai n-1 hingga mencapai base case |
| **Base Case** | n = 0 atau n = 1, mengembalikan nilai 1 |
| **Recursive Case** | n × factorial(n-1) |
| **Kompleksitas Waktu** | O(n) |
| **Kompleksitas Ruang** | O(n) - setiap pemanggilan menambah frame ke call stack |
| **Kelebihan** | Kode lebih intuitif sesuai definisi matematis |
| **Kekurangan** | Menggunakan memori lebih banyak, risiko Stack Overflow |

---

## ⏱️ Modul Benchmarking

### Fungsi `run_benchmark()`

```python
def run_benchmark():
    test_cases = [10, 100, 500, 1000, 2000, 3500, 4500]
    # ... pengukuran waktu ...
```

**Cara Kerja:**

1. **Menyiapkan Test Cases**: Daftar nilai N yang akan diuji
2. **Menggunakan `timeit`**: Setiap fungsi dijalankan 1000 kali untuk mendapatkan waktu yang stabil
3. **Menghitung Ratio**: Perbandingan waktu Rekursif / Iteratif
4. **Error Handling**: Menangkap `RecursionError` jika terjadi Stack Overflow

**Contoh Output:**

```
┌─────────────┬────────────────────┬────────────────────┬─────────────────┐
│   N Input   │  Iteratif (detik)  │  Rekursif (detik)  │  Ratio (R/I)    │
├─────────────┼────────────────────┼────────────────────┼─────────────────┤
│         10  │           0.001234 │           0.002345 │          1.90x  │
│        100  │           0.012345 │           0.034567 │          2.80x  │
│       1000  │           0.123456 │           0.456789 │          3.70x  │
└─────────────┴────────────────────┴────────────────────┴─────────────────┘
```

---

## 📊 Visualisasi Hasil

### Fungsi `plot_results()`

**Fitur:**
- Grafik garis perbandingan waktu eksekusi
- Garis **biru** (solid): Algoritma Iteratif
- Garis **merah** (putus-putus): Algoritma Rekursif
- Filtering otomatis untuk data yang error (None)

**Komponen Grafik:**
- **Sumbu X**: Ukuran Input (N)
- **Sumbu Y**: Waktu Eksekusi (detik per 1000 calls)
- **Legend**: Keterangan algoritma
- **Grid**: Garis bantu untuk kemudahan membaca

### Grafik Hasil Benchmark

![Grafik Benchmark Iteratif vs Rekursif](grafik_benchmark.png)

*Gambar: Perbandingan waktu eksekusi algoritma Iteratif (biru) vs Rekursif (merah)*

---

## 🚀 Cara Menjalankan Program

```powershell
# Pastikan matplotlib terinstall
pip install matplotlib

# Jalankan program
python Code.py
```

---

## 📈 Hasil Analisis

### Perbandingan Performa

| Input (N) | Iteratif | Rekursif | Keterangan |
|-----------|----------|----------|------------|
| Kecil (10-100) | Sangat cepat | Sangat cepat | Perbedaan minimal |
| Menengah (500-2000) | Cepat | Lebih lambat | Overhead rekursi mulai terasa |
| Besar (3500-4500) | Tetap stabil | Jauh lebih lambat | Call stack membesar |

### Kesimpulan

1. **Algoritma Iteratif lebih efisien** untuk perhitungan faktorial dalam skala besar
2. **Rekursif menggunakan memori O(n)** karena setiap pemanggilan menambah frame ke call stack
3. **Ratio Rekursif/Iteratif meningkat** seiring bertambahnya ukuran input
4. **Rekursif berisiko Stack Overflow** pada input yang sangat besar

---

## 📚 Library yang Digunakan

| Library | Fungsi |
|---------|--------|
| `sys` | Mengatur recursion limit |
| `timeit` | Mengukur waktu eksekusi dengan akurat |
| `matplotlib.pyplot` | Membuat visualisasi grafik |

---

## ⚠️ Error Handling

Program menangani dua jenis error:

1. **`ValueError`**: Jika input negatif
2. **`RecursionError`**: Jika stack overflow (ditampilkan sebagai "STACK OVERFLOW" di tabel)

---

## 👤 Informasi

- **Mata Kuliah**: Analisis dan Kompleksitas Algoritma
- **Jenis**: Tugas Besar
- **Bahasa**: Python 3.x

---

*Dokumentasi ini dibuat secara otomatis berdasarkan analisis kode program.*
