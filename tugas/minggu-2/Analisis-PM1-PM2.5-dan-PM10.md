# 5. Analisis PM1, PM2.5, dan PM10

## 5.1 Pendahuluan

**Particulate Matter (PM)** adalah istilah yang digunakan untuk partikel
padat atau cair yang tersuspensi di udara. Dalam analisis kualitas
udara, ukuran partikel menjadi salah satu karakteristik penting karena
ukuran memengaruhi perilaku partikel di atmosfer dan kemampuan partikel
untuk masuk ke saluran pernapasan.

Tiga variabel yang sering dianalisis adalah:

-   **PM1** --- partikel dengan diameter aerodinamis sekitar 1 µm atau
    lebih kecil;
-   **PM2.5** --- partikel halus dengan diameter aerodinamis sekitar 2.5
    µm atau lebih kecil;
-   **PM10** --- partikel inhalabel dengan diameter aerodinamis sekitar
    10 µm atau lebih kecil.

Dalam dataset KNIME pada materi ini, nama kolom yang terlihat antara
lain:

``` text
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Suffix:

``` text
_ug_m3
```

mengindikasikan satuan konsentrasi **µg/m³ (mikrogram per meter
kubik)**.

Analisis PM1, PM2.5, dan PM10 penting untuk:

1.  memahami tingkat konsentrasi partikulat;
2.  membandingkan karakteristik ketiga ukuran partikel;
3.  melihat variasi dan distribusi data;
4.  mendeteksi nilai ekstrem;
5.  memahami hubungan antarvariabel;
6.  menjadi dasar visualisasi dan analisis lanjutan.

> **Catatan:** nilai ambang kualitas udara dan klasifikasi "baik",
> "sedang", "tidak sehat", dan sebagainya bergantung pada
> standar/regulasi, lokasi, periode averaging, dan tujuan analisis.
> Jangan menggunakan satu threshold universal tanpa menyebutkan standar
> yang menjadi acuan.

------------------------------------------------------------------------

# 5.2 Apa Itu PM?

PM adalah campuran partikel yang berada di udara dalam bentuk padat
maupun cair.

Sumber PM dapat berasal dari:

-   emisi kendaraan;
-   pembakaran;
-   aktivitas industri;
-   konstruksi;
-   debu jalan;
-   kebakaran;
-   proses alam;
-   reaksi kimia di atmosfer.

Ukuran partikel biasanya dinyatakan dalam mikrometer (µm).

Perbandingan sederhana:

``` text
PM1       ≤ sekitar 1 µm
PM2.5     ≤ sekitar 2.5 µm
PM10      ≤ sekitar 10 µm
```

Semakin kecil ukuran partikelnya, semakin kecil diameter partikelnya dan
secara umum semakin mudah partikel tersebut masuk lebih jauh ke saluran
pernapasan.

------------------------------------------------------------------------

# 5.3 Perbedaan PM1, PM2.5, dan PM10

Secara konseptual:

``` text
PM10
├── PM2.5
│   └── PM1
```

Namun, hubungan ini perlu dipahami dengan hati-hati.

PM2.5 merupakan bagian dari fraksi PM10 berdasarkan ukuran aerodinamis,
dan PM1 merupakan fraksi yang lebih kecil. Tetapi **nilai pengukuran
sensor untuk masing-masing kanal tidak selalu memenuhi hubungan numerik
sederhana secara sempurna**, karena:

-   definisi instrumen dapat berbeda;
-   sensor memiliki karakteristik pengukuran sendiri;
-   pembacaan dapat dipengaruhi kelembapan;
-   proses sampling dan kalibrasi berbeda;
-   data dapat memiliki noise.

Secara fisik, jika ketiga variabel merepresentasikan fraksi massa yang
konsisten, nilai konsentrasi kumulatif dengan cutoff yang lebih besar
umumnya tidak lebih kecil daripada fraksi yang lebih sempit. Tetapi
output sensor perlu diperiksa sebelum memberlakukan constraint matematis
tertentu.

------------------------------------------------------------------------

# 5.4 PM1

## Definisi

PM1 adalah fraksi partikulat dengan diameter aerodinamis sekitar **1 µm
atau lebih kecil**.

Karena ukurannya sangat kecil, PM1 termasuk partikel halus.

Sumber PM1 dapat mencakup:

-   pembakaran;
-   emisi kendaraan;
-   proses industri;
-   aerosol sekunder;
-   aktivitas pembakaran biomassa.

## Karakteristik

PM1 cenderung berkaitan dengan partikel yang sangat halus dan dapat
menjadi indikator penting untuk mempelajari aerosol halus.

Namun, PM1 tidak selalu tersedia pada semua dataset atau semua stasiun
pemantauan.

------------------------------------------------------------------------

# 5.5 PM2.5

## Definisi

PM2.5 adalah partikel dengan diameter aerodinamis sekitar **2.5 µm atau
lebih kecil**.

PM2.5 banyak digunakan dalam analisis kualitas udara karena merupakan
salah satu indikator penting polusi partikulat halus.

Sumber PM2.5 dapat berasal dari:

-   kendaraan;
-   pembakaran bahan bakar;
-   pembakaran biomassa;
-   aktivitas industri;
-   pembentukan aerosol sekunder;
-   kebakaran.

## Mengapa PM2.5 Penting?

Ukuran yang kecil membuat PM2.5 dapat masuk lebih jauh ke dalam sistem
pernapasan dibandingkan partikel yang lebih besar.

Dalam analisis data, PM2.5 dapat digunakan untuk:

-   pemantauan kualitas udara;
-   analisis tren waktu;
-   perbandingan antar lokasi;
-   analisis korelasi dengan PM10;
-   deteksi episode polusi;
-   pemodelan kualitas udara.

------------------------------------------------------------------------

# 5.6 PM10

## Definisi

PM10 merupakan partikulat dengan diameter aerodinamis sekitar **10 µm
atau lebih kecil**.

PM10 dapat berasal dari:

-   debu;
-   aktivitas konstruksi;
-   debu jalan;
-   tanah;
-   kendaraan;
-   industri;
-   pembakaran.

Karena cutoff-nya lebih besar dibanding PM2.5, PM10 mencakup fraksi
partikel yang lebih luas.

------------------------------------------------------------------------

# 5.7 Satuan PM

Pada dataset:

``` text
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

