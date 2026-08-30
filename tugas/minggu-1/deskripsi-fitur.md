# 3. Deskripsi Fitur

## 3.1 Pendahuluan

Deskripsi fitur merupakan tahap untuk menjelaskan setiap variabel yang terdapat pada dataset kualitas udara Kabupaten Lamongan.

Dataset yang digunakan memiliki **6 kolom**, yaitu:

1. `valid_time`
2. `latitude`
3. `longitude`
4. `pm1_ug_m3`
5. `pm2p5_ug_m3`
6. `pm10_ug_m3`

Setiap fitur memiliki fungsi yang berbeda dalam proses analisis. Variabel waktu digunakan untuk mengetahui perubahan konsentrasi berdasarkan waktu, koordinat digunakan untuk menunjukkan lokasi data, sedangkan variabel PM digunakan untuk menganalisis konsentrasi partikulat.

---

## 3.2 Struktur Fitur Dataset

| No | Nama Fitur | Tipe Data | Keterangan |
|---:|---|---|---|
| 1 | `valid_time` | datetime64 | Waktu pengamatan |
| 2 | `latitude` | float64 | Koordinat lintang |
| 3 | `longitude` | float64 | Koordinat bujur |
| 4 | `pm1_ug_m3` | float64 | Konsentrasi PM1 |
| 5 | `pm2p5_ug_m3` | float64 | Konsentrasi PM2.5 |
| 6 | `pm10_ug_m3` | float64 | Konsentrasi PM10 |

Dataset memiliki:

```text
Jumlah baris  : 1.464
Jumlah kolom  : 6
```

---

## 3.3 Fitur `valid_time`

### Nama Fitur

```text
valid_time
```

### Tipe Data

```text
datetime64
```

### Fungsi

`valid_time` merupakan variabel yang menyimpan informasi tanggal dan waktu pengamatan data kualitas udara.

Fitur ini digunakan untuk mengetahui kapan nilai konsentrasi partikulat tercatat atau berlaku.

Periode data:

```text
29 Agustus 2025 – 29 Agustus 2026
```

Data tersedia pada empat waktu pengamatan dalam satu hari:

```text
00:00
06:00
12:00
18:00
```

### Peran dalam Analisis

Fitur `valid_time` merupakan fitur penting untuk analisis berbasis waktu atau **time series**.

Fitur ini dapat digunakan untuk:

- mengurutkan data berdasarkan waktu;
- melihat perubahan konsentrasi harian;
- melihat perubahan konsentrasi bulanan;
- mencari nilai tertinggi berdasarkan waktu;
- mencari nilai terendah berdasarkan waktu;
- dan membuat grafik time series.

---

## 3.4 Fitur `latitude`

### Nama Fitur

```text
latitude
```

### Tipe Data

```text
float64
```

### Fungsi

`latitude` menunjukkan posisi geografis berdasarkan garis lintang.

Pada dataset yang digunakan, nilai latitude adalah:

```text
-7.2
```

Nilai tersebut merupakan koordinat lintang dari titik data yang digunakan dalam dataset.

### Peran dalam Analisis

Latitude digunakan untuk:

- mengetahui posisi geografis data;
- memastikan data berada pada wilayah penelitian;
- memberikan informasi lokasi;
- dan mendukung analisis spasial apabila diperlukan.

Karena dataset utama menggunakan satu titik koordinat, variasi latitude pada dataset tidak digunakan sebagai variabel analisis utama.

---

## 3.5 Fitur `longitude`

### Nama Fitur

```text
longitude
```

### Tipe Data

```text
float64
```

### Fungsi

`longitude` menunjukkan posisi geografis berdasarkan garis bujur.

Pada dataset yang digunakan, nilai longitude adalah:

```text
112.4
```

Nilai tersebut merupakan koordinat bujur dari titik data yang digunakan dalam dataset.

### Peran dalam Analisis

Longitude digunakan untuk:

- mengetahui posisi geografis data;
- memastikan lokasi data;
- mendukung informasi wilayah penelitian;
- dan dapat digunakan dalam analisis spasial.

