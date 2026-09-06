# 4. Rumus dan Contoh Perhitungan Statistik

## 4.1 Pendahuluan

Statistik deskriptif digunakan untuk merangkum dan memahami
karakteristik suatu kumpulan data. Pada analisis data kualitas udara,
statistik deskriptif dapat digunakan untuk memahami nilai konsentrasi
polutan seperti **PM1, PM2.5, dan PM10** sebelum dilakukan analisis
lebih lanjut.

Beberapa ukuran statistik yang paling umum digunakan adalah:

1.  Minimum
2.  Maximum
3.  Range
4.  Mean
5.  Median
6.  Mode
7.  Variance
8.  Standard deviation
9.  Quartile
10. Interquartile Range (IQR)
11. Skewness
12. Z-score
13. Coefficient of Variation (CV)

Dokumen ini menjelaskan rumus, langkah perhitungan manual, contoh
numerik, dan interpretasi setiap ukuran statistik.

------------------------------------------------------------------------

# 4.2 Dataset Contoh

Untuk mempermudah perhitungan manual, gunakan dataset kecil berikut.

Misalkan terdapat data konsentrasi PM2.5:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

Jumlah data:

\[ n = 10 \]

Data sudah diurutkan dari nilai terkecil sampai terbesar.

Kita akan menggunakan dataset ini untuk menghitung sebagian besar
statistik secara manual.

------------------------------------------------------------------------

# 4.3 Notasi yang Digunakan

Dalam rumus statistik, simbol berikut sering digunakan:

  Simbol              Arti
  ------------------- -----------------------------
  (x_i)               Nilai pengamatan ke-i
  \(n\)               Jumlah observasi
  (`\bar`{=tex}{x})   Mean/rata-rata sampel
  (`\mu`{=tex})       Mean populasi
  \(s\)               Standard deviation sampel
  (`\sigma`{=tex})    Standard deviation populasi
  (Q_1)               Kuartil pertama
  (Q_2)               Kuartil kedua/median
  (Q_3)               Kuartil ketiga
  (IQR)               Interquartile Range

------------------------------------------------------------------------

# 4.4 Minimum

## Rumus

Minimum adalah nilai terkecil dalam dataset:

\[ Min(X) = `\min`{=tex}(x_1,x_2,`\ldots`{=tex},x_n) \]

## Contoh

Dataset:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

Nilai terkecil adalah:

\[ Min = 10 \]

## Interpretasi

Nilai minimum PM2.5 pada contoh adalah **10**.

Jika satuannya µg/m³, maka konsentrasi terendah yang tercatat adalah:

``` text
10 µg/m³
```

------------------------------------------------------------------------

# 4.5 Maximum

## Rumus

\[ Max(X) = `\max`{=tex}(x_1,x_2,`\ldots`{=tex},x_n) \]

## Contoh

Nilai terbesar dari:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

adalah:

\[ Max = 50 \]

## Interpretasi

Nilai PM2.5 tertinggi dalam contoh adalah **50 µg/m³** jika data
menggunakan satuan µg/m³.

------------------------------------------------------------------------

# 4.6 Range

Range menunjukkan jarak antara nilai maksimum dan minimum.

## Rumus

\[ Range = Max - Min \]

## Contoh

\[ Range = 50 - 10 \]

\[ Range = 40 \]

## Interpretasi

Data memiliki rentang sebesar **40 satuan**.

Range memberikan gambaran awal tentang seberapa luas penyebaran data,
tetapi hanya menggunakan dua nilai sehingga cukup sensitif terhadap
nilai ekstrem.

------------------------------------------------------------------------

# 4.7 Mean

Mean adalah rata-rata aritmetika.

## Rumus Sampel

\[ `\bar`{=tex}{x} = `\frac{\sum_{i=1}^{n}x_i}{n}`{=tex} \]

## Langkah 1 --- Jumlahkan seluruh nilai

\[ 10+12+15+18+20+20+22+25+30+50 \]

\[ =222 \]

## Langkah 2 --- Bagi dengan jumlah data

\[ `\bar`{=tex}{x} = `\frac{222}{10}`{=tex} \]

\[ `\bar`{=tex}{x}=22.2 \]

Jadi:

\[ `\boxed{\bar{x}=22.2}`{=tex} \]

## Interpretasi

Rata-rata konsentrasi PM2.5 pada dataset contoh adalah **22.2 µg/m³**.

------------------------------------------------------------------------

