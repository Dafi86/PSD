# 5. Eksplorasi Data

## 5.1 Pendahuluan

Eksplorasi Data atau **Exploratory Data Analysis (EDA)** merupakan tahap untuk memahami karakteristik dataset secara lebih mendalam.

Pada project ini, eksplorasi dilakukan terhadap dataset kualitas udara Kabupaten Lamongan yang berisi data:

- PM1;
- PM2.5;
- PM10;
- waktu pengamatan;
- serta koordinat lokasi.

Tahap ini dilakukan setelah **Business Understanding**, **Data Understanding**, **Deskripsi Fitur**, dan **Sumber Polutan**.

Tujuan eksplorasi adalah mengetahui pola, distribusi, karakteristik statistik, hubungan antarparameter, serta kemungkinan adanya nilai ekstrem pada data.

---

## 5.2 Dataset yang Digunakan

Dataset yang digunakan adalah:

```text
data_lamongan.csv
```

Dataset memiliki struktur:

| Komponen | Keterangan |
|---|---|
| Jumlah baris | 1.464 |
| Jumlah kolom | 6 |
| Periode awal | 29 Agustus 2025 |
| Periode akhir | 29 Agustus 2026 |
| Frekuensi | 4 observasi per hari |
| Wilayah | Kabupaten Lamongan |
| Parameter | PM1, PM2.5, PM10 |

Kolom dataset:

```text
valid_time
latitude
longitude
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

---

## 5.3 Tujuan Eksplorasi Data

Eksplorasi data dilakukan untuk menjawab beberapa pertanyaan:

1. Bagaimana struktur dataset kualitas udara?
2. Bagaimana distribusi nilai PM1, PM2.5, dan PM10?
3. Berapa nilai minimum, maksimum, dan rata-rata masing-masing parameter?
4. Apakah terdapat missing value?
5. Apakah terdapat data duplikat?
6. Apakah terdapat nilai negatif atau nilai yang tidak valid?
7. Apakah terdapat outlier?
8. Bagaimana perubahan konsentrasi partikulat berdasarkan waktu?
9. Bagaimana hubungan antara PM1, PM2.5, dan PM10?

---

## 5.4 Pemeriksaan Struktur Dataset

Pemeriksaan struktur dilakukan untuk memastikan dataset memiliki kolom dan jumlah observasi yang sesuai.

Dataset memiliki:

```text
Baris  : 1.464
Kolom  : 6
```

Struktur fitur:

| Fitur | Keterangan |
|---|---|
| `valid_time` | Waktu pengamatan |
| `latitude` | Koordinat lintang |
| `longitude` | Koordinat bujur |
| `pm1_ug_m3` | Konsentrasi PM1 |
| `pm2p5_ug_m3` | Konsentrasi PM2.5 |
| `pm10_ug_m3` | Konsentrasi PM10 |

Struktur tersebut sesuai dengan dataset yang telah dijelaskan pada tahap **Data Understanding**.

---

## 5.5 Pemeriksaan Tipe Data

Tipe data setiap kolom diperiksa agar dapat digunakan sesuai fungsinya.

| Kolom | Tipe Data |
|---|---|
| `valid_time` | datetime64 |
| `latitude` | float64 |
| `longitude` | float64 |
| `pm1_ug_m3` | float64 |
| `pm2p5_ug_m3` | float64 |
| `pm10_ug_m3` | float64 |

Kolom `valid_time` menggunakan tipe datetime sehingga dapat digunakan untuk analisis berdasarkan waktu.

Kolom PM menggunakan tipe numerik sehingga dapat digunakan untuk statistik deskriptif, visualisasi, dan analisis hubungan antarparameter.

---

## 5.6 Pemeriksaan Missing Value

Missing value merupakan data yang tidak memiliki nilai atau bernilai kosong.

Pemeriksaan missing value dilakukan pada seluruh kolom dataset.

Variabel yang diperiksa meliputi:

```text
valid_time
latitude
longitude
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Hasil pemeriksaan missing value perlu dicatat berdasarkan output notebook yang digunakan saat proses Data Understanding.

Apabila tidak ditemukan nilai kosong, maka dataset dapat dinyatakan tidak memiliki missing value pada kolom yang diperiksa.

Jika ditemukan missing value, penanganannya perlu dilakukan sebelum analisis lanjutan.

---

## 5.7 Pemeriksaan Data Duplikat

Data duplikat merupakan baris yang memiliki informasi yang sama dengan baris lainnya.

