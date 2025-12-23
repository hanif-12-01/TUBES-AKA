# PROJECT MBUT: Model Ban Usia Terprediksi
### Analisis Efisiensi Algoritma Iteratif vs Rekursif pada Simulasi F1

> **Mata Kuliah:** Analisis Kompleksitas Algoritma  
> **Topik:** Perbandingan Kompleksitas Waktu & Ruang (Time & Space Complexity)  
> **Studi Kasus:** Permutasi Strategi Urutan Ban (Tire Strategy Permutation)

---

## 📋 Deskripsi Proyek

Dalam ajang balap Formula 1, urutan penggunaan ban (misalnya: *Soft* ➝ *Medium* ➝ *Hard*) sangat menentukan kemenangan. **"Project MBUT"** adalah modul simulasi awal yang bertujuan untuk menghitung **total ruang pencarian (search space)** dari kombinasi strategi ban yang mungkin dilakukan oleh tim.

Program ini membandingkan dua pendekatan algoritma untuk menghitung permutasi strategi tersebut:
1.  **Iteratif (Looping)**
2.  **Rekursif (Recursive)**

Tujuannya adalah membuktikan algoritma mana yang paling efisien dan aman untuk dijalankan pada komputer strategi tim F1, terutama ketika memproses data dalam jumlah besar.

---

## 🏎️ Studi Kasus: Strategi Ban

**Masalah:**
Sebuah tim memiliki stok **N jenis ban** berbeda. Berapa banyak kemungkinan **urutan pemasangan ban** yang bisa mereka coba dalam simulasi strategi balapan?

**Solusi Matematis:**
Permasalahan ini diselesaikan dengan rumus **Faktorial (N!)**.

**Contoh:**
Jika ada 3 jenis ban (🔴Soft, 🟡Medium, ⚪Hard), maka:
$$3! = 3 \times 2 \times 1 = 6 \text{ kemungkinan strategi}$$

Daftar kemungkinannya:
1. 🔴 ➝ 🟡 ➝ ⚪
2. 🔴 ➝ ⚪ ➝ 🟡
3. 🟡 ➝ 🔴 ➝ ⚪
4. 🟡 ➝ ⚪ ➝ 🔴
5. ⚪ ➝ 🔴 ➝ 🟡
6. ⚪ ➝ 🟡 ➝ 🔴

---

## 💻 Implementasi Code

Program ditulis dalam Python dan menguji dua fungsi berikut:

### 1. Algoritma Iteratif
Menggunakan perulangan `for` untuk mengalikan angka dari 2 hingga N.

```python
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
