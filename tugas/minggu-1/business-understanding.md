# 1. Business Understanding

## 1.1 Latar Belakang

Kualitas udara merupakan salah satu aspek lingkungan yang penting untuk dipahami karena kondisi udara dapat berubah dari waktu ke waktu dan dipengaruhi oleh berbagai aktivitas serta kondisi lingkungan.

Kabupaten Lamongan merupakan salah satu wilayah di Provinsi Jawa Timur yang memiliki berbagai aktivitas masyarakat seperti transportasi, permukiman, pertanian, kegiatan perdagangan, serta aktivitas lainnya yang berpotensi menghasilkan partikulat udara.

Untuk memperoleh gambaran mengenai kondisi kualitas udara secara lebih terstruktur, diperlukan pemanfaatan data yang dapat dianalisis berdasarkan waktu dan parameter polutan.

Pada project Penambangan Sains Data ini dilakukan analisis terhadap data kualitas udara di wilayah Kabupaten Lamongan dengan menggunakan parameter partikulat:

- PM1
- PM2.5
- PM10

Data tersebut digunakan untuk memahami karakteristik konsentrasi partikulat selama periode pengamatan sekitar satu tahun.

---

## 1.2 Identifikasi Masalah

Permasalahan utama dalam project ini adalah bagaimana memahami karakteristik kualitas udara di Kabupaten Lamongan berdasarkan data konsentrasi partikulat.

Data kualitas udara yang diperoleh perlu dipahami terlebih dahulu sebelum dilakukan analisis lebih lanjut. Oleh karena itu, beberapa permasalahan yang menjadi perhatian adalah:

1. Bagaimana karakteristik data kualitas udara di Kabupaten Lamongan?
2. Bagaimana kondisi konsentrasi PM1, PM2.5, dan PM10 selama periode pengamatan?
3. Apakah data memiliki nilai yang hilang?
4. Apakah terdapat data duplikat?
5. Apakah terdapat nilai konsentrasi yang tidak valid?
6. Apakah terdapat nilai ekstrem atau outlier?
7. Bagaimana pola perubahan konsentrasi partikulat berdasarkan waktu?
8. Bagaimana hubungan antara PM1, PM2.5, dan PM10?

Permasalahan tersebut menjadi dasar dalam melakukan tahap **Data Understanding** dan **Exploratory Data Analysis**.

---

## 1.3 Tujuan Project

### Tujuan Umum

Tujuan umum dari project ini adalah:

> **Memahami karakteristik kualitas udara di Kabupaten Lamongan berdasarkan data konsentrasi PM1, PM2.5, dan PM10 selama periode pengamatan.**

### Tujuan Khusus

Project ini memiliki beberapa tujuan khusus, yaitu:

1. menentukan wilayah pengamatan yang digunakan dalam analisis;
2. memperoleh data kualitas udara untuk wilayah pengamatan;
3. menentukan parameter polutan yang akan dianalisis;
4. memahami struktur dataset kualitas udara;
5. mengetahui karakteristik PM1, PM2.5, dan PM10;
6. memeriksa kualitas data yang diperoleh;
7. mengidentifikasi missing value dan data duplikat;
8. mengidentifikasi nilai yang tidak valid;
9. mengidentifikasi outlier pada data;
10. mengetahui perubahan konsentrasi polutan berdasarkan waktu;
11. menyediakan dataset yang siap digunakan untuk tahap analisis berikutnya.

---

## 1.4 Pertanyaan Analisis

Berdasarkan tujuan tersebut, pertanyaan yang ingin dijawab melalui project ini adalah:

### Pertanyaan Utama

**Bagaimana karakteristik kualitas udara di Kabupaten Lamongan berdasarkan konsentrasi PM1, PM2.5, dan PM10 selama periode pengamatan?**

### Pertanyaan Pendukung