Pemeriksaan dilakukan untuk mengetahui apakah terdapat observasi yang tercatat lebih dari satu kali.

Kombinasi yang penting untuk diperhatikan adalah:

```text
valid_time
latitude
longitude
```

serta nilai partikulat pada observasi tersebut.

Jika terdapat duplikasi, data perlu diperiksa terlebih dahulu sebelum diputuskan untuk dihapus.

Penghapusan data duplikat tidak dilakukan secara otomatis tanpa mengetahui penyebab munculnya duplikasi.

---

## 5.8 Pemeriksaan Nilai Tidak Valid

Pada data kualitas udara, nilai konsentrasi partikulat secara fisik tidak seharusnya bernilai negatif.

Oleh karena itu, pemeriksaan dilakukan terhadap:

```text
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Nilai negatif perlu ditandai sebagai nilai yang harus diperiksa lebih lanjut.

Pemeriksaan ini penting karena nilai ekstrem belum tentu merupakan kesalahan, tetapi nilai negatif pada konsentrasi partikulat perlu mendapatkan perhatian khusus.

---

## 5.9 Statistik Deskriptif

Statistik deskriptif digunakan untuk mengetahui karakteristik dasar dari variabel partikulat.

Statistik yang diperiksa meliputi:

- jumlah data;
- rata-rata;
- standar deviasi;
- nilai minimum;
- kuartil 25%;
- median;
- kuartil 75%;
- nilai maksimum.

Parameter yang dianalisis:

```text
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Hasil statistik deskriptif digunakan untuk mengetahui rentang dan penyebaran konsentrasi partikulat selama periode pengamatan.

> **Catatan:** angka statistik detail sebaiknya diambil langsung dari output notebook eksplorasi agar dokumentasi website tetap sama dengan hasil dataset yang digunakan.

---

## 5.10 Rentang Nilai PM

Berdasarkan pemeriksaan data yang telah dilakukan, nilai partikulat perlu dibandingkan berdasarkan nilai minimum dan maksimum.

Pemeriksaan mencakup:

| Parameter | Nilai Minimum | Nilai Maksimum |
|---|---:|---:|
| PM1 | Hasil notebook | Hasil notebook |
| PM2.5 | Hasil notebook | Hasil notebook |
| PM10 | Hasil notebook | Hasil notebook |

Rentang nilai digunakan untuk mengetahui seberapa besar variasi konsentrasi partikulat selama periode pengamatan.

---

## 5.11 Distribusi PM1

PM1 merupakan partikulat dengan ukuran hingga sekitar 1 µm.

Distribusi PM1 dapat dianalisis menggunakan:

- histogram;
- boxplot;
- statistik deskriptif;
- dan time series.

Histogram digunakan untuk melihat bagaimana nilai PM1 tersebar.

Boxplot digunakan untuk melihat median, kuartil, serta kemungkinan nilai ekstrem.

Analisis distribusi membantu mengetahui apakah nilai PM1 cenderung terkonsentrasi pada rentang tertentu atau memiliki penyebaran yang lebar.

---

## 5.12 Distribusi PM2.5

PM2.5 merupakan partikulat dengan ukuran hingga sekitar 2,5 µm.

Distribusi PM2.5 dapat dianalisis menggunakan histogram dan boxplot.

Histogram digunakan untuk mengetahui pola penyebaran nilai, sedangkan boxplot digunakan untuk melihat median, kuartil, dan nilai ekstrem.

PM2.5 juga dapat dibandingkan dengan PM1 dan PM10 untuk melihat perbedaan karakteristik distribusinya.

---

## 5.13 Distribusi PM10

PM10 merupakan partikulat dengan ukuran hingga sekitar 10 µm.

Distribusi PM10 dapat dianalisis menggunakan:

- histogram;
- boxplot;
- statistik deskriptif;
- dan time series.

Analisis distribusi digunakan untuk mengetahui rentang nilai dan kemungkinan adanya nilai ekstrem.

---

## 5.14 Perbandingan Distribusi PM

Ketiga parameter dapat dibandingkan untuk mengetahui perbedaan karakteristiknya.

| Parameter | Ukuran Maksimum | Fokus Analisis |
|---|---:|---|
| PM1 | ≤ 1 µm | Partikulat sangat halus |
| PM2.5 | ≤ 2,5 µm | Partikulat halus |
| PM10 | ≤ 10 µm | Partikulat hingga ukuran 10 µm |

Perbandingan dapat dilakukan melalui:

```text
PM1
PM2.5
PM10
```

