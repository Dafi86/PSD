# 2. Data Understanding 

# Data Understanding

## Analisis dan Pemantauan Kualitas Udara Kecamatan Kalitengah

Tahap Data Understanding merupakan tahap untuk memahami karakteristik data kualitas udara yang telah dikumpulkan pada wilayah Kecamatan Kalitengah, Kabupaten Lamongan, Jawa Timur.

Data yang digunakan merupakan data konsentrasi polutan udara yang terdiri dari Nitrogen Dioksida (NO2), Karbon Monoksida (CO), dan Sulfur Dioksida (SO2). Data dikumpulkan dalam periode satu tahun, yaitu dari 31 Agustus 2025 sampai 31 Agustus 2026.

Tahap ini dilakukan untuk mengetahui struktur data, periode pengamatan, karakteristik setiap variabel, statistik deskriptif, jumlah data yang tersedia, serta kondisi missing values sebelum dilakukan proses eksplorasi dan pengolahan data lebih lanjut.
```

---

# 1. Import Library

## Cell 2 — Markdown

## 1. Import Library

Library Python digunakan untuk membantu proses pembacaan, pemeriksaan, pengolahan, dan visualisasi dataset.
```

## Cell 3 — Code

```
```

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

# 2. Membaca Dataset

## Cell 4 — Markdown

## 2. Membaca Dataset

Dataset kualitas udara Kecamatan Kalitengah disimpan dalam format CSV. Dataset tersebut berisi tanggal pengamatan serta nilai konsentrasi NO2, CO, dan SO2.

File dataset dibaca menggunakan library pandas.
```

## Cell 5 — Code

```
```

```
# Membaca dataset
df = pd.read_csv("../data/polutan_kalitengah_timeseries.csv")

# Menampilkan lima data pertama
df.head()
```

> Pastikan posisi Notebook:

```
```

```
tugas/minggu-1/data-understanding.ipynb
```

dan CSV:

```
```

```
tugas/data/polutan_kalitengah_timeseries.csv
```

Maka path `../data/...` sudah benar.

---

# 3. Pemeriksaan Awal Dataset

## Cell 6 — Markdown

## 3. Pemeriksaan Awal Dataset

Pemeriksaan awal dilakukan untuk mengetahui bentuk dan ukuran dataset. Informasi ini membantu mengetahui jumlah data yang tersedia serta jumlah variabel yang terdapat dalam dataset.
```

## Cell 7 — Code

```
```

```
print("Jumlah baris  :", df.shape[0])
print("Jumlah kolom  :", df.shape[1])
```

Untuk dataset kamu, seharusnya:

```
```

```
Jumlah baris : 366
Jumlah kolom : 4
```

Artinya terdapat **366 tanggal kalender** dan 4 kolom, yaitu `date`, `NO2`, `CO`, dan `SO2`.

---

# 4. Struktur Dataset

## Cell 8 — Markdown

## 4. Struktur Dataset

Struktur dataset diperiksa menggunakan fungsi `info()` untuk mengetahui nama kolom, jumlah data yang tersedia pada setiap kolom, dan tipe data yang digunakan.
```

## Cell 9 — Code

```
```

```
df.info()
```

Kemudian cek nama kolom:

## Cell 10 — Code

```
```

```
df.columns
```

Target:

```
```

```
Index(['date', 'NO2', 'CO', 'SO2'], dtype='object')
```

---

# 5. Mengubah Format Tanggal

## Cell 11 — Markdown

## 5. Konversi Kolom Tanggal

Kolom `date` digunakan sebagai informasi waktu pengamatan. Agar dapat digunakan dalam analisis time series, kolom tersebut dikonversi dari format teks menjadi tipe data datetime.
```

## Cell 12 — Code

```
```

```
df["date"] = pd.to_datetime(df["date"])

df.dtypes
```

---

# 6. Periode Pengamatan

## Cell 13 — Markdown

## 6. Periode Pengamatan

Periode pengamatan digunakan untuk mengetahui tanggal awal dan tanggal akhir data yang tersedia.
```

## Cell 14 — Code

```
```

```
print("Tanggal awal  :", df["date"].min().date())
print("Tanggal akhir :", df["date"].max().date())
print("Jumlah tanggal:", df["date"].nunique())
```

Berdasarkan dataset yang kita buat, hasilnya seharusnya:

```
```

```
Tanggal awal  : 2025-08-31
Tanggal akhir : 2026-08-31
Jumlah tanggal: 366
```

---

# 7. Pemeriksaan Duplikasi Tanggal

## Cell 15 — Markdown

## 7. Pemeriksaan Duplikasi

Pemeriksaan duplikasi dilakukan untuk mengetahui apakah terdapat tanggal pengamatan yang tercatat lebih dari satu kali.
```

