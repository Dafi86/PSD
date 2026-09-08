# Penambangan Sains Data

## Analisis Kualitas Udara Kecamatan Kalitengah

<div align="center">

<img src="images/dapi.jpeg" alt="Foto Ahmad Dafi Zidni Alfarisi" width="180">

### Ahmad Dafi Zidni Alfarisi

**Teknik Informatika — Universitas Trunojoyo Madura**

**Mata Kuliah Penambangan Sains Data (PSD)**

</div>

---

## Tentang Proyek

Proyek ini merupakan dokumentasi kegiatan mata kuliah **Penambangan Sains Data (PSD)** yang berfokus pada proses pengumpulan, pemahaman, pengolahan, eksplorasi, dan analisis data lingkungan.

Objek yang digunakan dalam proyek ini adalah **data kualitas udara di Kecamatan Kalitengah, Kabupaten Lamongan, Jawa Timur**. Data polutan dikumpulkan untuk memperoleh gambaran mengenai perubahan konsentrasi beberapa parameter pencemar udara selama periode pengamatan.

Proyek ini menerapkan tahapan pengolahan data secara bertahap, mulai dari memahami permasalahan bisnis, memahami karakteristik data, melakukan eksplorasi, menyimpan data ke dalam basis data, melakukan pengolahan menggunakan KNIME, hingga melakukan analisis statistik dan **time series**.

---

## 📍 Wilayah Penelitian

**Kecamatan Kalitengah**  
Kabupaten Lamongan  
Jawa Timur, Indonesia

Wilayah penelitian dibatasi berdasarkan area administratif Kecamatan Kalitengah. Batas wilayah digunakan sebagai **Area of Interest (AOI)** dalam proses pengambilan data sehingga data yang diperoleh dapat difokuskan pada wilayah penelitian.

---

## 📅 Periode Pengamatan

Data yang digunakan dalam proyek ini mencakup periode:

> **31 Agustus 2025 – 31 Agustus 2026**

Periode tersebut mencakup **366 tanggal kalender**, sehingga memungkinkan dilakukan pengamatan terhadap perubahan data polutan secara temporal selama kurang lebih satu tahun.

---

## 🌫️ Parameter Polutan

Proyek ini menganalisis tiga parameter polutan utama:

| Parameter | Keterangan |
|---|---|
| **NO₂** | Nitrogen Dioksida |
| **CO** | Karbon Monoksida |
| **SO₂** | Sulfur Dioksida |

Ketiga parameter tersebut digunakan untuk melihat pola perubahan konsentrasi polutan di wilayah Kecamatan Kalitengah.

---

## 🎯 Tujuan Proyek

Proyek ini memiliki beberapa tujuan utama:

1. Mengumpulkan data polutan udara di Kecamatan Kalitengah.
2. Memahami karakteristik dan struktur data yang diperoleh.
3. Mengidentifikasi variabel dan parameter yang terdapat dalam dataset.
4. Memahami sumber dan karakteristik masing-masing polutan.
5. Melakukan eksplorasi terhadap data polutan.
6. Mengidentifikasi pola perubahan konsentrasi polutan berdasarkan waktu.
7. Menyimpan dan mengelola data menggunakan **PostgreSQL Aiven**.
8. Melakukan pengolahan data menggunakan **KNIME**.
9. Melakukan analisis statistik terhadap data.
10. Melakukan analisis **time series** untuk melihat perubahan polutan dari waktu ke waktu.
11. Mendokumentasikan seluruh proses pengolahan data secara sistematis.

---

## 🔎 Ruang Lingkup

Ruang lingkup proyek meliputi:

- Wilayah penelitian: **Kecamatan Kalitengah, Kabupaten Lamongan, Jawa Timur**.
- Periode data: **31 Agustus 2025 sampai 31 Agustus 2026**.
- Parameter yang dianalisis: **NO₂, CO, dan SO₂**.
- Pengambilan data berdasarkan wilayah administratif Kecamatan Kalitengah.
- Pengolahan data menggunakan Python.
- Penyimpanan data menggunakan PostgreSQL Aiven.
- Pengolahan data menggunakan KNIME.
- Analisis statistik.
- Analisis data berdasarkan urutan waktu atau **time series**.
- Visualisasi data dalam bentuk grafik.

---

# 🧭 Tahapan Proyek

Proyek Penambangan Sains Data ini dilakukan secara bertahap agar proses pengolahan data dapat terdokumentasi dengan baik.

### 1. Business Understanding

Tahap pertama berfokus pada pemahaman permasalahan yang akan diselesaikan melalui data.

Pada tahap ini dibahas:

- Latar belakang permasalahan.
- Kondisi dan pentingnya pemantauan kualitas udara.
- Tujuan bisnis.
- Tujuan analisis.
- Manfaat analisis data polutan.

---

### 2. Data Understanding

Tahap ini digunakan untuk memahami data yang telah dikumpulkan.

Pembahasan meliputi:

- Sumber data.
- Metode pengambilan data.
- Wilayah pengambilan data.
- Periode pengamatan.
- Struktur dataset.
- Jumlah data.
- Variabel yang tersedia.
- Missing values.
- Outliers.
- Kondisi dan kualitas data.

---

### 3. Deskripsi Fitur

Tahap ini menjelaskan setiap fitur yang terdapat dalam dataset.

Fitur utama yang digunakan antara lain:

- `date`
- `NO2`
- `CO`
- `SO2`

Setiap fitur dijelaskan berdasarkan nama, tipe data, satuan, fungsi, serta penggunaannya dalam proses analisis.

---

### 4. Sumber Polutan

Tahap ini membahas karakteristik dan sumber dari masing-masing polutan yang digunakan dalam penelitian.

