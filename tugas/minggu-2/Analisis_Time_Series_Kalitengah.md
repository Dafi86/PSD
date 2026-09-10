# 6. Analisis Time Series

## 6.1 Pendahuluan

Analisis *time series* digunakan untuk melihat perubahan nilai suatu
data berdasarkan urutan waktu. Berbeda dengan statistika deskriptif yang
memberikan gambaran umum mengenai karakteristik data, analisis *time
series* memungkinkan perubahan nilai diamati secara kronologis dari satu
tanggal ke tanggal berikutnya.

Pada penelitian ini, analisis *time series* digunakan untuk mengamati
perubahan konsentrasi tiga polutan, yaitu **Nitrogen Dioksida (NO₂)**,
**Karbon Monoksida (CO)**, dan **Sulfur Dioksida (SO₂)** di Kecamatan
Kalitengah, Kabupaten Lamongan.

Data yang dianalisis memiliki rentang waktu mulai **31 Agustus 2025
sampai 31 Agustus 2026**. Dengan rentang tersebut, terdapat **366
tanggal kalender**. Data polutan diperoleh dari hasil pengolahan data
**Sentinel-5P**, kemudian disimpan dalam **database PostgreSQL Aiven**
sebelum digunakan dalam proses pengolahan dan analisis menggunakan
**KNIME**.

Analisis ini berfokus pada pola perubahan nilai polutan terhadap waktu,
kelengkapan data, nilai minimum dan maksimum, serta karakteristik
distribusi masing-masing polutan. Analisis yang dilakukan bersifat
deskriptif sehingga hasilnya digunakan untuk menggambarkan kondisi data,
bukan untuk menentukan hubungan sebab-akibat.

------------------------------------------------------------------------

## 6.2 Struktur Data Time Series

Data *time series* disusun berdasarkan tanggal pengamatan. Kolom `date`
digunakan sebagai penanda waktu, sedangkan kolom `NO2`, `CO`, dan `SO2`
digunakan sebagai variabel polutan yang diamati.

Struktur data yang digunakan adalah sebagai berikut:

  Kolom    Keterangan
  -------- -------------------------
  `date`   Tanggal pengamatan
  `NO2`    Nilai Nitrogen Dioksida
  `CO`     Nilai Karbon Monoksida
  `SO2`    Nilai Sulfur Dioksida

Contoh data yang digunakan:

  Tanggal               NO₂           CO           SO₂
  ------------ ------------ ------------ -------------
  2025-08-31     0.00003774   0.02549803    0.00027628
  2025-09-01     0.00003116   0.02842947   -0.00016491
  2025-09-02           NULL   0.02262214          NULL
  2025-09-03     0.00002038   0.02528949   -0.00010800
  2025-09-04     0.00005897   0.02827020    0.00005221

Berdasarkan contoh tersebut, terlihat bahwa tidak semua tanggal memiliki
nilai untuk setiap polutan. Kondisi ini menunjukkan adanya *missing
data* pada beberapa tanggal pengamatan.

Nilai `NULL` tidak menunjukkan bahwa konsentrasi polutan bernilai nol.
Nilai tersebut menunjukkan bahwa pada tanggal terkait tidak terdapat
nilai pengamatan yang tersedia pada dataset.

------------------------------------------------------------------------

## 6.3 Periode Pengamatan

Periode pengamatan dimulai pada:

``` text
31 Agustus 2025
```

dan berakhir pada:

``` text
31 Agustus 2026
```

Total terdapat:

``` text
366 tanggal kalender
```

Rentang tersebut mencakup satu tahun pengamatan dan tahun 2026 merupakan
tahun kabisat, sehingga terdapat 366 hari kalender.

Penggunaan seluruh tanggal dalam rentang pengamatan bertujuan untuk
mempertahankan urutan waktu secara lengkap. Dengan demikian, tanggal
yang tidak memiliki nilai polutan tetap dapat dikenali sebagai bagian
dari periode pengamatan.