satuan yang digunakan adalah:

\[ `\mu `{=tex}g/m\^3 \]

dibaca:

> mikrogram per meter kubik.

Artinya, konsentrasi menunjukkan jumlah massa partikulat dalam volume
udara tertentu.

Contoh:

``` text
PM2.5 = 50 µg/m³
```

berarti terdapat konsentrasi partikulat PM2.5 sebesar 50 mikrogram per
meter kubik udara pada kondisi pengukuran tersebut.

------------------------------------------------------------------------

# 5.8 Analisis Statistics Node pada PM

Dari contoh output **Statistics Node** pada workflow, diperoleh
ringkasan:

  Variabel        Min       Max     Mean   Std. deviation   Variance   Skewness
  ---------- -------- --------- -------- ---------------- ---------- ----------
  PM1            8.04   193.528   57.529           33.979   1,154.57      0.967
  PM2.5        10.248   204.640   62.028           35.869   1,286.60      0.968
  PM10         10.407   207.295   63.610           36.421   1,326.47      0.958

Nilai tersebut merupakan contoh hasil yang terlihat pada screenshot
workflow.

------------------------------------------------------------------------

# 5.9 Analisis PM1

Berdasarkan output:

``` text
Min       = 8.04
Max       = 193.528
Mean      = 57.529
Std Dev   = 33.979
Variance  = 1,154.57
Skewness  = 0.967
```

## 5.9.1 Rentang

\[ Range = Max-Min \]

\[ Range = 193.528-8.04 \]

\[ Range=185.488 \]

Jadi rentang PM1 sekitar:

\[ `\boxed{185.488\ \mu g/m^3}`{=tex} \]

Rentang yang besar menunjukkan bahwa konsentrasi PM1 pada data memiliki
variasi yang cukup luas.

## 5.9.2 Mean

Mean:

\[ `\bar`{=tex}{x}=57.529 \]

Artinya, rata-rata konsentrasi PM1 pada data contoh sekitar:

``` text
57.529 µg/m³
```

## 5.9.3 Standard Deviation

Standard deviation:

\[ s`\approx33.979`{=tex} \]

Nilai ini menunjukkan adanya penyebaran yang cukup besar dari rata-rata.

## 5.9.4 Skewness

Skewness:

\[ 0.967 \]

bernilai positif.

Interpretasi awal:

> Distribusi PM1 cenderung **positively skewed/right-skewed**.

Artinya, terdapat kecenderungan ekor distribusi ke arah nilai PM1 yang
lebih tinggi.

------------------------------------------------------------------------

# 5.10 Analisis PM2.5

Berdasarkan output:

``` text
Min       = 10.248
Max       = 204.640
Mean      = 62.028
Std Dev   = 35.869
Variance  = 1,286.60
Skewness  = 0.968
```

## 5.10.1 Range

\[ Range=204.640-10.248 \]

\[ Range=194.392 \]

Jadi rentangnya:

\[ `\boxed{194.392\ \mu g/m^3}`{=tex} \]

## 5.10.2 Mean

\[ Mean=62.028 `\mu `{=tex}g/m\^3 \]

Ini merupakan rata-rata konsentrasi PM2.5 pada data contoh.

## 5.10.3 Standard Deviation

\[ Std. deviation=35.869 \]

Penyebaran PM2.5 cukup besar dibandingkan rata-ratanya.

## 5.10.4 Skewness

\[ Skewness=0.968 \]

Distribusi cenderung positif skewed.

Hal ini mengindikasikan bahwa sejumlah observasi dengan konsentrasi
lebih tinggi dapat menarik distribusi ke arah kanan.

------------------------------------------------------------------------

# 5.11 Analisis PM10

Berdasarkan output:

``` text
Min       = 10.407
Max       = 207.295
Mean      = 63.610
Std Dev   = 36.421
Variance  = 1,326.47
Skewness  = 0.958
```

## 5.11.1 Range

\[ Range=207.295-10.407 \]

\[ Range=196.888 \]

Jadi:

\[ `\boxed{Range=196.888\ \mu g/m^3}`{=tex} \]

## 5.11.2 Mean

\[ Mean=63.610 `\mu `{=tex}g/m\^3 \]

## 5.11.3 Standard Deviation

\[ Std. deviation=36.421 \]

Nilai ini menunjukkan penyebaran yang cukup besar.

## 5.11.4 Skewness

\[ Skewness=0.958 \]

Distribusi PM10 juga cenderung positif skewed.

------------------------------------------------------------------------

# 5.12 Perbandingan PM1, PM2.5, dan PM10

