# 6. Analisis Time Series dan Kesimpulan

## 6.1 Pendahuluan

Analisis *time series* digunakan untuk melihat bagaimana nilai suatu variabel berubah berdasarkan waktu. Pada dataset kualitas udara, kolom `valid_time` berperan sebagai penanda waktu pengamatan, sedangkan parameter yang diamati adalah konsentrasi partikulat `pm1_ug_m3`, `pm2p5_ug_m3`, dan `pm10_ug_m3`.

Dataset yang digunakan berasal dari data kualitas udara Lamongan dan telah dipindahkan ke PostgreSQL Aiven pada tabel `public.air_quality`. Struktur tabel menggunakan `valid_time` sebagai waktu pengamatan dan tiga kolom PM sebagai variabel konsentrasi. Data yang berhasil disimpan berjumlah **1.464 baris**.

Tujuan analisis pada tahap ini adalah:

1. memahami perubahan konsentrasi partikulat terhadap waktu;
2. melihat kecenderungan atau pola perubahan PM;
3. mengidentifikasi lonjakan konsentrasi;
4. menghubungkan hasil time series dengan statistik deskriptif;
5. menentukan kesimpulan dari keseluruhan proses analisis.

---

## 6.2 Struktur Data Time Series

Data yang digunakan memiliki beberapa atribut utama:

| Kolom | Keterangan |
|---|---|
| `id` | ID unik data |
| `valid_time` | Waktu pengamatan |
| `latitude` | Koordinat lintang |
| `longitude` | Koordinat bujur |
| `pm1_ug_m3` | Konsentrasi PM1 dalam µg/m³ |
| `pm2p5_ug_m3` | Konsentrasi PM2.5 dalam µg/m³ |
| `pm10_ug_m3` | Konsentrasi PM10 dalam µg/m³ |

Kolom `valid_time` menjadi komponen utama dalam analisis time series karena setiap pengukuran partikulat harus dikaitkan dengan waktu tertentu.

Alur data yang digunakan:

```text
CSV
 ↓
PostgreSQL Aiven
 ↓
public.air_quality
 ↓
KNIME
 ↓
Statistics
 ↓
Analisis Time Series
 ↓
Interpretasi
```

Data dari CSV telah berhasil diimport ke PostgreSQL dan diverifikasi sebanyak **1.464 baris**.

---

## 6.3 Analisis Perubahan PM terhadap Waktu

Secara konsep, analisis time series dilakukan dengan menempatkan `valid_time` sebagai sumbu-X dan nilai konsentrasi PM sebagai sumbu-Y.

Visualisasi dapat dibuat untuk masing-masing parameter:

```text
Sumbu-X → valid_time
Sumbu-Y → pm1_ug_m3
```

```text
Sumbu-X → valid_time
Sumbu-Y → pm2p5_ug_m3
```

```text
Sumbu-X → valid_time
Sumbu-Y → pm10_ug_m3
```

Ketiga grafik tersebut dapat digunakan untuk mengamati:

- perubahan konsentrasi dari waktu ke waktu;
- periode ketika konsentrasi meningkat;
- periode ketika konsentrasi menurun;
- lonjakan nilai (*spike*);
- kemungkinan pola berulang;
- kecenderungan umum (*trend*);
- episode partikulat dengan konsentrasi tinggi.

> **Catatan:** berdasarkan bahan yang tersedia, hasil statistik numerik telah tersedia, tetapi angka rinci untuk setiap timestamp atau hasil grafik time series tidak tersedia. Oleh karena itu, pola harian tertentu tidak dibuat-buat sebagai hasil pengamatan.

---

## 6.4 Hubungan Hasil Time Series dengan Statistik Deskriptif

Hasil `Statistics` pada KNIME memberikan gambaran keseluruhan terhadap 1.464 pengukuran. Ringkasan parameter partikulat adalah sebagai berikut:

| Parameter | Minimum | Maximum | Mean | Std. Deviation | Variance | Skewness |
|---|---:|---:|---:|---:|---:|---:|
| PM1 | 8.040 | 193.528 | 57.529 | 33.979 | 1,154.57 | 0.967 |
| PM2.5 | 10.248 | 204.640 | 62.028 | 35.869 | 1,286.60 | 0.968 |
| PM10 | 10.407 | 207.295 | 63.610 | 36.421 | 1,326.47 | 0.958 |

Dari tabel tersebut dapat diketahui beberapa hal penting.

### 6.4.1 PM1

PM1 mempunyai nilai minimum **8.040 µg/m³**, maksimum **193.528 µg/m³**, dan mean **57.529 µg/m³**.

Standar deviasi sebesar **33.979** menunjukkan adanya penyebaran nilai yang cukup besar dari rata-ratanya. Skewness sebesar **0.967** menunjukkan distribusi PM1 cenderung menceng ke kanan.

Dalam konteks time series, nilai maksimum yang jauh di atas mean perlu diperiksa kembali pada timestamp tempat nilai tersebut terjadi.

### 6.4.2 PM2.5

PM2.5 mempunyai nilai minimum **10.248 µg/m³**, maksimum **204.640 µg/m³**, dan mean **62.028 µg/m³**.

Standar deviasi sebesar **35.869** menunjukkan variasi pengukuran yang cukup besar. Skewness sebesar **0.968** juga menunjukkan kecenderungan distribusi ke arah kanan.

Perbedaan antara maksimum dan mean adalah:

```text
204.640 - 62.028 = 142.612 µg/m³
```

Hal ini menunjukkan bahwa terdapat nilai pengukuran tinggi yang perlu diperiksa pada analisis berdasarkan waktu.

### 6.4.3 PM10

PM10 mempunyai nilai minimum **10.407 µg/m³**, maksimum **207.295 µg/m³**, dan mean **63.610 µg/m³**.

PM10 mempunyai:

- mean paling tinggi;
- maksimum paling tinggi;
- standar deviasi paling tinggi;
- variance paling tinggi.

Skewness sebesar **0.958** juga menunjukkan distribusi cenderung menceng ke kanan.

Dengan demikian, apabila grafik time series menunjukkan lonjakan pada PM10, lonjakan tersebut perlu dikaitkan dengan timestamp dan dibandingkan dengan PM1 serta PM2.5 pada waktu yang sama.

---

## 6.5 Pola dan Variasi Data

Berdasarkan statistik deskriptif yang tersedia, ketiga parameter mempunyai pola distribusi yang relatif serupa.

Urutan mean:

```text
PM10 > PM2.5 > PM1
```

Urutan standar deviasi:

```text
PM10 > PM2.5 > PM1
```

Urutan variance:

```text
PM10 > PM2.5 > PM1
```

Urutan range:

```text
PM10 > PM2.5 > PM1
```

Sedangkan skewness ketiganya hampir sama:

```text
PM1    = 0.967
PM2.5  = 0.968
PM10   = 0.958
```

Ketiga nilai tersebut positif dan mendekati 1. Artinya, distribusi data memiliki kecenderungan ekor ke arah nilai konsentrasi yang lebih tinggi.

### 6.5.1 Variasi PM

Rentang masing-masing parameter:

| Parameter | Range (µg/m³) |
|---|---:|
| PM1 | 185.488 |
| PM2.5 | 194.392 |
| PM10 | 196.888 |

PM10 memiliki rentang terbesar. Hal ini menunjukkan bahwa secara absolut PM10 mempunyai perubahan nilai yang paling luas pada dataset yang dianalisis.

Namun, statistik tersebut tidak menunjukkan kapan perubahan terjadi. Untuk mengetahui waktunya, diperlukan grafik atau tabel time series berdasarkan `valid_time`.

---

## 6.6 Analisis Nilai Ekstrem