Struktur tanggal yang lengkap juga membantu proses visualisasi karena
jarak waktu antar-pengamatan tetap merepresentasikan kondisi kalender
sebenarnya.

------------------------------------------------------------------------

## 6.4 Kelengkapan Data Time Series

Berdasarkan hasil pengolahan data, tidak seluruh tanggal mempunyai nilai
valid untuk ketiga polutan. Kondisi tersebut menyebabkan jumlah data
valid pada setiap polutan berbeda.

  Polutan     Data Valid   Missing   Persentase Missing
  --------- ------------ --------- --------------------
  NO₂                218       148               40,44%
  CO                 209       157               42,90%
  SO₂                262       104               28,42%

Dari tabel tersebut, **CO memiliki jumlah data valid paling sedikit**,
yaitu 209 data, sekaligus memiliki jumlah *missing data* paling banyak,
yaitu 157 data atau sekitar 42,90%.

Sebaliknya, **SO₂ memiliki jumlah data valid paling banyak**, yaitu 262
data, dengan *missing data* sebanyak 104 data atau sekitar 28,42%.

NO₂ memiliki 218 data valid dan 148 data *missing*, dengan persentase
*missing data* sebesar 40,44%.

Perbedaan kelengkapan data perlu diperhatikan dalam interpretasi grafik.
Pola yang terlihat pada satu polutan tidak selalu dapat dibandingkan
secara langsung dengan polutan lain karena jumlah titik pengamatan
validnya berbeda.

------------------------------------------------------------------------

## 6.5 Grafik Time Series NO₂

### 6.5.1 Visualisasi

Grafik *time series* NO₂ digunakan untuk melihat perubahan nilai
Nitrogen Dioksida dari tanggal ke tanggal selama periode pengamatan.

![Time Series NO₂ Kecamatan
Kalitengah](../data/timeseries_NO2_Kalitengah.png)

**Gambar 6.1. Grafik Time Series NO₂ Kecamatan Kalitengah**

### 6.5.2 Statistik Deskriptif

Nilai statistik utama NO₂ adalah sebagai berikut:

  Parameter                   Nilai
  -------------------- ------------
  Minimum                0.00000017
  Maximum                0.00012250
  Mean                   0.00004497
  Median                 0.00004283
  Standard deviation     0.00002479
  Skewness                    0.868

Berdasarkan tabel tersebut, nilai NO₂ memiliki nilai minimum sebesar
**0.00000017** dan nilai maksimum sebesar **0.00012250**. Rata-rata
nilai NO₂ dari seluruh data valid adalah **0.00004497**, sedangkan
median sebesar **0.00004283**.

Nilai rata-rata yang sedikit lebih besar daripada median menunjukkan
adanya pengaruh beberapa nilai yang relatif tinggi. Hal tersebut sejalan
dengan nilai **skewness sebesar 0.868**, yang menunjukkan bahwa
distribusi nilai NO₂ cenderung menceng ke kanan (*right-skewed*).

Pada grafik, perubahan nilai NO₂ dapat diamati berdasarkan posisi titik
atau garis terhadap tanggal pengamatan. Nilai yang berada lebih tinggi
menunjukkan periode dengan konsentrasi NO₂ yang relatif lebih besar,
sedangkan nilai yang lebih rendah menunjukkan periode dengan konsentrasi
relatif lebih kecil.

Bagian grafik yang tidak memiliki garis menunjukkan tanggal dengan nilai
NO₂ yang tidak tersedia.

------------------------------------------------------------------------

## 6.6 Grafik Time Series CO

### 6.6.1 Visualisasi

Grafik *time series* CO digunakan untuk melihat perubahan nilai Karbon
Monoksida selama periode pengamatan.

![Time Series CO Kecamatan
Kalitengah](../data/timeseries_CO_Kalitengah.png)

**Gambar 6.2. Grafik Time Series CO Kecamatan Kalitengah**

### 6.6.2 Statistik Deskriptif

