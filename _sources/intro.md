# Penambangan Sains Data

## Analisis Kualitas Udara

Selamat datang di website dokumentasi mata kuliah **Penambangan Sains Data (PSD)**.

Website ini digunakan untuk mendokumentasikan proses pengerjaan tugas, mulai dari pemahaman permasalahan, pengumpulan data, pemahaman dataset, eksplorasi data, hingga analisis dan visualisasi.

Pada pertemuan ini, fokus utama adalah memahami permasalahan dan dataset kualitas udara pada wilayah pengamatan yang dipilih.

---

## Identitas

| Keterangan | Informasi |
|---|---|
| Nama | **Ahmad Dafi Zidni Alfarisi** |
| Program Studi | **Teknik Informatika** |
| Mata Kuliah | **Penambangan Sains Data** |
| Universitas | **Universitas Trunojoyo Madura** |
| Repository | **Dafi86/PSD** |

---

## Tentang Project

Project ini bertujuan untuk mengetahui kondisi kualitas udara pada suatu wilayah berdasarkan data polutan.

Data kualitas udara akan dikumpulkan dari sumber data yang tersedia melalui proses crawling atau pemanfaatan API. Selanjutnya, data akan dibatasi berdasarkan wilayah pengamatan menggunakan koordinat, GeoJSON, atau tools geografis lainnya.

Data yang telah diperoleh kemudian disimpan dalam format **CSV** dan dianalisis untuk mengetahui karakteristik serta perubahan kualitas udara dari waktu ke waktu.

---

## Tujuan Project

Tujuan utama project ini adalah:

> **Mengetahui dan menganalisis kualitas udara di wilayah pengamatan berdasarkan data polutan.**

Beberapa hal yang akan dilakukan dalam project ini meliputi:

- mengumpulkan data polutan;
- menentukan wilayah pengamatan;
- membatasi data berdasarkan wilayah;
- menyimpan data dalam format CSV;
- memahami setiap fitur pada dataset;
- melakukan eksplorasi data;
- menemukan data yang tidak lengkap atau tidak wajar;
- menganalisis perubahan polutan;
- membuat visualisasi time series.

---

## Wilayah Pengamatan

Wilayah penelitian akan ditentukan berdasarkan daerah masing-masing.

**Wilayah:** `[ISI WILAYAH]`

**Kabupaten/Kota:** `[ISI KABUPATEN/KOTA]`

**Provinsi:** `[ISI PROVINSI]`

**Latitude:** `[ISI LATITUDE]`

**Longitude:** `[ISI LONGITUDE]`

Koordinat tersebut nantinya digunakan sebagai salah satu dasar untuk menentukan wilayah pengambilan data.

---

## Periode Data

Data yang digunakan ditargetkan mencakup periode minimal **1 tahun** dan data terbaru sampai dengan:

> **31 Agustus 2026**

Periode aktual akan disesuaikan dengan ketersediaan data dari sumber yang digunakan.

**Tanggal awal:** `[ISI]`

**Tanggal akhir:** `31 Agustus 2026`

---

## Data yang Digunakan

Data yang akan digunakan merupakan data kualitas udara yang dapat mencakup beberapa parameter polutan, seperti:

- PM2.5
- PM10
- CO
- NO₂
- SO₂
- O₃

Tidak semua parameter harus tersedia. Fitur yang ditampilkan pada analisis akhir akan disesuaikan dengan dataset yang berhasil diperoleh.

---

## Tahapan Project

Secara umum, project akan dilakukan melalui beberapa tahapan:

```text
Business Understanding
        ↓
Data Understanding
        ↓
Data Collection / Crawling
        ↓
Penentuan Wilayah
        ↓
GeoJSON / Spatial Filtering
        ↓
Penyimpanan CSV
        ↓
Data Preparation
        ↓
Explorasi Data
        ↓
Analisis
        ↓
Time Series
        ↓
Kesimpulan