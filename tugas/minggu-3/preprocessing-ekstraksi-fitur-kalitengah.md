# Minggu 2 — Preprocessing dan Ekstraksi Fitur TSFEL

## 1. Gambaran Umum

Pada tahap ini dilakukan preprocessing terhadap data kualitas udara Kecamatan Kalitengah, Kabupaten Lamongan. Preprocessing dilakukan sebelum proses ekstraksi fitur agar data time series dapat digunakan dengan lebih baik.

Alur keseluruhan tahap ini adalah:

```text
Data kualitas udara
        ↓
Preprocessing
        ↓
Data bersih
        ↓
Ekstraksi fitur TSFEL
        ↓
65 fitur / polutan
        ↓
195 fitur keseluruhan
```

Data yang digunakan terdiri dari tiga parameter polutan, yaitu **NO₂, CO, dan SO₂**.

---

# 2. Preprocessing Data Kualitas Udara

## 2.1 Tujuan

Preprocessing adalah tahap untuk membersihkan dan menyiapkan data sebelum digunakan pada proses analisis berikutnya.

Tahapan preprocessing yang dilakukan adalah:

1. menggunakan data sesuai wilayah penelitian;
2. memeriksa missing value;
3. mendeteksi outlier menggunakan metode IQR;
4. mengubah outlier menjadi missing value;
5. melakukan imputasi missing value;
6. memastikan seluruh data sudah terisi sebelum ekstraksi fitur.

## 2.2 Dataset

Data yang digunakan merupakan data harian dari Kecamatan Kalitengah, Kabupaten Lamongan.

Periode data:

**31 Agustus 2025 sampai 31 Agustus 2026**

Jumlah tanggal:

**366 tanggal**

Kolom yang digunakan:

| Kolom | Keterangan |
|---|---|
| `date` | Tanggal pengamatan |
| `NO2` | Data nitrogen dioksida |
| `CO` | Data karbon monoksida |
| `SO2` | Data sulfur dioksida |

---

## 2.3 Missing Value Data Awal

Pada data awal masih terdapat beberapa nilai yang kosong.

| Polutan | Missing Value |
|---|---:|
| NO₂ | 148 |
| CO | 157 |
| SO₂ | 104 |

Missing value tidak langsung dihapus karena data yang digunakan merupakan data time series harian. Penghapusan data dapat membuat rangkaian waktu menjadi tidak lengkap.

Sederhananya, missing value adalah nilai yang tidak tersedia pada suatu tanggal. Data tersebut tetap dipertahankan tanggalnya dan nantinya dilakukan proses pengisian.

---

## 2.4 Deteksi Outlier

Outlier adalah nilai yang berbeda cukup jauh dari pola data lainnya.

Deteksi outlier dilakukan menggunakan metode **Interquartile Range (IQR)**.

Rumus IQR:

$$
IQR = Q3 - Q1
$$

Batas bawah:

$$
Batas\ Bawah = Q1 - 1.5 	imes IQR
$$

Batas atas:

$$
Batas\ Atas = Q3 + 1.5 	imes IQR
$$

Data yang berada di bawah batas bawah atau di atas batas atas dianggap sebagai outlier.

### Hasil Deteksi Outlier

| Polutan | Q1 | Q3 | IQR | Batas Bawah | Batas Atas | Outlier |
|---|---:|---:|---:|---:|---:|---:|
| NO₂ | 0.000024 | 0.000059 | 0.000035 | -0.000028 | 0.000112 | 3 |
| CO | 0.027155 | 0.032214 | 0.005059 | 0.019567 | 0.039802 | 5 |
| SO₂ | -0.000063 | 0.000184 | 0.000247 | -0.000434 | 0.000555 | 13 |

Jumlah outlier yang ditemukan:

- NO₂ = 3
- CO = 5
- SO₂ = 13

Total terdapat **21 nilai yang terdeteksi sebagai outlier**.

---

## 2.5 Penanganan Outlier

