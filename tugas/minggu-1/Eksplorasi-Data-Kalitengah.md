# 5. Eksplorasi Data

Pada tahap ini dilakukan eksplorasi terhadap dataset polutan udara Kecamatan Kalitengah, Kabupaten Lamongan.

Eksplorasi dilakukan untuk memahami karakteristik data, distribusi nilai, missing value, serta perubahan nilai NO₂, CO, dan SO₂ selama periode pengamatan.

Analisis dilakukan menggunakan Python dengan library Pandas, NumPy, dan Matplotlib.

---

## 5.0 Import Library

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## 5.0.1 Membaca Dataset

```python
df = pd.read_csv("../data/polutan_kalitengah_timeseries.csv")

df.head()
```

---

## 5.1 Ukuran Dataset

Tahap pertama eksplorasi dilakukan dengan melihat jumlah baris dan kolom pada dataset.

```python
print("Jumlah baris :", df.shape[0])
print("Jumlah kolom :", df.shape[1])
```

Hasil yang diharapkan:

```text
Jumlah baris : 366
Jumlah kolom : 4
```

---

## 5.2 Informasi Dataset

Informasi dataset digunakan untuk melihat:

- nama kolom;
- tipe data;
- jumlah data non-null;
- penggunaan memory.

```python
df.info()
```

---

## 5.3 Persiapan Variabel Waktu

Kolom `date` digunakan sebagai variabel waktu. Oleh karena itu, kolom tersebut dikonversi menjadi tipe data datetime agar dapat digunakan dalam analisis time series.

```python
df["date"] = pd.to_datetime(df["date"])

df.dtypes
```

---

## 5.3.1 Melihat Periode Data

```python
print("Tanggal awal :", df["date"].min())
print("Tanggal akhir:", df["date"].max())
```

Hasil:

```text
Tanggal awal : 2025-08-31
Tanggal akhir: 2026-08-31
```

---

## 5.4 Pemeriksaan Duplikasi

Pemeriksaan duplikasi dilakukan untuk mengetahui apakah terdapat tanggal pengamatan yang tercatat lebih dari satu kali.

```python
print("Jumlah baris duplikat:", df.duplicated().sum())
print("Jumlah tanggal duplikat:", df["date"].duplicated().sum())
```

---

## 5.5 Statistik Deskriptif

Statistik deskriptif digunakan untuk mengetahui karakteristik dasar dari data numerik.

Statistik yang diamati meliputi jumlah data, rata-rata, standar deviasi, nilai minimum, kuartil, median, dan nilai maksimum.

```python
df[["NO2", "CO", "SO2"]].describe()
```

---

## 5.6 Analisis Missing Value

Missing value merupakan kondisi ketika suatu tanggal tidak memiliki nilai pengamatan yang valid.

Pemeriksaan missing value dilakukan untuk mengetahui tingkat kelengkapan data masing-masing polutan.

```python
missing = df[["NO2", "CO", "SO2"]].isnull().sum()

missing
```

Kemudian persentase missing value dihitung sebagai berikut:

```python
missing_percentage = (
    df[["NO2", "CO", "SO2"]]
    .isnull()
    .mean()
    .mul(100)
    .round(2)
)

missing_percentage
```

Hasilnya sekitar:

```text
NO2    40.44
CO     42.90
SO2    28.42
```

---

## 5.6.1 Data Valid

Jumlah data valid untuk masing-masing polutan dapat diperiksa menggunakan kode berikut:

```python
valid = df[["NO2", "CO", "SO2"]].notnull().sum()

valid
```

Hasil:

```text
NO2    218
CO     209
SO2    262
```

---

## 5.6.2 Visualisasi Missing Value

Visualisasi digunakan untuk membandingkan jumlah missing value pada masing-masing polutan.

```python
missing.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Jumlah Missing Value Setiap Polutan")
plt.xlabel("Polutan")
plt.ylabel("Jumlah Missing Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

---

## 5.7 Analisis Time Series NO₂

Visualisasi time series digunakan untuk melihat perubahan nilai NO₂ selama periode pengamatan.

Nilai kosong tidak diubah menjadi nol sehingga bagian yang tidak memiliki data tetap ditampilkan sebagai gap pada grafik.

```python
plt.figure(figsize=(12, 5))