Statistik utama CO adalah sebagai berikut:

  Parameter                 Nilai
  -------------------- ----------
  Minimum                0.016442
  Maximum                0.042702
  Mean                   0.029909
  Median                 0.029526
  Standard deviation     0.004086
  Skewness                  0.335

Nilai minimum CO sebesar **0.016442**, sedangkan nilai maksimum sebesar
**0.042702**. Rata-rata CO adalah **0.029909** dan median sebesar
**0.029526**.

Nilai skewness sebesar **0.335** menunjukkan bahwa distribusi CO
cenderung menceng ke kanan, tetapi tingkat kemencengannya relatif lebih
rendah dibandingkan NO₂.

Perubahan nilai CO dari waktu ke waktu dapat diamati melalui grafik.
Periode dengan nilai yang lebih tinggi menunjukkan adanya peningkatan
relatif terhadap tanggal lainnya, sedangkan periode dengan nilai yang
lebih rendah menunjukkan penurunan relatif.

CO mempunyai jumlah data *missing* paling banyak dibandingkan kedua
polutan lainnya. Oleh karena itu, terdapat lebih banyak bagian pada
grafik CO yang tidak mempunyai nilai pengamatan.

------------------------------------------------------------------------

## 6.7 Grafik Time Series SO₂

### 6.7.1 Visualisasi

Grafik *time series* SO₂ digunakan untuk melihat perubahan nilai Sulfur
Dioksida berdasarkan tanggal selama periode pengamatan.

![Time Series SO₂ Kecamatan
Kalitengah](../data/timeseries_SO2_Kalitengah.png)

**Gambar 6.3. Grafik Time Series SO₂ Kecamatan Kalitengah**

### 6.7.2 Statistik Deskriptif

Statistik utama SO₂ adalah sebagai berikut:

  Parameter                  Nilai
  -------------------- -----------
  Minimum                -0.000806
  Maximum                 0.000926
  Mean                    0.000057
  Median                  0.000043
  Standard deviation      0.000232
  Skewness                   0.143
  Kurtosis                   2.342

Nilai minimum SO₂ sebesar **-0.000806**, sedangkan nilai maksimum
sebesar **0.000926**. Rata-rata SO₂ adalah **0.000057** dan median
sebesar **0.000043**.

Nilai skewness sebesar **0.143** menunjukkan bahwa distribusi SO₂
relatif mendekati simetris dibandingkan dengan NO₂ dan CO.

SO₂ mempunyai nilai kurtosis sebesar **2.342**. Nilai tersebut
menunjukkan karakteristik keruncingan distribusi yang perlu diperhatikan
dalam analisis statistik. Interpretasi kurtosis perlu disesuaikan dengan
definisi yang digunakan pada perangkat atau metode statistik yang
menghasilkan nilai tersebut.

SO₂ memiliki jumlah data valid paling banyak sehingga kontinuitas
informasi pada grafik relatif lebih baik dibandingkan NO₂ dan CO.
Meskipun demikian, masih terdapat 104 tanggal yang tidak memiliki nilai
valid.

------------------------------------------------------------------------

## 6.8 Pola Perubahan Berdasarkan Waktu

Analisis *time series* digunakan untuk melihat bagaimana nilai polutan
berubah sepanjang periode pengamatan. Fokus analisis tidak hanya pada
nilai rata-rata, tetapi juga pada perubahan nilai dari satu tanggal ke
tanggal lainnya.

Beberapa aspek yang diamati dalam grafik meliputi:

1.  Perubahan nilai dari hari ke hari.
2.  Periode ketika nilai polutan relatif tinggi.
3.  Periode ketika nilai polutan relatif rendah.
4.  Tanggal yang tidak memiliki nilai pengamatan.
5.  Perubahan pola pada periode tertentu.
6.  Fluktuasi nilai selama periode pengamatan.

Berdasarkan grafik, perubahan nilai polutan dapat diamati secara
kronologis. Namun, interpretasi terhadap suatu kenaikan atau penurunan
harus dilakukan secara hati-hati karena adanya *missing data* pada
sejumlah tanggal.

