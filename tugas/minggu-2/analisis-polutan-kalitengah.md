# 5. Analisis Polutan Kalitengah

## Pendahuluan

Setelah data berhasil diolah menggunakan PostgreSQL Aiven dan KNIME, tahap selanjutnya adalah melakukan analisis terhadap karakteristik masing-masing polutan.

Polutan yang dianalisis adalah:

- Nitrogen Dioksida (NO₂)
- Karbon Monoksida (CO)
- Sulfur Dioksida (SO₂)

Analisis dilakukan menggunakan statistik deskriptif dan data time series yang telah dikumpulkan pada periode **31 Agustus 2025 sampai 31 Agustus 2026**.

Perlu diperhatikan bahwa jumlah data valid pada masing-masing polutan berbeda karena terdapat data yang kosong pada beberapa tanggal.

---

## 5.1 Analisis Nitrogen Dioksida (NO₂)

Nitrogen Dioksida atau NO₂ merupakan salah satu parameter polutan yang terdapat pada dataset.

Berdasarkan data yang tersedia, terdapat **218 nilai NO₂ yang valid** dari total 366 tanggal. Sementara itu, terdapat **148 data missing**.

### Statistik NO₂

| Parameter | Nilai |
|---|---:|
| Jumlah data valid | 218 |
| Missing | 148 |
| Minimum | 0.00000017 |
| Maximum | 0.0001225 |
| Mean | 0.00004497 |
| Median | 0.00004283 |
| Standard deviation | 0.00002479 |
| Skewness | 0.868 |
| Kurtosis | 0.390 |

Nilai rata-rata NO₂ adalah sekitar **0.00004497**, sedangkan nilai mediannya sekitar **0.00004283**.

Nilai mean sedikit lebih besar daripada median. Hal tersebut sejalan dengan nilai skewness yang positif, yaitu **0.868**, yang menunjukkan bahwa distribusi data NO₂ cenderung menceng ke arah kanan.

Nilai maksimum NO₂ mencapai sekitar **0.0001225**, sedangkan nilai minimumnya sekitar **0.00000017**.

### Missing Data NO₂

Dari 366 tanggal pengamatan terdapat 148 data missing.

Persentasenya:

$$
\frac{148}{366}\times100\%
=40.44\%
$$

Artinya sekitar **40,44%** tanggal tidak mempunyai nilai NO₂ yang tersedia.

Kondisi missing data ini perlu diperhatikan ketika melakukan analisis time series karena dapat menyebabkan adanya celah pada grafik.

---

## 5.2 Analisis Karbon Monoksida (CO)

Karbon Monoksida atau CO merupakan parameter polutan kedua yang dianalisis.

Terdapat **209 nilai CO yang valid** dari total 366 tanggal, sedangkan **157 tanggal** tidak mempunyai nilai CO.

### Statistik CO

| Parameter | Nilai |
|---|---:|
| Jumlah data valid | 209 |
| Missing | 157 |
| Minimum | 0.016442 |
| Maximum | 0.042702 |
| Mean | 0.029909 |
| Median | 0.029526 |
| Standard deviation | 0.004086 |
| Skewness | 0.335 |
| Kurtosis | 0.524 |

Nilai rata-rata CO adalah **0.029909**, sedangkan median sebesar **0.029526**.

Perbedaan antara mean dan median relatif kecil. Nilai skewness sebesar **0.335** menunjukkan distribusi CO memiliki kemencengan positif, tetapi tidak sebesar NO₂.

Nilai CO terendah yang tercatat adalah **0.016442**, sedangkan nilai tertingginya adalah **0.042702**.

### Missing Data CO

Jumlah data missing pada CO adalah 157 dari 366 tanggal.

Persentasenya:

$$
\frac{157}{366}\times100\%
=42.90\%
$$

Dengan demikian, sekitar **42,90%** data CO pada periode pengamatan tidak memiliki nilai.

CO memiliki persentase missing paling tinggi dibandingkan NO₂ dan SO₂.

---

## 5.3 Analisis Sulfur Dioksida (SO₂)

Sulfur Dioksida atau SO₂ merupakan parameter ketiga yang dianalisis.

Dari total 366 tanggal, terdapat **262 nilai SO₂ yang valid** dan **104 data missing**.

### Statistik SO₂

| Parameter | Nilai |
|---|---:|
| Jumlah data valid | 262 |
| Missing | 104 |
| Minimum | -0.000806 |
| Maximum | 0.000926 |
| Mean | 0.000057 |
| Median | 0.000043 |
| Standard deviation | 0.000232 |
| Skewness | 0.143 |
| Kurtosis | 2.342 |

Nilai rata-rata SO₂ adalah sekitar **0.000057**, sedangkan median sebesar **0.000043**.

Nilai skewness sebesar **0.143** menunjukkan distribusi SO₂ relatif lebih dekat dengan kondisi simetris dibandingkan NO₂ dan CO.

Kurtosis SO₂ memiliki nilai **2.342**, lebih tinggi dibandingkan NO₂ dan CO. Hal ini menunjukkan karakteristik distribusi SO₂ memiliki ekor yang lebih kuat.

### Nilai Negatif SO₂

Pada data SO₂ terdapat beberapa nilai negatif, dengan nilai minimum sekitar **-0.000806**.

Nilai negatif tersebut tidak langsung dihapus pada tahap ini.