plt.plot(
    df["date"],
    df["NO2"],
    marker=".",
    linewidth=1
)

plt.title("Time Series NO₂ Kecamatan Kalitengah")
plt.xlabel("Tanggal")
plt.ylabel("NO₂")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 5.7.1 Analisis Time Series CO

```python
plt.figure(figsize=(12, 5))

plt.plot(
    df["date"],
    df["CO"],
    marker=".",
    linewidth=1
)

plt.title("Time Series CO Kecamatan Kalitengah")
plt.xlabel("Tanggal")
plt.ylabel("CO")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 5.7.2 Analisis Time Series SO₂

```python
plt.figure(figsize=(12, 5))

plt.plot(
    df["date"],
    df["SO2"],
    marker=".",
    linewidth=1
)

plt.title("Time Series SO₂ Kecamatan Kalitengah")
plt.xlabel("Tanggal")
plt.ylabel("SO₂")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 5.8 Nilai Minimum dan Maksimum

Analisis nilai minimum dan maksimum dilakukan untuk mengetahui rentang nilai masing-masing polutan selama periode pengamatan.

```python
summary_min_max = pd.DataFrame({
    "Minimum": df[["NO2", "CO", "SO2"]].min(),
    "Maksimum": df[["NO2", "CO", "SO2"]].max()
})

summary_min_max
```

---

## 5.8.1 Tanggal Nilai Tertinggi

Analisis ini tidak hanya mencari nilai tertinggi, tetapi juga mengetahui kapan nilai tersebut terjadi.

```python
for pollutant in ["NO2", "CO", "SO2"]:
    idx = df[pollutant].idxmax()

    print(f"{pollutant}")
    print("Tanggal :", df.loc[idx, "date"].date())
    print("Nilai   :", df.loc[idx, pollutant])
    print()
```

---

## 5.8.2 Tanggal Nilai Terendah

```python
for pollutant in ["NO2", "CO", "SO2"]:
    idx = df[pollutant].idxmin()

    print(f"{pollutant}")
    print("Tanggal :", df.loc[idx, "date"].date())
    print("Nilai   :", df.loc[idx, pollutant])
    print()
```

---

## 5.9 Pemeriksaan Nilai Negatif

Pemeriksaan nilai negatif dilakukan untuk mengetahui apakah terdapat nilai yang berada di bawah nol.

Secara interpretasi fisik, konsentrasi polutan tidak diharapkan bernilai negatif. Oleh karena itu, nilai negatif yang ditemukan perlu diperiksa lebih lanjut pada tahap preprocessing.

Pada tahap eksplorasi, nilai tersebut tidak langsung dihapus agar informasi dari data asli tetap dipertahankan.

```python
negative_values = {}

for pollutant in ["NO2", "CO", "SO2"]:
    negative_values[pollutant] = (df[pollutant] < 0).sum()

pd.Series(negative_values)
```

---

## 5.10 Kesimpulan Eksplorasi Data

Berdasarkan hasil eksplorasi, dataset polutan Kecamatan Kalitengah memiliki 366 tanggal pengamatan dengan empat variabel utama, yaitu `date`, `NO2`, `CO`, dan `SO2`.

Ketiga variabel polutan memiliki jumlah data valid yang berbeda. NO₂ memiliki 218 data valid, CO memiliki 209 data valid, dan SO₂ memiliki 262 data valid.

Hasil pemeriksaan menunjukkan adanya missing value pada ketiga variabel polutan. Persentase missing value masing-masing adalah sekitar 40,44% untuk NO₂, 42,90% untuk CO, dan 28,42% untuk SO₂.

Visualisasi time series digunakan untuk melihat perubahan nilai NO₂, CO, dan SO₂ selama periode 31 Agustus 2025 sampai 31 Agustus 2026.

Eksplorasi juga menemukan adanya nilai negatif pada variabel SO₂. Nilai tersebut tidak langsung dihapus pada tahap eksplorasi karena diperlukan pemeriksaan lebih lanjut untuk menentukan metode penanganannya.

Hasil eksplorasi ini menjadi dasar untuk tahap pengolahan data berikutnya, terutama dalam menangani missing value, memeriksa nilai yang tidak normal, dan mempersiapkan data untuk analisis lebih lanjut.