Outlier tidak dihapus dari baris data. Nilai yang terdeteksi sebagai outlier diubah menjadi missing value agar jumlah tanggal tetap 366.

Setelah proses tersebut:

| Polutan | Missing Awal | Outlier | Missing Setelah Outlier |
|---|---:|---:|---:|
| NO₂ | 148 | 3 | 151 |
| CO | 157 | 5 | 162 |
| SO₂ | 104 | 13 | 117 |

Dengan cara ini, tanggal pengamatan tetap dipertahankan.

---

## 2.6 Imputasi Missing Value

Setelah outlier ditandai sebagai missing, dilakukan proses imputasi.

Metode yang digunakan adalah:

1. interpolasi linear;
2. `forward fill`;
3. `backward fill`.

### Interpolasi Linear

Interpolasi digunakan untuk mengisi nilai yang berada di antara dua data yang tersedia.

Contoh sederhana:

```text
Hari 1 = 10
Hari 2 = ?
Hari 3 = 14
```

Nilai Hari 2 dapat diperkirakan berada di antara nilai Hari 1 dan Hari 3.

### Forward Fill

`forward fill` menggunakan nilai yang tersedia sebelumnya untuk membantu mengisi nilai yang kosong.

### Backward Fill

`backward fill` menggunakan nilai yang tersedia setelah data kosong untuk membantu mengisi nilai tersebut.

`forward fill` dan `backward fill` digunakan sebagai pengaman untuk bagian awal atau akhir rangkaian data.

### Alur Preprocessing

```text
Data awal
   ↓
Deteksi missing value
   ↓
Deteksi outlier dengan IQR
   ↓
Outlier → NaN
   ↓
Interpolasi linear
   ↓
Forward fill / Backward fill
   ↓
Data lengkap
```

---

## 2.7 Hasil Preprocessing

Setelah proses imputasi selesai, tidak terdapat lagi missing value.

| Polutan | Missing Setelah Imputasi |
|---|---:|
| NO₂ | 0 |
| CO | 0 |
| SO₂ | 0 |

Dengan demikian, seluruh **366 tanggal** sudah memiliki nilai untuk ketiga parameter polutan.

Data hasil preprocessing disimpan dalam file:

`polutan_kalitengah_preprocessed.csv`

### Inti dari Preprocessing

Sederhananya:

> **Preprocessing digunakan untuk membersihkan data sebelum data digunakan pada tahap ekstraksi fitur.**

---

# 3. Ekstraksi Fitur Menggunakan TSFEL

## 3.1 Tujuan

Setelah data melalui tahap preprocessing, langkah berikutnya adalah melakukan ekstraksi fitur.

Ekstraksi fitur dilakukan untuk mendapatkan karakteristik dari data time series dalam bentuk nilai numerik yang dapat digunakan pada tahap analisis selanjutnya.

Library yang digunakan adalah **TSFEL (Time Series Feature Extraction Library)**.

---

## 3.2 Data yang Digunakan

Ekstraksi fitur menggunakan data hasil preprocessing:

`polutan_kalitengah_preprocessed.csv`

Data terdiri dari tiga parameter:

- NO₂
- CO
- SO₂

Masing-masing parameter memiliki **366 data harian**.

---

## 3.3 Apa Itu Fitur?

Fitur merupakan nilai yang menggambarkan karakteristik tertentu dari suatu data.

Misalnya dari 366 data NO₂, TSFEL dapat menghitung berbagai karakteristik seperti:

- Mean
- Median
- Min
- Max
- Variance
- Standard deviation
- Skewness
- dan karakteristik lainnya.

Jadi, 366 data harian tidak hanya dilihat satu per satu, tetapi diringkas menjadi berbagai nilai karakteristik.

---

## 3.4 Proses Ekstraksi

Proses ekstraksi dilakukan menggunakan TSFEL dengan domain:

- statistical;
- temporal;
- spectral.

Untuk setiap parameter polutan dihasilkan **65 fitur**.

