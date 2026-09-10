# 3. Statistika Deskriptif Polutan

## Pendahuluan

Statistika deskriptif digunakan untuk memberikan gambaran umum mengenai karakteristik suatu dataset. Statistik ini membantu menjelaskan pusat data, tingkat penyebaran, bentuk distribusi, serta kelengkapan data sebelum dilakukan analisis lebih lanjut.

Pada penelitian ini, statistika deskriptif digunakan untuk menganalisis data polutan **NO₂, CO, dan SO₂** di Kecamatan Kalitengah, Kabupaten Lamongan.

Analisis dilakukan menggunakan node **Statistics** pada **KNIME Analytics Platform**. Statistik yang diperhatikan meliputi:

- Minimum
- Maximum
- Mean
- Standard Deviation
- Variance
- Skewness
- Kurtosis
- Overall Sum
- No. Missings
- No. NaNs
- No. +∞s
- No. -∞s
- Median

Data yang digunakan mencakup periode **31 Agustus 2025 sampai 31 Agustus 2026** dengan total **366 tanggal kalender**.

---

## 3.1 Minimum

**Minimum (Min)** merupakan nilai paling kecil yang terdapat pada data valid suatu variabel.

Secara sederhana:

```text
Minimum = nilai terkecil dalam data valid
```

Nilai `NULL` atau data kosong tidak digunakan sebagai nilai minimum.

Minimum berguna untuk mengetahui batas bawah nilai pengamatan yang tersedia. Dalam konteks kualitas udara, nilai minimum dapat digunakan untuk mengetahui nilai konsentrasi terendah yang tercatat selama periode pengamatan.

Nilai minimum berdasarkan data yang tersedia adalah:

| Polutan | Minimum |
|---|---:|
| NO₂ | 0.00000017 |
| CO | 0.016442 |
| SO₂ | -0.000806 |

> **Catatan:** Nilai minimum NO₂ dan SO₂ dapat terlihat sebagai `0` pada Statistics View apabila tampilan menggunakan pembulatan desimal yang terbatas. Nilai pada tabel di atas ditampilkan dengan presisi yang lebih tinggi.

---

## 3.2 Maximum

**Maximum (Max)** merupakan nilai paling besar yang terdapat pada data valid suatu variabel.

Secara sederhana:

```text
Maximum = nilai terbesar dalam data valid
```

Nilai maksimum digunakan untuk mengetahui batas atas pengamatan.

Hasil nilai maksimum:

| Polutan | Maximum |
|---|---:|
| NO₂ | 0.0001225 |
| CO | 0.042702 |
| SO₂ | 0.000926 |

Dalam analisis kualitas udara, nilai maksimum dapat membantu mengidentifikasi nilai pengamatan tertinggi selama periode data.

Nilai maksimum tidak secara otomatis berarti telah terjadi kondisi pencemaran tertentu karena penilaian kualitas udara juga memerlukan perbandingan dengan standar atau ambang batas yang relevan.

---

## 3.3 Mean

**Mean** atau rata-rata merupakan ukuran pemusatan data yang diperoleh dengan menjumlahkan seluruh nilai valid kemudian membaginya dengan jumlah data valid.

Rumus mean:

$$
\bar{x} = \frac{\sum_{i=1}^{n}x_i}{n}
$$

Keterangan:

- $\bar{x}$ = nilai rata-rata;
- $x_i$ = nilai data ke-$i$;
- $n$ = jumlah data valid;
- $\sum x_i$ = jumlah seluruh nilai data valid.

Pada dataset Kalitengah, nilai `NULL` tidak dimasukkan dalam perhitungan mean.

Hasil mean:

| Polutan | Mean |
|---|---:|
| NO₂ | 0.00004497 |
| CO | 0.029909 |
| SO₂ | 0.000057 |

Nilai tersebut menunjukkan nilai rata-rata masing-masing polutan berdasarkan data yang tersedia.

---

