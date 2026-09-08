# 3. Deskripsi Fitur

## 3.1 Pendahuluan

Dataset yang digunakan dalam penelitian ini memiliki empat fitur utama yang terdiri dari satu fitur waktu dan tiga fitur polutan udara. Fitur tersebut adalah `date`, Nitrogen Dioxide (`NO2`), Carbon Monoxide (`CO`), dan Sulfur Dioxide (`SO2`).

Tiga fitur polutan digunakan untuk menggambarkan perubahan kondisi polusi udara di Kecamatan Kalitengah, Kabupaten Lamongan, Jawa Timur. Data polutan diperoleh dari hasil pengamatan Sentinel-5P/TROPOMI selama periode pengamatan yang digunakan dalam penelitian.

Sementara itu, fitur `date` digunakan sebagai penanda waktu agar setiap nilai polutan dapat dikaitkan dengan tanggal pengamatannya. Dengan adanya fitur waktu, dataset dapat dianalisis menggunakan pendekatan time series untuk melihat perubahan nilai polutan dari waktu ke waktu.

Secara umum, hubungan antarfitur dalam dataset dapat digambarkan sebagai berikut:

- `date` menunjukkan waktu atau tanggal pengamatan;
- `NO2` menunjukkan nilai pengamatan Nitrogen Dioxide;
- `CO` menunjukkan nilai pengamatan Carbon Monoxide;
- `SO2` menunjukkan nilai pengamatan Sulfur Dioxide.

Keempat fitur tersebut menjadi dasar dalam proses Data Understanding dan selanjutnya digunakan pada tahap Eksplorasi Data.

---

## 3.2 Fitur Date

### Nama Fitur

`date`

### Deskripsi

Fitur `date` menunjukkan tanggal pengamatan untuk setiap data polutan yang terdapat dalam dataset.

Fitur ini digunakan sebagai dasar untuk mengetahui kapan suatu nilai NO2, CO, dan SO2 diamati. Kolom `date` memiliki peran penting karena penelitian ini menggunakan data berdasarkan urutan waktu.

Data memiliki rentang tanggal:

**31 Agustus 2025 sampai 31 Agustus 2026.**

Berdasarkan periode tersebut, dataset memiliki total **366 tanggal kalender**. Jumlah tersebut menunjukkan banyaknya tanggal dalam periode pengamatan dan tidak selalu sama dengan jumlah data valid pada setiap fitur polutan karena terdapat missing values.

Agar dapat digunakan dalam analisis time series, fitur `date` dikonversi menjadi tipe data `datetime`.

### Peran dalam Analisis

Fitur `date` digunakan untuk:

- mengurutkan data berdasarkan waktu;
- mengetahui tanggal awal dan akhir pengamatan;
- mengetahui periode pengamatan;
- menghubungkan nilai polutan dengan waktu pengamatan;
- melihat perubahan polutan dari waktu ke waktu;
- membuat grafik time series;
- mengidentifikasi pola atau tren temporal;
- membandingkan kondisi polutan pada periode yang berbeda.

### Karakteristik

Fitur `date` tidak digunakan sebagai nilai polutan, melainkan sebagai variabel waktu. Oleh karena itu, fitur ini berfungsi sebagai indeks atau penanda urutan dalam proses analisis time series.

Contoh penggunaan fitur `date` dalam analisis adalah:

```python
df["date"] = pd.to_datetime(df["date"])
```

Setelah dikonversi, nilai minimum dan maksimum pada fitur tanggal dapat digunakan untuk mengetahui periode pengamatan.

---

## 3.3 Fitur NO2

### Nama Fitur

`NO2`

### Nama Polutan

**Nitrogen Dioxide (NO₂)**

### Deskripsi

Nitrogen Dioxide (NO₂) merupakan salah satu polutan udara yang diamati dalam dataset.

Fitur `NO2` digunakan untuk menyimpan nilai hasil pengamatan Nitrogen Dioxide pada setiap tanggal yang tersedia. Perubahan nilai pada fitur ini dapat digunakan untuk melihat bagaimana kondisi NO₂ berubah selama periode penelitian.

Dalam konteks penelitian di Kecamatan Kalitengah, fitur NO₂ digunakan sebagai salah satu indikator untuk menggambarkan kondisi polusi udara berdasarkan data pengamatan yang tersedia.

### Sumber NO2

NO₂ umumnya berkaitan dengan proses pembakaran bahan bakar. Beberapa aktivitas yang dapat menghasilkan emisi yang berkaitan dengan NO₂ antara lain:

- kendaraan bermotor;
- pembakaran bahan bakar;
- aktivitas industri;
- pembangkit energi;
- pembakaran terbuka.