Berdasarkan statistik deskriptif:

  Statistik               PM1      PM2.5       PM10
  ---------------- ---------- ---------- ----------
  Minimum                8.04     10.248     10.407
  Maximum             193.528    204.640    207.295
  Mean                 57.529     62.028     63.610
  Std. deviation       33.979     35.869     36.421
  Variance           1,154.57   1,286.60   1,326.47
  Skewness              0.967      0.968      0.958

## Kesimpulan awal

Dari angka tersebut:

1.  **PM10 memiliki mean tertinggi**.
2.  **PM10 memiliki standard deviation tertinggi**.
3.  **PM10 memiliki variance tertinggi**.
4.  PM2.5 dan PM10 memiliki skewness yang sangat mirip.
5.  Ketiga variabel memiliki skewness positif.
6.  Ketiganya menunjukkan variasi yang cukup besar.

Namun, perbedaan angka tidak boleh langsung diartikan sebagai perbedaan
tingkat bahaya karena ketiga variabel mewakili fraksi ukuran partikel
yang berbeda.

------------------------------------------------------------------------

# 5.13 Membandingkan Mean

Mean:

``` text
PM1    = 57.529
PM2.5  = 62.028
PM10   = 63.610
```

Urutan mean:

\[ PM10 \> PM2.5 \> PM1 \]

Dengan demikian, berdasarkan dataset contoh, konsentrasi rata-rata yang
tercatat adalah:

``` text
PM10  → tertinggi
PM2.5 → menengah
PM1   → terendah
```

Jika ketiga kanal sensor memang mengukur fraksi massa yang konsisten,
pola tersebut secara umum masuk akal karena cutoff PM10 mencakup fraksi
yang lebih luas. Namun, validasi karakteristik sensor tetap diperlukan.

------------------------------------------------------------------------

# 5.14 Membandingkan Maximum

Nilai maksimum:

``` text
PM1    = 193.528
PM2.5  = 204.640
PM10   = 207.295
```

Urutannya:

\[ PM10 \> PM2.5 \> PM1 \]

PM10 memiliki nilai maksimum paling tinggi pada data contoh.

Hal ini menunjukkan bahwa episode konsentrasi partikulat tertinggi pada
kanal PM10 mencapai sekitar:

``` text
207.295 µg/m³
```

------------------------------------------------------------------------

# 5.15 Membandingkan Standard Deviation

Standard deviation:

``` text
PM1    = 33.979
PM2.5  = 35.869
PM10   = 36.421
```

Urutan:

\[ PM10 \> PM2.5 \> PM1 \]

PM10 memiliki penyebaran absolut terbesar.

Namun, untuk membandingkan **variabilitas relatif**, standard deviation
saja belum cukup. Gunakan coefficient of variation.

------------------------------------------------------------------------

# 5.16 Coefficient of Variation PM

Rumus:

\[ CV=`\frac{Std.Dev}{Mean}`{=tex}`\times100`{=tex}% \]

## PM1

\[ CV\_{PM1} = `\frac{33.979}{57.529}`{=tex}`\times100`{=tex}% \]

\[ CV\_{PM1}`\approx59.06`{=tex}% \]

## PM2.5

\[ CV\_{PM2.5} = `\frac{35.869}{62.028}`{=tex}`\times100`{=tex}% \]

\[ CV\_{PM2.5}`\approx57.83`{=tex}% \]

## PM10

\[ CV\_{PM10} = `\frac{36.421}{63.610}`{=tex}`\times100`{=tex}% \]

\[ CV\_{PM10}`\approx57.26`{=tex}% \]

Ringkasan:

  Variabel       Mean   Std. Dev.        CV
  ---------- -------- ----------- ---------
  PM1          57.529      33.979   ≈59.06%
  PM2.5        62.028      35.869   ≈57.83%
  PM10         63.610      36.421   ≈57.26%

Interpretasi:

-   PM1 memiliki variasi relatif paling tinggi;
-   PM10 memiliki variasi absolut paling tinggi;
-   perbedaan CV ketiganya relatif kecil.

------------------------------------------------------------------------

# 5.17 Skewness Ketiga Variabel

Nilai:

``` text
PM1    = 0.967
PM2.5  = 0.968
PM10   = 0.958
```

Ketiganya:

``` text
> 0
```

sehingga distribusi cenderung right-skewed.

PM2.5 memiliki skewness sedikit lebih tinggi pada contoh:

\[ 0.968 \]

sedangkan PM10:

\[ 0.958 \]

Perbedaannya kecil.

### Interpretasi penting

Jangan menyimpulkan bahwa PM2.5 "jauh lebih skewed" daripada PM10 hanya
karena perbedaan:

``` text
0.968 - 0.958 = 0.010
```

Perbedaan ini sangat kecil dan perlu dipertimbangkan bersama ukuran
sampel dan distribusi sebenarnya.

------------------------------------------------------------------------

# 5.18 Hubungan PM1 → PM2.5 → PM10

Secara konseptual, ketiga variabel memiliki hubungan berdasarkan ukuran
partikel.

``` text
PM1
 ↓
bagian partikel sangat halus

PM2.5
 ↓
fraksi yang lebih luas

PM10
 ↓
fraksi yang lebih luas lagi
```

Karena itu, pada data yang benar-benar merepresentasikan massa kumulatif
berdasarkan cutoff ukuran, diharapkan terdapat hubungan positif yang
kuat.