1. Berapa nilai konsentrasi PM1, PM2.5, dan PM10?
2. Bagaimana distribusi masing-masing parameter?
3. Apakah terdapat perubahan konsentrasi berdasarkan waktu?
4. Apakah terdapat nilai ekstrem pada dataset?
5. Apakah terdapat masalah kualitas data?
6. Apakah terdapat hubungan antara ketiga parameter partikulat?

---

## 1.5 Wilayah Penelitian

Wilayah yang digunakan dalam project adalah:

**Kabupaten Lamongan, Provinsi Jawa Timur.**

Penentuan wilayah dilakukan menggunakan data batas wilayah dalam format **GeoJSON**.

GeoJSON digunakan untuk membantu menentukan wilayah yang menjadi fokus pengambilan dan analisis data.

Informasi wilayah:

| Komponen | Keterangan |
|---|---|
| Wilayah | Kabupaten Lamongan |
| Provinsi | Jawa Timur |
| Negara | Indonesia |
| Format batas wilayah | GeoJSON |
| Tools | GeoJSON.io |

File batas wilayah disimpan dalam project:

```text
data/lamongan.geojson
```

---

## 1.6 Penentuan Wilayah Menggunakan GeoJSON

Wilayah penelitian dalam project ini adalah **Kabupaten Lamongan, Provinsi Jawa Timur**.

Untuk menentukan wilayah pengamatan, digunakan data batas wilayah dalam format **GeoJSON**. GeoJSON merupakan format berbasis JSON yang digunakan untuk menyimpan dan merepresentasikan data geografis.

Pada project ini, file batas wilayah Kabupaten Lamongan digunakan sebagai acuan dalam menentukan wilayah yang menjadi fokus pengambilan dan analisis data kualitas udara.

File GeoJSON yang digunakan dalam project disimpan pada:

```text
data/lamongan.geojson
```

Penggunaan GeoJSON bertujuan agar wilayah penelitian dapat ditentukan secara lebih terstruktur dan jelas.

### Proses Penentuan Wilayah

Tahapan penentuan wilayah dilakukan sebagai berikut:

1. Menentukan Kabupaten Lamongan sebagai wilayah penelitian.
2. Menyiapkan data batas wilayah Kabupaten Lamongan.
3. Menyimpan batas wilayah dalam format GeoJSON.
4. Memeriksa struktur dan koordinat GeoJSON.
5. Menggunakan GeoJSON sebagai acuan wilayah penelitian.

### Alur Penentuan Wilayah

```text
Menentukan Kabupaten Lamongan
            ↓
Menyiapkan Batas Wilayah
            ↓
Membuat/Memeriksa GeoJSON
            ↓
Menyimpan lamongan.geojson
            ↓
Menentukan Wilayah Pengamatan
            ↓
Pengambilan Data Kualitas Udara
```

---

## 1.7 Sumber Data

Data kualitas udara yang digunakan dalam project ini berasal dari **Copernicus Atmosphere Monitoring Service (CAMS)**.

CAMS merupakan layanan yang menyediakan informasi mengenai komposisi atmosfer dan kualitas udara berdasarkan sistem pemodelan atmosfer.

Dataset yang digunakan dalam project adalah:

> **CAMS Global Atmospheric Composition Forecasts**

Dataset tersebut menyediakan berbagai variabel atmosfer, termasuk beberapa parameter partikulat yang digunakan dalam penelitian ini.

Parameter yang dipilih adalah:

- **Particulate Matter d < 1 µm (PM1)**
- **Particulate Matter d < 2.5 µm (PM2.5)**
- **Particulate Matter d < 10 µm (PM10)**

Data awal diperoleh dalam format **GRIB**. Selanjutnya data dibaca dan diolah menggunakan Python sehingga dapat digunakan dalam bentuk tabel dan CSV.

### Sumber Resmi

Data diperoleh melalui Copernicus Atmosphere Data Store (ADS):

https://ads.atmosphere.copernicus.eu/

### Informasi Dataset