Sumber emisi tersebut tidak digunakan untuk menyimpulkan penyebab langsung dari setiap perubahan nilai pada dataset. Informasi mengenai sumber NO₂ digunakan sebagai konteks untuk memahami karakteristik polutan.

### Peran dalam Analisis

Fitur NO₂ digunakan untuk:

- mengetahui perubahan nilai NO₂ berdasarkan waktu;
- melihat pola peningkatan dan penurunan;
- mengamati tren selama periode pengamatan;
- membandingkan kondisi NO₂ antarperiode;
- melihat distribusi nilai NO₂;
- mengidentifikasi nilai minimum dan maksimum;
- menjadi salah satu parameter dalam analisis kualitas udara.

### Karakteristik Data

Berdasarkan tahap Data Understanding, fitur NO₂ memiliki:

- **218 data valid**;
- **148 missing values**.

Persentase missing values pada fitur NO₂ adalah sekitar **40,44%**.

Kondisi tersebut menunjukkan bahwa tidak semua tanggal dalam periode pengamatan memiliki nilai NO₂. Oleh karena itu, nilai yang kosong perlu tetap diperhatikan dalam proses analisis dan tidak langsung dianggap sebagai nilai nol.

### Tipe Data

Fitur `NO2` merupakan data numerik dengan tipe data `float` sehingga dapat digunakan untuk:

- perhitungan statistik;
- visualisasi;
- analisis distribusi;
- analisis tren;
- perbandingan nilai antarperiode.

---

## 3.4 Fitur CO

### Nama Fitur

`CO`

### Nama Polutan

**Carbon Monoxide (CO)**

### Deskripsi

Carbon Monoxide (CO) merupakan salah satu gas polutan yang diamati dalam dataset.

Fitur `CO` menyimpan nilai hasil pengamatan Carbon Monoxide pada setiap tanggal yang tersedia. Nilai tersebut digunakan untuk melihat perubahan kondisi CO selama periode pengamatan.

CO dapat terbentuk akibat proses pembakaran yang tidak sempurna. Oleh karena itu, keberadaan CO dapat digunakan sebagai salah satu informasi untuk menggambarkan kondisi polusi udara.

### Sumber CO

CO dapat dihasilkan dari berbagai aktivitas yang melibatkan proses pembakaran, seperti:

- kendaraan bermotor;
- pembakaran bahan bakar;
- aktivitas industri;
- pembakaran biomassa;
- pembakaran terbuka.

Seperti pada fitur NO₂, informasi sumber CO digunakan sebagai konteks umum dan tidak secara langsung digunakan untuk menentukan sumber perubahan nilai pada setiap tanggal pengamatan.

### Peran dalam Analisis

Fitur CO digunakan untuk:

- mengetahui perubahan nilai CO dari waktu ke waktu;
- mengamati pola temporal;
- melihat tren peningkatan atau penurunan;
- membandingkan nilai CO antarperiode;
- melihat distribusi data;
- mengetahui rentang nilai minimum dan maksimum;
- membantu menggambarkan kondisi polusi udara di wilayah penelitian.

### Karakteristik Data

Berdasarkan tahap Data Understanding, fitur CO memiliki:

- **209 data valid**;
- **157 missing values**.

Persentase missing values pada fitur CO adalah sekitar **42,90%**.

Dibandingkan dengan NO₂ dan SO₂, fitur CO memiliki persentase missing values paling tinggi. Hal ini menunjukkan bahwa ketersediaan data valid CO lebih rendah dibandingkan fitur polutan lainnya.

### Tipe Data

Fitur `CO` merupakan data numerik dengan tipe data `float`. Data tersebut dapat digunakan dalam proses:

- statistik deskriptif;
- visualisasi;
- analisis distribusi;
- analisis tren;
- perbandingan antarperiode.

---

## 3.5 Fitur SO2

### Nama Fitur

`SO2`

### Nama Polutan

**Sulfur Dioxide (SO₂)**

### Deskripsi

Sulfur Dioxide (SO₂) merupakan salah satu gas polutan yang diamati dalam dataset.

Fitur `SO2` digunakan untuk menyimpan nilai hasil pengamatan Sulfur Dioxide pada setiap tanggal yang tersedia. Data tersebut dapat digunakan untuk melihat perubahan nilai SO₂ selama periode penelitian.

SO₂ umumnya berkaitan dengan proses pembakaran bahan bakar atau material yang mengandung sulfur.

### Sumber SO2

SO₂ dapat berasal dari aktivitas yang menggunakan bahan bakar atau material yang mengandung sulfur, antara lain:

- pembakaran bahan bakar fosil;
- aktivitas industri;
- pembangkit energi;
- proses pembakaran tertentu;
- aktivitas yang menghasilkan emisi sulfur.

Informasi tersebut digunakan sebagai konteks umum mengenai karakteristik polutan SO₂ dan tidak secara langsung digunakan untuk menentukan sumber emisi pada Kecamatan Kalitengah.

