# 3. Statistics Node

## 3.1 Pengertian

**Statistics** adalah node pada KNIME Analytics Platform yang digunakan
untuk melakukan **eksplorasi dan ringkasan statistik awal** terhadap
data. Node ini membantu melihat karakteristik setiap kolom secara cepat,
terutama untuk kolom numerik dan kolom kategorikal/nominal.

Pada workflow analisis kualitas udara, node **Statistics** dapat
digunakan untuk mengetahui:

-   jumlah baris data;
-   nilai minimum dan maksimum;
-   nilai rata-rata (*mean*);
-   standar deviasi;
-   varians;
-   skewness;
-   median, jika diaktifkan;
-   jumlah/nilai yang hilang (*missing values*);
-   jumlah atau frekuensi nilai pada kolom nominal;
-   distribusi nilai kategorikal melalui output occurrence/histogram
    pada versi node yang mendukungnya.

> **Catatan versi:** Tampilan dan jumlah output pada node Statistics
> dapat berbeda antarversi KNIME. Pada versi yang lebih baru, node
> Statistics dapat menyediakan **Statistics Table**, **Nominal Histogram
> Table**, dan **Occurrences Table**. Pada versi tertentu atau node
> Statistics lama, output yang tersedia dapat lebih sedikit.

------------------------------------------------------------------------

## 3.2 Tujuan Penggunaan

Node Statistics biasanya digunakan pada tahap **Exploratory Data
Analysis (EDA)** sebelum analisis lanjutan atau pemodelan.

Tujuan utamanya adalah:

1.  **Memahami struktur data**
    -   mengetahui jumlah baris dan kolom;
    -   mengetahui tipe data setiap kolom;
    -   mengetahui rentang nilai setiap variabel.
2.  **Mengetahui karakteristik numerik**
    -   nilai minimum;
    -   nilai maksimum;
    -   rata-rata;
    -   standar deviasi;
    -   varians;
    -   skewness;
    -   median jika diperlukan.
3.  **Mendeteksi masalah kualitas data**
    -   missing value;
    -   nilai yang tidak wajar;
    -   rentang nilai yang terlalu besar atau terlalu kecil;
    -   distribusi yang sangat tidak simetris.
4.  **Memahami variabel kategorikal**
    -   nilai-nilai yang muncul;
    -   frekuensi kemunculan setiap nilai;
    -   nilai yang paling sering dan paling jarang muncul.
5.  **Menjadi dasar pemilihan metode analisis berikutnya**
    -   transformasi data;
    -   penanganan outlier;
    -   imputasi missing value;
    -   normalisasi/standardisasi;
    -   visualisasi;
    -   pemodelan statistik atau machine learning.

------------------------------------------------------------------------

## 3.3 Posisi Statistics dalam Workflow

Contoh alur sederhana:

``` text
Data Reader
    |
    v
Data Preparation
    |
    v
Statistics
    |
    +--------------------+
    |                    |
    v                    v
Statistics Table     Occurrences /
                     Histogram Table
    |
    v
Interpretasi Data
    |
    v
Preprocessing / Analisis Lanjutan
```

Untuk dataset kualitas udara, contoh workflow dapat berupa:

``` text
CSV Reader
   |
   v
Column Rename / Type Conversion
   |
   v
Missing Value
   |
   v
Statistics
   |
   +--> Statistics Table
   |
   +--> Nominal Histogram Table
   |
   +--> Occurrences Table
   |
   v
Visualization / Analysis
```

Statistics sebaiknya digunakan pada tahap awal agar kondisi data dapat
diketahui sebelum mengambil keputusan analitis.

------------------------------------------------------------------------

# 3.4 Input dan Output

## Input Port

Statistics menerima:

**Input Port 0 --- Data Table**

Input berupa tabel KNIME yang terdiri dari baris dan kolom.