Selain itu, analisis *time series* pada tahap ini bersifat
**deskriptif**. Oleh karena itu, perubahan nilai yang terjadi pada
grafik belum dapat digunakan untuk menyatakan bahwa suatu faktor
tertentu menyebabkan peningkatan atau penurunan konsentrasi polutan.

Untuk mengetahui faktor penyebab, diperlukan analisis lanjutan dengan
variabel pendukung seperti kondisi meteorologi, penggunaan lahan,
aktivitas transportasi, kepadatan penduduk, atau faktor lingkungan
lainnya.

------------------------------------------------------------------------

## 6.9 Missing Data pada Grafik

Pada grafik *time series*, beberapa bagian garis dapat terputus atau
tidak menampilkan nilai. Kondisi tersebut terjadi karena terdapat nilai
`NULL` pada tanggal tertentu.

Jumlah *missing data* masing-masing polutan adalah:

-   **NO₂ = 148 tanggal**
-   **CO = 157 tanggal**
-   **SO₂ = 104 tanggal**

Data kosong tidak langsung dihilangkan dari struktur tanggal. Tanggal
tetap dipertahankan agar periode pengamatan tetap mencakup seluruh
rentang **31 Agustus 2025 sampai 31 Agustus 2026**.

Pendekatan tersebut memiliki beberapa keuntungan. Pertama, urutan waktu
tetap sesuai dengan kondisi kalender sebenarnya. Kedua, tanggal tanpa
data dapat dibedakan dari tanggal yang memiliki nilai nol. Ketiga,
visualisasi dapat menunjukkan secara jelas adanya keterbatasan
ketersediaan data.

Dengan demikian, `NULL` pada grafik harus dipahami sebagai **tidak
tersedianya data**, bukan sebagai nilai konsentrasi nol.

------------------------------------------------------------------------

## 6.10 Perbandingan Time Series Ketiga Polutan

Ketiga polutan mempunyai tingkat kelengkapan data yang berbeda.

  Polutan     Data Valid   Missing   Persentase Missing         Mean
  --------- ------------ --------- -------------------- ------------
  NO₂                218       148               40,44%   0.00004497
  CO                 209       157               42,90%     0.029909
  SO₂                262       104               28,42%     0.000057

Berdasarkan kelengkapan data, **SO₂ merupakan polutan dengan data paling
lengkap**, sedangkan **CO merupakan polutan dengan data paling banyak
hilang**.

NO₂ berada di antara keduanya dalam hal jumlah data valid.

Nilai rata-rata ketiga polutan tidak dapat dibandingkan hanya
berdasarkan besar angka karena setiap polutan memiliki karakteristik dan
skala pengukuran yang berbeda. Oleh sebab itu, nilai mean lebih tepat
digunakan untuk memahami karakteristik masing-masing variabel secara
individual.

Perbandingan *time series* juga perlu memperhatikan jumlah titik data
yang tersedia. Polutan dengan data lebih lengkap dapat memberikan
gambaran temporal yang lebih kontinu, sedangkan polutan dengan *missing
data* lebih banyak akan memiliki lebih banyak bagian grafik yang
terputus.

------------------------------------------------------------------------

## 6.11 Hubungan Analisis Statistik dan Time Series

Statistika deskriptif dan analisis *time series* saling melengkapi dalam
memahami karakteristik dataset.

Statistika deskriptif memberikan informasi mengenai:

-   nilai minimum;
-   nilai maksimum;
-   nilai rata-rata;
-   median;
-   standar deviasi;
-   skewness;
-   kurtosis; dan
-   jumlah data *missing*.

Sementara itu, analisis *time series* menunjukkan bagaimana nilai
tersebut berubah berdasarkan waktu.

Sebagai contoh, nilai mean NO₂ sebesar **0.00004497** memberikan
gambaran mengenai rata-rata seluruh nilai NO₂ yang tersedia. Namun,
nilai tersebut tidak menunjukkan kapan nilai NO₂ berada pada kondisi
tinggi atau rendah.