Tetapi hubungan tersebut **harus diuji dari data**, bukan hanya
diasumsikan.

------------------------------------------------------------------------

# 5.19 Korelasi PM1, PM2.5, dan PM10

Salah satu cara menguji hubungan adalah menggunakan korelasi.

Korelasi Pearson:

\[ r= `\frac{
\sum(x_i-\bar{x})(y_i-\bar{y})
}{
\sqrt{
\sum(x_i-\bar{x})^2
\sum(y_i-\bar{y})^2
}
}`{=tex} \]

Nilai (r) berada antara:

\[ -1`\le `{=tex}r`\le1`{=tex} \]

Interpretasi umum:

               r Interpretasi
  -------------- ---------------------------------
    mendekati +1 hubungan linear positif kuat
     mendekati 0 hubungan linear lemah/tidak ada
    mendekati -1 hubungan linear negatif kuat

Contoh:

``` text
r(PM2.5, PM10) = 0.95
```

menunjukkan hubungan linear positif yang sangat kuat.

Namun, korelasi **tidak sama dengan sebab-akibat**.

------------------------------------------------------------------------

# 5.20 Mengapa PM2.5 dan PM10 Bisa Berkorelasi?

Konsentrasi PM2.5 dan PM10 dapat meningkat bersamaan karena keduanya
dipengaruhi oleh kondisi lingkungan yang sama.

Contohnya:

-   aktivitas lalu lintas;
-   pembakaran;
-   kondisi meteorologi;
-   sumber emisi lokal;
-   kebakaran.

Ketika terjadi episode polusi partikulat, beberapa fraksi ukuran
partikel dapat meningkat secara bersamaan.

------------------------------------------------------------------------

# 5.21 Scatter Plot PM2.5 vs PM10

Untuk memeriksa hubungan secara visual, gunakan scatter plot.

Konsep:

``` text
PM10
 ^
 |                    *
 |                *
 |             *
 |         *
 |      *
 |   *
 +--------------------------> PM2.5
```

Jika titik-titik cenderung membentuk garis naik, terdapat indikasi
hubungan positif.

Dalam KNIME, scatter plot dapat digunakan untuk:

``` text
X-axis = PM2.5
Y-axis = PM10
```

Kemudian tambahkan scatter plot untuk:

``` text
PM1 vs PM2.5
PM1 vs PM10
PM2.5 vs PM10
```

------------------------------------------------------------------------

# 5.22 Time Series PM

Karena dataset kualitas udara biasanya memiliki timestamp, analisis
tidak hanya dilakukan berdasarkan distribusi keseluruhan.

Pertanyaan penting:

> Bagaimana PM berubah terhadap waktu?

Contoh:

``` text
PM2.5
 ^
 |        /\          /\
 |       /  \        /  \
 |  /\  /    \  /\  /    \
 |_/  \/      \/  \/      \__
 +----------------------------> waktu
```

Time series dapat menunjukkan:

-   jam dengan konsentrasi tinggi;
-   pola harian;
-   tren;
-   episode polusi;
-   perubahan musiman;
-   hubungan dengan aktivitas manusia.

------------------------------------------------------------------------

# 5.23 Pola Harian

Jika timestamp tersedia, data dapat dikelompokkan berdasarkan jam.

Contoh:

``` text
00:00
01:00
02:00
...
23:00
```

Kemudian hitung:

``` text
Mean PM2.5 per jam
```

Hasil dapat digunakan untuk mencari pola seperti:

``` text
pagi       → tinggi
siang      → menurun
sore       → meningkat
malam      → menurun
```

Pola tersebut hanya contoh. Jangan menganggap pola tertentu sebagai
fakta sebelum dihitung dari dataset.

------------------------------------------------------------------------

# 5.24 Moving Average

Untuk mengurangi noise pada time series, dapat digunakan moving average.

Contoh moving average 3 periode:

\[ MA_t = `\frac{x_t+x_{t-1}+x_{t-2}}{3}`{=tex} \]

Misalkan:

``` text
t-2 = 20
t-1 = 30
t   = 40
```

maka:

\[ MA_t=`\frac{20+30+40}{3}`{=tex} \]

\[ MA_t=30 \]

Moving average membantu melihat tren umum, tetapi dapat menghaluskan
lonjakan penting.

------------------------------------------------------------------------

# 5.25 Analisis Outlier PM

Nilai maksimum yang jauh lebih tinggi daripada mean dapat menjadi
kandidat outlier.

Contoh PM2.5:

``` text
Mean = 62.028
Max  = 204.640
```

Perbedaan:

\[ 204.640-62.028=142.612 \]

Nilai maksimum cukup jauh dari rata-rata.

Namun, nilai tersebut tidak boleh langsung dihapus.

## Pemeriksaan yang disarankan

Periksa:

1.  timestamp;
2.  sensor;
3.  lokasi;
4.  nilai PM1 dan PM10 pada timestamp yang sama;
5.  kelembapan;
6.  temperatur;
7.  kondisi lingkungan;
8.  data mentah/sumber sensor.

Jika PM2.5, PM10, dan variabel lain semuanya meningkat pada waktu yang
sama, lonjakan tersebut mungkin merupakan kejadian nyata.

------------------------------------------------------------------------

# 5.26 Validasi Outlier dengan Variabel Lain

Misalnya pada satu timestamp:

  Variabel     Nilai
  ---------- -------
  PM1            180
  PM2.5          195
  PM10           205

