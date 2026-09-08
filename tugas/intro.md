<div class="psd-hero">

  <img
    src="images/header-psd.png"
    alt="Penambangan Sains Data"
    class="psd-header-image"
  >

  <div class="psd-hero-content">

    <h1>Penambangan Sains Data</h1>

    <h2>Analisis Kualitas Udara Kecamatan Kalitengah</h2>

    <p class="psd-subtitle">
      Analisis dan eksplorasi data polutan udara menggunakan pendekatan
      data science untuk memahami kondisi lingkungan di Kecamatan Kalitengah,
      Kabupaten Lamongan.
    </p>

  </div>

</div>

<div class="profile-card">

  <img
    src="images/dapi.jpeg"
    alt="Foto Ahmad Dafi Zidni Alfarisi"
    class="profile-photo"
  >

  <div class="profile-info">
    <h2>Ahmad Dafi Zidni Alfarisi</h2>

    <p>
      <strong>Teknik Informatika</strong><br>
      Universitas Trunojoyo Madura
    </p>

    <p>
      Mata Kuliah <strong>Penambangan Sains Data</strong>
    </p>
  </div>

</div>

---

# Analisis Kualitas Udara Kecamatan Kalitengah

## Tentang Proyek

Proyek ini merupakan bagian dari kegiatan pembelajaran pada mata kuliah
**Penambangan Sains Data (PSD)**.

Fokus utama proyek adalah melakukan proses pengumpulan, pemahaman,
pengolahan, dan eksplorasi data kualitas udara di **Kecamatan Kalitengah,
Kabupaten Lamongan, Jawa Timur**.

Data yang dianalisis mencakup beberapa parameter polutan udara, yaitu:

- **NO₂ (Nitrogen Dioksida)**
- **CO (Karbon Monoksida)**
- **SO₂ (Sulfur Dioksida)**

Periode data yang digunakan adalah:

**31 Agustus 2025 – 31 Agustus 2026**

Dataset memiliki **366 tanggal kalender**, dengan jumlah observasi valid
yang berbeda pada masing-masing parameter karena adanya missing value.

| Parameter | Observasi Valid | Missing |
|---|---:|---:|
| NO₂ | 218 | 148 |
| CO | 209 | 157 |
| SO₂ | 262 | 104 |

---

## Tujuan Proyek

Proyek ini bertujuan untuk:

1. Mengumpulkan data polutan udara pada wilayah Kecamatan Kalitengah.
2. Memahami karakteristik data kualitas udara.
3. Mengidentifikasi pola dan perubahan konsentrasi polutan.
4. Melakukan eksplorasi data menggunakan visualisasi.
5. Melakukan analisis statistik terhadap data.
6. Mengolah data menggunakan PostgreSQL dan Aiven.
7. Melakukan pengolahan lanjutan menggunakan KNIME.
8. Melakukan analisis time series.
9. Menyusun hasil analisis dalam bentuk dokumentasi Jupyter Book.

---

## Wilayah Studi

Wilayah yang menjadi objek penelitian adalah:

**Kecamatan Kalitengah, Kabupaten Lamongan, Jawa Timur.**

Area pengambilan data menggunakan batas wilayah Kecamatan Kalitengah
sebagai Area of Interest (AOI).

---

## Tahapan Proyek

Proyek Penambangan Sains Data ini dilakukan secara bertahap.

### Minggu 1 — Analisis Kualitas Udara

Tahapan pertama meliputi:

1. **Business Understanding**
2. **Data Understanding**
3. **Deskripsi Fitur**
4. **Sumber Polutan**
5. **Eksplorasi Data**

Pada tahap ini dilakukan proses memahami tujuan analisis, sumber data,
karakteristik setiap fitur, sumber polutan, serta pola data melalui
visualisasi.

### Minggu 2 — PostgreSQL Aiven dan KNIME

Tahapan berikutnya meliputi:

1. Pemindahan data ke PostgreSQL Aiven
2. Pengolahan data menggunakan KNIME
3. Statistics Node
4. Perhitungan statistik
5. Analisis parameter polutan
6. Analisis time series

---

## Dataset

Data hasil crawling disimpan dalam format CSV:

`polutan_kalitengah_timeseries.csv`

Struktur utama dataset:

| Kolom | Keterangan |
|---|---|
| `date` | Tanggal pengamatan |
| `NO2` | Konsentrasi nitrogen dioksida |
| `CO` | Konsentrasi karbon monoksida |
| `SO2` | Konsentrasi sulfur dioksida |

Data kemudian digunakan sebagai dasar untuk proses eksplorasi,
visualisasi, analisis statistik, dan analisis time series.

---

## Teknologi yang Digunakan

Beberapa teknologi yang digunakan dalam proyek ini antara lain:

- Python
- Pandas
- NumPy
- Matplotlib
- openEO
- Jupyter Book
- PostgreSQL
- Aiven
- KNIME
- Git
- GitHub

---

## Hasil yang Diharapkan

Melalui proyek ini diharapkan dapat diperoleh pemahaman mengenai:

- karakteristik data polutan udara,
- distribusi masing-masing parameter,
- perubahan konsentrasi polutan dari waktu ke waktu,
- pola temporal data,
- kondisi missing value,
- kemungkinan adanya outlier,
- serta hasil analisis statistik dari data kualitas udara.

---

## Dokumentasi Proyek

Seluruh proses analisis disusun secara bertahap dalam dokumentasi ini,
mulai dari **Business Understanding** hingga analisis data dan time series.

Gunakan menu navigasi di sebelah kiri untuk melihat setiap tahap proyek.

---

<div class="psd-footer">

**Penambangan Sains Data**

Analisis Kualitas Udara Kecamatan Kalitengah

<br>

*Data • Science • Technology*

</div>