# 4.8 Mean dan Pengaruh Outlier

Mean sangat mudah dipengaruhi oleh nilai ekstrem.

Bandingkan dua dataset berikut:

### Dataset A

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

Mean:

\[ 22.2 \]

### Dataset B

Jika nilai 50 diganti menjadi 200:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 200
```

Jumlah:

\[ 372 \]

Mean:

\[ `\frac{372}{10}`{=tex}=37.2 \]

Satu nilai ekstrem menyebabkan mean meningkat dari:

``` text
22.2 → 37.2
```

Hal ini menunjukkan mengapa mean perlu dianalisis bersama median dan
statistik lainnya.

------------------------------------------------------------------------

# 4.9 Median

Median adalah nilai tengah setelah data diurutkan.

Dataset:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

Jumlah data:

\[ n=10 \]

Karena jumlah data genap, median adalah rata-rata dua nilai tengah.

Posisi tengah:

``` text
Posisi 5 = 20
Posisi 6 = 20
```

## Rumus untuk n genap

\[ Median=`\frac{x_{n/2}+x_{n/2+1}}{2}`{=tex} \]

Maka:

\[ Median=`\frac{20+20}{2}`{=tex} \]

\[ Median=20 \]

Jadi:

\[ `\boxed{Median=20}`{=tex} \]

------------------------------------------------------------------------

# 4.10 Median untuk Jumlah Data Ganjil

Misalkan:

``` text
10, 15, 20, 25, 30
```

Jumlah data:

\[ n=5 \]

Posisi median:

\[ `\frac{n+1}{2}`{=tex} = `\frac{5+1}{2}`{=tex} =3 \]

Maka median adalah nilai pada posisi ke-3:

\[ Median=20 \]

------------------------------------------------------------------------

# 4.11 Mean vs Median

Untuk dataset contoh:

``` text
Mean   = 22.2
Median = 20
```

Mean lebih besar daripada median.

Hal tersebut dapat menjadi indikasi bahwa beberapa nilai yang lebih
tinggi, terutama **50**, menarik mean ke arah kanan.

Jika:

``` text
Mean > Median
```

dan terdapat nilai tinggi yang relatif jauh dari sebagian besar data,
distribusi dapat cenderung **positively skewed/right-skewed**.

Namun, mean \> median saja **tidak cukup** untuk membuktikan bentuk
distribusi. Sebaiknya periksa histogram dan skewness.

------------------------------------------------------------------------

# 4.12 Mode

Mode adalah nilai yang paling sering muncul.

Dataset:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

Nilai:

``` text
20
```

muncul dua kali.

Nilai lainnya muncul satu kali.

Maka:

\[ `\boxed{Mode=20}`{=tex} \]

## Interpretasi

Mode menunjukkan nilai yang paling sering muncul.

Mode sangat berguna untuk data kategorikal.

Contoh:

``` text
Good
Good
Moderate
Good
Unhealthy
```

Mode:

``` text
Good
```

------------------------------------------------------------------------

# 4.13 Variance

Variance mengukur penyebaran data terhadap mean.

Untuk **sampel**, rumusnya:

\[ s\^2 = `\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}`{=tex} \]

Untuk **populasi**:

\[ `\sigma`{=tex}\^2 = `\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}`{=tex} \]

Perbedaan utama adalah penyebut:

``` text
Sampel    → n - 1
Populasi  → N
```

------------------------------------------------------------------------

# 4.14 Contoh Perhitungan Variance Sampel

Dataset:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

Mean:

\[ `\bar`{=tex}{x}=22.2 \]

Buat tabel:

     x   x - mean   (x - mean)²
  ---- ---------- -------------
    10      -12.2        148.84
    12      -10.2        104.04
    15       -7.2         51.84
    18       -4.2         17.64
    20       -2.2          4.84
    20       -2.2          4.84
    22       -0.2          0.04
    25        2.8          7.84
    30        7.8         60.84
    50       27.8        772.84

Jumlah kuadrat deviasi:

\[ `\sum`{=tex}(x_i-`\bar`{=tex}{x})\^2=1173.6 \]

Karena ini contoh **sampel**:

\[ s\^2= `\frac{1173.6}{10-1}`{=tex} \]

\[ s\^2= `\frac{1173.6}{9}`{=tex} \]

\[ s\^2=130.4 \]

Jadi:

\[ `\boxed{s^2=130.4}`{=tex} \]

------------------------------------------------------------------------

# 4.15 Standard Deviation

Standard deviation adalah akar kuadrat variance.

## Rumus Sampel

\[ s=`\sqrt{s^2}`{=tex} \]

Dengan variance:

\[ s\^2=130.4 \]

maka:

\[ s=`\sqrt{130.4}`{=tex} \]

\[ s`\approx11.42`{=tex} \]

Jadi:

\[ `\boxed{s\approx11.42}`{=tex} \]

## Interpretasi

Standard deviation sekitar **11.42** berarti data memiliki penyebaran
yang cukup besar di sekitar mean 22.2.

Standard deviation menggunakan satuan yang sama dengan data asli,
sehingga biasanya lebih mudah diinterpretasikan daripada variance.

------------------------------------------------------------------------

# 4.16 Hubungan Variance dan Standard Deviation

Hubungannya:

\[ Standard Deviation = `\sqrt{Variance}`{=tex} \]

dan:

\[ Variance = (Standard Deviation)\^2 \]

Pada contoh:

``` text
Variance ≈ 130.4
Std. deviation ≈ 11.42
```

Karena:

\[ 11.42\^2`\approx130.4`{=tex} \]

------------------------------------------------------------------------

# 4.17 Population vs Sample

Ini merupakan konsep penting dalam perhitungan statistik.

## Population

Populasi adalah seluruh objek yang ingin diteliti.

Contoh:

> Seluruh pengukuran kualitas udara selama satu tahun pada semua sensor
> yang menjadi target penelitian.

Gunakan:

\[ `\sigma`{=tex}\^2 = `\frac{\sum(x_i-\mu)^2}{N}`{=tex} \]

## Sample

Sampel adalah sebagian data yang digunakan untuk merepresentasikan
populasi.

Contoh:

> 1.464 pengukuran yang dipilih sebagai sampel dari periode pengamatan
> yang lebih besar.

Gunakan:

\[ s\^2 = `\frac{\sum(x_i-\bar{x})^2}{n-1}`{=tex} \]

------------------------------------------------------------------------

# 4.18 Mengapa Sampel Menggunakan n - 1?

Pembagian dengan (n-1) dikenal sebagai **Bessel's correction**.

Ketika mean populasi tidak diketahui dan mean sampel digunakan untuk
memperkirakan pusat data, pembagian dengan (n-1) membantu menghasilkan
estimator variance populasi yang tidak bias.

Secara praktis:

``` text
Jika data dianggap sampel → gunakan n - 1
Jika data mencakup seluruh populasi → gunakan N
```

Dalam software, pastikan memahami definisi statistik yang digunakan
sebelum membandingkan hasil dengan perhitungan manual.

------------------------------------------------------------------------

# 4.19 Quartile

Quartile membagi data terurut menjadi empat bagian.

Tiga kuartil utama:

``` text
Q1 = 25th percentile
Q2 = 50th percentile = Median
Q3 = 75th percentile
```

Secara visual:

``` text
Minimum ---- Q1 ---- Q2 ---- Q3 ---- Maximum
              25%    50%    75%