Sama seperti latitude, longitude bukan merupakan variabel utama dalam analisis konsentrasi partikulat.

---

## 3.6 Fitur `pm1_ug_m3`

### Nama Fitur

```text
pm1_ug_m3
```

### Tipe Data

```text
float64
```

### Satuan

```text
µg/m³
```

### Fungsi

`pm1_ug_m3` merupakan variabel yang menyimpan konsentrasi partikulat dengan ukuran diameter hingga sekitar **1 mikrometer**.

PM1 termasuk partikulat berukuran sangat kecil.

Nama variabel menggunakan akhiran:

```text
_ug_m3
```

yang menunjukkan bahwa nilai telah dinyatakan dalam satuan mikrogram per meter kubik.

### Peran dalam Analisis

PM1 digunakan untuk:

- mengetahui konsentrasi partikulat sangat halus;
- melihat perubahan konsentrasi berdasarkan waktu;
- membandingkan karakteristik dengan PM2.5 dan PM10;
- dan mengetahui pola distribusi partikulat.

---

## 3.7 Fitur `pm2p5_ug_m3`

### Nama Fitur

```text
pm2p5_ug_m3
```

### Tipe Data

```text
float64
```

### Satuan

```text
µg/m³
```

### Fungsi

`pm2p5_ug_m3` merupakan variabel yang menyimpan konsentrasi partikulat dengan ukuran diameter hingga sekitar **2,5 mikrometer**.

PM2.5 merupakan salah satu parameter penting dalam analisis kualitas udara.

### Peran dalam Analisis

PM2.5 digunakan untuk:

- mengetahui konsentrasi partikulat halus;
- melihat perubahan konsentrasi berdasarkan waktu;
- mengetahui distribusi nilai;
- membandingkan dengan PM1 dan PM10;
- dan melakukan analisis korelasi antarparameter.

---

## 3.8 Fitur `pm10_ug_m3`

### Nama Fitur

```text
pm10_ug_m3
```

### Tipe Data

```text
float64
```

### Satuan

```text
µg/m³
```

### Fungsi

`pm10_ug_m3` merupakan variabel yang menyimpan konsentrasi partikulat dengan ukuran diameter hingga sekitar **10 mikrometer**.

PM10 mencakup partikulat dengan ukuran lebih besar dibandingkan PM1 dan PM2.5.

### Peran dalam Analisis

PM10 digunakan untuk:

- mengetahui konsentrasi partikulat hingga ukuran 10 µm;
- melihat perubahan konsentrasi berdasarkan waktu;
- mengetahui distribusi data;
- membandingkan karakteristik dengan PM1 dan PM2.5;
- serta melakukan analisis hubungan antarparameter.

---

## 3.9 Perbandingan Fitur Partikulat

Ketiga variabel partikulat memiliki karakteristik ukuran yang berbeda.

| Parameter | Nama Kolom | Ukuran Partikel |
|---|---|---|
| PM1 | `pm1_ug_m3` | ≤ 1 µm |
| PM2.5 | `pm2p5_ug_m3` | ≤ 2,5 µm |
| PM10 | `pm10_ug_m3` | ≤ 10 µm |

Secara umum:

```text
PM1
 ↓
PM2.5
 ↓
PM10
```

Ukuran maksimum partikulat meningkat dari PM1 ke PM10.

---

## 3.10 Kategori Fitur

Fitur dataset dapat dikelompokkan menjadi tiga kategori.

### 1. Fitur Waktu

```text
valid_time
```

Digunakan untuk analisis berdasarkan waktu.

### 2. Fitur Lokasi

```text
latitude
longitude
```

Digunakan untuk menunjukkan lokasi geografis data.

### 3. Fitur Kualitas Udara

```text
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Digunakan sebagai variabel utama untuk menganalisis kualitas udara.

---

## 3.11 Variabel Utama dan Pendukung

Berdasarkan tujuan project, variabel dapat dibedakan menjadi:

### Variabel Utama

```text
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Ketiga variabel tersebut merupakan parameter yang dianalisis untuk memahami karakteristik partikulat udara.

### Variabel Pendukung

```text
valid_time
latitude
longitude
```