Jika ketiga kanal meningkat bersamaan, lebih masuk akal untuk
menganggapnya sebagai **episode partikulat tinggi yang perlu
diverifikasi**, bukan langsung sebagai kesalahan PM2.5.

Sebaliknya, jika:

  Variabel     Nilai
  ---------- -------
  PM1             20
  PM2.5          200
  PM10            25

maka data tersebut lebih patut diperiksa karena hubungan antarfraksi
terlihat tidak biasa.

Tetapi keputusan akhir tetap bergantung pada karakteristik instrumen dan
kualitas data.

------------------------------------------------------------------------

# 5.27 Pemeriksaan Konsistensi Antar-PM

Dalam dataset partikulat, kita dapat membuat beberapa pemeriksaan
kualitas data.

Contoh aturan pemeriksaan:

``` text
PM1 <= PM2.5
PM2.5 <= PM10
```

Aturan ini dapat digunakan sebagai **quality-control check** jika ketiga
kolom memang memiliki definisi fraksi massa kumulatif yang konsisten.

Jangan menerapkan aturan ini secara otomatis pada semua dataset tanpa
memeriksa dokumentasi sensor, karena metode pengukuran dapat berbeda.

------------------------------------------------------------------------

# 5.28 Contoh Rule Engine untuk QC

Jika aturan konsistensi sesuai dengan definisi dataset, dapat dibuat
aturan konseptual:

``` text
PM1 <= PM2.5 AND PM2.5 <= PM10
    → Valid

Selain itu
    → Check
```

Di KNIME, pemeriksaan semacam ini dapat dilakukan menggunakan:

-   Rule Engine;
-   Rule-based Row Filter;
-   Column Expressions;
-   atau node lain yang sesuai.

Contoh output:

    PM1   PM2.5   PM10 QC
  ----- ------- ------ -------
     20      30     40 Valid
     50      45     60 Check
     30      50     45 Check

------------------------------------------------------------------------

# 5.29 Histogram PM

Histogram digunakan untuk melihat distribusi.

Contoh konsep:

``` text
Frekuensi
 ^
 |        ███
 |       █████
 |     ███████
 |   █████████
 | ███████████
 +--------------------> PM2.5
```

Histogram dapat membantu melihat:

-   pusat distribusi;
-   penyebaran;
-   skewness;
-   beberapa puncak distribusi;
-   nilai ekstrem.

Karena ketiga variabel memiliki skewness positif pada contoh, histogram
kemungkinan menunjukkan ekor ke arah nilai tinggi.

------------------------------------------------------------------------

# 5.30 Box Plot PM

Box plot dapat digunakan untuk membandingkan distribusi PM1, PM2.5, dan
PM10.

Komponen:

``` text
Maximum
   |
   |
 ┌─────┐
 │     │
 ├─────┤ ← Median
 │     │
 └─────┘
   |
   |
Minimum
```

Box plot dapat membantu melihat:

-   median;
-   Q1;
-   Q3;
-   IQR;
-   outlier.

Jika beberapa box plot diletakkan berdampingan, perbandingan distribusi
menjadi lebih mudah.

------------------------------------------------------------------------

# 5.31 Contoh Interpretasi Box Plot

Misalnya hasil menunjukkan:

``` text
PM1    → median lebih rendah
PM2.5  → median lebih tinggi
PM10   → median paling tinggi
```

Interpretasinya:

> Pada dataset tersebut, pusat distribusi PM10 lebih tinggi daripada
> PM2.5 dan PM1.

Namun, interpretasi harus menggunakan nilai aktual hasil analisis, bukan
hanya bentuk grafik.

------------------------------------------------------------------------

# 5.32 Mean, Median, dan Skewness

Ketiga ukuran dapat digunakan bersama.

Contoh pola:

``` text
Mean > Median
Skewness > 0
```

Hal ini konsisten dengan distribusi yang cenderung right-skewed.

Pada data contoh:

``` text
PM1    → skewness ≈ 0.967
PM2.5  → skewness ≈ 0.968
PM10   → skewness ≈ 0.958
```

Semua positif.

Jika median dihitung, bandingkan:

``` text
Mean vs Median
```

untuk mendapatkan gambaran tambahan tentang pusat distribusi.

------------------------------------------------------------------------

# 5.33 Mengapa Tidak Cukup Menggunakan Mean?

Misalkan:

``` text
PM2.5:
Mean = 62.028
```

Angka tersebut tidak memberi tahu:

-   apakah sebagian besar data berada dekat 62;
-   apakah ada banyak nilai sangat rendah;
-   apakah terdapat nilai sangat tinggi;
-   apakah distribusi simetris;
-   apakah terdapat beberapa kelompok data.

Karena itu, analisis perlu dilengkapi dengan:

``` text
Median
Std. deviation
Quartile
IQR
Skewness
Histogram
Box plot
Time series
```

------------------------------------------------------------------------

# 5.34 Analisis Perbandingan dengan Range

Range:

  Variabel       Range
  ---------- ---------
  PM1          185.488
  PM2.5        194.392
  PM10         196.888

Urutan:

\[ PM10 \> PM2.5 \> PM1 \]

PM10 mempunyai rentang paling besar pada data contoh.

------------------------------------------------------------------------

# 5.35 Analisis Variance

Variance:

``` text
PM1    = 1,154.57
PM2.5  = 1,286.60
PM10   = 1,326.47
```

Urutan:

\[ PM10 \> PM2.5 \> PM1 \]