```

------------------------------------------------------------------------

# 4.20 Contoh Quartile

Dataset:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

Karena terdapat 10 data, salah satu metode sederhana adalah membagi data
menjadi dua bagian.

### Bagian bawah

``` text
10, 12, 15, 18, 20
```

Median bagian bawah:

\[ Q_1=15 \]

### Bagian atas

``` text
20, 22, 25, 30, 50
```

Median bagian atas:

\[ Q_3=25 \]

Sedangkan:

\[ Q_2=20 \]

Jadi:

``` text
Q1 = 15
Q2 = 20
Q3 = 25
```

> **Catatan penting:** terdapat beberapa metode perhitungan
> percentile/quartile. Software yang berbeda dapat menghasilkan Q1 dan
> Q3 yang sedikit berbeda karena menggunakan definisi interpolasi yang
> berbeda. Untuk laporan, sebutkan metode jika presisi metode kuartil
> penting.

------------------------------------------------------------------------

# 4.21 Interquartile Range (IQR)

IQR mengukur penyebaran 50% data bagian tengah.

## Rumus

\[ IQR=Q_3-Q_1 \]

Dengan:

\[ Q_1=15 \]

dan:

\[ Q_3=25 \]

maka:

\[ IQR=25-15 \]

\[ IQR=10 \]

Jadi:

\[ `\boxed{IQR=10}`{=tex} \]

------------------------------------------------------------------------

# 4.22 Deteksi Outlier Menggunakan IQR

Aturan umum:

### Lower Fence

\[ Lower=Q_1-1.5(IQR) \]

### Upper Fence

\[ Upper=Q_3+1.5(IQR) \]

Dengan:

``` text
Q1 = 15
Q3 = 25
IQR = 10
```

maka:

\[ Lower=15-1.5(10) \]

\[ Lower=0 \]

dan:

\[ Upper=25+1.5(10) \]

\[ Upper=40 \]

Jadi nilai yang berada:

``` text
x < 0
```

atau:

``` text
x > 40
```

dapat dianggap kandidat outlier menurut aturan IQR.

Pada dataset contoh terdapat:

``` text
50
```

Karena:

\[ 50\>40 \]

maka 50 merupakan **kandidat outlier**.

------------------------------------------------------------------------

# 4.23 Outlier Bukan Berarti Kesalahan

Sangat penting untuk membedakan:

``` text
Outlier
≠
Data salah
```

Contoh PM2.5 = 200 µg/m³ dapat disebabkan oleh:

-   kejadian polusi;
-   kebakaran;
-   aktivitas industri;
-   kondisi cuaca tertentu;
-   sensor error.

Sebelum menghapus outlier, lakukan validasi berdasarkan:

-   waktu;
-   lokasi;
-   sensor;
-   kondisi lingkungan;
-   variabel terkait;
-   sumber data.

------------------------------------------------------------------------

# 4.24 Percentile

Percentile menunjukkan posisi relatif suatu nilai dalam distribusi.

Contoh:

``` text
P25 = Q1
P50 = Median
P75 = Q3
```

Jika PM2.5 memiliki:

``` text
P75 = 80 µg/m³
```

maka sekitar 75% observasi berada pada atau di bawah nilai tersebut
menurut definisi percentile yang digunakan.

Percentile berguna untuk:

-   memahami distribusi;
-   menentukan threshold;
-   membandingkan lokasi;
-   membuat kategori;
-   analisis risiko.

------------------------------------------------------------------------

# 4.25 Z-Score

Z-score menunjukkan berapa standard deviation suatu nilai berada dari
mean.

## Rumus

Untuk data dengan mean (`\mu`{=tex}) dan standard deviation
(`\sigma`{=tex}):

\[ z=`\frac{x-\mu}{\sigma}`{=tex} \]

## Contoh

Misalkan:

``` text
Mean = 22.2
Std Dev = 11.42
```

Untuk nilai:

``` text
x = 50
```

maka:

\[ z=`\frac{50-22.2}{11.42}`{=tex} \]

\[ z`\approx2.43`{=tex} \]

Jadi nilai 50 berada sekitar:

\[ `\boxed{2.43}`{=tex} \]

standard deviation di atas mean.

------------------------------------------------------------------------

# 4.26 Interpretasi Z-Score

Secara umum:

``` text
z = 0
    → tepat pada mean

