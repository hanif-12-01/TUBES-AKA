# 📘 DOKUMENTASI CODE.PY
## Tugas Besar Analisis dan Kompleksitas Algoritma
### Analisis Komparatif Efisiensi Algoritmik pada Pembangkitan Ruang Sampel Strategi Balap Formula 1: Pendekatan Iteratif versus Rekursif

---

## 1️⃣ Pendahuluan

### 1.1 Latar Belakang Masalah

Dalam ekosistem balap modern seperti Formula 1, pengambilan keputusan strategis tidak lagi hanya bergantung pada intuisi manusia atau pengalaman pembalap semata, melainkan telah berevolusi menjadi disiplin ilmu data yang sangat kompleks. Setiap detik dalam balapan menghasilkan ribuan titik data telemetri, mulai dari degradasi ban, beban bahan bakar, hingga posisi relatif pesaing di lintasan.

Salah satu tantangan komputasi terbesar dalam simulasi strategi balapan adalah memprediksi hasil akhir berdasarkan permutasi urutan pembalap. Dengan 20 pembalap di grid start, jumlah total kemungkinan urutan finis adalah faktorial dari 20 ($20!$), yang menghasilkan angka astronomis sebesar $2,43 \times 10^{18}$ kemungkinan kombinasi. Ruang sampel yang masif ini menjadi dasar bagi simulasi Monte Carlo yang digunakan tim strategi untuk menghitung probabilitas kemenangan atau peluang podium.

Mahasiswa Teknik Informatika, dalam konteks akademis, dituntut untuk memahami bagaimana mesin komputasi menangani beban kerja sebesar ini melalui desain algoritma yang efisien. Dua paradigma fundamental dalam penyelesaian masalah komputasi yang berulang adalah **Iterasi** dan **Rekursif**. Meskipun kedua pendekatan ini dapat menghasilkan output matematis yang identik—misalnya dalam perhitungan faktorial untuk menentukan ruang sampel permutasi—karakteristik kinerja keduanya sangat berbeda dalam hal penggunaan memori (*space complexity*) dan waktu eksekusi (*time complexity*).

Pemilihan antara iterasi dan rekursi bukan sekadar preferensi gaya penulisan kode, melainkan keputusan arsitektural yang berdampak pada stabilitas sistem, terutama dalam lingkungan dengan batasan sumber daya atau kebutuhan waktu nyata (*real-time*) seperti sistem tertanam (*embedded systems*) pada mobil balap atau server simulasi strategi.

Laporan tugas besar ini bertujuan untuk membedah secara mendalam perbandingan antara algoritma iteratif dan rekursif melalui studi kasus **"Prediksi Permutasi Podium Formula 1"**. Analisis ini tidak hanya akan melihat pada notasi Big-O secara teoritis, tetapi juga menyelidiki perilaku runtime pada interpreter Python, manajemen memori stack, dan implikasi risiko stack overflow yang krusial dalam rekayasa perangkat lunak berkinerja tinggi.

### 1.2 Rumusan Masalah

Berdasarkan latar belakang di atas, permasalahan yang akan dikaji dalam laporan ini adalah:

1. Bagaimana karakteristik kinerja waktu dan ruang dari algoritma iteratif dibandingkan dengan algoritma rekursif dalam menyelesaikan masalah perhitungan faktorial sebagai representasi pembangkitan ruang sampel permutasi balap?
2. Sejauh mana batasan *recursion depth* dalam bahasa pemrograman Python mempengaruhi skalabilitas solusi rekursif pada input data yang besar?
3. Manakah pendekatan yang lebih direkomendasikan untuk implementasi sistem simulasi strategi Formula 1 yang membutuhkan keandalan dan efisiensi tinggi?

### 1.3 Tujuan Penelitian

Tujuan dari penyusunan laporan ini adalah:

1. Menyediakan analisis komparatif yang komprehensif mengenai kompleksitas algoritma iteratif dan rekursif, didukung oleh data empiris dan landasan teoritis yang kuat.
2. Mendemonstrasikan implementasi kode Python untuk kedua pendekatan dalam konteks studi kasus Formula 1.
3. Menyajikan sintesis visual dalam bentuk poster akademis yang merangkum temuan kunci, termasuk grafik perbandingan kinerja dan kesimpulan strategis.
4. Memberikan wawasan mendalam mengenai mekanisme internal eksekusi program (seperti stack frames dan loops) yang relevan bagi mahasiswa teknik informatika.

### 1.4 Ruang Lingkup

Analisis ini akan berfokus pada:

- **Algoritma**: Perhitungan Faktorial ($n!$) sebagai fungsi dasar untuk menentukan jumlah permutasi ($P(n,r)$).
- **Bahasa Pemrograman**: Python 3.x, dipilih karena popularitasnya dalam data science dan relevansinya dengan pustaka analisis data modern (seperti FastF1), meskipun memiliki karakteristik manajemen memori yang unik terkait rekursi.
- **Metrik Evaluasi**: Waktu eksekusi (*Execution Time*), penggunaan memori tumpukan (*Stack Memory Usage*), dan kompleksitas asimtotik (Big-O).