| Komponen | Keterangan |
|---|---|
| Penyedia | Copernicus Atmosphere Monitoring Service |
| Platform | Copernicus Atmosphere Data Store |
| Dataset | CAMS Global Atmospheric Composition Forecasts |
| Jenis Data | Data komposisi atmosfer |
| Parameter Utama | PM1, PM2.5, PM10 |
| Format Awal | GRIB |
| Format Analisis | CSV |

---

## 1.8 Proses Pengambilan Data

Pengambilan data dilakukan dengan menentukan terlebih dahulu wilayah, periode, dan parameter yang dibutuhkan.

Proses pengambilan data dilakukan melalui beberapa tahap.

### Tahap 1 — Menentukan Wilayah

Wilayah penelitian ditentukan yaitu Kabupaten Lamongan, Jawa Timur.

Batas wilayah disimpan dalam file:

```text
data/lamongan.geojson
```

### Tahap 2 — Menentukan Dataset

Dataset yang digunakan adalah:

> **CAMS Global Atmospheric Composition Forecasts**

### Tahap 3 — Menentukan Variabel

Variabel yang dipilih:

- PM1
- PM2.5
- PM10

### Tahap 4 — Menentukan Periode

Periode pengamatan ditentukan selama sekitar satu tahun:

> **29 Agustus 2025 – 29 Agustus 2026**

### Tahap 5 — Ekstraksi Data

Data kemudian diekstraksi berdasarkan parameter dan wilayah pengamatan yang telah ditentukan.

Data hasil ekstraksi kemudian diunduh dan diproses menggunakan Python.

### Tahap 6 — Pengolahan Data

Data GRIB dibaca menggunakan Python dan kemudian diubah menjadi bentuk tabel.

Selanjutnya dilakukan:

- pemilihan variabel;
- penyusunan waktu;
- penggabungan data;
- konversi satuan;
- pemeriksaan data;
- dan penyimpanan dalam CSV.

### Alur Pengambilan Data

```text
Kabupaten Lamongan
        ↓
Batas Wilayah GeoJSON
        ↓
Menentukan Area Pengamatan
        ↓
CAMS Global Atmospheric Composition Forecasts
        ↓
Memilih PM1, PM2.5, PM10
        ↓
Menentukan Periode
        ↓
Ekstraksi Data
        ↓
Data GRIB
        ↓
Pengolahan Python
        ↓
Penyusunan Dataset
        ↓
Konversi Satuan
        ↓
CSV
        ↓
Data Cleaning
        ↓
Data Understanding
```

---

## 1.9 Periode Data

Dataset yang digunakan memiliki periode pengamatan:

> **29 Agustus 2025 – 29 Agustus 2026**

Periode tersebut mencakup sekitar satu tahun data.

Tanggal awal:

> **29 Agustus 2025**

Tanggal akhir:

> **29 Agustus 2026**

Periode ini dipilih karena tugas membutuhkan data terkini dengan periode minimal satu tahun sampai dengan sekitar **31 Agustus 2026**.

### Frekuensi Data

Dataset memiliki data pada empat waktu pengamatan dalam satu hari:

| Waktu | Keterangan |
|---|---|
| 00:00 | Pengamatan pertama |
| 06:00 | Pengamatan kedua |
| 12:00 | Pengamatan ketiga |
| 18:00 | Pengamatan keempat |

Dengan demikian terdapat:

> **4 observasi per hari**

### Jumlah Data

Dataset yang telah diolah memiliki:

> **1.464 baris data**

dan:

> **6 kolom**

Perhitungan jumlah observasi:

```text
366 hari × 4 waktu pengamatan
= 1.464 observasi
```

Periode tersebut mencakup tahun 2025–2026 dan digunakan sebagai dataset utama untuk analisis kualitas udara.

---

## 1.10 Parameter yang Dianalisis

Terdapat tiga parameter utama yang digunakan dalam project ini:

- PM1
- PM2.5
- PM10

Ketiga parameter tersebut merupakan partikulat dengan ukuran diameter yang berbeda.

### 1.10.1 PM1

PM1 adalah partikulat dengan ukuran diameter hingga sekitar 1 mikrometer.