z > 0
    → di atas mean

z < 0
    → di bawah mean
```

Semakin besar nilai absolut:

\[ \|z\| \]

semakin jauh observasi dari mean.

Sebagai aturan praktis yang sering digunakan:

``` text
|z| > 2  → perlu diperhatikan
|z| > 3  → kandidat outlier yang kuat
```

Namun threshold tersebut bukan hukum universal. Distribusi data dan
konteks domain tetap harus diperhatikan.

------------------------------------------------------------------------

# 4.27 Skewness

Skewness mengukur ketidaksimetrian distribusi.

Secara konseptual, skewness sampel dapat ditulis dalam beberapa bentuk.
Salah satu bentuk koefisien momen adalah:

\[ g_1 = `\frac{\frac{1}{n}\sum(x_i-\bar{x})^3}`{=tex}
{`\left`{=tex}(`\frac{1}{n}`{=tex}`\sum`{=tex}(x_i-`\bar`{=tex}{x})^2`\right`{=tex})^{3/2}}
\]

Software statistik dapat menggunakan versi **bias-corrected sample
skewness**, sehingga hasil manual dapat berbeda jika rumus yang
digunakan tidak sama.

## Interpretasi umum

``` text
Skewness ≈ 0
    → relatif simetris

Skewness > 0
    → right-skewed

Skewness < 0
    → left-skewed