---

## 2️⃣ Tinjauan Pustaka dan Landasan Teori

### 2.1 Paradigma Algoritma: Iterasi vs. Rekursi

Dalam ilmu komputer teoritis, kemampuan untuk mengulang eksekusi instruksi adalah salah satu pilar utama yang membedakan komputer dari kalkulator sederhana. Dua mekanisme utama untuk mencapai hal ini adalah **iterasi** dan **rekursi**. Donald Knuth, dalam mahakaryanya *The Art of Computer Programming*, menekankan bahwa meskipun kedua metode ini ekuivalen dalam hal kemampuan komputasi (Turing Complete), implementasi praktisnya pada arsitektur Von Neumann memiliki konsekuensi yang sangat berbeda.

#### 2.1.1 Iterasi

Iterasi adalah proses pengulangan blok kode instruksi di mana kontrol aliran program kembali ke titik awal blok tersebut sampai kondisi terminasi terpenuhi. Konstruksi ini biasanya diwujudkan dalam bentuk perulangan `for`, `while`, atau `do-while`.

- **Mekanisme**: Iterasi bekerja dengan memanipulasi *Instruction Pointer* (IP) CPU untuk melompat (*jump*) kembali ke alamat memori instruksi sebelumnya. Variabel kontrol (seperti counter) biasanya disimpan dalam register CPU atau memori lokal yang sama, diperbarui secara *in-place*.
- **Keunggulan**: Efisiensi memori yang tinggi karena tidak membutuhkan alokasi memori tambahan untuk setiap putaran (loop). Ruang lingkup variabel (*scope*) tetap konstan sepanjang eksekusi.

#### 2.1.2 Rekursi

Rekursi terjadi ketika sebuah prosedur atau fungsi memanggil dirinya sendiri sebagai bagian dari langkah penyelesaian masalah. Pendekatan ini didasarkan pada prinsip **"Divide and Conquer"**, di mana masalah besar dipecah menjadi sub-masalah yang lebih kecil yang identik dengan masalah aslinya.

**Struktur Dasar**: Setiap fungsi rekursif yang valid harus memiliki:
1. **Base Case (Kasus Dasar)**: Kondisi terminasi yang mengembalikan nilai tanpa melakukan pemanggilan rekursif lagi. Ini berfungsi sebagai "jangkar" untuk menghentikan rantai pemanggilan.
2. **Recursive Step (Langkah Rekursif)**: Bagian di mana fungsi memanggil dirinya sendiri dengan argumen yang dimodifikasi mendekati kasus dasar.

- **Mekanisme**: Setiap kali fungsi memanggil dirinya sendiri, sistem operasi harus membuat *Activation Record* atau *Stack Frame* baru pada *Call Stack*. Frame ini menyimpan parameter fungsi, variabel lokal, dan alamat kembali (*return address*).
- **Kelemahan**: Overhead memori dan waktu. Pembuatan dan penghancuran stack frame membutuhkan siklus CPU tambahan dan konsumsi memori yang berbanding lurus dengan kedalaman rekursi ($O(N)$).

### 2.2 Analisis Kompleksitas Asimtotik (Big-O Notation)

Untuk membandingkan algoritma secara objektif tanpa terikat pada spesifikasi perangkat keras tertentu, ilmuwan komputer menggunakan **Notasi Big-O**. Notasi ini mendeskripsikan batas atas (*upper bound*) dari pertumbuhan kebutuhan waktu atau ruang algoritma terhadap ukuran input ($n$).

| Jenis Kompleksitas | Deskripsi |
|-------------------|-----------|
| **Kompleksitas Waktu** (*Time Complexity*) | Mengukur seberapa cepat waktu eksekusi meningkat seiring bertambahnya input. Baik algoritma faktorial iteratif maupun rekursif secara teoritis memiliki kompleksitas waktu linear, yaitu $O(N)$, karena jumlah operasi perkalian bertambah secara linear dengan nilai $N$. |
| **Kompleksitas Ruang** (*Space Complexity*) | Mengukur memori tambahan yang dibutuhkan. Di sinilah perbedaan fundamental muncul. **Iterasi** memiliki kompleksitas ruang konstan $O(1)$ karena hanya menggunakan beberapa variabel tetap. Sebaliknya, **Rekursi** memiliki kompleksitas ruang linear $O(N)$ karena kebutuhan untuk menyimpan stack frame sebanyak $N$ pemanggilan. |

### 2.3 Konteks Python dan Manajemen Memori

Dalam bahasa Python, rekursi memiliki karakteristik khusus. Interpreter Python (CPython) **tidak mengimplementasikan optimasi Tail-Call Optimization (TCO)** yang umum ditemukan pada bahasa fungsional seperti Haskell atau Lisp. TCO memungkinkan kompilator untuk mengubah rekursi ekor menjadi iterasi di level mesin, menghilangkan overhead tumpukan.