Nilai maksimum yang jauh lebih tinggi dibandingkan mean dapat menjadi kandidat nilai ekstrem.

Contohnya:

```text
PM1
Mean = 57.529
Max  = 193.528
```

```text
PM2.5
Mean = 62.028
Max  = 204.640
```

```text
PM10
Mean = 63.610
Max  = 207.295
```

Nilai maksimum tersebut tidak boleh langsung dianggap sebagai kesalahan data atau langsung dihapus.

Langkah validasi yang lebih tepat adalah:

```text
Nilai ekstrem ditemukan
        ↓
Periksa timestamp
        ↓
Bandingkan PM1, PM2.5, dan PM10
        ↓
Periksa lokasi
        ↓
Periksa kondisi lingkungan
        ↓
Periksa sensor / sumber data
        ↓
Tentukan valid atau error
```

Jika beberapa parameter PM meningkat pada timestamp yang sama, nilai tersebut dapat merupakan indikasi episode partikulat tinggi yang benar-benar terjadi.

Sebaliknya, jika hanya satu parameter yang mengalami lonjakan sangat besar sementara parameter lainnya tetap rendah, data tersebut perlu diperiksa lebih lanjut.

---

## 6.7 Moving Average

Moving average dapat digunakan untuk membantu melihat kecenderungan umum pada data time series dengan mengurangi fluktuasi jangka pendek.

Untuk moving average tiga periode:

\[
MA_t = \frac{x_t + x_{t-1} + x_{t-2}}{3}
\]

Contoh:

```text
t-2 = 20
t-1 = 30
t   = 40
```

Maka:

```text
MA = (20 + 30 + 40) / 3
   = 30
```

Pada data kualitas udara, moving average dapat diterapkan pada PM1, PM2.5, maupun PM10.

Tujuannya adalah membantu membedakan:

- fluktuasi jangka pendek;
- lonjakan sesaat;
- kecenderungan konsentrasi dalam periode tertentu.

Namun, moving average juga dapat menghaluskan lonjakan penting. Oleh karena itu, grafik data asli tetap perlu dipertahankan.

---

## 6.8 Interpretasi Keseluruhan

Dari seluruh proses analisis, dapat diperoleh beberapa temuan utama.

### 1. Dataset berhasil disiapkan

Dataset kualitas udara telah dipindahkan dari CSV ke PostgreSQL Aiven dan berhasil diverifikasi sebanyak **1.464 baris**.

### 2. Data memiliki komponen waktu

Kolom `valid_time` digunakan sebagai dasar untuk melakukan analisis perubahan konsentrasi terhadap waktu.

### 3. PM10 memiliki nilai rata-rata tertinggi

Rata-rata konsentrasi:

```text
PM1    = 57.529 µg/m³
PM2.5  = 62.028 µg/m³
PM10   = 63.610 µg/m³
```

Sehingga:

```text
PM10 > PM2.5 > PM1
```

### 4. PM10 memiliki penyebaran absolut terbesar

Standar deviasi:

```text
PM1    = 33.979
PM2.5  = 35.869
PM10   = 36.421
```

PM10 memiliki variasi absolut paling besar.

### 5. Ketiga parameter memiliki distribusi right-skewed

Skewness PM1, PM2.5, dan PM10 semuanya positif dan mendekati 1. Hal tersebut menunjukkan adanya kecenderungan nilai tinggi yang membentuk ekor distribusi ke arah kanan.

### 6. Terdapat indikasi nilai ekstrem

Nilai maksimum ketiga parameter jauh lebih tinggi dibandingkan nilai rata-ratanya. Kondisi ini menunjukkan perlunya pemeriksaan lebih lanjut berdasarkan timestamp.

### 7. Nilai ekstrem tidak boleh langsung dihapus