```

------------------------------------------------------------------------

# 4.28 Right-Skewed

Distribusi right-skewed memiliki ekor yang lebih panjang ke arah nilai
besar.

Contoh:

``` text
10 12 15 18 20 20 22 25 30 -------- 50
```

Nilai 50 relatif jauh dari mayoritas data sehingga ekor distribusi
memanjang ke kanan.

Pada data kualitas udara, kondisi ini dapat terjadi ketika:

-   sebagian besar waktu kualitas udara relatif normal;
-   tetapi pada beberapa waktu tertentu terjadi lonjakan konsentrasi
    polutan.

------------------------------------------------------------------------

# 4.29 Left-Skewed

Distribusi left-skewed memiliki ekor yang lebih panjang ke arah nilai
kecil.

Secara umum:

``` text
nilai rendah ---- 10
                |
             mayoritas data
```

Skewness:

\[ \<0 \]

------------------------------------------------------------------------

# 4.30 Coefficient of Variation (CV)

Coefficient of Variation digunakan untuk membandingkan tingkat variasi
relatif antara variabel dengan skala atau satuan yang berbeda.

## Rumus

\[ CV=`\frac{s}{\bar{x}}`{=tex}`\times100`{=tex}% \]

## Contoh

Dengan:

``` text
Mean = 22.2
Std Dev = 11.42
```

maka:

\[ CV=`\frac{11.42}{22.2}`{=tex}`\times100`{=tex}% \]

\[ CV`\approx51.44`{=tex}% \]

Jadi:

\[ `\boxed{CV\approx51.44\%}`{=tex} \]

## Interpretasi

CV sekitar 51.44% menunjukkan standard deviation cukup besar
dibandingkan mean.

CV berguna untuk membandingkan **variabilitas relatif**, bukan untuk
menggantikan standard deviation.

> CV paling bermakna untuk variabel yang mean-nya positif dan tidak
> mendekati nol. Jika mean mendekati nol, CV dapat menjadi sangat besar
> dan menyesatkan.

------------------------------------------------------------------------

# 4.31 Sum

Sum adalah jumlah seluruh observasi.

## Rumus

\[ Sum=`\sum`{=tex}\_{i=1}\^{n}x_i \]

Pada dataset:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

jumlahnya:

\[ Sum=222 \]

Hubungan dengan mean:

\[ Mean=`\frac{Sum}{n}`{=tex} \]

sehingga:

\[ 22.2=`\frac{222}{10}`{=tex} \]

------------------------------------------------------------------------

# 4.32 Count

Count menunjukkan jumlah observasi yang dihitung.

Untuk dataset contoh:

\[ n=10 \]

Jadi:

``` text
Count = 10
```

Count harus dibedakan dari:

``` text
Missing Count
```

Jika dataset memiliki 1.000 baris tetapi 50 nilai PM2.5 missing, jumlah
nilai PM2.5 yang tersedia dapat menjadi 950, tergantung definisi/count
yang digunakan oleh node.

------------------------------------------------------------------------

# 4.33 Missing Value Rate

Persentase missing value dapat dihitung dengan:

\[ Missing Rate=
`\frac{Missing\ Count}{Total\ Count}`{=tex}`\times100`{=tex}% \]

Contoh:

``` text
Total data = 1,000
Missing = 50
```

maka:

\[ Missing Rate= `\frac{50}{1000}`{=tex}`\times100`{=tex}% \]

\[ =5% \]

Jadi 5% data pada kolom tersebut missing.

------------------------------------------------------------------------

# 4.34 Contoh Perhitungan Statistik dengan Dataset Air Quality

Misalkan diperoleh 10 pengukuran PM2.5:

  Waktu     PM2.5
  ------- -------
  01:00        10
  02:00        12
  03:00        15
  04:00        18
  05:00        20
  06:00        20
  07:00        22
  08:00        25
  09:00        30
  10:00        50

Ringkasan:

  Statistik                   Nilai
  ----------------------- ---------
  Count                          10
  Sum                           222
  Min                            10
  Max                            50
  Range                          40
  Mean                         22.2
  Median                         20
  Mode                           20
  Sample Variance             130.4
  Sample Std. deviation      ≈11.42
  Q1\*                           15
  Q2\*                           20
  Q3\*                           25
  IQR\*                          10
  CV                        ≈51.44%
  Z-score nilai 50            ≈2.43

\*Menggunakan metode kuartil sederhana yang dijelaskan pada bagian
sebelumnya.

------------------------------------------------------------------------

# 4.35 Interpretasi Dataset Contoh

Berdasarkan perhitungan:

### 1. Pusat data

``` text
Mean   = 22.2
Median = 20
Mode   = 20
```

Mean lebih tinggi daripada median.

### 2. Penyebaran

``` text
Range ≈ 40
Std Dev ≈ 11.42
```

Data memiliki variasi yang cukup terlihat.

### 3. Outlier

Dengan aturan IQR:

``` text
Upper Fence = 40
```

Nilai:

``` text
50
```

merupakan kandidat outlier.

### 4. Nilai ekstrem

Z-score nilai 50 sekitar:

``` text
2.43
```

Nilai ini cukup jauh dari mean dan layak diperiksa lebih lanjut.

### 5. Kesimpulan

Distribusi contoh cenderung memiliki nilai tinggi yang menarik mean ke
atas. Nilai 50 perlu diperiksa apakah merupakan pengukuran valid atau
error.

------------------------------------------------------------------------

# 4.36 Hubungan Statistik dengan Statistics Node di KNIME

Dalam node **Statistics**, beberapa statistik pada output dapat
diperoleh secara otomatis.

Contoh:

``` text
Data
 |
 v