Pembahasan meliputi:

- Nitrogen Dioksida (NO₂).
- Karbon Monoksida (CO).
- Sulfur Dioksida (SO₂).
- Sumber emisi polutan.
- Aktivitas manusia yang dapat menghasilkan polutan.
- Hubungan sumber emisi dengan kualitas udara.

---

### 5. Eksplorasi Data

Pada tahap eksplorasi dilakukan pemeriksaan awal terhadap dataset untuk memahami pola dan karakteristik data.

Kegiatan meliputi:

- Pemeriksaan struktur data.
- Pemeriksaan jumlah data.
- Pemeriksaan missing values.
- Statistik deskriptif.
- Visualisasi data.
- Grafik perubahan NO₂.
- Grafik perubahan CO.
- Grafik perubahan SO₂.
- Pengamatan pola perubahan berdasarkan waktu.

---

### 6. Pemindahan Data ke PostgreSQL Aiven

Dataset yang telah diperoleh kemudian dipindahkan ke database **PostgreSQL Aiven**.

Tahap ini bertujuan untuk:

- Menyimpan data secara terstruktur.
- Mempermudah pengelolaan dataset.
- Menyediakan database yang dapat diakses untuk proses analisis berikutnya.
- Memahami proses pemindahan data dari file CSV ke database PostgreSQL.

---

### 7. Pengolahan Data dengan KNIME

Data yang telah tersedia di PostgreSQL kemudian digunakan dalam proses pengolahan menggunakan **KNIME**.

Tahapan pengolahan dapat mencakup:

- Membaca data.
- Memeriksa struktur data.
- Membersihkan data.
- Mengolah missing values.
- Melakukan transformasi data.
- Menghasilkan data yang siap digunakan untuk analisis.

---

### 8. Analisis Statistik

Tahap berikutnya dilakukan analisis statistik untuk memperoleh gambaran numerik mengenai dataset.

Analisis meliputi:

- Mean.
- Median.
- Minimum.
- Maksimum.
- Standar deviasi.
- Kuartil.
- Distribusi data.
- Perbandingan karakteristik antarparameter polutan.

Hasil analisis digunakan untuk membantu memahami karakteristik konsentrasi NO₂, CO, dan SO₂.

---

### 9. Analisis Time Series

Analisis **time series** digunakan untuk melihat perubahan konsentrasi polutan berdasarkan waktu.

Analisis dilakukan dengan memperhatikan:

- Urutan waktu pengamatan.
- Perubahan konsentrasi polutan.
- Tren.
- Fluktuasi.
- Periode dengan perubahan nilai.
- Perbandingan pola NO₂, CO, dan SO₂.

Visualisasi time series digunakan untuk membantu melihat pola yang sulit diamati hanya melalui tabel data.

---

## 📊 Dataset

Dataset utama yang digunakan dalam proyek ini adalah:

**`polutan_kalitengah_timeseries.csv`**

Dataset memiliki **366 tanggal kalender** dengan tiga parameter polutan utama.

Tidak semua tanggal memiliki nilai valid untuk setiap parameter karena terdapat **missing values** pada hasil pengambilan data. Kondisi tersebut tetap dipertahankan dalam dataset agar tidak menghasilkan data buatan atau mengubah hasil pengamatan asli.

---

## 📈 Hasil yang Diharapkan

Melalui proyek ini diharapkan dapat diperoleh:

- Dataset polutan Kecamatan Kalitengah yang terdokumentasi.
- Pemahaman mengenai karakteristik data.
- Informasi mengenai sumber masing-masing polutan.
- Visualisasi perubahan konsentrasi polutan.
- Statistik deskriptif data.
- Hasil pengolahan data menggunakan KNIME.
- Database PostgreSQL yang berisi dataset.
- Analisis time series.
- Kesimpulan mengenai pola perubahan data polutan selama periode pengamatan.

---

## 🛠️ Teknologi yang Digunakan

Beberapa teknologi dan tools yang digunakan dalam proyek ini antara lain:

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **openEO**
- **Jupyter Book**
- **PostgreSQL**
- **Aiven**
- **KNIME**
- **Git & GitHub**

---

## 📚 Struktur Dokumentasi

Dokumentasi proyek disusun berdasarkan tahapan berikut:

**Minggu 1 — Analisis Kualitas Udara**

1. Business Understanding
2. Data Understanding
3. Deskripsi Fitur
4. Sumber Polutan
5. Eksplorasi Data

**Minggu 2 — PostgreSQL Aiven dan KNIME**

6. Pemindahan Data ke PostgreSQL Aiven
7. Pengolahan Data dengan KNIME
8. Analisis Statistik
9. Rumus dan Contoh Perhitungan Statistik
10. Analisis Polutan
11. Analisis Time Series dan Kesimpulan

---

## 👨‍💻 Identitas Proyek

**Nama:** Ahmad Dafi Zidni Alfarisi  
**Program Studi:** Teknik Informatika  
**Universitas:** Universitas Trunojoyo Madura  
**Mata Kuliah:** Penambangan Sains Data  
**Wilayah Analisis:** Kecamatan Kalitengah, Kabupaten Lamongan, Jawa Timur  
**Periode:** 31 Agustus 2025 – 31 Agustus 2026

---

## 📝 Catatan

Dokumentasi ini dibuat sebagai bagian dari proses pembelajaran **Penambangan Sains Data**. Seluruh tahapan analisis didokumentasikan secara bertahap agar proses pengolahan data dapat ditelusuri mulai dari pengumpulan data hingga analisis akhir.

---

> **Penambangan Sains Data — Analisis Kualitas Udara Kecamatan Kalitengah**
>
> *From raw data to meaningful insights.*