Tanpa TCO, setiap panggilan rekursif di Python benar-benar menambah beban pada tumpukan memori. Untuk mencegah program menghabiskan seluruh memori sistem akibat rekursi tak terbatas (misalnya karena bug pada base case), Python menetapkan **batas kedalaman rekursi** (*recursion limit*), yang secara default biasanya diset pada **1000 lapis**. Jika batas ini terlampaui, interpreter akan memunculkan `RecursionError`. Hal ini menjadi batasan kritis dalam aplikasi yang memproses data besar atau struktur pohon yang dalam.

### 2.4 Studi Kasus Formula 1: Permutasi dan Probabilitas

Formula 1 adalah olahraga yang sangat bergantung pada data. Tim seperti Mercedes, Red Bull, dan Ferrari menggunakan simulasi canggih untuk memprediksi hasil balapan. Salah satu komponen dasar probabilitas adalah menghitung jumlah kemungkinan urutan finis.

Jika kita ingin mengetahui berapa banyak variasi podium (Top 3) yang mungkin terjadi dari 20 pembalap, kita menggunakan rumus permutasi:

$$P(n, r) = \frac{n!}{(n-r)!}$$

Di mana:
- $n$ adalah jumlah pembalap (20)
- $r$ adalah jumlah posisi podium (3)

**Inti dari perhitungan ini adalah fungsi faktorial ($n!$)**. Memahami efisiensi perhitungan faktorial ini memberikan wawasan mikro tentang bagaimana sistem simulasi yang lebih besar bekerja.

#### Contoh Perhitungan Permutasi Podium F1

Untuk menghitung jumlah kemungkinan variasi podium (Top 3) dari 20 pembalap:

$$P(20, 3) = \frac{20!}{(20-3)!} = \frac{20!}{17!} = 20 \times 19 \times 18 = 6.840 \text{ kombinasi}$$

Program benchmark ini menguji efisiensi perhitungan $20!$ dan $17!$ yang menjadi komponen kritis dalam simulasi strategi F1.

---

## 3️⃣ Deskripsi Program

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

![Grafik Benchmark Iteratif vs Rekursif](https://github.com/hanif-12-01/TUBES-AKA/blob/main/TUBES/grafik_benchmark.png?raw=true)

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

**Menjawab Rumusan Masalah:**

1. **Karakteristik Kinerja (RM 1)**: Algoritma Iteratif lebih efisien untuk perhitungan faktorial dalam skala besar. Meskipun keduanya memiliki kompleksitas waktu O(n), iteratif memiliki kompleksitas ruang O(1) sementara rekursif O(n).

2. **Batasan Recursion Depth (RM 2)**: Python memiliki batas rekursi default 1000. Untuk menghitung $20!$ (kebutuhan simulasi F1), rekursi masih aman. Namun untuk simulasi yang lebih kompleks dengan input besar, rekursi berisiko Stack Overflow.

3. **Rekomendasi untuk Simulasi F1 (RM 3)**: **Algoritma Iteratif direkomendasikan** untuk implementasi sistem simulasi strategi Formula 1 karena:
   - Lebih stabil tanpa risiko stack overflow
   - Performa konsisten pada berbagai ukuran input
   - Penggunaan memori yang efisien untuk komputasi real-time

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

## 📖 Referensi

1. J. Á. Velázquez-Iturbide, M. E. Castellanos, dan R. Hijón-Neira, "Recursion Removal as an Instructional Method to Enhance the Understanding of Recursion Tracing," *IEEE Transactions on Education*, vol. 59, no. 3, pp. 1-1, Aug. 2015.

2. A. Ayodele dan F. Oluwade, "A Comparative Analysis of Quick, Merge and Insertion Sort Algorithms using Three Programming Languages I: Execution Time Analysis," *African Journal of Management Information Systems*, vol. 1, no. 1, pp. 1–18, Jan. 2019.

3. N. Kumar dan R. Singh, "Performance Comparison of Sorting Algorithms On The Basis Of Complexity," *International Journal of Computer Science and Information Technology Research*, vol. 2, no. 3, pp. 394-398, 2014.

4. I. T. R. Yanto, et al., "An Analysis of a Recursive and an Iterative Algorithm for Generating Permutations Modified for Travelling Salesman Problem," *International Journal on Advanced Science, Engineering and Information Technology*, vol. 7, no. 5, 2017.

5. P. B. V. S. V. Prasad, "A Comparative Study and Analysis on the Performance of the Algorithms," *International Journal of Computer Science and Mobile Computing (IJCSMC)*, vol. 5, no. 1, Jan. 2016.

---

## 👤 Informasi

- **Mata Kuliah**: Analisis dan Kompleksitas Algoritma
- **Jenis**: Tugas Besar
- **Bahasa**: Python 3.x

---

*Dokumentasi ini dibuat secara otomatis berdasarkan analisis kode program.*