+----------------+
|   Statistics   |
+----------------+
 |
 v
Statistics Table
```

Kolom statistik yang umum terlihat antara lain:

``` text
Min
Max
Mean
Std. deviation
Variance
Skewness
```

Jika median diaktifkan, node juga dapat menghitung:

``` text
Median
```

Tergantung versi dan konfigurasi node, informasi tambahan seperti count,
missing values, dan statistik nominal juga dapat tersedia.

------------------------------------------------------------------------

# 4.37 Contoh Menghubungkan Hasil Manual dengan KNIME

Misalkan perhitungan manual memberikan:

``` text
PM2.5

Min      = 10
Max      = 50
Mean     = 22.2
Variance = 130.4
Std Dev  = 11.42
```

Setelah data dimasukkan ke KNIME Statistics Node, hasil pada Statistics
Table seharusnya konsisten dengan definisi statistik yang digunakan.

Namun, jika hasil berbeda, periksa:

1.  apakah variance yang digunakan sample atau population;
2.  apakah ada missing values;
3.  apakah data yang dihitung sama;
4.  apakah ada filter baris;
5.  apakah tipe kolom benar;
6.  apakah metode median/percentile berbeda;
7.  apakah node menggunakan definisi skewness yang berbeda.

------------------------------------------------------------------------

# 4.38 Contoh Perhitungan Menggunakan Python

Untuk memverifikasi hasil secara programatis, contoh berikut dapat
digunakan:

``` python
import numpy as np

data = np.array([10, 12, 15, 18, 20, 20, 22, 25, 30, 50])

mean = np.mean(data)
median = np.median(data)
minimum = np.min(data)
maximum = np.max(data)
variance_sample = np.var(data, ddof=1)
std_sample = np.std(data, ddof=1)