Variance terbesar terdapat pada PM10.

Karena variance menggunakan kuadrat satuan, standard deviation biasanya
lebih mudah digunakan untuk interpretasi langsung.

------------------------------------------------------------------------

# 5.36 Membandingkan Variabilitas Absolut dan Relatif

Penting membedakan:

### Variabilitas absolut

Gunakan:

``` text
Standard deviation
Variance
Range
```

### Variabilitas relatif

Gunakan:

``` text
Coefficient of Variation
```

Dalam contoh:

``` text
PM10
→ Std Dev tertinggi
→ Variance tertinggi

PM1
→ CV tertinggi
```

Artinya PM10 memiliki penyebaran absolut terbesar, tetapi PM1 memiliki
penyebaran relatif terhadap mean yang sedikit lebih tinggi.

------------------------------------------------------------------------

# 5.37 Contoh Pertanyaan Analisis

Setelah Statistics Node dijalankan, gunakan pertanyaan berikut:

### Pertanyaan 1

> Variabel PM mana yang memiliki mean paling tinggi?

Jawaban dari contoh:

``` text
PM10
```

### Pertanyaan 2

> Variabel mana yang memiliki standard deviation terbesar?

``` text
PM10
```

### Pertanyaan 3

> Apakah distribusi PM cenderung simetris?

Tidak sepenuhnya. Ketiganya memiliki skewness positif.

### Pertanyaan 4

> Apakah terdapat indikasi nilai ekstrem?

Ya, rentang yang luas dan skewness positif menunjukkan perlunya
pemeriksaan lebih lanjut terhadap nilai tinggi.

### Pertanyaan 5

> Apakah PM2.5 dan PM10 berhubungan?

Kemungkinan memiliki hubungan positif, tetapi perlu diuji menggunakan
korelasi dan scatter plot.

------------------------------------------------------------------------

# 5.38 Workflow KNIME yang Disarankan

Contoh workflow:

``` text
                    +-------------+
                    |  CSV Reader |
                    +------+------+
                           |
                           v
                    +-------------+
                    | Data Cleaner|
                    +------+------+
                           |
                           v
                    +-------------+
                    |  Statistics |
                    +------+------+
                           |
            +--------------+--------------+
            |              |              |
            v              v              v
       Statistics      Histogram     Occurrences
         Table
            |
            v
      +-------------+
      |  Filtering  |
      +------+------+
             |
             v
      +-------------+
      | Correlation |
      +------+------+
             |
             v
      +-------------+
      | Visualization|
      +-------------+
```

------------------------------------------------------------------------

# 5.39 Node yang Dapat Digunakan untuk Analisis PM

Beberapa node KNIME yang dapat mendukung analisis:

  Kebutuhan               Node/pendekatan
  ----------------------- ---------------------------------------------
  Statistik deskriptif    Statistics
  Visualisasi statistik   Statistics View
  Distribusi              Histogram / visualization
  Korelasi                Linear Correlation / Correlation tools
  Filter baris            Row Filter
  Validasi aturan         Rule Engine
  Perhitungan kolom       Math Formula / Column Expressions
  Time series             Date&Time + visualization/time-series nodes
  Missing value           Missing Value
  Outlier                 Rule Engine / statistik / visualisasi
  Scatter plot            Scatter Plot / visualization
  Box plot                Box Plot / visualization

Nama node dapat berbeda menurut versi KNIME dan extension yang
terpasang.

------------------------------------------------------------------------

# 5.40 Contoh Perhitungan Range dengan KNIME

Jika kolom:

``` text
pm2p5_ug_m3
```

memiliki:

``` text
Min = 10.248
Max = 204.640
```

maka:

\[ Range=204.640-10.248 \]

\[ Range=194.392 \]

Jika ingin membuat kolom range menggunakan KNIME, konsepnya adalah:

``` text
Max - Min
```

Untuk statistik keseluruhan kolom, nilai Min dan Max biasanya berasal
dari output Statistics dan bukan dihitung per baris.

------------------------------------------------------------------------

# 5.41 Contoh Perhitungan CV

Untuk PM10:

``` text
Mean = 63.610
Std Dev = 36.421
```

\[ CV= `\frac{36.421}{63.610}`{=tex}`\times100`{=tex}% \]

\[ CV`\approx57.26`{=tex}% \]

Interpretasi:

> Standard deviation PM10 sekitar 57% dari nilai mean.

Ini menunjukkan variabilitas relatif yang cukup besar.

------------------------------------------------------------------------

# 5.42 Contoh Analisis Nilai Tinggi

Untuk PM10:

``` text
Mean = 63.610
Maximum = 207.295
```

Rasio maximum terhadap mean:

\[ `\frac{207.295}{63.610}`{=tex}`\approx3.26`{=tex} \]

Artinya nilai maksimum sekitar 3.26 kali mean.

Ini menunjukkan bahwa terdapat pengamatan dengan konsentrasi jauh lebih
tinggi daripada rata-rata.

Namun, rasio ini bukan ukuran outlier formal. Untuk itu dapat digunakan
IQR atau z-score.

------------------------------------------------------------------------

# 5.43 Z-Score Nilai Maksimum

Jika menggunakan standard deviation yang ditampilkan:

### PM10

\[ z= `\frac{207.295-63.610}{36.421}`{=tex} \]

\[ z`\approx3.95`{=tex} \]