Dalam dataset, variabel ini disimpan sebagai:

```text
pm1_ug_m3
```

PM1 digunakan untuk menggambarkan konsentrasi partikulat berukuran sangat kecil.

### 1.10.2 PM2.5

PM2.5 adalah partikulat dengan ukuran diameter hingga sekitar 2,5 mikrometer.

Dalam dataset, variabel ini disimpan sebagai:

```text
pm2p5_ug_m3
```

PM2.5 digunakan sebagai salah satu parameter utama dalam pengamatan kualitas udara.

### 1.10.3 PM10

PM10 adalah partikulat dengan ukuran diameter hingga sekitar 10 mikrometer.

Dalam dataset, variabel ini disimpan sebagai:

```text
pm10_ug_m3
```

PM10 digunakan untuk menggambarkan konsentrasi partikulat dengan ukuran hingga 10 mikrometer.

### Ringkasan Parameter

| Parameter | Nama Kolom | Keterangan |
|---|---|---|
| PM1 | `pm1_ug_m3` | Partikulat hingga sekitar 1 µm |
| PM2.5 | `pm2p5_ug_m3` | Partikulat hingga sekitar 2,5 µm |
| PM10 | `pm10_ug_m3` | Partikulat hingga sekitar 10 µm |

Ketiga parameter tersebut dianalisis secara bersamaan untuk mendapatkan gambaran karakteristik partikulat udara di wilayah penelitian.

---

## 1.11 Manfaat Project

Project analisis kualitas udara ini memiliki beberapa manfaat.

### 1. Manfaat Akademik

Project ini menjadi penerapan konsep **Penambangan Sains Data** pada data lingkungan.

Melalui project ini, proses pengumpulan, pembersihan, pemahaman, eksplorasi, dan visualisasi data dapat diterapkan secara langsung.

### 2. Memahami Kualitas Udara

Data PM1, PM2.5, dan PM10 dapat digunakan untuk memahami karakteristik konsentrasi partikulat di Kabupaten Lamongan.

### 3. Melihat Perubahan Berdasarkan Waktu

Karena dataset memiliki informasi waktu, perubahan konsentrasi partikulat dapat diamati dari waktu ke waktu.

### 4. Mengetahui Karakteristik Dataset

Tahap Data Understanding dapat digunakan untuk mengetahui:

- jumlah data;
- jumlah variabel;
- tipe data;
- periode data;
- missing value;
- data duplikat;
- nilai tidak valid;
- outlier;
- nilai minimum;
- nilai maksimum;
- rata-rata;
- dan distribusi data.

### 5. Dasar Analisis Selanjutnya

Dataset yang telah dipahami dan dibersihkan dapat digunakan sebagai dasar untuk melakukan analisis lebih lanjut.

Analisis tersebut dapat berupa:

- eksplorasi statistik;
- visualisasi;
- analisis hubungan antarvariabel;
- dan analisis time series.

---

## 1.12 Output yang Diharapkan

Output yang diharapkan dari project ini adalah:

### 1. Data Wilayah

File batas wilayah Kabupaten Lamongan dalam format:

```text
lamongan.geojson
```

### 2. Dataset Kualitas Udara

Dataset hasil pengolahan dalam format:

```text
data_lamongan.csv
```

### 3. Dokumentasi Business Understanding

Dokumentasi mengenai:

- latar belakang;
- permasalahan;
- tujuan;
- wilayah;
- sumber data;
- parameter;
- manfaat;
- dan batasan penelitian.

### 4. Dokumentasi Data Understanding

Dokumentasi mengenai:

- struktur data;
- periode;
- jumlah data;
- tipe data;
- missing value;
- duplikasi;
- outlier;
- dan kualitas dataset.

### 5. Deskripsi Fitur

Penjelasan mengenai setiap variabel yang digunakan.

### 6. Sumber Polutan

Pembahasan mengenai sumber yang berpotensi menghasilkan PM1, PM2.5, dan PM10.

### 7. Eksplorasi Data