## 3.4 Standard Deviation

**Standard deviation** atau standar deviasi merupakan ukuran yang digunakan untuk mengetahui seberapa besar penyebaran data terhadap nilai rata-ratanya.

Secara umum:

- standar deviasi kecil menunjukkan data cenderung dekat dengan rata-rata;
- standar deviasi besar menunjukkan data memiliki penyebaran yang lebih besar.

Untuk data sampel, rumus standar deviasi adalah:

$$
s = \sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}
$$

Keterangan:

- $s$ = standar deviasi sampel;
- $x_i$ = nilai data ke-$i$;
- $\bar{x}$ = rata-rata;
- $n$ = jumlah data valid.

Hasil standar deviasi:

| Polutan | Standard Deviation |
|---|---:|
| NO₂ | 0.00002479 |
| CO | 0.004086 |
| SO₂ | 0.000232 |

Standar deviasi menunjukkan tingkat variasi masing-masing polutan selama periode pengamatan.

---

## 3.5 Variance

**Variance** atau varians merupakan ukuran penyebaran data yang berkaitan langsung dengan standar deviasi.

Untuk varians sampel:

$$
s^2 = \frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

Hubungan antara variance dan standard deviation adalah:

$$
s = \sqrt{s^2}
$$

atau:

$$
s^2 = (\text{Standard Deviation})^2
$$

Semakin besar variance, semakin besar penyebaran data terhadap nilai rata-ratanya.

### Contoh hubungan

Jika standar deviasi suatu variabel adalah:

```text
s = 0.004086
```

maka varians secara pendekatan:

```text
s² = (0.004086)²
```

Hasil tersebut menunjukkan bahwa variance memiliki satuan kuadrat dari satuan data asli.

> **Catatan:** Karena nilai variance dapat sangat kecil, terutama pada NO₂ dan SO₂, hasilnya sebaiknya ditampilkan dengan jumlah digit desimal yang cukup agar tidak terlihat sebagai `0` akibat pembulatan.

---

## 3.6 Skewness

**Skewness** digunakan untuk mengetahui tingkat kemencengan atau ketidaksimetrisan distribusi data.

Secara umum:

- skewness mendekati `0` → distribusi relatif simetris;
- skewness positif → distribusi cenderung memiliki ekor lebih panjang ke kanan;
- skewness negatif → distribusi cenderung memiliki ekor lebih panjang ke kiri.

Hasil skewness dari KNIME:

| Polutan | Skewness |
|---|---:|
| NO₂ | 0.868 |
| CO | 0.335 |
| SO₂ | 0.143 |

Ketiga polutan memiliki nilai skewness positif.

Urutan nilai skewness:

```text
NO₂ > CO > SO₂
```

NO₂ mempunyai nilai skewness paling tinggi sehingga menunjukkan kemencengan positif yang paling kuat di antara ketiga polutan.

SO₂ memiliki nilai paling dekat dengan nol sehingga distribusinya relatif lebih simetris dibandingkan NO₂ dan CO.

---

## 3.7 Kurtosis

**Kurtosis** digunakan untuk menggambarkan karakteristik bentuk distribusi, khususnya perilaku ekor distribusi dan konsentrasi nilai.

Hasil kurtosis:

| Polutan | Kurtosis |
|---|---:|
| NO₂ | 0.390 |
| CO | 0.524 |
| SO₂ | 2.342 |

SO₂ memiliki nilai kurtosis paling tinggi.

Hal tersebut menunjukkan bahwa distribusi SO₂ memiliki karakteristik ekor distribusi yang lebih kuat dibandingkan NO₂ dan CO.

Interpretasi kurtosis sebaiknya dilakukan bersama statistik lainnya karena nilai kurtosis dapat memiliki definisi atau konvensi pelaporan yang berbeda pada perangkat lunak statistik.

---

## 3.8 Overall Sum

**Overall Sum** merupakan jumlah seluruh nilai valid pada suatu kolom.