Sehingga hasil keseluruhan adalah:

$$
65 	imes 3 = 195
$$

Jadi terdapat **195 hasil fitur**, yang terdiri dari:

| Polutan | Jumlah Fitur |
|---|---:|
| NO₂ | 65 |
| CO | 65 |
| SO₂ | 65 |
| **Total** | **195** |

---

## 3.5 Hasil Ekstraksi

Hasil ekstraksi disimpan dalam file:

`fitur_tsfel_65_kalitengah.csv`

File tersebut berisi nilai fitur untuk masing-masing polutan.

Selain itu terdapat file:

`daftar_65_fitur_tsfel_kalitengah.csv`

yang digunakan untuk melihat nama fitur dan kelompok domainnya.

---

# 4. Pengelompokan Fitur TSFEL

## 4.1 Pembagian Domain

Dari 65 fitur yang digunakan, fitur dibagi menjadi tiga domain:

| Domain | Jumlah |
|---|---:|
| Statistical | 31 |
| Temporal | 14 |
| Spectral | 20 |
| **Total** | **65** |

Pembagian tersebut digunakan untuk menjelaskan karakteristik fitur yang dihasilkan oleh TSFEL.

---

## 4.2 Domain Statistical

Domain statistical digunakan untuk menggambarkan karakteristik statistik dari data.

Fitur yang termasuk dalam domain ini berhubungan dengan nilai pusat data, penyebaran data, distribusi, dan karakteristik statistik lainnya.

Beberapa fitur yang digunakan antara lain:

- Absolute energy
- Average power
- ECDF
- Entropy
- Histogram mode
- Interquartile range
- Kurtosis
- Max
- Mean
- Mean absolute deviation
- Median
- Median absolute deviation
- Min
- Peak to peak distance
- Root mean square
- Skewness
- Standard deviation
- Variance

Jumlah fitur pada domain statistical adalah:

**31 fitur**

### Cara Memahaminya

Domain statistical lebih fokus pada pertanyaan seperti:

> "Bagaimana karakteristik nilai data secara statistik?"

Contohnya, **Mean** digunakan untuk melihat nilai rata-rata, sedangkan **Standard deviation** menggambarkan penyebaran data.

---

## 4.3 Domain Temporal

Domain temporal digunakan untuk menggambarkan karakteristik perubahan data berdasarkan urutan waktu.

Fitur yang digunakan antara lain:

- Area under the curve
- Autocorrelation
- Centroid
- Mean absolute diff
- Mean diff
- Median absolute diff
- Median diff
- Negative turning points
- Neighbourhood peaks
- Positive turning points
- Signal distance
- Slope
- Sum absolute diff
- Zero crossing rate

Jumlah fitur pada domain temporal adalah:

**14 fitur**

### Cara Memahaminya

Domain temporal lebih fokus pada perubahan data dari waktu ke waktu.

Contohnya:

- **Slope** dapat menggambarkan kecenderungan perubahan data.
- **Autocorrelation** berkaitan dengan hubungan nilai pada suatu waktu dengan nilai pada waktu sebelumnya.
- **Mean diff** melihat perubahan rata-rata antar data.

Sederhananya:

> **Temporal = bagaimana data berubah sepanjang waktu.**

---

## 4.4 Domain Spectral

Domain spectral digunakan untuk melihat karakteristik data berdasarkan komponen frekuensi.

Pada hasil ekstraksi terdapat 20 fitur **Spectrogram mean coefficient** pada beberapa frekuensi.

Frekuensi yang digunakan meliputi:

```text
0.00 Hz
0.02 Hz
0.03 Hz
0.05 Hz
0.06 Hz
0.08 Hz
0.10 Hz
0.11 Hz
0.13 Hz
0.15 Hz
0.16 Hz
0.18 Hz
0.19 Hz
0.21 Hz
0.23 Hz
0.24 Hz
0.26 Hz
0.27 Hz
0.29 Hz
0.31 Hz
```

Jumlah fitur pada domain spectral adalah:

**20 fitur**

### Cara Memahaminya

Domain spectral tidak hanya melihat besar kecilnya nilai polutan, tetapi melihat karakteristik data berdasarkan frekuensi.

Sederhananya:

> **Spectral = melihat karakteristik pola data berdasarkan frekuensi.**

---

# 5. Ringkasan 65 Fitur

Secara keseluruhan pembagian fitur adalah:

```text
65 Fitur TSFEL
│
├── Statistical
│   └── 31 fitur
│
├── Temporal
│   └── 14 fitur
│
└── Spectral
    └── 20 fitur
```

Perhitungannya:

$$
31 + 14 + 20 = 65
$$

Jumlah tersebut dapat diverifikasi pada file:

`daftar_65_fitur_tsfel_kalitengah.csv`

---

# 6. Hasil untuk Setiap Polutan

Ketiga parameter polutan memiliki jumlah fitur yang sama.

| Polutan | Statistical | Temporal | Spectral | Total |
|---|---:|---:|---:|---:|
| NO₂ | 31 | 14 | 20 | 65 |
| CO | 31 | 14 | 20 | 65 |
| SO₂ | 31 | 14 | 20 | 65 |

Sehingga total hasil ekstraksi:

| Parameter | Jumlah |
|---|---:|
| NO₂ | 65 |
| CO | 65 |
| SO₂ | 65 |
| **Total** | **195** |

---

# 7. Hubungan Preprocessing dengan TSFEL

Kedua tahap ini saling berhubungan.

Preprocessing dilakukan terlebih dahulu karena data awal masih memiliki missing value dan outlier.

Setelah data dibersihkan:

```text
Data awal
   ↓
Preprocessing
   ↓
Data lengkap
   ↓
TSFEL
   ↓
Ekstraksi fitur
   ↓
195 fitur
```

Jadi:

> **Preprocessing = membersihkan dan menyiapkan data.**

> **TSFEL = mengambil karakteristik dari data time series yang sudah disiapkan.**

Preprocessing harus dilakukan terlebih dahulu agar proses ekstraksi fitur menggunakan data yang sudah ditangani missing value dan outlier-nya.

---

# 8. File Hasil

File yang digunakan pada tahap ini:

- `polutan_kalitengah_preprocessed.csv`
- `fitur_tsfel_65_kalitengah.csv`
- `daftar_65_fitur_tsfel_kalitengah.csv`

File pertama merupakan hasil preprocessing.

File kedua berisi nilai hasil ekstraksi fitur.

File ketiga berisi daftar nama fitur dan domainnya.

---

# 9. Kesimpulan

Preprocessing berhasil dilakukan pada data kualitas udara Kecamatan Kalitengah. Dari data awal ditemukan missing value dan beberapa outlier.

Outlier dideteksi menggunakan metode IQR, yaitu 3 pada NO₂, 5 pada CO, dan 13 pada SO₂. Setelah outlier ditandai sebagai missing, dilakukan interpolasi dan pengisian pada bagian awal atau akhir data.

Hasil akhirnya adalah data dengan **366 tanggal dan tanpa missing value**, sehingga data siap digunakan untuk tahap ekstraksi fitur menggunakan TSFEL.

Data hasil preprocessing kemudian digunakan untuk ekstraksi fitur menggunakan TSFEL.

Dari setiap parameter polutan dihasilkan 65 fitur. Karena terdapat tiga parameter polutan, jumlah keseluruhan hasil ekstraksi adalah 195 fitur.

Fitur tersebut dikelompokkan menjadi tiga domain, yaitu:

- **Statistical = 31 fitur**
- **Temporal = 14 fitur**
- **Spectral = 20 fitur**

Dengan demikian:

$$
31 + 14 + 20 = 65
$$

dan:

$$
65 	imes 3 = 195
$$

Hasil ini memberikan representasi data time series dalam bentuk fitur numerik yang dapat digunakan untuk tahap analisis berikutnya.