Eksplorasi terhadap karakteristik data menggunakan statistik dan visualisasi.

### 8. Visualisasi Time Series

Membuat grafik perubahan konsentrasi:

- PM1;
- PM2.5;
- PM10;

berdasarkan waktu.

### 9. Website Statis

Seluruh dokumentasi dan hasil analisis akan dipublikasikan menggunakan:

> **Jupyter Book + GitHub Pages**

---

## 1.13 Batasan Project

Untuk menjaga agar project tetap terarah, terdapat beberapa batasan penelitian.

1. Wilayah penelitian difokuskan pada Kabupaten Lamongan, Jawa Timur.
2. Parameter utama yang dianalisis adalah PM1, PM2.5, dan PM10.
3. Periode data adalah 29 Agustus 2025 sampai 29 Agustus 2026.
4. Data kualitas udara diperoleh dari CAMS.
5. Data yang digunakan merupakan data atmosfer berbasis model/grid dan bukan pengukuran langsung menggunakan sensor lapangan.
6. Analisis dilakukan berdasarkan data yang tersedia dalam dataset.
7. Nilai ekstrem tidak langsung dianggap sebagai kesalahan.
8. Nilai outlier akan diperiksa terlebih dahulu sebelum menentukan apakah nilai tersebut perlu dipertahankan atau ditangani.
9. Project tidak melakukan diagnosis kesehatan terhadap individu.
10. Hasil analisis digunakan untuk memahami pola dan karakteristik data kualitas udara.
11. Analisis pada tahap awal difokuskan pada Data Understanding dan Exploratory Data Analysis.

---

## 1.14 Ruang Lingkup Minggu 1

Sesuai dengan instruksi tugas, kegiatan pada minggu pertama difokuskan pada pemahaman data dan lingkungan penelitian.

Tahapan yang dilakukan meliputi:

### 1. Business Understanding

Menentukan:

- latar belakang;
- permasalahan;
- tujuan;
- pertanyaan analisis;
- manfaat;
- wilayah penelitian;
- sumber data;
- dan batasan project.

### 2. Data Understanding

Memahami:

- sumber data;
- periode data;
- jumlah data;
- jumlah kolom;
- struktur dataset;
- tipe data;
- missing value;
- data duplikat;
- nilai tidak valid;
- dan outlier.

### 3. Deskripsi Fitur

Menjelaskan setiap fitur dalam dataset:

```text
valid_time
latitude
longitude
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

### 4. Sumber Polutan

Mengidentifikasi sumber yang berpotensi menghasilkan partikulat.

Contohnya:

- transportasi;
- aktivitas industri;
- pembakaran bahan bakar;
- pembakaran terbuka;
- aktivitas pertanian;
- debu jalan;
- dan sumber alami.

### 5. Eksplorasi Data

Melakukan eksplorasi awal menggunakan:

- statistik deskriptif;
- distribusi data;
- pemeriksaan nilai ekstrem;
- hubungan antarparameter;
- dan visualisasi time series.

---

## 1.15 Alur Project

Secara keseluruhan, project dilakukan melalui tahapan berikut:

```text
Business Understanding
          ↓
Penentuan Wilayah
          ↓
GeoJSON Kabupaten Lamongan
          ↓
Pengambilan Data CAMS
          ↓
Data GRIB
          ↓
Pengolahan Python
          ↓
Konversi ke CSV
          ↓
Data Cleaning
          ↓
Data Understanding
          ↓
Deskripsi Fitur
          ↓
Identifikasi Sumber Polutan
          ↓
Eksplorasi Data
          ↓
Visualisasi
          ↓
Time Series
          ↓
Interpretasi Hasil
          ↓