Rumus:

$$
\text{Sum} = \sum_{i=1}^{n}x_i
$$

Nilai `NULL` tidak ikut dijumlahkan.

Hasil yang ditampilkan pada KNIME:

| Polutan | Overall Sum |
|---|---:|
| NO₂ | 0.01 |
| CO | 6.251 |
| SO₂ | 0.015 |

Nilai NO₂ dan SO₂ terlihat kecil karena skala nilai pengamatannya juga relatif kecil.

Untuk NO₂ dan SO₂, tampilan angka dengan presisi rendah dapat menyebabkan nilai total terlihat lebih sederhana daripada nilai sebenarnya. Oleh karena itu, apabila diperlukan untuk perhitungan atau pembuktian manual, gunakan nilai dengan presisi yang lebih tinggi dari data sumber.

---

## 3.9 No. Missings

**No. Missings** menunjukkan jumlah data yang tidak memiliki nilai atau bernilai kosong.

Hasil yang diperoleh:

| Polutan | Jumlah Missing |
|---|---:|
| NO₂ | 148 |
| CO | 157 |
| SO₂ | 104 |

Dari hasil tersebut:

- CO memiliki jumlah missing paling banyak;
- NO₂ berada di urutan kedua;
- SO₂ memiliki jumlah missing paling sedikit.

Persentase missing dihitung dengan rumus:

$$
\text{Persentase Missing}
=
\frac{\text{Jumlah Missing}}{\text{Total Data}}
\times 100\%
$$

Dengan total 366 baris:

| Polutan | Missing | Persentase Missing |
|---|---:|---:|
| NO₂ | 148 | 40,44% |
| CO | 157 | 42,90% |
| SO₂ | 104 | 28,42% |

Artinya, SO₂ mempunyai kelengkapan data paling baik dibandingkan NO₂ dan CO.

Data missing tidak langsung dihapus pada tahap ini karena keberadaan missing value merupakan informasi penting mengenai kondisi dataset dan perlu dianalisis sebelum menentukan metode penanganannya.

---

## 3.10 No. NaNs

**No. NaNs** menunjukkan jumlah nilai `NaN` atau *Not a Number*.

Hasil Statistics View:

| Polutan | NaN |
|---|---:|
| NO₂ | 0 |
| CO | 0 |
| SO₂ | 0 |

Tidak ditemukan nilai `NaN` pada ketiga variabel polutan.

Perlu dibedakan antara `NULL` dan `NaN`:

- `NULL` → nilai tidak tersedia atau kosong;
- `NaN` → nilai khusus yang menunjukkan hasil numerik bukan angka valid.

Dalam dataset ini terdapat `NULL`, tetapi tidak terdapat `NaN`.

---

## 3.11 No. +∞s dan No. -∞s

KNIME juga memeriksa kemungkinan adanya nilai tak hingga (*infinity*).

Hasil pemeriksaan:

| Polutan | +∞ | -∞ |
|---|---:|---:|
| NO₂ | 0 | 0 |
| CO | 0 | 0 |
| SO₂ | 0 | 0 |

Dengan demikian, tidak ditemukan nilai `+∞` maupun `-∞` pada data polutan.

Pemeriksaan ini penting karena nilai infinity dapat mengganggu beberapa proses perhitungan statistik maupun analisis lanjutan.

---

## 3.12 Median

**Median** merupakan nilai tengah setelah data valid diurutkan dari nilai terkecil sampai terbesar.

Jika jumlah data valid ganjil:

$$
Median = x_{\frac{n+1}{2}}
$$

Jika jumlah data valid genap:

$$
Median =
\frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2}
$$

Pada KNIME, perhitungan median diaktifkan melalui:

```text
Calculate median values (computationally expensive)
```

Median yang diperoleh:

| Polutan | Median |
|---|---:|
| NO₂ | 0.00004283 |
| CO | 0.029526 |
| SO₂ | 0.000043 |