Nilai maksimum PM10 sekitar 3.95 standard deviation di atas mean
berdasarkan angka ringkasan tersebut.

### PM2.5

\[ z= `\frac{204.640-62.028}{35.869}`{=tex} \]

\[ z`\approx3.97`{=tex} \]

### PM1

\[ z= `\frac{193.528-57.529}{33.979}`{=tex} \]

\[ z`\approx4.00`{=tex} \]

Ketiganya menunjukkan bahwa nilai maksimum cukup jauh dari mean.

> **Peringatan:** z-score di atas dihitung dari ringkasan yang
> dibulatkan pada screenshot, sehingga hasilnya merupakan pendekatan.
> Untuk perhitungan final gunakan nilai statistik dengan presisi penuh.

------------------------------------------------------------------------

# 5.44 Apakah Nilai Maksimum Harus Dihapus?

Tidak.

Proses yang benar:

``` text
Temukan nilai ekstrem
        ↓
Periksa timestamp
        ↓
Periksa sensor
        ↓
Bandingkan PM1/PM2.5/PM10
        ↓
Periksa variabel lingkungan
        ↓
Validasi dengan sumber data
        ↓
Putuskan apakah valid/error
```

Jika valid:

``` text
Pertahankan
```

Jika terbukti error:

``` text
Perbaiki / hapus / imputasi
```

Dokumentasikan keputusan tersebut.

------------------------------------------------------------------------

# 5.45 Hubungan dengan Analisis Kualitas Udara

Analisis PM tidak berhenti pada statistik deskriptif.

Setelah mengetahui distribusi PM, langkah berikutnya dapat berupa:

``` text
PM Analysis
    |
    +--> Trend waktu
    |
    +--> Perbandingan lokasi
    |
    +--> Korelasi
    |
    +--> Outlier
    |
    +--> Klasifikasi kualitas udara
    |
    +--> Forecasting
    |
    +--> Machine Learning
```

Statistics Node menjadi fondasi untuk memahami data sebelum analisis
tersebut dilakukan.

------------------------------------------------------------------------

# 5.46 Contoh Narasi untuk Laporan

Berikut contoh narasi yang dapat digunakan dalam laporan:

> Berdasarkan analisis statistik deskriptif, konsentrasi rata-rata PM1,
> PM2.5, dan PM10 masing-masing sebesar 57.529, 62.028, dan 63.610
> µg/m³. PM10 memiliki nilai rata-rata, standar deviasi, dan rentang
> tertinggi dibandingkan kedua variabel lainnya. Ketiga variabel
> menunjukkan skewness positif, masing-masing sekitar 0.967 untuk PM1,
> 0.968 untuk PM2.5, dan 0.958 untuk PM10, yang mengindikasikan
> distribusi cenderung miring ke kanan. Nilai maksimum yang relatif jauh
> dari mean menunjukkan perlunya pemeriksaan terhadap observasi ekstrem.
> Namun, nilai ekstrem tidak langsung dianggap sebagai kesalahan dan
> perlu divalidasi menggunakan timestamp, sensor, variabel partikulat
> lainnya, serta informasi kondisi lingkungan.

------------------------------------------------------------------------

# 5.47 Contoh Narasi yang Lebih Singkat

> Hasil Statistics Node menunjukkan bahwa PM10 memiliki konsentrasi
> rata-rata tertinggi sebesar 63.610 µg/m³, diikuti PM2.5 sebesar 62.028
> µg/m³ dan PM1 sebesar 57.529 µg/m³. Ketiga variabel memiliki skewness
> positif sekitar 0.96, sehingga distribusinya cenderung right-skewed.
> PM10 juga memiliki standar deviasi terbesar, yaitu 36.421, yang
> menunjukkan penyebaran absolut tertinggi pada dataset contoh.

------------------------------------------------------------------------

# 5.48 Hal yang Perlu Diperhatikan

## 1. Jangan membandingkan nilai PM tanpa konteks

PM1, PM2.5, dan PM10 bukan variabel yang identik.

## 2. Jangan langsung menghapus nilai maksimum

Nilai ekstrem dapat merupakan kejadian nyata.

## 3. Jangan menggunakan threshold tanpa sumber

Jika ingin menentukan kategori kualitas udara, sebutkan standar/regulasi
yang digunakan.

## 4. Perhatikan periode waktu

Nilai hourly, daily average, dan annual average tidak dapat dibandingkan
secara sembarangan.

## 5. Perhatikan kalibrasi sensor

Sensor yang berbeda dapat menghasilkan karakteristik pengukuran berbeda.

## 6. Periksa missing value

Missing value dapat memengaruhi mean dan statistik lainnya.

## 7. Perhatikan kelembapan

Sensor partikulat tertentu dapat dipengaruhi oleh kelembapan relatif.
Jika data kelembapan tersedia, pertimbangkan dalam quality control.

------------------------------------------------------------------------

# 5.49 Checklist Analisis PM

Gunakan checklist berikut:

-   [ ] Kolom PM1 sudah bertipe numerik.
-   [ ] Kolom PM2.5 sudah bertipe numerik.
-   [ ] Kolom PM10 sudah bertipe numerik.
-   [ ] Satuan µg/m³ sudah diketahui.
-   [ ] Missing value sudah diperiksa.
-   [ ] Min sudah diperiksa.
-   [ ] Max sudah diperiksa.
-   [ ] Mean sudah dihitung.
-   [ ] Median sudah diperiksa.
-   [ ] Standard deviation sudah diperiksa.
-   [ ] Skewness sudah diperiksa.
-   [ ] Histogram sudah dibuat bila diperlukan.
-   [ ] Box plot sudah diperiksa bila diperlukan.
-   [ ] Outlier sudah divalidasi.
-   [ ] Hubungan PM1--PM2.5--PM10 sudah diperiksa.
-   [ ] Korelasi sudah dianalisis bila diperlukan.
-   [ ] Timestamp sudah digunakan untuk analisis tren.
-   [ ] Threshold kualitas udara memiliki sumber yang jelas.
-   [ ] Karakteristik sensor sudah dipertimbangkan.

------------------------------------------------------------------------

# 5.50 Ringkasan Hasil Dataset Contoh

  Parameter               PM1      PM2.5       PM10
  ---------------- ---------- ---------- ----------
  Min                   8.040     10.248     10.407
  Max                 193.528    204.640    207.295
  Range               185.488    194.392    196.888
  Mean                 57.529     62.028     63.610
  Std. deviation       33.979     35.869     36.421
  Variance           1,154.57   1,286.60   1,326.47
  Skewness              0.967      0.968      0.958
  CV                  ≈59.06%    ≈57.83%    ≈57.26%

### Temuan utama

``` text
Mean:
PM10 > PM2.5 > PM1

Std. deviation:
PM10 > PM2.5 > PM1

Variance:
PM10 > PM2.5 > PM1

Range:
PM10 > PM2.5 > PM1

Skewness:
PM1 ≈ PM2.5 ≈ PM10
dan semuanya positif.
```

------------------------------------------------------------------------

# 5.51 Kesimpulan

Analisis PM1, PM2.5, dan PM10 memberikan gambaran penting mengenai
karakteristik partikulat dalam dataset kualitas udara.

Pada contoh hasil Statistics Node:

-   PM10 mempunyai mean tertinggi;
-   PM10 mempunyai maximum tertinggi;
-   PM10 mempunyai standard deviation dan variance tertinggi;
-   PM1 mempunyai CV sedikit lebih tinggi;
-   ketiga variabel mempunyai skewness positif;
-   ketiga variabel menunjukkan variasi yang cukup besar;
-   terdapat nilai maksimum yang jauh dari mean dan perlu diperiksa
    lebih lanjut.

Analisis statistik deskriptif sebaiknya menjadi **langkah awal**, bukan
akhir. Untuk memperoleh pemahaman yang lebih kuat, hasil tersebut perlu
dilanjutkan dengan:

``` text
Histogram
      ↓
Box Plot
      ↓
Time Series
      ↓
Correlation
      ↓
Outlier Validation
      ↓
Quality Control
      ↓
Analisis lanjutan
```

Hal yang paling penting adalah membedakan **nilai ekstrem yang valid**
dari **kesalahan pengukuran**. Pada data kualitas udara, lonjakan PM
dapat benar-benar mencerminkan episode polusi sehingga tidak boleh
dihapus hanya karena nilainya tinggi.

------------------------------------------------------------------------

# 5.52 Hubungan dengan Materi Sebelumnya

Materi ini merupakan kelanjutan dari:

``` text
3. Statistics Node
        ↓
4. Rumus dan Contoh Perhitungan Statistik
        ↓
5. Analisis PM1, PM2.5, dan PM10
```

Materi 3 menjelaskan **cara mendapatkan statistik menggunakan KNIME**.

Materi 4 menjelaskan **rumus dan cara menghitung statistik secara
manual**.

Materi 5 menerapkan statistik tersebut pada **variabel kualitas udara
PM1, PM2.5, dan PM10**.

Dengan demikian, alur pembelajaran menjadi:

``` text
Data Air Quality
      ↓
Statistics Node
      ↓
Min / Max / Mean / Std / Variance / Skewness
      ↓
Perhitungan & Verifikasi
      ↓
Analisis PM1 / PM2.5 / PM10
      ↓
Interpretasi
      ↓
Visualisasi & Analisis Lanjutan
```

------------------------------------------------------------------------

# 5.53 Kesimpulan Akhir

**PM1, PM2.5, dan PM10 merupakan tiga indikator penting untuk
menganalisis partikulat udara dengan ukuran yang berbeda.**

Statistics Node membantu menghasilkan ringkasan numerik, sedangkan
analisis lanjutan membantu memahami:

-   tingkat konsentrasi;
-   variasi;
-   distribusi;
-   nilai ekstrem;
-   hubungan antarfraksi;
-   perubahan terhadap waktu.

Untuk dataset contoh, hasil utama adalah:

\[ Mean\_{PM10}\>Mean\_{PM2.5}\>Mean\_{PM1} \]

dan:

\[ Std\_{PM10}\>Std\_{PM2.5}\>Std\_{PM1} \]

sementara:

\[ Skewness\_{PM1}, Skewness\_{PM2.5}, Skewness\_{PM10}\>0 \]

sehingga ketiga distribusi cenderung **positively skewed**.

Interpretasi tersebut menjadi dasar untuk tahap berikutnya seperti
visualisasi, korelasi, pemeriksaan kualitas data, analisis time series,
dan pemodelan.

> **Catatan akhir:** angka statistik dalam dokumen ini mengikuti contoh
> yang terlihat pada screenshot workflow. Untuk laporan resmi, gunakan
> hasil eksekusi langsung pada dataset final dan simpan presisi angka
> yang sesuai dengan kebutuhan analisis.