Contoh:

    id   latitude   longitude   pm1_ug_m3   pm2p5_ug_m3   pm10_ug_m3
  ---- ---------- ----------- ----------- ------------- ------------
     1       -7.2       112.4        8.04        10.248       10.407
     2       -7.2       112.4       15.20        18.350       21.100
     3       -7.2       112.4       42.10        48.700       55.200

Kolom numerik akan digunakan untuk perhitungan statistik numerik,
sedangkan kolom nominal/kategorikal dapat digunakan untuk menghitung
kemunculan nilai.

------------------------------------------------------------------------

## Output

Pada versi Statistics yang menyediakan tiga output, output utamanya
adalah:

### 1. Statistics Table

Berisi ringkasan statistik untuk kolom yang dianalisis.

Contoh statistik:

  Statistik        Keterangan
  ---------------- -----------------------------------
  Min              Nilai minimum
  Max              Nilai maksimum
  Mean             Nilai rata-rata
  Std. deviation   Standar deviasi
  Variance         Varians
  Median           Nilai tengah, jika diaktifkan
  Missing values   Jumlah data yang hilang
  Row count        Jumlah baris
  Skewness         Kemencengan distribusi
  Sum              Jumlah keseluruhan, jika tersedia

### 2. Nominal Histogram Table

Berisi informasi histogram/distribusi untuk kolom nominal yang dipilih,
pada versi node yang menyediakan output ini.

### 3. Occurrences Table

Berisi nilai-nilai nominal dan jumlah kemunculannya.

Contoh:

  Category      Count
  ----------- -------
  Good            120
  Moderate         85
  Unhealthy        30

> Jika versi KNIME yang digunakan hanya menyediakan sebagian output,
> gunakan output yang tersedia pada node tersebut.

------------------------------------------------------------------------

# 3.5 Cara Menambahkan Statistics Node

## Langkah 1 --- Siapkan Data

Pastikan data sudah masuk ke workflow melalui node seperti:

-   CSV Reader;
-   Excel Reader;
-   File Reader;
-   Database Reader;
-   atau node pembaca data lainnya.

## Langkah 2 --- Cari Node Statistics

Pada panel **Nodes**:

1.  klik kotak pencarian;
2.  ketik `Statistics`;
3.  pilih node **Statistics**;
4.  drag-and-drop node ke workflow.

Contoh tampilan pencarian pada KNIME:

``` text
Nodes
+---------------------------+
| Search: Statistics        |
+---------------------------+

Statistics
Statistics View
Tree Ensemble Statistics
...
```

## Langkah 3 --- Hubungkan Data

Hubungkan output dari node pembaca data ke input Statistics.

``` text
[CSV Reader]
      |
      v
[Statistics]
```

Garis koneksi harus berasal dari **output data port** node sebelumnya
menuju **input data port** Statistics.

## Langkah 4 --- Buka Konfigurasi

Klik dua kali node Statistics atau klik kanan kemudian pilih
konfigurasi.

Atur opsi yang diperlukan.

## Langkah 5 --- Execute

Setelah konfigurasi selesai:

1.  klik **Apply and Execute**, atau
2.  klik **Execute** pada toolbar.

Setelah berhasil dijalankan, node akan berubah menjadi status executed
dan output dapat dibuka.

------------------------------------------------------------------------

# 3.6 Konfigurasi Statistics

Tampilan konfigurasi dapat berbeda tergantung versi KNIME. Secara umum
terdapat beberapa pengaturan penting.

## 3.6.1 Calculate Median Values

Opsi:

**Calculate median values (computationally expensive)**

Jika diaktifkan, KNIME akan menghitung median untuk kolom numerik.

Median adalah nilai tengah setelah data diurutkan.

Contoh:

``` text
Data:
10, 20, 30, 40, 50

Median = 30
```

Untuk jumlah data genap:

``` text
10, 20, 30, 40

Median = (20 + 30) / 2
       = 25
```

### Mengapa median bersifat computationally expensive?