Informasi mengenai perubahan berdasarkan tanggal dapat diperoleh melalui
grafik *time series*. Dengan melihat grafik tersebut, periode kenaikan,
penurunan, dan fluktuasi nilai dapat diamati secara kronologis.

Dengan menggabungkan statistik deskriptif dan *time series*, analisis
menjadi lebih informatif karena karakteristik umum data dapat dilihat
bersamaan dengan pola perubahan waktunya.

------------------------------------------------------------------------

## 6.12 Interpretasi Hasil Analisis

Berdasarkan hasil analisis, ketiga polutan mempunyai karakteristik
temporal dan statistik yang berbeda.

### 6.12.1 NO₂

NO₂ memiliki **218 data valid** dari total 366 tanggal pengamatan.
Rata-rata nilai NO₂ adalah **0.00004497**, dengan median **0.00004283**.

Nilai skewness sebesar **0.868** menunjukkan distribusi NO₂ cenderung
menceng ke kanan. Kondisi tersebut menunjukkan adanya beberapa nilai
yang relatif tinggi dibandingkan sebagian besar data.

Dalam konteks *time series*, nilai tersebut perlu dilihat kembali pada
tanggal terjadinya agar dapat diketahui apakah kenaikan tersebut terjadi
secara terisolasi atau membentuk pola tertentu.

### 6.12.2 CO

CO memiliki **209 data valid** dari total 366 tanggal pengamatan. Nilai
rata-ratanya adalah **0.029909**, dengan median **0.029526**.

CO mempunyai persentase *missing data* tertinggi, yaitu **42,90%**.
Kondisi ini menyebabkan kontinuitas grafik CO lebih rendah dibandingkan
SO₂.

Nilai skewness sebesar **0.335** menunjukkan distribusi CO cenderung
menceng ke kanan, tetapi kemencengannya lebih rendah dibandingkan NO₂.

### 6.12.3 SO₂

SO₂ memiliki **262 data valid**, sehingga merupakan polutan dengan
jumlah data valid paling banyak.

Rata-rata nilai SO₂ adalah **0.000057**, dengan median **0.000043**.
Nilai skewness sebesar **0.143** menunjukkan distribusi yang relatif
mendekati simetris.

SO₂ juga memiliki jumlah *missing data* paling sedikit, yaitu **104
tanggal** atau sekitar **28,42%**. Oleh karena itu, pola perubahan SO₂
dari waktu ke waktu dapat diamati dengan tingkat kelengkapan yang
relatif lebih baik dibandingkan NO₂ dan CO.

------------------------------------------------------------------------

## 6.13 Keterbatasan Analisis

Hasil analisis *time series* pada penelitian ini memiliki beberapa
keterbatasan yang perlu diperhatikan.

Pertama, terdapat *missing data* yang cukup besar pada seluruh polutan.
Persentase *missing data* mencapai lebih dari 28% pada SO₂ dan lebih
dari 40% pada NO₂ serta CO. Kondisi tersebut dapat memengaruhi
kontinuitas pola yang terlihat pada grafik.

Kedua, analisis yang dilakukan masih bersifat deskriptif. Analisis ini
belum mencakup metode statistik *time series* seperti uji stasioneritas,
dekomposisi tren dan musiman, analisis autokorelasi, maupun pemodelan
prediktif.

Ketiga, nilai ketiga polutan mempunyai skala yang berbeda sehingga
perbandingan langsung berdasarkan tinggi rendahnya angka tidak tepat
dilakukan.

Keempat, hasil analisis tidak dapat digunakan untuk menyimpulkan
hubungan sebab-akibat. Kenaikan atau penurunan nilai polutan pada
periode tertentu belum dapat dikaitkan secara langsung dengan faktor
lingkungan tertentu tanpa analisis tambahan.

------------------------------------------------------------------------