## Cell 16 — Code

```
```

```
duplicate_dates = df["date"].duplicated().sum()

print("Jumlah tanggal duplikat:", duplicate_dates)
```

---

# 8. Statistik Deskriptif

## Cell 17 — Markdown

## 8. Statistik Deskriptif

Statistik deskriptif digunakan untuk mengetahui karakteristik dasar dari masing-masing variabel polutan. Statistik yang diperiksa meliputi jumlah data valid, nilai rata-rata, standar deviasi, nilai minimum, kuartil, median, dan nilai maksimum.
```

## Cell 18 — Code

```
```

```
df[["NO2", "CO", "SO2"]].describe()
```

Dari data yang sebelumnya kita dapatkan, karakteristiknya adalah:

| StatistikNO2COSO2 |            |          |           |
| ----------------- | ---------- | -------- | --------- |
| Count             | 218        | 209      | 262       |
| Mean              | 0.00004497 | 0.029909 | 0.000057  |
| Std               | 0.00002479 | 0.004086 | 0.000232  |
| Min               | 0.00000017 | 0.016442 | -0.000806 |
| 25%               | 0.00002444 | 0.027155 | -0.000063 |
| 50%               | 0.00004283 | 0.029526 | 0.000043  |
| 75%               | 0.00005938 | 0.032214 | 0.000184  |
| Max               | 0.00012250 | 0.042702 | 0.000926  |

**Catatan:** nilai statistik tersebut sebaiknya tetap dihasilkan langsung oleh Notebook menggunakan `describe()`, sehingga laporan selalu mengikuti dataset aktual.

---

# 9. Missing Values

## Cell 19 — Markdown

## 9. Pemeriksaan Missing Values

Missing values merupakan data yang tidak memiliki nilai pada suatu variabel. Pemeriksaan missing values penting dilakukan karena data yang tidak tersedia dapat memengaruhi proses analisis dan visualisasi.

Pada tahap Data Understanding, missing values tidak langsung dihapus atau diisi. Kondisinya terlebih dahulu diperiksa untuk mengetahui tingkat kelengkapan data.
```

## Cell 20 — Code

```
```

```
missing = df.isna().sum()

missing
```

Hasil dataset kamu:

```
```

```
date      0
NO2     148
CO      157
SO2     104
```

---

# 10. Persentase Missing Values

## Cell 21 — Markdown

### Persentase Missing Values

Persentase missing values dihitung untuk mengetahui proporsi data yang tidak tersedia pada masing-masing variabel polutan.
```

## Cell 22 — Code

```
```

```
missing_percentage = (
    df[["NO2", "CO", "SO2"]].isna().mean() * 100
).round(2)

missing_percentage
```

Hasil:

| VariabelMissingPersentase |     |        |
| ------------------------- | --- | ------ |
| NO2                       | 148 | 40.44% |
| CO                        | 157 | 42.90% |
| SO2                       | 104 | 28.42% |

Jadi, **SO2 memiliki kelengkapan data paling tinggi**, sedangkan CO memiliki persentase missing value paling tinggi.

---

# 11. Jumlah Data Valid

## Cell 23 — Markdown

## 11. Jumlah Data Valid

Selain mengetahui jumlah missing values, perlu diketahui jumlah observasi yang memiliki nilai valid pada masing-masing variabel polutan.
```

## Cell 24 — Code

```
```

```
valid_data = df[["NO2", "CO", "SO2"]].count()

valid_data
```

Hasil:

```
```

```
NO2    218
CO     209
SO2    262
```

Penting: **366 adalah jumlah tanggal kalender, bukan jumlah observasi valid untuk setiap polutan.**

---

# 12. Nilai Minimum dan Maksimum

## Cell 25 — Markdown

## 12. Nilai Minimum dan Maksimum

Nilai minimum dan maksimum digunakan untuk mengetahui rentang nilai yang terdapat pada masing-masing variabel polutan.
```

## Cell 26 — Code

```
```

```
summary = pd.DataFrame({
    "Minimum": df[["NO2", "CO", "SO2"]].min(),
    "Maksimum": df[["NO2", "CO", "SO2"]].max()
})

summary
```

---

# 13. Pemeriksaan Nilai Negatif

Ini penting khusus untuk dataset kamu karena **SO2 memiliki nilai negatif**.

## Cell 27 — Markdown

## 13. Pemeriksaan Nilai Negatif

Pemeriksaan nilai negatif dilakukan untuk mengetahui apakah terdapat nilai di bawah nol pada data polutan.

Secara fisik, konsentrasi polutan umumnya tidak diinterpretasikan sebagai nilai negatif. Oleh karena itu, nilai negatif perlu diperiksa lebih lanjut sebelum dilakukan analisis lanjutan.

Nilai negatif pada dataset tidak langsung dihapus pada tahap Data Understanding. Hal tersebut dilakukan agar data asli tetap dapat ditelusuri dan keputusan pembersihan data dapat dilakukan secara terkontrol pada tahap berikutnya.
```