Perhitungan median memerlukan proses pengurutan nilai pada kolom. Pada
dataset yang sangat besar, proses ini dapat membutuhkan sumber daya
lebih besar dibanding statistik sederhana seperti mean atau minimum.

### Kapan median perlu diaktifkan?

Median berguna ketika:

-   data memiliki outlier;
-   distribusi sangat miring (*skewed*);
-   mean dianggap kurang representatif;
-   ingin membandingkan mean dan median.

------------------------------------------------------------------------

# 3.7 Column Filter pada Nominal Values

Statistics dapat memiliki pengaturan **Column filter** untuk menentukan
kolom mana yang digunakan dalam analisis nilai nominal.

Contoh data:

  city       status       pm2p5_ug_m3
  ---------- ---------- -------------
  Surabaya   Good                10.2
  Surabaya   Moderate            35.4
  Malang     Good                12.1

Kolom yang dapat dipilih untuk analisis nominal:

-   `city`
-   `status`

Sedangkan:

-   `pm2p5_ug_m3`

merupakan kolom numerik.

Column filter berguna agar perhitungan nilai kategorikal hanya dilakukan
pada kolom yang memang relevan.

------------------------------------------------------------------------

# 3.8 Max Number of Most Frequent and Infrequent Values

Pada versi Statistics yang lebih baru, terdapat pengaturan jumlah nilai
yang akan ditampilkan sebagai:

-   nilai paling sering (*most frequent*);
-   nilai paling jarang (*infrequent*).

Misalnya diatur menjadi:

``` text
5
```

Maka node dapat menampilkan hingga 5 nilai paling sering dan 5 nilai
paling jarang pada tampilan statistik, tergantung data dan konfigurasi.

Pengaturan ini terutama berguna untuk data kategorikal dengan banyak
kategori.

------------------------------------------------------------------------

# 3.9 Max Number of Possible Values per Column

Pengaturan ini menentukan batas jumlah nilai nominal yang dimasukkan ke
output.

Misalnya:

``` text
Max no. of possible values per column = 100
```

Artinya output nominal dibatasi hingga jumlah nilai yang ditentukan.

Pengaturan ini penting pada dataset dengan kolom kategorikal yang
memiliki jumlah kategori sangat besar.

Contoh:

``` text
id_pengguna
A00001
A00002
A00003
...
A99999
```

Kolom seperti ID dapat memiliki banyak nilai unik dan biasanya tidak
terlalu berguna untuk analisis distribusi kategorikal.

------------------------------------------------------------------------

# 3.10 Statistik pada Output Table

Pada screenshot workflow, terlihat **Statistics Table** dengan beberapa
kolom statistik.

Contoh hasil:

  Column             Min       Max     Mean   Std. deviation   Variance   Skewness
  ------------- -------- --------- -------- ---------------- ---------- ----------
  id                   1      1464    732.5          422.765    178,730          0
  latitude          -7.2      -7.2     -7.2                0          0          0
  longitude        112.4     112.4    112.4                0          0          0
  pm1_ug_m3         8.04   193.528   57.529           33.979   1,154.57      0.967
  pm2p5_ug_m3     10.248    204.64   62.028           35.869    1,286.6      0.968
  pm10_ug_m3      10.407   207.295    63.61           36.421   1,326.47      0.958

> Nilai di atas mengikuti angka yang terlihat pada screenshot contoh.
> Untuk analisis dataset sebenarnya, gunakan hasil eksekusi node pada
> data yang digunakan.

------------------------------------------------------------------------

# 3.11 Interpretasi Statistik pada Screenshot

## 3.11.1 ID

Dari contoh:

``` text
Min  = 1
Max  = 1464
Mean = 732.5
```

Hal ini menunjukkan ID berada pada rentang 1 sampai 1464.

Karena ID merupakan identifier, nilai seperti mean dan standar deviasi
biasanya **tidak memiliki makna statistik substantif**.

