# 4. Rumus Statistika

## Pendahuluan

Pada bagian sebelumnya telah dibahas hasil statistika deskriptif dari data polutan NO₂, CO, dan SO₂ menggunakan KNIME.

Pada bagian ini dijelaskan rumus dasar yang digunakan untuk menghitung beberapa metrik statistika tersebut. Penjelasan ini digunakan untuk memahami bagaimana nilai statistik diperoleh dari data yang tersedia.

Metrik yang dibahas meliputi:

- Mean
- Median
- Variance
- Standard Deviation
- Skewness
- Kurtosis

---

## 4.1 Mean

Mean atau rata-rata merupakan hasil pembagian jumlah seluruh nilai data dengan jumlah data yang digunakan.

Rumus mean:

$$
\bar{x} = \frac{\sum_{i=1}^{n}x_i}{n}
$$

Keterangan:

- $\bar{x}$ = nilai rata-rata
- $x_i$ = nilai data ke-i
- $n$ = jumlah data valid
- $\sum x_i$ = jumlah seluruh nilai data

### Contoh

Misalnya terdapat data:

$$
2,\ 4,\ 6,\ 8
$$

Maka:

$$
\bar{x} = \frac{2+4+6+8}{4}
$$

$$
\bar{x} = \frac{20}{4}=5
$$

Jadi, nilai rata-ratanya adalah **5**.

Pada dataset Kalitengah, perhitungan mean dilakukan berdasarkan nilai polutan yang tersedia.

---

## 4.2 Median

Median merupakan nilai tengah dari data yang telah diurutkan.

Jika jumlah data ganjil, rumus posisi median adalah:

$$
Median = x_{\frac{n+1}{2}}
$$

Sedangkan jika jumlah data genap:

$$
Median =
\frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2}
$$

### Contoh jumlah data ganjil

Data:

$$
2,\ 4,\ 6,\ 8,\ 10
$$

Nilai tengahnya adalah:

$$
Median = 6
$$

### Contoh jumlah data genap

Data:

$$
2,\ 4,\ 6,\ 8
$$

Maka:

$$
Median = \frac{4+6}{2}
$$

$$
Median = 5
$$

Median berguna untuk melihat nilai tengah data dan relatif tidak terlalu dipengaruhi oleh nilai yang sangat tinggi atau sangat rendah.

---

## 4.3 Variance

Variance atau varians digunakan untuk mengukur tingkat penyebaran data terhadap nilai rata-ratanya.

Untuk data sampel, rumus variance adalah:

$$
s^2 =
\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

Keterangan:

- $s^2$ = variance
- $x_i$ = nilai data ke-i
- $\bar{x}$ = rata-rata
- $n$ = jumlah data

Langkah perhitungannya adalah:

1. Menghitung rata-rata data.
2. Menghitung selisih setiap data dengan rata-rata.
3. Mengkuadratkan setiap selisih.
4. Menjumlahkan hasil kuadrat.
5. Membaginya dengan $n-1$ untuk data sampel.

### Contoh

Misalnya terdapat data:

$$
2,\ 4,\ 6
$$

Rata-ratanya:

$$
\bar{x} = \frac{2+4+6}{3}=4
$$

Selisih terhadap rata-rata:

$$
2-4=-2
$$

$$
4-4=0
$$

$$
6-4=2
$$

Kuadrat selisih:

$$
4,\ 0,\ 4
$$

Sehingga:

$$
s^2=\frac{4+0+4}{3-1}
$$

$$
s^2=4
$$

Jadi variance data tersebut adalah **4**.

---

## 4.4 Standard Deviation

Standard deviation atau standar deviasi merupakan akar kuadrat dari variance.

Rumusnya:

$$
s = \sqrt{s^2}
$$

atau:

$$
s =
\sqrt{
\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
}
$$

Standar deviasi digunakan untuk mengetahui seberapa jauh data tersebar dari nilai rata-ratanya.

Nilai standar deviasi yang lebih besar menunjukkan penyebaran data yang lebih besar.

Sebaliknya, nilai yang lebih kecil menunjukkan data lebih dekat dengan nilai rata-rata.

---

## 4.5 Skewness

Skewness digunakan untuk melihat tingkat kemencengan distribusi data.

Secara umum:

| Nilai Skewness | Interpretasi |
|---|---|
| Mendekati 0 | Distribusi relatif simetris |
| Positif | Distribusi menceng ke kanan |
| Negatif | Distribusi menceng ke kiri |

Pada data Kalitengah, hasil KNIME menunjukkan:

| Polutan | Skewness |
|---|---:|
| NO₂ | 0.868 |
| CO | 0.335 |
| SO₂ | 0.143 |

Ketiganya memiliki nilai positif.

Hal ini menunjukkan distribusi ketiga polutan cenderung menceng ke arah kanan.

NO₂ memiliki nilai skewness paling tinggi sehingga kemencengannya lebih terlihat dibandingkan CO dan SO₂.

---

## 4.6 Kurtosis

Kurtosis digunakan untuk melihat karakteristik bentuk distribusi, terutama bagian ekor distribusi.

Hasil dari KNIME:

| Polutan | Kurtosis |
|---|---:|
| NO₂ | 0.390 |
| CO | 0.524 |
| SO₂ | 2.342 |

Nilai kurtosis SO₂ paling tinggi.

Hal tersebut menunjukkan bahwa distribusi SO₂ memiliki karakteristik ekor yang lebih kuat dibandingkan NO₂ dan CO.

Interpretasi kurtosis sebaiknya tidak dilakukan secara terpisah. Nilainya perlu dilihat bersama mean, standar deviasi, skewness, dan distribusi data.

---

## 4.7 Hubungan Variance dan Standard Deviation

Variance dan standard deviation memiliki hubungan langsung.

Rumusnya:

$$
s = \sqrt{s^2}
$$

dan:

$$
s^2 = (s)^2
$$

Artinya, apabila variance diketahui, standard deviation dapat diperoleh dengan mengambil akar kuadratnya.

Sebaliknya, apabila standard deviation diketahui, variance dapat diperoleh dengan mengkuadratkannya.

---

## 4.8 Perhitungan Statistik pada Dataset

Dalam dataset Kalitengah terdapat 366 tanggal kalender.

Namun, jumlah data valid untuk setiap polutan berbeda:

| Polutan | Data Valid | Missing |
|---|---:|---:|
| NO₂ | 218 | 148 |
| CO | 209 | 157 |
| SO₂ | 262 | 104 |

Oleh karena itu, perhitungan statistik untuk setiap polutan menggunakan jumlah data valid masing-masing.

Contohnya, mean NO₂ tidak dihitung menggunakan 366 nilai, tetapi menggunakan **218 nilai NO₂ yang tersedia**.

Hal yang sama berlaku untuk CO dan SO₂.

---

## 4.9 Perhitungan Mean Data Kalitengah

Berdasarkan data yang tersedia, rata-rata masing-masing polutan adalah:

| Polutan | Jumlah Data Valid | Mean |
|---|---:|---:|
| NO₂ | 218 | 0.00004497 |
| CO | 209 | 0.029909 |
| SO₂ | 262 | 0.000057 |

Perbedaan skala nilai antara ketiga polutan terlihat cukup besar.

NO₂ dan SO₂ mempunyai nilai numerik yang jauh lebih kecil dibandingkan CO. Hal ini berkaitan dengan satuan dan skala data yang digunakan.

---

## 4.10 Perhitungan Missing Data

Jumlah missing dapat dihitung dengan:

$$
Missing = Total\ Data - Data\ Valid
$$

Sebagai contoh untuk NO₂:

$$
Missing = 366-218
$$

$$
Missing = 148
$$

Untuk CO:

$$
Missing = 366-209
$$

$$
Missing = 157
$$

Sedangkan untuk SO₂:

$$
Missing = 366-262
$$

$$
Missing = 104
$$

Persentase missing dapat dihitung menggunakan:

$$
Persentase\ Missing =
\frac{Missing}{Total\ Data}\times100\%
$$

Contoh untuk NO₂:

$$
\frac{148}{366}\times100\%
\approx40.44\%
$$

Sehingga sekitar **40,44%** data NO₂ pada periode tersebut tidak memiliki nilai.

---

## 4.11 Kesimpulan

Rumus statistika digunakan untuk memahami proses perhitungan yang menghasilkan nilai statistik pada KNIME.

Mean digunakan untuk mengetahui nilai rata-rata, median untuk mengetahui nilai tengah, variance dan standard deviation untuk mengetahui penyebaran data, sedangkan skewness dan kurtosis digunakan untuk memahami karakteristik distribusi data.

Pada dataset Kalitengah, jumlah data valid berbeda untuk setiap polutan sehingga proses perhitungan statistik dilakukan berdasarkan data yang tersedia pada masing-masing kolom.

Hasil perhitungan tersebut kemudian digunakan sebagai dasar untuk melakukan analisis karakteristik NO₂, CO, dan SO₂ serta analisis perubahan data berdasarkan waktu.