## 6.14 Hasil Analisis Time Series

Berdasarkan hasil pengolahan dan visualisasi, diperoleh beberapa hasil
utama sebagai berikut:

1.  Dataset mempunyai **366 tanggal kalender** dalam periode 31 Agustus
    2025 sampai 31 Agustus 2026.
2.  NO₂ mempunyai **218 data valid** dan **148 data missing** atau
    sekitar **40,44%**.
3.  CO mempunyai **209 data valid** dan **157 data missing** atau
    sekitar **42,90%**.
4.  SO₂ mempunyai **262 data valid** dan **104 data missing** atau
    sekitar **28,42%**.
5.  SO₂ merupakan polutan dengan data valid paling banyak dan persentase
    *missing data* paling rendah.
6.  CO merupakan polutan dengan jumlah *missing data* paling banyak.
7.  NO₂ mempunyai skewness **0.868**, yang menunjukkan distribusi
    cenderung menceng ke kanan.
8.  CO mempunyai skewness **0.335**, yang menunjukkan kecenderungan
    menceng ke kanan dengan tingkat lebih rendah dibandingkan NO₂.
9.  SO₂ mempunyai skewness **0.143**, sehingga distribusinya relatif
    lebih mendekati simetris.
10. Perbedaan nilai rata-rata ketiga polutan tidak dapat digunakan
    sebagai dasar perbandingan langsung karena skala masing-masing
    variabel berbeda.
11. Nilai `NULL` dipertahankan dalam struktur tanggal agar urutan waktu
    tidak berubah dan tanggal tanpa data tetap dapat diidentifikasi.
12. Analisis *time series* pada tahap ini bersifat deskriptif dan belum
    digunakan untuk menentukan hubungan sebab-akibat maupun melakukan
    prediksi.

------------------------------------------------------------------------

## 6.15 Kesimpulan

Analisis *time series* dilakukan untuk mengetahui perubahan nilai
polutan NO₂, CO, dan SO₂ berdasarkan waktu selama periode **31 Agustus
2025 sampai 31 Agustus 2026**. Dataset terdiri atas **366 tanggal
kalender**, dengan jumlah data valid yang berbeda pada setiap polutan.

NO₂ memiliki **218 data valid**, CO memiliki **209 data valid**,
sedangkan SO₂ memiliki **262 data valid**. Dengan demikian, SO₂
mempunyai tingkat kelengkapan data paling baik, sedangkan CO mempunyai
jumlah *missing data* paling tinggi.

Hasil statistik menunjukkan bahwa NO₂ mempunyai mean **0.00004497** dan
skewness **0.868**, CO mempunyai mean **0.029909** dan skewness
**0.335**, sedangkan SO₂ mempunyai mean **0.000057** dan skewness
**0.143**. Perbedaan karakteristik tersebut menunjukkan bahwa
masing-masing polutan mempunyai distribusi data yang berbeda.

Visualisasi *time series* memungkinkan perubahan nilai polutan diamati
berdasarkan tanggal, termasuk periode dengan nilai relatif tinggi, nilai
relatif rendah, dan tanggal yang tidak memiliki data. Nilai `NULL` tetap
dipertahankan sehingga struktur waktu tidak berubah dan *missing data*
dapat terlihat pada grafik.

Secara keseluruhan, analisis pada tahap ini memberikan gambaran awal
mengenai karakteristik temporal data polutan di Kecamatan Kalitengah.
Hasil tersebut dapat menjadi dasar untuk tahap analisis berikutnya,
seperti pembersihan dan penanganan *missing data*, analisis tren,
pengujian pola musiman, analisis korelasi temporal, maupun pemodelan
*time series* untuk kebutuhan prediksi.

Dengan demikian, proses **Week 2** telah mencakup pemindahan data ke
**PostgreSQL Aiven**, pengolahan data menggunakan **KNIME**, analisis
statistika deskriptif, serta visualisasi dan analisis *time series*
untuk polutan NO₂, CO, dan SO₂.