Contoh:

``` text
mean(id) = 732.5
```

Tidak berarti bahwa "nilai ID rata-rata" memiliki arti terhadap kualitas
udara.

**Kesimpulan:** kolom ID biasanya tidak digunakan sebagai variabel
prediktor atau variabel analisis numerik.

------------------------------------------------------------------------

## 3.11.2 Latitude

Pada contoh:

``` text
Min  = -7.2
Max  = -7.2
Mean = -7.2
Std. deviation = 0
Variance = 0
```

Karena nilai minimum dan maksimum sama, seluruh data kemungkinan
menggunakan satu nilai latitude.

Secara matematis:

``` text
x₁ = x₂ = ... = xₙ = -7.2
```

Maka:

``` text
Mean = -7.2
Variance = 0
Std. deviation = 0
```

Hal ini menunjukkan tidak terdapat variasi latitude pada data contoh.

------------------------------------------------------------------------

## 3.11.3 Longitude

Contoh:

``` text
Min  = 112.4
Max  = 112.4
Mean = 112.4
Std. deviation = 0
Variance = 0
```

Interpretasinya sama seperti latitude: nilai longitude tidak berubah
pada data contoh.

Jika latitude dan longitude selalu konstan, kedua kolom tersebut tidak
memberikan variasi lokasi untuk analisis statistik pada dataset
tersebut.

------------------------------------------------------------------------

## 3.11.4 PM1

Contoh:

``` text
Min = 8.04
Max = 193.528
Mean = 57.529
Std. deviation = 33.979
Variance = 1,154.57
Skewness = 0.967
```

Rentang nilai cukup besar:

``` text
Range = Max - Min
      = 193.528 - 8.04
      = 185.488
```

Skewness bernilai positif:

``` text
Skewness ≈ 0.967
```

Hal ini menunjukkan distribusi PM1 cenderung **right-skewed / positively
skewed**, yaitu terdapat ekor distribusi ke arah nilai yang lebih
tinggi.

------------------------------------------------------------------------

## 3.11.5 PM2.5

Contoh:

``` text
Min = 10.248
Max = 204.64
Mean = 62.028
Std. deviation = 35.869
Variance = 1,286.6
Skewness = 0.968
```

Skewness positif menunjukkan bahwa distribusi PM2.5 cenderung memiliki
ekor ke kanan.

Artinya, terdapat sebagian pengamatan dengan konsentrasi PM2.5 yang jauh
lebih tinggi dibanding sebagian besar data.

Perlu diperhatikan bahwa **skewness positif tidak otomatis berarti data
salah**. Nilai tersebut dapat mencerminkan kondisi polusi yang memang
sesekali meningkat tajam.

------------------------------------------------------------------------

## 3.11.6 PM10

Contoh:

``` text
Min = 10.407
Max = 207.295
Mean = 63.61
Std. deviation = 36.421
Variance = 1,326.47
Skewness = 0.958
```

Interpretasinya:

-   nilai PM10 memiliki variasi yang cukup besar;
-   terdapat rentang nilai yang luas;
-   distribusi cenderung positif skewed;
-   terdapat kemungkinan sejumlah observasi dengan konsentrasi tinggi.

------------------------------------------------------------------------

# 3.12 Penjelasan Setiap Statistik

## Minimum

Minimum adalah nilai terkecil dalam suatu kolom.

Rumus sederhana:

``` text
Min(X) = nilai X terkecil
```

Contoh:

``` text
Data = 10, 20, 30, 40

Min = 10
```

### Kegunaan

Minimum berguna untuk:

-   mengetahui batas bawah data;
-   mendeteksi nilai tidak wajar;
-   memeriksa rentang pengukuran.

------------------------------------------------------------------------

## Maximum

Maximum adalah nilai terbesar.

``` text
Max(X) = nilai X terbesar
```

Contoh:

``` text
Data = 10, 20, 30, 40

Max = 40
```

### Kegunaan

Maximum berguna untuk:

-   mengetahui nilai tertinggi;
-   mendeteksi kemungkinan outlier;
-   mengecek batas alat ukur atau batas domain data.

------------------------------------------------------------------------

## Mean

Mean atau rata-rata:

\[ `\bar`{=tex}{x} = `\frac{\sum_{i=1}^{n}x_i}{n}`{=tex} \]

Contoh:

``` text
Data = 10, 20, 30

Mean = (10 + 20 + 30) / 3
     = 20
```

Mean sensitif terhadap outlier.

Contoh:

``` text
10, 20, 30, 100
```

Nilai 100 akan meningkatkan mean secara signifikan.

------------------------------------------------------------------------

## Median

Median adalah nilai tengah data yang sudah diurutkan.

Median lebih tahan terhadap outlier dibandingkan mean.

Contoh:

``` text
10, 20, 30, 100, 200

Median = 30
```

Sedangkan mean:

``` text
Mean = 72
```

Karena itu, membandingkan mean dan median dapat membantu memahami bentuk
distribusi.

------------------------------------------------------------------------

## Standard Deviation

Standard deviation atau standar deviasi mengukur seberapa jauh data
tersebar dari rata-rata.

Secara umum:

``` text
Std. deviation kecil
    -> data relatif dekat dengan mean

Std. deviation besar
    -> data lebih tersebar
```

Untuk populasi, salah satu bentuk rumusnya:

\[ `\sigma `{=tex}= `\sqrt{\frac{\sum (x_i-\mu)^2}{N}}`{=tex} \]

Untuk sampel:

\[ s = `\sqrt{\frac{\sum (x_i-\bar{x})^2}{n-1}}`{=tex} \]

Interpretasi harus mempertimbangkan satuan variabel.

------------------------------------------------------------------------

## Variance

Variance adalah kuadrat dari standar deviasi.

Secara umum:

\[ Variance = (Std. deviation)\^2 \]

Contoh dari screenshot:

``` text
Std. deviation PM1 ≈ 33.979

Variance ≈ 33.979²
         ≈ 1,154.57
```

Variance memiliki satuan yang dikuadratkan, sehingga standar deviasi
biasanya lebih mudah diinterpretasikan secara langsung.

------------------------------------------------------------------------

## Skewness

Skewness mengukur tingkat kemencengan distribusi.

Secara umum:

``` text
Skewness ≈ 0
    -> distribusi relatif simetris

Skewness > 0
    -> right-skewed / ekor ke kanan

Skewness < 0
    -> left-skewed / ekor ke kiri
```

Pada contoh:

``` text
PM1    ≈ 0.967
PM2.5  ≈ 0.968
PM10   ≈ 0.958
```

Ketiganya positif dan mendekati 1, sehingga distribusi cenderung
**miring ke kanan**.

------------------------------------------------------------------------

# 3.13 Mengapa Statistik Penting untuk Data Kualitas Udara?

Data kualitas udara biasanya memiliki variasi yang cukup besar.

Contoh variabel:

-   PM1;
-   PM2.5;
-   PM10;
-   CO;
-   NO₂;
-   SO₂;
-   O₃;
-   temperatur;
-   kelembapan;
-   tekanan;
-   kecepatan angin.

Statistics membantu menjawab pertanyaan awal seperti:

### Pertanyaan 1

> Berapa konsentrasi PM2.5 terendah?

Gunakan:

``` text
Minimum
```

### Pertanyaan 2

> Berapa konsentrasi PM2.5 tertinggi?

Gunakan:

``` text
Maximum
```

### Pertanyaan 3

> Berapa rata-rata konsentrasi PM2.5?

Gunakan:

``` text
Mean
```

### Pertanyaan 4

> Apakah konsentrasi PM2.5 sangat bervariasi?

Periksa:

``` text
Standard deviation
Variance
Range
```

### Pertanyaan 5

> Apakah distribusinya simetris?

Periksa:

``` text
Skewness
```

### Pertanyaan 6

> Apakah terdapat nilai ekstrim?

Bandingkan:

``` text
Minimum
Maximum
Mean
Median
Standard deviation
```

dan lanjutkan dengan visualisasi/histogram jika diperlukan.

------------------------------------------------------------------------

# 3.14 Contoh Analisis PM2.5

Misalkan Statistics menghasilkan:

``` text
Min      = 10.248
Max      = 204.640
Mean     = 62.028
Std Dev  = 35.869
Variance = 1,286.600
Skewness = 0.968
```

## Langkah 1 --- Hitung range

\[ Range = Max - Min \]

\[ Range = 204.640 - 10.248 \]

\[ Range = 194.392 \]

Range cukup besar sehingga konsentrasi PM2.5 memiliki variasi yang cukup
tinggi.

## Langkah 2 --- Bandingkan mean dengan median

Jika median tersedia, bandingkan:

``` text
Mean > Median
```

Jika mean lebih besar daripada median dan skewness positif, hal tersebut
konsisten dengan distribusi yang memiliki ekor ke kanan.

## Langkah 3 --- Evaluasi standar deviasi

``` text
Mean ≈ 62.028
Std Dev ≈ 35.869
```

Standar deviasi cukup besar dibanding mean, sehingga data menunjukkan
penyebaran yang cukup besar di sekitar rata-rata.

## Langkah 4 --- Evaluasi skewness

``` text
Skewness ≈ 0.968
```

Distribusi cenderung positif skewed.

### Kesimpulan contoh

Data PM2.5 memiliki rentang yang luas, variasi yang cukup besar, dan
distribusi yang cenderung miring ke kanan. Oleh karena itu, analisis
lanjutan sebaiknya mempertimbangkan keberadaan nilai tinggi/outlier dan
tidak hanya mengandalkan mean.

------------------------------------------------------------------------

# 3.15 Missing Values

Salah satu fungsi penting Statistics adalah membantu memeriksa kualitas
data.

Missing value dapat terjadi karena:

-   sensor tidak membaca data;
-   koneksi terputus;
-   kesalahan input;
-   data tidak tersedia;
-   proses pengumpulan data gagal.

Contoh:

``` text
PM2.5

10.2
12.3
?
15.8
?
20.1
```

Jika terdapat missing value, statistik harus diinterpretasikan dengan
memperhatikan jumlah data yang benar-benar tersedia.

### Tindakan lanjutan

Setelah menemukan missing value, beberapa pilihan adalah:

1.  menghapus baris;
2.  mengganti dengan mean;
3.  mengganti dengan median;
4.  menggunakan metode imputasi;
5.  mempertahankan missing value jika secara analitis memang bermakna.

Untuk data sensor, **jangan langsung mengganti semua missing value
dengan mean**. Pertimbangkan pola waktu, lokasi, dan karakteristik
sensor terlebih dahulu.

------------------------------------------------------------------------

# 3.16 Statistics dan Outlier

Statistics dapat menjadi langkah awal untuk mendeteksi outlier, tetapi
Statistics saja tidak selalu cukup untuk menentukan apakah suatu nilai
benar-benar outlier.

Contoh:

``` text
Mean = 50
Std Dev = 10
Max = 200
```

Nilai 200 terlihat jauh dari rata-rata.

Namun, nilai tersebut belum tentu salah.

Kemungkinan:

-   sensor error;
-   kejadian polusi ekstrem;
-   kebakaran;
-   aktivitas industri;
-   kondisi meteorologis tertentu.

Karena itu, lakukan validasi menggunakan:

-   histogram;
-   box plot;
-   line chart berdasarkan waktu;
-   informasi lokasi;
-   data sensor lainnya.

------------------------------------------------------------------------