### Peran dalam Analisis

Fitur SO₂ digunakan untuk:

- mengetahui perubahan nilai SO₂ dari waktu ke waktu;
- mengidentifikasi pola temporal;
- melihat tren peningkatan dan penurunan;
- membandingkan kondisi SO₂ antarperiode;
- melihat distribusi data;
- mengetahui nilai minimum dan maksimum;
- menjadi salah satu parameter dalam analisis kualitas udara.

### Karakteristik Data

Berdasarkan tahap Data Understanding, fitur SO₂ memiliki:

- **262 data valid**;
- **104 missing values**.

Persentase missing values pada fitur SO₂ adalah sekitar **28,42%**.

SO₂ memiliki jumlah data valid paling tinggi dibandingkan NO₂ dan CO. Dengan demikian, fitur SO₂ memiliki tingkat kelengkapan data yang lebih baik dalam dataset yang digunakan.

### Pemeriksaan Nilai Negatif

Berdasarkan hasil Data Understanding, fitur SO₂ memiliki nilai negatif pada sebagian data.

Kondisi tersebut menjadi salah satu hal yang perlu diperhatikan sebelum dilakukan analisis lanjutan. Pada tahap Data Understanding, nilai negatif tidak langsung dihapus atau diubah agar karakteristik data asli tetap dapat diperiksa.

Keputusan mengenai penanganan nilai negatif dilakukan pada tahap pengolahan data setelah dilakukan pemeriksaan lebih lanjut.

### Tipe Data

Fitur `SO2` merupakan data numerik dengan tipe data `float` sehingga dapat digunakan dalam:

- perhitungan statistik;
- visualisasi;
- analisis distribusi;
- analisis tren;
- perbandingan nilai antarperiode.

---

## 3.6 Hubungan Antarfitur

Keempat fitur dalam dataset memiliki hubungan berdasarkan waktu pengamatan.

Fitur `date` berfungsi sebagai penanda waktu, sedangkan fitur `NO2`, `CO`, dan `SO2` menyimpan nilai tiga polutan yang diamati.

Ketiga fitur polutan dapat dianalisis secara bersamaan untuk memperoleh gambaran perubahan kondisi polusi udara selama periode penelitian.

Namun, setiap polutan memiliki karakteristik dan sumber emisi yang berbeda. Oleh karena itu, perubahan nilai pada satu polutan tidak selalu menunjukkan pola perubahan yang sama pada polutan lainnya.

Sebagai contoh, peningkatan nilai CO pada suatu periode tidak selalu diikuti oleh peningkatan NO₂ atau SO₂ pada periode yang sama.

Analisis hubungan antarfitur dapat dilakukan dengan melihat:

- perubahan nilai masing-masing polutan;
- pola kenaikan dan penurunan;
- periode dengan nilai relatif tinggi;
- periode dengan nilai relatif rendah;
- tren masing-masing polutan;
- perbandingan perubahan antarpolutan;
- kemungkinan pola perubahan yang terjadi pada waktu yang sama.

Fitur `date` menjadi dasar utama dalam melihat hubungan tersebut secara temporal.

---

## 3.7 Struktur dan Tipe Data Fitur

Secara umum, struktur fitur pada dataset adalah sebagai berikut:

| Fitur | Tipe Data | Fungsi |
|---|---|---|
| `date` | datetime | Menunjukkan waktu pengamatan |
| `NO2` | float | Nilai pengamatan Nitrogen Dioxide |
| `CO` | float | Nilai pengamatan Carbon Monoxide |
| `SO2` | float | Nilai pengamatan Sulfur Dioxide |

Fitur `NO2`, `CO`, dan `SO2` merupakan data numerik sehingga dapat digunakan dalam berbagai proses analisis kuantitatif.

Sementara itu, fitur `date` digunakan sebagai variabel waktu untuk analisis time series.

Secara umum, proses pemeriksaan tipe data dapat dilakukan menggunakan:

```python
df.dtypes
```

atau:

```python
df.info()
```

Pemeriksaan tersebut penting untuk memastikan bahwa kolom `date` telah dikonversi menjadi `datetime` dan fitur polutan dapat digunakan sebagai data numerik.

---

## 3.8 Karakteristik Data Fitur

Berdasarkan hasil Data Understanding, setiap fitur polutan memiliki jumlah data valid yang berbeda.

| Fitur | Data Valid | Missing | Persentase Missing |
|---|---:|---:|---:|
| NO₂ | 218 | 148 | 40,44% |
| CO | 209 | 157 | 42,90% |
| SO₂ | 262 | 104 | 28,42% |

Perbedaan jumlah data valid menunjukkan bahwa ketersediaan data hasil observasi tidak sama untuk setiap polutan.