dengan menggunakan statistik deskriptif dan visualisasi.

---

## 5.15 Pemeriksaan Outlier

Outlier merupakan nilai yang memiliki karakteristik berbeda secara signifikan dibandingkan sebagian besar observasi.

Pada pemeriksaan awal dataset, ditemukan adanya nilai yang teridentifikasi sebagai outlier.

Hasil pemeriksaan sebelumnya menunjukkan:

```text
Jumlah outlier: 22
```

Batas bawah yang teridentifikasi pada salah satu pemeriksaan adalah:

```text
-44.0256375
```

sedangkan batas atas:

```text
164.6698785
```

Nilai tersebut menunjukkan bahwa terdapat observasi yang perlu diperiksa lebih lanjut.

Namun, **outlier tidak langsung dihapus**.

Outlier perlu diperiksa berdasarkan:

- waktu kejadian;
- parameter yang terkena;
- nilai konsentrasi;
- kemungkinan kesalahan data;
- dan konteks dataset.

Pendekatan ini dilakukan agar informasi penting tidak hilang hanya karena suatu nilai memiliki karakteristik ekstrem.

---

## 5.16 Interpretasi Outlier

Keberadaan outlier dapat disebabkan oleh beberapa kemungkinan, misalnya:

1. variasi konsentrasi yang memang tinggi;
2. kondisi atmosfer tertentu;
3. proses pemodelan atau interpolasi;
4. kesalahan data;
5. atau nilai yang berada di luar pola umum dataset.

Karena dataset berasal dari sistem pemodelan atmosfer, nilai ekstrem tidak dapat langsung dianggap sebagai hasil kesalahan pengukuran sensor.

Oleh karena itu, observasi yang teridentifikasi sebagai outlier perlu dianalisis lebih lanjut.

---

## 5.17 Analisis Berdasarkan Waktu

Variabel:

```text
valid_time
```

digunakan untuk melakukan analisis temporal.

Dataset memiliki empat waktu pengamatan dalam satu hari:

```text
00:00
06:00
12:00
18:00
```

Dengan adanya dimensi waktu, perubahan konsentrasi partikulat dapat diamati sepanjang periode:

```text
29 Agustus 2025
        ↓
29 Agustus 2026
```

Analisis temporal dapat dilakukan pada tingkat:

- harian;
- mingguan;
- bulanan;
- dan keseluruhan periode.

---

## 5.18 Visualisasi Time Series

Visualisasi time series digunakan untuk melihat perubahan konsentrasi PM1, PM2.5, dan PM10 berdasarkan waktu.

Contoh bentuk analisis:

```text
Waktu
  ↓
PM1
PM2.5
PM10
  ↓
Perubahan konsentrasi
```

Grafik time series dapat digunakan untuk mengidentifikasi:

- periode dengan konsentrasi tinggi;
- periode dengan konsentrasi rendah;
- pola berulang;
- perubahan mendadak;
- dan nilai ekstrem.

Interpretasi grafik harus dilakukan berdasarkan pola data yang benar-benar terlihat pada hasil visualisasi.

---

## 5.19 Analisis Hubungan Antarparameter

Hubungan antara PM1, PM2.5, dan PM10 dapat diperiksa menggunakan korelasi.

Tujuannya adalah mengetahui apakah peningkatan salah satu parameter cenderung diikuti peningkatan parameter lainnya.

Variabel yang dibandingkan:

```text
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Analisis dapat dilakukan menggunakan:

- matriks korelasi;
- heatmap;
- scatter plot.

Korelasi yang tinggi menunjukkan adanya hubungan linear yang kuat, sedangkan korelasi yang rendah menunjukkan hubungan linear yang lebih lemah.

Korelasi tidak secara otomatis menunjukkan hubungan sebab-akibat.

---

## 5.20 Scatter Plot Antarparameter

Scatter plot dapat digunakan untuk melihat hubungan pasangan variabel:

```text
PM1 vs PM2.5
PM1 vs PM10
PM2.5 vs PM10
```

Pola titik pada scatter plot dapat memberikan gambaran apakah terdapat hubungan positif, negatif, atau tidak jelas.

Jika titik-titik cenderung membentuk pola naik, maka terdapat indikasi hubungan positif.

Jika pola tidak membentuk kecenderungan tertentu, hubungan linear kemungkinan lebih lemah.

---

## 5.21 Analisis Koordinat

Dataset memiliki koordinat:

```text
latitude  = -7.2
longitude = 112.4
```

Koordinat digunakan untuk menunjukkan lokasi titik data yang dianalisis.

Karena dataset menggunakan satu titik koordinat, analisis spasial antarwilayah belum dapat dilakukan menggunakan dataset utama ini.

Koordinat tetap penting sebagai informasi lokasi dan untuk memastikan konteks wilayah penelitian.

---

## 5.22 Ringkasan Hasil Eksplorasi

Berdasarkan eksplorasi awal, dataset memiliki:

| Komponen | Hasil |
|---|---|
| Jumlah baris | 1.464 |
| Jumlah kolom | 6 |
| Periode | 29 Agustus 2025 – 29 Agustus 2026 |
| Frekuensi | 4 observasi per hari |
| Parameter | PM1, PM2.5, PM10 |
| Latitude | -7.2 |
| Longitude | 112.4 |
| Outlier teridentifikasi | 22 |

Dataset kemudian dapat digunakan untuk analisis lebih lanjut setelah kualitas data diperiksa.

---

## 5.23 Tahapan Eksplorasi yang Dilakukan

Alur eksplorasi data:

```text
Data CSV
   ↓