# 3.17 Perbedaan Statistics Node dan Statistics View

KNIME memiliki node yang namanya mirip, sehingga penting membedakannya.

## Statistics

Node **Statistics** digunakan untuk menghitung dan menghasilkan
ringkasan statistik sebagai output table, termasuk statistik numerik dan
informasi nominal pada versi yang mendukungnya.

## Statistics View

**Statistics View** lebih berorientasi pada penyajian statistik sebagai
visualisasi/view.

Dengan kata lain:

``` text
Statistics
    -> fokus pada perhitungan dan output data

Statistics View
    -> fokus pada tampilan/view statistik
```

Pastikan node yang digunakan sesuai dengan kebutuhan workflow.

------------------------------------------------------------------------

# 3.18 Kesalahan Umum

## Kesalahan 1 --- Menganggap ID sebagai variabel numerik

ID memang sering berupa angka, tetapi angka tersebut belum tentu
memiliki makna matematis.

Contoh:

``` text
id = 1, 2, 3, 4, ...
```

Jangan menyimpulkan bahwa ID memiliki hubungan linear dengan kualitas
udara.

### Solusi

Gunakan ID sebagai identifier, bukan sebagai variabel analisis.

------------------------------------------------------------------------

## Kesalahan 2 --- Menganggap mean sebagai kondisi tipikal

Mean dapat terpengaruh oleh outlier.

Jika distribusi sangat skewed, median dapat memberikan gambaran pusat
data yang lebih representatif.

------------------------------------------------------------------------

## Kesalahan 3 --- Menganggap nilai maksimum pasti error

Nilai maksimum yang tinggi belum tentu kesalahan.

Perlu dilakukan validasi terhadap:

-   waktu;
-   lokasi;
-   sensor;
-   kondisi lingkungan;
-   variabel lain.

------------------------------------------------------------------------

## Kesalahan 4 --- Mengabaikan satuan

Contoh:

``` text
PM2.5 = 62.028
```

Angka tersebut tidak cukup informatif tanpa mengetahui satuannya,
misalnya:

``` text
µg/m³
```

Nama kolom pada screenshot menggunakan pola:

``` text
pm2p5_ug_m3
```

yang mengindikasikan konsentrasi PM2.5 dalam satuan mikrogram per meter
kubik.

------------------------------------------------------------------------

## Kesalahan 5 --- Membandingkan variance tanpa memperhatikan satuan

Variance memiliki satuan kuadrat.

Jika PM2.5 menggunakan:

``` text
µg/m³
```

maka variance secara konseptual menggunakan satuan:

``` text
(µg/m³)²
```

Untuk interpretasi praktis, standard deviation sering lebih mudah
dipahami.

------------------------------------------------------------------------

# 3.19 Rekomendasi Workflow untuk Dataset Air Quality

Workflow yang disarankan:

``` text
                 +----------------+
                 |   Data Reader  |
                 +-------+--------+
                         |
                         v
                 +----------------+
                 | Type Conversion|
                 +-------+--------+
                         |
                         v
                 +----------------+
                 | Missing Value  |
                 +-------+--------+
                         |
                         v
                 +----------------+
                 |   Statistics   |
                 +-------+--------+
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
   Statistics Table  Histogram      Occurrences
          |              |              |
          +--------------+--------------+
                         |
                         v
                 +----------------+
                 | Visualization  |
                 +-------+--------+
                         |
                         v
                 +----------------+
                 | Analysis / ML  |
                 +----------------+
```

------------------------------------------------------------------------

# 3.20 Checklist Setelah Menjalankan Statistics

Gunakan checklist berikut:

-   [ ] Apakah jumlah baris sudah sesuai?
-   [ ] Apakah semua kolom memiliki tipe data yang benar?
-   [ ] Apakah terdapat missing value?
-   [ ] Apakah terdapat nilai minimum yang tidak masuk akal?
-   [ ] Apakah terdapat nilai maksimum yang tidak masuk akal?
-   [ ] Apakah mean dan median berbeda jauh?
-   [ ] Apakah standar deviasi besar?
-   [ ] Apakah variance besar?
-   [ ] Apakah skewness positif atau negatif?
-   [ ] Apakah ada kolom dengan variance = 0?
-   [ ] Apakah ada kolom ID yang sebaiknya tidak dianalisis sebagai
    numerik?
-   [ ] Apakah ada kolom kategorikal dengan terlalu banyak nilai unik?
-   [ ] Apakah diperlukan histogram atau box plot untuk pemeriksaan
    lebih lanjut?

------------------------------------------------------------------------

# 3.21 Ringkasan

**Statistics Node** merupakan salah satu node penting untuk tahap awal
analisis data di KNIME.

Node ini membantu memperoleh gambaran statistik secara cepat sebelum
masuk ke analisis yang lebih kompleks.

Statistik utama yang perlu diperhatikan:

  Statistik        Fungsi utama
  ---------------- ---------------------------
  Min              Nilai terkecil
  Max              Nilai terbesar
  Mean             Nilai rata-rata
  Median           Nilai tengah
  Std. deviation   Tingkat penyebaran data
  Variance         Kuadrat standar deviasi
  Skewness         Kemencengan distribusi
  Missing values   Data yang tidak tersedia
  Occurrences      Frekuensi nilai nominal
  Histogram        Gambaran distribusi nilai

Pada contoh data kualitas udara dalam screenshot, PM1, PM2.5, dan PM10
memiliki **skewness positif sekitar 0.96**, yang menunjukkan distribusi
cenderung miring ke kanan. Sementara latitude dan longitude pada contoh
memiliki **standar deviasi dan variance sebesar 0**, yang menunjukkan
tidak terdapat variasi lokasi pada nilai tersebut.

Dengan demikian, Statistics dapat digunakan sebagai dasar untuk
menentukan langkah berikutnya, misalnya:

``` text
Statistics
    ↓
Pemeriksaan missing value
    ↓
Pemeriksaan distribusi
    ↓
Deteksi/validasi outlier
    ↓
Transformasi / preprocessing
    ↓
Visualisasi
    ↓
Analisis lanjutan / Machine Learning
```

------------------------------------------------------------------------

# 3.22 Kesimpulan

Node **Statistics** digunakan untuk melakukan **deskripsi statistik dan
pemeriksaan awal terhadap data**.

Untuk dataset kualitas udara, node ini sangat berguna untuk memahami:

1.  rentang konsentrasi polutan;
2.  nilai rata-rata;
3.  tingkat variasi;
4.  kemencengan distribusi;
5.  keberadaan missing value;
6.  frekuensi kategori;
7.  kemungkinan nilai ekstrem;
8.  kolom yang tidak memiliki variasi.

Namun, output Statistics sebaiknya tidak langsung dianggap sebagai
kesimpulan akhir. Statistik deskriptif perlu dikombinasikan dengan
visualisasi dan pengetahuan domain agar interpretasi data kualitas udara
menjadi lebih valid.

------------------------------------------------------------------------

## Referensi

Dokumentasi dan informasi node yang digunakan sebagai acuan:

-   KNIME Analytics Platform User Guide --- pembahasan data table,
    column types, node monitor, dan statistics.
-   Dokumentasi node **Statistics** KNIME/KNIME Base.
-   NodePit --- dokumentasi teknis Statistics Node untuk versi KNIME
    yang lebih baru.
-   KNIME Analytics Platform --- dokumentasi resmi mengenai data table
    dan node workflow.

> **Catatan:** Nama opsi, jumlah output port, dan tampilan dialog dapat
> berubah mengikuti versi KNIME Analytics Platform yang digunakan.
> Screenshot pada materi ini menunjukkan konfigurasi/tampilan Statistics
> pada workflow analisis kualitas udara.