## Cell 28 — Code

```
```

```
negative_values = {
    "NO2": (df["NO2"] < 0).sum(),
    "CO": (df["CO"] < 0).sum(),
    "SO2": (df["SO2"] < 0).sum()
}

negative_values
```

Untuk dataset kamu, kemungkinan yang perlu diperhatikan terutama adalah **SO2**.

---

# 14. Melihat Data Secara Keseluruhan

## Cell 29 — Markdown

## 14. Menampilkan Dataset

Dataset secara keseluruhan dapat ditampilkan untuk memastikan bahwa struktur data telah sesuai dengan kebutuhan analisis.
```

## Cell 30 — Code

```
```

```
df
```

---

# 15. Time Series NO2

## Cell 31 — Markdown

## 15. Visualisasi Time Series NO2

Visualisasi time series digunakan untuk melihat perubahan konsentrasi NO2 sepanjang periode pengamatan.

Nilai yang kosong akan menghasilkan bagian grafik yang terputus. Kondisi tersebut merupakan representasi dari missing values pada dataset.
```

## Cell 32 — Code

```
```

```
plt.figure(figsize=(12, 5))

plt.plot(
    df["date"],
    df["NO2"]
)

plt.title("Time Series NO2 Kecamatan Kalitengah")
plt.xlabel("Tanggal")
plt.ylabel("Konsentrasi NO2")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

---

# 16. Time Series CO

## Cell 33 — Markdown

## 16. Visualisasi Time Series CO

Visualisasi berikut menunjukkan perubahan konsentrasi CO selama periode pengamatan.
```

## Cell 34 — Code

```
```

```
plt.figure(figsize=(12, 5))

plt.plot(
    df["date"],
    df["CO"]
)

plt.title("Time Series CO Kecamatan Kalitengah")
plt.xlabel("Tanggal")
plt.ylabel("Konsentrasi CO")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

---

# 17. Time Series SO2

## Cell 35 — Markdown

## 17. Visualisasi Time Series SO2

Visualisasi berikut menunjukkan perubahan konsentrasi SO2 selama periode pengamatan.

Adanya nilai negatif pada sebagian data perlu menjadi perhatian pada tahap pemeriksaan dan pembersihan data berikutnya.
```

## Cell 36 — Code

```
```

```
plt.figure(figsize=(12, 5))

plt.plot(
    df["date"],
    df["SO2"]
)

plt.title("Time Series SO2 Kecamatan Kalitengah")
plt.xlabel("Tanggal")
plt.ylabel("Konsentrasi SO2")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

---

# 18. Ringkasan Data Understanding

## Cell 37 — Markdown

# Kesimpulan Data Understanding

Berdasarkan pemeriksaan yang telah dilakukan, dataset kualitas udara Kecamatan Kalitengah memiliki periode pengamatan dari **31 Agustus 2025 sampai 31 Agustus 2026** dengan total **366 tanggal kalender**.

Dataset terdiri dari empat kolom, yaitu `date`, `NO2`, `CO`, dan `SO2`. Variabel `date` digunakan sebagai informasi waktu, sedangkan NO2, CO, dan SO2 merupakan variabel polutan yang dianalisis.

Jumlah data valid pada masing-masing polutan berbeda. NO2 memiliki 218 data valid, CO memiliki 209 data valid, dan SO2 memiliki 262 data valid. Dengan demikian, terdapat missing values pada ketiga variabel tersebut.

Persentase missing values adalah sekitar **40,44% pada NO2, 42,90% pada CO, dan 28,42% pada SO2**. Kondisi tersebut perlu diperhatikan dalam proses analisis berikutnya karena dapat memengaruhi hasil statistik dan visualisasi.

Pemeriksaan rentang nilai juga menunjukkan adanya nilai negatif pada variabel SO2. Nilai tersebut tidak langsung dihapus pada tahap Data Understanding karena perlu dilakukan pemeriksaan lebih lanjut terhadap karakteristik dan sumber data sebelum menentukan metode pembersihan yang tepat.

Secara keseluruhan, tahap Data Understanding memberikan gambaran awal mengenai struktur, periode, kelengkapan, distribusi dasar, dan karakteristik data kualitas udara Kecamatan Kalitengah. Hasil ini selanjutnya dapat digunakan sebagai dasar untuk tahap **Eksplorasi Data** dan pengolahan lebih lanjut.
```