Median dapat dibandingkan dengan mean untuk melihat indikasi kemencengan distribusi.

Sebagai contoh:

- NO₂: mean lebih besar daripada median;
- CO: mean lebih besar daripada median;
- SO₂: mean lebih besar daripada median.

Perbandingan tersebut konsisten dengan hasil skewness yang seluruhnya bernilai positif.

---

## 3.13 Perbandingan Mean dan Median

Perbandingan mean dan median dapat memberikan gambaran awal mengenai bentuk distribusi.

| Polutan | Mean | Median | Mean > Median |
|---|---:|---:|:---:|
| NO₂ | 0.00004497 | 0.00004283 | Ya |
| CO | 0.029909 | 0.029526 | Ya |
| SO₂ | 0.000057 | 0.000043 | Ya |

Ketiga polutan mempunyai mean yang lebih besar daripada median.

Secara umum, kondisi tersebut dapat menjadi salah satu indikasi adanya kecenderungan distribusi ke kanan, yang juga terlihat dari nilai skewness positif.

Namun, mean dan median saja tidak cukup untuk menyimpulkan bentuk distribusi secara keseluruhan. Kesimpulan sebaiknya tetap didukung oleh nilai skewness dan pemeriksaan visual seperti histogram apabila diperlukan.

---

## 3.14 Ringkasan Statistik

Hasil statistik deskriptif dapat dirangkum sebagai berikut:

| Metrik | NO₂ | CO | SO₂ |
|---|---:|---:|---:|
| Data valid | 218 | 209 | 262 |
| Missing | 148 | 157 | 104 |
| Mean | 0.00004497 | 0.029909 | 0.000057 |
| Std. deviation | 0.00002479 | 0.004086 | 0.000232 |
| Skewness | 0.868 | 0.335 | 0.143 |
| Kurtosis | 0.390 | 0.524 | 2.342 |
| Median | 0.00004283 | 0.029526 | 0.000043 |

Nilai minimum dan maksimum:

| Polutan | Minimum | Maximum |
|---|---:|---:|
| NO₂ | 0.00000017 | 0.0001225 |
| CO | 0.016442 | 0.042702 |
| SO₂ | -0.000806 | 0.000926 |

Pemeriksaan nilai khusus:

| Polutan | NaN | +∞ | -∞ |
|---|---:|---:|---:|
| NO₂ | 0 | 0 | 0 |
| CO | 0 | 0 | 0 |
| SO₂ | 0 | 0 | 0 |

---

## 3.15 Interpretasi Umum

Berdasarkan hasil statistik deskriptif, terdapat beberapa temuan utama.

### 1. Kelengkapan data berbeda

Jumlah data valid tidak sama untuk setiap polutan. SO₂ memiliki data valid paling banyak, yaitu 262 data, sedangkan CO memiliki data valid paling sedikit, yaitu 209 data.

### 2. Missing value cukup besar

Persentase missing berada pada rentang sekitar 28% sampai 43%. Kondisi ini perlu diperhatikan sebelum analisis time series lebih lanjut.

### 3. Distribusi cenderung positif

Ketiga polutan memiliki skewness positif. NO₂ memiliki skewness paling tinggi, sedangkan SO₂ paling dekat dengan nol.

### 4. SO₂ memiliki kurtosis paling tinggi

Nilai kurtosis SO₂ sebesar 2.342 merupakan nilai tertinggi di antara ketiga polutan. Hal tersebut menunjukkan karakteristik ekor distribusi yang lebih kuat.

### 5. Tidak terdapat NaN dan infinity

Tidak ditemukan nilai `NaN`, `+∞`, atau `-∞` pada ketiga variabel polutan.

---

## 3.16 Catatan Mengenai Pembulatan Angka

Beberapa nilai NO₂ dan SO₂ terlihat sangat kecil. Akibatnya, nilai tersebut dapat ditampilkan sebagai `0` pada Statistics View apabila jumlah angka desimal yang ditampilkan terbatas.