Publikasi Website
```

Tahapan tersebut dilakukan secara berurutan agar setiap tahap menghasilkan informasi yang dapat digunakan pada tahap berikutnya.

---

## 1.16 Kesimpulan

Project ini berfokus pada analisis kualitas udara di **Kabupaten Lamongan, Provinsi Jawa Timur** menggunakan data konsentrasi partikulat PM1, PM2.5, dan PM10.

Wilayah penelitian ditentukan menggunakan batas wilayah dalam format GeoJSON. File tersebut digunakan sebagai acuan dalam menentukan wilayah pengamatan.

Data kualitas udara diperoleh dari **Copernicus Atmosphere Monitoring Service (CAMS)** melalui dataset **CAMS Global Atmospheric Composition Forecasts**.

Data yang digunakan memiliki periode:

> **29 Agustus 2025 – 29 Agustus 2026**

Dataset memiliki empat waktu pengamatan dalam satu hari, yaitu:

- 00:00;
- 06:00;
- 12:00;
- 18:00.

Setelah dilakukan pengolahan, dataset memiliki:

> **1.464 baris dan 6 kolom**

Enam kolom tersebut terdiri dari:

```text
valid_time
latitude
longitude
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Dataset kemudian digunakan untuk memahami karakteristik kualitas udara, melakukan pemeriksaan kualitas data, mendeskripsikan fitur, mengidentifikasi sumber polutan, serta melakukan eksplorasi data.

Tahap berikutnya adalah melakukan analisis eksploratif dan membuat visualisasi **time series** untuk melihat perubahan konsentrasi PM1, PM2.5, dan PM10 selama periode pengamatan.

---

## 1.17 Ringkasan Business Understanding

| Komponen | Keterangan |
|---|---|
| Topik | Analisis Kualitas Udara |
| Wilayah Penelitian | Kabupaten Lamongan |
| Provinsi | Jawa Timur |
| Negara | Indonesia |
| Sumber Data | Copernicus Atmosphere Monitoring Service (CAMS) |
| Platform Data | Copernicus Atmosphere Data Store |
| Dataset | CAMS Global Atmospheric Composition Forecasts |
| Parameter | PM1, PM2.5, PM10 |
| Periode Awal | 29 Agustus 2025 |
| Periode Akhir | 29 Agustus 2026 |
| Lama Pengamatan | Sekitar 1 tahun |
| Frekuensi | 4 observasi per hari |
| Jumlah Baris | 1.464 |
| Jumlah Kolom | 6 |
| Variabel Waktu | `valid_time` |
| Variabel Lokasi | `latitude`, `longitude` |
| Variabel PM1 | `pm1_ug_m3` |
| Variabel PM2.5 | `pm2p5_ug_m3` |
| Variabel PM10 | `pm10_ug_m3` |
| Format Data Awal | GRIB |
| Format Data Analisis | CSV |
| Batas Wilayah | GeoJSON |
| File GeoJSON | `data/lamongan.geojson` |
| File Dataset | `data_lamongan.csv` |
| Analisis Awal | Data Understanding |
| Analisis Berikutnya | Exploratory Data Analysis |
| Visualisasi | Time Series |
| Platform Publikasi | Jupyter Book |
| Hosting | GitHub Pages |

### Ringkasan Akhir

Project ini menggunakan data kualitas udara dari CAMS untuk menganalisis karakteristik partikulat PM1, PM2.5, dan PM10 di Kabupaten Lamongan.

Data wilayah ditentukan menggunakan GeoJSON, sedangkan data kualitas udara diperoleh dari dataset CAMS Global Atmospheric Composition Forecasts.

Dataset yang digunakan mencakup periode sekitar satu tahun, yaitu 29 Agustus 2025 sampai 29 Agustus 2026, dengan empat waktu pengamatan setiap hari.

Hasil pengolahan menghasilkan dataset dengan **1.464 observasi dan 6 variabel** yang terdiri dari informasi waktu, koordinat, PM1, PM2.5, dan PM10.

Dataset tersebut menjadi dasar untuk tahap berikutnya, yaitu **Data Understanding, Deskripsi Fitur, Sumber Polutan, dan Eksplorasi Data**.

Hasil akhir project akan disajikan dalam bentuk dokumentasi dan visualisasi pada website statis menggunakan **Jupyter Book dan GitHub Pages**.