`valid_time` digunakan untuk analisis temporal, sedangkan latitude dan longitude digunakan untuk informasi lokasi.

---

## 3.12 Hubungan Antarfitur

Hubungan antarfitur dalam dataset dapat digambarkan sebagai berikut:

```text
                  DATASET
                     │
          ┌──────────┴──────────┐
          │                     │
       WAKTU                  LOKASI
          │                     │
    valid_time          latitude + longitude
          │
          ↓
   Analisis Time Series
          │
          ↓
   Kualitas Udara
          │
    ┌─────┼─────┐
    ↓     ↓     ↓
   PM1   PM2.5  PM10
```

Dengan struktur tersebut, `valid_time` dapat digunakan sebagai dasar untuk melihat bagaimana nilai PM berubah sepanjang periode pengamatan.

---

## 3.13 Peran Fitur dalam Analisis Minggu 1

| Fitur | Peran |
|---|---|
| `valid_time` | Analisis temporal dan time series |
| `latitude` | Informasi lokasi |
| `longitude` | Informasi lokasi |
| `pm1_ug_m3` | Analisis konsentrasi PM1 |
| `pm2p5_ug_m3` | Analisis konsentrasi PM2.5 |
| `pm10_ug_m3` | Analisis konsentrasi PM10 |

Fitur-fitur tersebut akan digunakan pada tahap eksplorasi data untuk mengetahui karakteristik dataset.

---

## 3.14 Satuan Data

Variabel partikulat pada dataset digunakan dalam satuan:

```text
µg/m³
```

atau mikrogram per meter kubik.

Satuan ini digunakan untuk menyatakan konsentrasi massa partikulat dalam volume udara.

Kolom yang digunakan dalam dataset telah menggunakan penamaan yang menunjukkan satuan tersebut:

```text
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

---

## 3.15 Kualitas dan Validitas Fitur

Sebelum digunakan dalam analisis, setiap fitur perlu diperiksa untuk memastikan data dapat digunakan.

Pemeriksaan yang dilakukan meliputi:

- pemeriksaan tipe data;
- pemeriksaan nilai kosong;
- pemeriksaan duplikasi;
- pemeriksaan nilai negatif;
- pemeriksaan nilai ekstrem;
- pemeriksaan konsistensi waktu;
- dan pemeriksaan koordinat.

Hasil pemeriksaan kualitas data akan dibahas lebih lanjut pada tahap **Data Understanding** dan **Eksplorasi Data**.

---

## 3.16 Ringkasan Deskripsi Fitur

| Fitur | Jenis | Peran |
|---|---|---|
| `valid_time` | Waktu | Menunjukkan tanggal dan waktu data |
| `latitude` | Lokasi | Menunjukkan koordinat lintang |
| `longitude` | Lokasi | Menunjukkan koordinat bujur |
| `pm1_ug_m3` | Polutan | Konsentrasi PM1 |
| `pm2p5_ug_m3` | Polutan | Konsentrasi PM2.5 |
| `pm10_ug_m3` | Polutan | Konsentrasi PM10 |

---

## 3.17 Kesimpulan

Dataset kualitas udara Kabupaten Lamongan memiliki enam fitur utama yang terdiri dari satu fitur waktu, dua fitur lokasi, dan tiga fitur kualitas udara.

Fitur `valid_time` digunakan untuk mengetahui waktu pengamatan dan menjadi dasar dalam analisis time series.

Fitur `latitude` dan `longitude` digunakan untuk memberikan informasi mengenai lokasi geografis data.

Sementara itu, `pm1_ug_m3`, `pm2p5_ug_m3`, dan `pm10_ug_m3` merupakan variabel utama yang digunakan untuk menganalisis konsentrasi partikulat udara.

Pemahaman terhadap fungsi setiap fitur diperlukan sebelum melakukan eksplorasi data, analisis statistik, dan visualisasi.

Pada tahap berikutnya, fitur-fitur tersebut akan digunakan untuk melakukan **Eksplorasi Data** guna mengetahui distribusi, karakteristik, hubungan antarparameter, serta perubahan konsentrasi partikulat berdasarkan waktu.