Dalam data kualitas udara, lonjakan konsentrasi dapat merupakan kejadian nyata. Validasi harus dilakukan dengan melihat waktu, parameter PM lainnya, kondisi lingkungan, dan karakteristik sensor.

---

## 6.9 Kesimpulan

Berdasarkan analisis data kualitas udara menggunakan KNIME dan PostgreSQL, dapat disimpulkan bahwa dataset yang digunakan terdiri dari **1.464 pengukuran** dengan parameter waktu `valid_time` dan konsentrasi PM1, PM2.5, serta PM10.

Hasil statistik menunjukkan bahwa PM10 mempunyai nilai rata-rata tertinggi sebesar **63.610 µg/m³**, diikuti PM2.5 sebesar **62.028 µg/m³**, dan PM1 sebesar **57.529 µg/m³**. PM10 juga mempunyai standar deviasi, variance, dan range paling besar sehingga menunjukkan penyebaran absolut yang paling tinggi pada dataset.

Ketiga parameter mempunyai skewness positif, yaitu sekitar **0.96**, sehingga distribusi konsentrasi partikulat cenderung menceng ke kanan. Kondisi ini sejalan dengan adanya nilai maksimum yang cukup jauh dibandingkan nilai rata-rata.

Analisis time series diperlukan untuk melengkapi statistik deskriptif karena statistik keseluruhan belum menunjukkan **kapan** nilai tinggi tersebut terjadi. Dengan menggunakan `valid_time` sebagai sumbu waktu, perubahan PM dapat dianalisis untuk menemukan tren, fluktuasi, dan episode konsentrasi tinggi.

Dengan demikian, proses analisis dapat dirangkum sebagai berikut:

```text
Dataset Kualitas Udara
        ↓
PostgreSQL Aiven
        ↓
1.464 Data Pengamatan
        ↓
KNIME Statistics
        ↓
Min / Max / Mean / Std / Variance / Skewness
        ↓
Analisis PM1 / PM2.5 / PM10
        ↓
Time Series berdasarkan valid_time
        ↓
Pemeriksaan Tren dan Nilai Ekstrem
        ↓
Interpretasi dan Kesimpulan
```

Secara keseluruhan, analisis menunjukkan bahwa data memiliki variasi konsentrasi partikulat yang cukup besar dan terdapat beberapa nilai tinggi yang perlu divalidasi berdasarkan waktu pengamatan. Hasil statistik dan time series dapat menjadi dasar untuk analisis lanjutan seperti korelasi antarparameter, deteksi outlier, analisis pola harian, dan forecasting kualitas udara.

---

## 6.10 Catatan untuk Dokumentasi

Pada dokumentasi final, apabila grafik time series dari KNIME sudah tersedia, grafik dapat ditempatkan pada bagian **6.3 Analisis Perubahan PM terhadap Waktu** dengan format:

```markdown
![Time Series PM1](./assets/time-series-pm1.png)

**Gambar 6.1.** Perubahan konsentrasi PM1 terhadap waktu.
```

Kemudian:

```markdown
![Time Series PM2.5](./assets/time-series-pm25.png)

**Gambar 6.2.** Perubahan konsentrasi PM2.5 terhadap waktu.
```

Dan:

```markdown
![Time Series PM10](./assets/time-series-pm10.png)

**Gambar 6.3.** Perubahan konsentrasi PM10 terhadap waktu.
```

Jika ketiga parameter ditampilkan dalam satu grafik:

```markdown
![Time Series PM](./assets/time-series-pm.png)

**Gambar 6.4.** Perbandingan perubahan PM1, PM2.5, dan PM10 terhadap waktu.
```

> **Catatan penting:** bagian ini sengaja tidak mengklaim adanya pola pagi/siang/malam atau tren naik/turun tertentu karena hasil timestamp per observasi dan grafik time series belum tersedia dalam bahan yang diberikan. Hal tersebut lebih aman daripada memasukkan pola yang belum benar-benar dihitung dari dataset.