print("Mean:", mean)
print("Median:", median)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sample Variance:", variance_sample)
print("Sample Std:", std_sample)
```

Hasil penting:

``` text
Mean             = 22.2
Median           = 20.0
Minimum          = 10
Maximum          = 50
Sample Variance  = 130.4
Sample Std       ≈ 11.42
```

Parameter:

``` python
ddof=1
```

digunakan untuk sample variance dan sample standard deviation.

Jika ingin variance populasi:

``` python
np.var(data, ddof=0)
```

------------------------------------------------------------------------

# 4.39 Contoh Perhitungan di Excel

Misalkan data PM2.5 berada pada:

``` text
A2:A11
```

### Mean

``` excel
=AVERAGE(A2:A11)
```

### Median

``` excel
=MEDIAN(A2:A11)
```

### Minimum

``` excel
=MIN(A2:A11)
```

### Maximum

``` excel
=MAX(A2:A11)
```

### Sample Variance

``` excel
=VAR.S(A2:A11)
```

### Population Variance

``` excel
=VAR.P(A2:A11)
```

### Sample Standard Deviation

``` excel
=STDEV.S(A2:A11)
```

### Population Standard Deviation

``` excel
=STDEV.P(A2:A11)
```

### Quartile

``` excel
=QUARTILE.INC(A2:A11,1)
```

untuk Q1 dan:

``` excel
=QUARTILE.INC(A2:A11,3)
```

untuk Q3.

> Excel memiliki beberapa fungsi percentile/quartile. Pastikan fungsi
> yang digunakan konsisten dengan metode yang dipakai dalam analisis.

------------------------------------------------------------------------

# 4.40 Contoh Perhitungan dengan Kalkulator

Untuk perhitungan manual sederhana:

### Mean

``` text
(10 + 12 + 15 + 18 + 20 + 20 + 22 + 25 + 30 + 50) / 10
= 22.2
```

### Range

``` text
50 - 10
= 40
```

### Sample Variance

``` text
1173.6 / 9
= 130.4
```

### Sample Standard Deviation

``` text
√130.4
≈ 11.42
```

------------------------------------------------------------------------

# 4.41 Perbedaan Statistik Deskriptif dan Inferensial

## Statistik Deskriptif

Digunakan untuk menjelaskan data yang tersedia.

Contoh:

``` text
Mean
Median
Min
Max
Std. deviation
Variance
Quartile
Skewness
```

## Statistik Inferensial

Digunakan untuk membuat kesimpulan atau estimasi mengenai populasi
berdasarkan sampel.

Contoh:

-   confidence interval;
-   hypothesis testing;
-   t-test;
-   ANOVA;
-   regression;
-   correlation testing.

Statistics Node terutama digunakan untuk **statistik deskriptif** dan
eksplorasi awal.

------------------------------------------------------------------------

# 4.42 Mengapa Rumus Harus Dipahami?

Software seperti KNIME dapat menghitung statistik secara otomatis.

Namun, pengguna tetap perlu memahami rumus karena:

1.  dapat memeriksa apakah hasil masuk akal;
2.  dapat menjelaskan hasil dalam laporan;
3.  dapat mengetahui perbedaan sample dan population;
4.  dapat memahami efek outlier;
5.  dapat memilih statistik yang sesuai;
6.  dapat menghindari kesalahan interpretasi.

Contohnya, melihat:

``` text
Variance = 1,154.57
```

tidak cukup.

Kita juga harus memahami bahwa:

\[ Std. deviation `\approx `{=tex}`\sqrt{Variance}`{=tex} \]

sehingga:

\[ `\sqrt{1154.57}`{=tex}`\approx33.98`{=tex} \]

Hal ini sesuai dengan nilai standard deviation yang terlihat pada contoh
Statistics Table.

------------------------------------------------------------------------

# 4.43 Contoh Verifikasi dari Screenshot Statistics Node

Pada contoh hasil Statistics Node, untuk PM1 terlihat kira-kira:

``` text
Std. deviation = 33.979
Variance       = 1,154.57
```

Kita dapat melakukan verifikasi:

\[ 33.979\^2`\approx1154.57`{=tex} \]

Hasil tersebut menunjukkan hubungan variance dan standard deviation
konsisten.

Untuk PM2.5:

``` text
Std. deviation ≈ 35.869
Variance ≈ 1,286.6
```

Verifikasi:

\[ 35.869\^2`\approx1286.6`{=tex} \]

Untuk PM10:

``` text
Std. deviation ≈ 36.421
Variance ≈ 1,326.47
```

Verifikasi:

\[ 36.421\^2`\approx1326.47`{=tex} \]

Dengan demikian, nilai variance pada output dapat diperiksa dengan
mengkuadratkan standard deviation, dengan perbedaan kecil yang mungkin
berasal dari pembulatan tampilan.

------------------------------------------------------------------------

# 4.44 Ringkasan Rumus

  Statistik              Rumus
  ---------------------- ---------------------------------------------------
  Minimum                (`\min`{=tex}(x_i))
  Maximum                (`\max`{=tex}(x_i))
  Range                  (Max-Min)
  Mean                   (`\frac{\sum x_i}{n}`{=tex})
  Median                 Nilai tengah
  Mode                   Nilai paling sering
  Sample Variance        (`\frac{\sum(x_i-\bar{x})^2}{n-1}`{=tex})
  Population Variance    (`\frac{\sum(x_i-\mu)^2}{N}`{=tex})
  Sample Std. Dev.       (`\sqrt{s^2}`{=tex})
  Population Std. Dev.   (`\sqrt{\sigma^2}`{=tex})
  IQR                    (Q_3-Q_1)
  Lower Fence            (Q_1-1.5(IQR))
  Upper Fence            (Q_3+1.5(IQR))
  Z-score                (`\frac{x-\mu}{\sigma}`{=tex})
  CV                     (`\frac{s}{\bar{x}}`{=tex}`\times100`{=tex}%)
  Missing Rate           (`\frac{Missing}{Total}`{=tex}`\times100`{=tex}%)

------------------------------------------------------------------------

# 4.45 Cheat Sheet

``` text
MIN
↓
Nilai paling kecil