Sebagai contoh:

```text
Nilai asli:
0.00004497

Tampilan dengan pembulatan terbatas:
0
```

Oleh karena itu, angka `0` pada tampilan KNIME tidak boleh langsung dianggap bahwa nilai sebenarnya adalah nol.

Untuk laporan dan perhitungan manual, gunakan angka dengan presisi yang sesuai dari data sumber.

Hal yang sama berlaku ketika membaca nilai **variance**, **standard deviation**, dan **overall sum** pada polutan yang memiliki skala kecil.

---

## 3.17 Hubungan Statistik dengan Analisis Time Series

Statistika deskriptif merupakan tahap awal sebelum analisis time series yang lebih lanjut.

Hasil statistik dapat digunakan untuk:

- memahami rentang nilai masing-masing polutan;
- melihat tingkat variasi data;
- mengetahui apakah distribusi cenderung simetris atau menceng;
- mengetahui jumlah data yang hilang;
- menentukan apakah diperlukan penanganan missing value;
- menjadi dasar untuk analisis tren berdasarkan waktu.

Namun, statistik deskriptif tidak menunjukkan perubahan nilai dari waktu ke waktu secara langsung. Untuk mengetahui pola temporal, diperlukan analisis tambahan seperti:

- grafik time series;
- analisis tren;
- moving average;
- analisis musiman apabila relevan;
- perbandingan antarperiode.

Dengan demikian, hasil pada tahap ini merupakan dasar untuk analisis time series pada tahap berikutnya.

---

## 3.18 Dokumentasi Hasil KNIME

Untuk memperkuat dokumentasi laporan, hasil pengolahan dapat dilengkapi dengan screenshot dari:

1. **Workflow KNIME** yang menunjukkan hubungan antar-node.
2. **PostgreSQL Connector** yang menunjukkan konfigurasi koneksi tanpa menampilkan password.
3. **DB Table Selector** yang menunjukkan tabel `public.air_quality`.
4. **Statistics View** yang menunjukkan hasil statistik.
5. Tampilan statistik yang memperlihatkan **No. Missings**, **No. NaNs**, dan nilai infinity.

Screenshot sebaiknya dimasukkan setelah hasil workflow final agar dokumentasi visual sesuai dengan hasil yang dibahas dalam teks.

---

## 3.19 Kesimpulan

Statistika deskriptif memberikan gambaran awal mengenai karakteristik data polutan **NO₂, CO, dan SO₂** di Kecamatan Kalitengah, Kabupaten Lamongan.

Dari total **366 baris data**, terdapat 218 data valid untuk NO₂, 209 data valid untuk CO, dan 262 data valid untuk SO₂. Dengan demikian, jumlah missing masing-masing adalah 148, 157, dan 104.

Nilai mean yang diperoleh adalah **0.00004497 untuk NO₂**, **0.029909 untuk CO**, dan **0.000057 untuk SO₂**. Sementara itu, standar deviasi masing-masing adalah **0.00002479**, **0.004086**, dan **0.000232**.

Ketiga polutan memiliki skewness positif. NO₂ mempunyai nilai skewness tertinggi yaitu **0.868**, sedangkan SO₂ mempunyai nilai paling dekat dengan nol yaitu **0.143**. Untuk kurtosis, SO₂ memiliki nilai tertinggi yaitu **2.342**.

Hasil pemeriksaan juga menunjukkan tidak terdapat **NaN**, **+∞**, maupun **-∞** pada ketiga polutan. Meskipun demikian, jumlah missing value cukup besar sehingga perlu menjadi perhatian dalam tahap analisis selanjutnya.

Secara keseluruhan, hasil statistika deskriptif memberikan dasar untuk memahami kondisi data sebelum dilanjutkan ke pembahasan **rumus statistik dan contoh perhitungan** secara lebih detail.