Hal ini karena proses pengumpulan data menghasilkan nilai tersebut dan perlu dilakukan pemeriksaan lebih lanjut sebelum menentukan apakah nilai tersebut merupakan noise, hasil estimasi penginderaan jauh, atau nilai yang perlu dibersihkan pada tahap preprocessing.

Oleh karena itu, nilai negatif dicatat sebagai bagian dari karakteristik dataset dan akan menjadi pertimbangan pada proses analisis dan pembersihan data berikutnya.

---

## 5.4 Perbandingan Ketiga Polutan

Berdasarkan hasil statistik deskriptif, karakteristik ketiga polutan dapat dibandingkan sebagai berikut:

| Parameter | NO₂ | CO | SO₂ |
|---|---:|---:|---:|
| Data valid | 218 | 209 | 262 |
| Missing | 148 | 157 | 104 |
| Mean | 0.00004497 | 0.029909 | 0.000057 |
| Median | 0.00004283 | 0.029526 | 0.000043 |
| Standard deviation | 0.00002479 | 0.004086 | 0.000232 |
| Skewness | 0.868 | 0.335 | 0.143 |
| Kurtosis | 0.390 | 0.524 | 2.342 |

Dari tabel tersebut dapat diketahui beberapa hal.

### Data valid

SO₂ memiliki jumlah data valid paling banyak, yaitu **262 data**.

CO memiliki jumlah data valid paling sedikit, yaitu **209 data**.

### Missing data

CO memiliki jumlah missing paling banyak, yaitu **157 data** atau sekitar **42,90%**.

SO₂ memiliki jumlah missing paling sedikit, yaitu **104 data** atau sekitar **28,42%**.

### Skewness

NO₂ memiliki nilai skewness paling tinggi, yaitu **0.868**.

Hal tersebut menunjukkan distribusi NO₂ lebih menceng ke kanan dibandingkan CO dan SO₂.

### Kurtosis

SO₂ mempunyai nilai kurtosis paling tinggi, yaitu **2.342**.

Hal tersebut menunjukkan karakteristik ekor distribusi SO₂ lebih kuat dibandingkan kedua polutan lainnya.

---

## 5.5 Interpretasi Mean dan Median

Perbandingan mean dan median dapat digunakan sebagai gambaran awal mengenai distribusi data.

| Polutan | Mean | Median |
|---|---:|---:|
| NO₂ | 0.00004497 | 0.00004283 |
| CO | 0.029909 | 0.029526 |
| SO₂ | 0.000057 | 0.000043 |

Pada ketiga polutan, nilai mean lebih besar daripada median.

Perbedaan tersebut paling terlihat pada NO₂ dan SO₂. Kondisi ini juga berkaitan dengan nilai skewness yang bernilai positif.

Namun, mean dan median saja belum cukup untuk menjelaskan keseluruhan distribusi. Oleh karena itu, analisis juga mempertimbangkan standard deviation, skewness, kurtosis, serta grafik time series.

---

## 5.6 Perbandingan Missing Data

Persentase missing data dapat digambarkan sebagai berikut:

| Polutan | Data Valid | Missing | Persentase Missing |
|---|---:|---:|---:|
| NO₂ | 218 | 148 | 40,44% |
| CO | 209 | 157 | 42,90% |
| SO₂ | 262 | 104 | 28,42% |

Dari hasil tersebut, CO mempunyai tingkat kelengkapan data paling rendah karena mempunyai persentase missing paling tinggi.

Sebaliknya, SO₂ mempunyai data yang relatif lebih lengkap karena persentase missing-nya paling rendah.

Kondisi ini penting dalam analisis time series karena semakin banyak data yang hilang, semakin banyak bagian grafik yang tidak memiliki nilai.

---

## 5.7 Pemeriksaan Data

Hasil Statistics View KNIME menunjukkan bahwa ketiga polutan tidak mempunyai:

- nilai NaN,
- nilai +∞,
- nilai -∞.

Namun, terdapat data missing pada ketiga kolom.

Perbedaan antara missing dan NaN perlu diperhatikan. Missing menunjukkan tidak adanya nilai pada suatu pengamatan, sedangkan NaN merupakan nilai khusus yang menunjukkan hasil numerik yang tidak valid atau tidak terdefinisi.

Dalam dataset ini, masalah utama yang terlihat dari Statistics View adalah keberadaan **missing data**, bukan NaN atau infinity.

---

## 5.8 Kesimpulan Analisis Polutan

Berdasarkan hasil analisis, ketiga polutan mempunyai karakteristik yang berbeda.

NO₂ memiliki skewness paling tinggi dengan nilai **0.868**, sehingga distribusinya lebih menceng ke kanan.

CO mempunyai jumlah data missing paling banyak, yaitu **157 data** atau sekitar **42,90%** dari total 366 tanggal.

SO₂ mempunyai jumlah data valid paling banyak, yaitu **262 data**, serta mempunyai nilai kurtosis paling tinggi sebesar **2.342**.

Secara keseluruhan, data menunjukkan bahwa kelengkapan data dan karakteristik distribusi berbeda pada setiap polutan. Oleh karena itu, analisis tidak cukup hanya menggunakan nilai rata-rata, tetapi perlu mempertimbangkan median, penyebaran data, bentuk distribusi, serta perubahan nilai dari waktu ke waktu.

Tahap berikutnya adalah melakukan **analisis time series** untuk melihat perubahan nilai NO₂, CO, dan SO₂ berdasarkan tanggal pengamatan.