MAX
↓
Nilai paling besar

RANGE
↓
MAX - MIN

MEAN
↓
Jumlah semua nilai / jumlah data

MEDIAN
↓
Nilai tengah setelah data diurutkan

MODE
↓
Nilai yang paling sering muncul

VARIANCE
↓
Ukuran penyebaran kuadrat

STANDARD DEVIATION
↓
√Variance

Q1
↓
25% percentile

Q2
↓
50% percentile / Median

Q3
↓
75% percentile

IQR
↓
Q3 - Q1

SKEWNESS
↓
Kemencengan distribusi

Z-SCORE
↓
Jarak observasi dari mean dalam satuan standard deviation

CV
↓
Variasi relatif terhadap mean
```

------------------------------------------------------------------------

# 4.46 Checklist Perhitungan Statistik

Sebelum menyimpulkan hasil statistik, periksa:

-   [ ] Data sudah diurutkan ketika menghitung median/quartile secara
    manual.
-   [ ] Jumlah observasi (n) sudah benar.
-   [ ] Mean dihitung dari data yang benar.
-   [ ] Sample dan population variance tidak tertukar.
-   [ ] Standard deviation merupakan akar variance.
-   [ ] Satuan data diketahui.
-   [ ] Missing value diperiksa.
-   [ ] Outlier tidak langsung dihapus tanpa validasi.
-   [ ] Metode quartile/percentile diketahui.
-   [ ] Skewness dipahami berdasarkan definisi software yang digunakan.
-   [ ] Hasil manual dibandingkan dengan hasil KNIME jika diperlukan.

------------------------------------------------------------------------

# 4.47 Kesimpulan

Rumus statistik merupakan dasar penting untuk memahami output dari
**Statistics Node** pada KNIME.

Ukuran yang paling penting untuk analisis awal adalah:

``` text
Min
Max
Mean
Median
Variance
Standard Deviation
Skewness
```

Untuk analisis penyebaran dan outlier, tambahkan:

``` text
Q1
Q3
IQR
Z-score
```

Contoh dataset:

``` text
10, 12, 15, 18, 20, 20, 22, 25, 30, 50
```

menghasilkan:

``` text
Mean              = 22.2
Median            = 20
Mode              = 20
Minimum           = 10
Maximum           = 50
Range             = 40
Sample Variance   = 130.4
Sample Std. Dev.  ≈ 11.42
IQR*              = 10
CV                ≈ 51.44%
```

Nilai 50 menjadi kandidat outlier berdasarkan aturan IQR dan memiliki
z-score sekitar 2.43.

Hal terpenting adalah **statistik tidak hanya dihitung, tetapi juga
diinterpretasikan**. Dalam analisis kualitas udara, nilai ekstrem harus
divalidasi karena dapat merupakan error sensor maupun kejadian polusi
yang benar-benar terjadi.

------------------------------------------------------------------------

# 4.48 Hubungan dengan Materi Sebelumnya

Materi ini merupakan kelanjutan dari:

``` text
3. Statistics Node
```

Pada materi sebelumnya, kita mempelajari cara menggunakan node
Statistics untuk menghasilkan tabel statistik.

Pada materi ini, kita mempelajari **bagaimana angka-angka tersebut
diperoleh dan bagaimana menginterpretasikannya**.

Alurnya:

``` text
Data
  ↓
Statistics Node
  ↓
Statistics Table
  ↓
Rumus Statistik
  ↓
Verifikasi
  ↓
Interpretasi
  ↓
Kesimpulan
```

Dengan memahami rumus, pengguna KNIME tidak hanya mengetahui cara
menjalankan node, tetapi juga memahami makna statistik yang dihasilkan.

------------------------------------------------------------------------

## Referensi Konsep

Materi ini menggunakan konsep umum statistik deskriptif dan definisi
sample/population variance, standard deviation, quartile, IQR, z-score,
dan skewness yang umum digunakan dalam analisis data.

Untuk implementasi praktis, selalu periksa dokumentasi versi software
yang digunakan karena detail algoritma---terutama percentile, quartile,
dan skewness---dapat berbeda antarperangkat lunak.