Dari ketiga fitur tersebut:

- SO₂ memiliki jumlah data valid paling tinggi;
- CO memiliki jumlah data valid paling rendah;
- CO memiliki persentase missing values paling tinggi;
- SO₂ memiliki persentase missing values paling rendah.

Kondisi missing values perlu diperhatikan ketika melakukan analisis dan visualisasi.

Nilai yang hilang tidak boleh langsung dianggap sebagai nilai nol karena missing values menunjukkan tidak tersedianya nilai pengamatan.

---

## 3.9 Statistik dan Rentang Nilai

Setiap fitur polutan memiliki karakteristik statistik yang berbeda.

Pemeriksaan statistik deskriptif dapat dilakukan menggunakan:

```python
df[["NO2", "CO", "SO2"]].describe()
```

Statistik deskriptif digunakan untuk melihat:

- jumlah data valid;
- nilai rata-rata;
- standar deviasi;
- nilai minimum;
- kuartil pertama;
- median;
- kuartil ketiga;
- nilai maksimum.

Berdasarkan hasil pemeriksaan sebelumnya, statistik perlu selalu dihasilkan langsung dari dataset yang digunakan agar hasil analisis sesuai dengan data aktual.

Selain statistik deskriptif, nilai minimum dan maksimum juga dapat diperiksa menggunakan:

```python
summary = pd.DataFrame({
    "Minimum": df[["NO2", "CO", "SO2"]].min(),
    "Maksimum": df[["NO2", "CO", "SO2"]].max()
})

summary
```

Pemeriksaan rentang nilai membantu memahami karakteristik masing-masing polutan sebelum dilakukan tahap pembersihan atau analisis lanjutan.

---

## 3.10 Peran Fitur dalam Analisis Time Series

Dataset ini memiliki karakteristik time series karena setiap nilai polutan dikaitkan dengan waktu pengamatan.

Dalam analisis time series:

- `date` berfungsi sebagai sumbu waktu;
- `NO2` menjadi variabel nilai polutan pertama;
- `CO` menjadi variabel nilai polutan kedua;
- `SO2` menjadi variabel nilai polutan ketiga.

Visualisasi time series dapat digunakan untuk melihat perubahan masing-masing fitur.

Contoh visualisasi:

```python
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

Proses yang sama dapat dilakukan untuk fitur CO dan SO₂.

Apabila terdapat missing values, grafik dapat memiliki bagian yang terputus. Hal tersebut merupakan representasi dari data yang tidak tersedia pada periode tertentu.

---

## 3.11 Ringkasan Peran Setiap Fitur

| Fitur | Peran Utama |
|---|---|
| `date` | Menunjukkan waktu dan urutan pengamatan |
| `NO2` | Menggambarkan perubahan nilai Nitrogen Dioxide |
| `CO` | Menggambarkan perubahan nilai Carbon Monoxide |
| `SO2` | Menggambarkan perubahan nilai Sulfur Dioxide |

Keempat fitur tersebut saling melengkapi dalam proses analisis.

Fitur `date` memberikan informasi mengenai kapan data diamati, sedangkan NO₂, CO, dan SO₂ memberikan informasi mengenai nilai polutan pada waktu tersebut.

---

## 3.12 Kesimpulan

Dataset yang digunakan dalam penelitian ini memiliki empat fitur, yaitu `date`, `NO2`, `CO`, dan `SO2`.

Fitur `date` berfungsi sebagai penanda waktu pengamatan dan memungkinkan dataset dianalisis menggunakan pendekatan time series.

Sementara itu, fitur `NO2`, `CO`, dan `SO2` merupakan fitur numerik yang digunakan untuk merepresentasikan tiga jenis polutan udara yang diamati.

Ketiga polutan memiliki karakteristik yang berbeda sehingga perubahan nilai satu polutan tidak selalu sama dengan perubahan polutan lainnya.

Berdasarkan hasil Data Understanding, jumlah data valid pada setiap fitur polutan juga berbeda. NO₂ memiliki 218 data valid, CO memiliki 209 data valid, dan SO₂ memiliki 262 data valid.

Missing values merupakan salah satu karakteristik penting dalam dataset. Persentase missing values mencapai sekitar 40,44% pada NO₂, 42,90% pada CO, dan 28,42% pada SO₂.

Selain missing values, fitur SO₂ juga memiliki nilai negatif yang perlu diperhatikan pada tahap pengolahan data berikutnya.

Secara keseluruhan, keempat fitur tersebut menjadi dasar dalam proses analisis kualitas udara Kecamatan Kalitengah. Tahap selanjutnya adalah **Eksplorasi Data**, yang digunakan untuk melihat distribusi, pola, tren, perubahan nilai, serta karakteristik hubungan antarfitur selama periode pengamatan.