Pemeriksaan Struktur
   ↓
Pemeriksaan Tipe Data
   ↓
Missing Value
   ↓
Data Duplikat
   ↓
Nilai Tidak Valid
   ↓
Statistik Deskriptif
   ↓
Distribusi PM
   ↓
Pemeriksaan Outlier
   ↓
Analisis Time Series
   ↓
Analisis Korelasi
   ↓
Visualisasi
   ↓
Interpretasi
```

---

## 5.24 Keterbatasan Eksplorasi

Eksplorasi data memiliki beberapa keterbatasan.

Pertama, dataset utama hanya memiliki tiga parameter partikulat, yaitu PM1, PM2.5, dan PM10.

Kedua, dataset menggunakan satu titik koordinat sehingga analisis spasial antarwilayah belum dapat dilakukan.

Ketiga, dataset utama tidak mencakup seluruh faktor meteorologi seperti kecepatan angin, arah angin, suhu, dan kelembapan sebagai variabel analisis utama.

Keempat, hubungan antara sumber polutan dan konsentrasi partikulat tidak dapat dibuktikan secara kausal hanya dari dataset ini.

Oleh karena itu, hasil eksplorasi digunakan untuk memahami pola dan karakteristik data, bukan untuk menyimpulkan penyebab secara langsung.

---

## 5.25 Kesimpulan

Eksplorasi data dilakukan terhadap dataset kualitas udara Kabupaten Lamongan yang terdiri dari **1.464 baris dan 6 kolom**.

Dataset mencakup periode **29 Agustus 2025 sampai 29 Agustus 2026** dengan empat waktu pengamatan setiap hari.

Parameter utama yang dianalisis adalah:

- PM1;
- PM2.5;
- PM10.

Eksplorasi meliputi pemeriksaan struktur data, tipe data, missing value, duplikasi, nilai tidak valid, statistik deskriptif, distribusi, outlier, analisis berdasarkan waktu, serta hubungan antarparameter.

Pada pemeriksaan awal ditemukan **22 outlier** yang perlu ditinjau lebih lanjut. Outlier tersebut tidak langsung dihapus karena nilai ekstrem dapat mengandung informasi yang penting.

Hasil eksplorasi menjadi dasar untuk melakukan analisis lanjutan, khususnya visualisasi time series, analisis hubungan antarparameter, dan interpretasi pola kualitas udara selama periode pengamatan.

---

## 5.26 Ringkasan Eksplorasi Data

| Aspek | Hasil |
|---|---|
| Dataset | `data_lamongan.csv` |
| Wilayah | Kabupaten Lamongan |
| Periode | 29 Agustus 2025 – 29 Agustus 2026 |
| Jumlah observasi | 1.464 |
| Jumlah fitur | 6 |
| Variabel waktu | `valid_time` |
| Variabel lokasi | `latitude`, `longitude` |
| Variabel utama | `pm1_ug_m3`, `pm2p5_ug_m3`, `pm10_ug_m3` |
| Waktu pengamatan | 00:00, 06:00, 12:00, 18:00 |
| Latitude | -7.2 |
| Longitude | 112.4 |
| Outlier awal | 22 |
| Analisis utama | Statistik, distribusi, time series, korelasi |
| Output | Dasar interpretasi kualitas udara |

Dengan demikian, tahap **Eksplorasi Data** telah memberikan dasar untuk memahami karakteristik dataset sebelum masuk ke analisis dan visualisasi yang lebih mendalam.
