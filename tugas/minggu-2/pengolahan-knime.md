# 2. Pengolahan Data dengan KNIME

## Pendahuluan

Setelah data kualitas udara berhasil dipindahkan dari file CSV ke **PostgreSQL Aiven**, tahap berikutnya adalah melakukan pengolahan data menggunakan **KNIME Analytics Platform**.

Pada tahap ini, KNIME digunakan untuk membaca data langsung dari database PostgreSQL dan menghasilkan **statistik deskriptif**. Penggunaan KNIME membantu proses analisis menjadi lebih terstruktur karena data tidak perlu dipindahkan kembali secara manual ke spreadsheet.

Data yang dianalisis adalah data kualitas udara Kecamatan Kalitengah, Kabupaten Lamongan dengan variabel:

- **NO₂** — Nitrogen Dioksida
- **CO** — Karbon Monoksida
- **SO₂** — Sulfur Dioksida

Periode data adalah **31 Agustus 2025 sampai 31 Agustus 2026**, dengan total **366 baris/tanggal kalender**.

---

## 2.1 Tujuan Pengolahan Data dengan KNIME

Pengolahan menggunakan KNIME dilakukan untuk:

1. Menghubungkan KNIME dengan database PostgreSQL Aiven.
2. Mengambil tabel `public.air_quality` dari database.
3. Membaca data ke dalam workflow KNIME.
4. Menghasilkan statistik deskriptif.
5. Mengetahui jumlah data valid dan data missing.
6. Mengamati karakteristik distribusi data melalui **skewness** dan **kurtosis**.
7. Memastikan tidak terdapat nilai `NaN`, `+∞`, atau `-∞` pada data numerik.

Hasil dari tahap ini digunakan sebagai dasar untuk analisis statistik pada tahap berikutnya.

---

## 2.2 Alur Workflow KNIME

Workflow dibuat sederhana agar setiap tahap pengolahan dapat terlihat dengan jelas.

Alur yang digunakan adalah:

```text
PostgreSQL Connector
        ↓
DB Table Selector
        ↓
DB Reader
        ↓
Statistics
```

Secara konseptual, alurnya adalah:

```text
PostgreSQL Aiven
       │
       ▼
PostgreSQL Connector
       │
       ▼
DB Table Selector
       │
       ▼
DB Reader
       │
       ▼
Statistics
       │
       ▼
Statistik Deskriptif
```

Setiap node memiliki fungsi yang berbeda dan saling terhubung untuk menghasilkan output statistik.

---

## 2.3 PostgreSQL Connector

Node pertama yang digunakan adalah **PostgreSQL Connector**.

Node ini berfungsi untuk membuat koneksi antara **KNIME Analytics Platform** dengan database PostgreSQL yang berada di Aiven.

Informasi koneksi yang digunakan:

| Pengaturan | Nilai |
|---|---|
| Database | `defaultdb` |
| Host | `pg-1af3ba92-analisis-time-series.a.aivencloud.com` |
| Port | `15751` |
| User | `avnadmin` |
| SSL Mode | `require` |

Password database tidak dicantumkan dalam dokumentasi karena merupakan informasi kredensial yang harus dijaga kerahasiaannya.

### Tujuan koneksi

Koneksi ini memungkinkan KNIME mengakses data yang sebelumnya telah disimpan di PostgreSQL tanpa perlu melakukan import file CSV secara langsung.

Setelah konfigurasi selesai, koneksi diuji untuk memastikan KNIME dapat berkomunikasi dengan database Aiven.

Jika koneksi berhasil, node PostgreSQL Connector dapat digunakan sebagai sumber koneksi untuk node database berikutnya.

---

## 2.4 DB Table Selector

Setelah koneksi database berhasil dibuat, node berikutnya adalah **DB Table Selector**.

Node ini digunakan untuk memilih tabel yang akan digunakan dalam proses analisis.

Tabel yang digunakan adalah:

```text
public.air_quality
```

Struktur pemilihannya:

```text
defaultdb
    ↓
public
    ↓
air_quality
```

Tabel `air_quality` memiliki kolom:

| Kolom | Keterangan |
|---|---|
| `id` | Identitas setiap baris data |
| `date` | Tanggal pengamatan |
| `no2` | Nilai polutan NO₂ |
| `co` | Nilai polutan CO |
| `so2` | Nilai polutan SO₂ |

Setelah tabel `air_quality` dipilih, node dijalankan untuk memastikan tabel dapat diakses oleh KNIME.

---

## 2.5 DB Reader

Node **DB Reader** digunakan untuk membaca data dari tabel yang telah dipilih menggunakan DB Table Selector.

Alur pada tahap ini:

```text
PostgreSQL Aiven
       ↓
DB Table Selector
       ↓
DB Reader
```

DB Reader mengambil data dari database dan meneruskannya ke node **Statistics**.

Dengan pendekatan ini, KNIME bekerja langsung dengan data yang tersimpan pada database sehingga proses pengolahan menjadi lebih terintegrasi.

### Data yang dibaca

Data yang diteruskan dari DB Reader memiliki struktur:

```text
id
date
no2
co
so2
```

Jumlah baris yang dibaca adalah **366 baris**.

Nilai kosong pada kolom polutan tetap dipertahankan sebagai data missing.

---

## 2.6 Statistics

Node terakhir yang digunakan adalah **Statistics**.

Node ini digunakan untuk menghasilkan **statistik deskriptif** dari data yang telah dibaca oleh DB Reader.

Statistik deskriptif digunakan untuk memberikan gambaran umum mengenai karakteristik data tanpa melakukan pemodelan prediktif.

Beberapa informasi yang dapat diperoleh antara lain:

- jumlah data;
- nilai minimum;
- nilai maksimum;
- mean;
- median;
- standar deviasi;
- skewness;
- kurtosis;
- jumlah data missing;
- jumlah NaN;
- jumlah `+∞`;
- jumlah `-∞`.

### Pengaturan median

Pada konfigurasi Statistics, pilihan:

```text
Calculate median values (computationally expensive)
```

diaktifkan.

Pengaturan tersebut diperlukan agar KNIME menghitung nilai **median** selain statistik lainnya.

### Pengelompokan kolom

Kolom `id` dan `date` merupakan informasi identitas dan waktu, sedangkan `no2`, `co`, dan `so2` merupakan variabel numerik yang menjadi fokus analisis statistik.

---

## 2.7 Alur Lengkap Workflow

Keseluruhan workflow dapat digambarkan sebagai berikut:

```text
┌──────────────────────────┐
│ PostgreSQL Connector     │
│ Menghubungkan KNIME      │
│ dengan PostgreSQL Aiven  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ DB Table Selector        │
│ Memilih air_quality      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ DB Reader                │
│ Membaca data tabel       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Statistics               │
│ Statistik deskriptif     │
└──────────────────────────┘
```

Workflow tersebut menunjukkan bahwa data berasal dari PostgreSQL, kemudian dipilih, dibaca, dan akhirnya dianalisis menggunakan Statistics.

---

## 2.8 Hasil Statistics View

Setelah node **Statistics** berhasil dijalankan, hasil analisis dapat dilihat melalui **Statistics View**.

Hasil yang diperoleh menunjukkan beberapa metrik statistik untuk variabel numerik.

| Kolom | Min | Max | Mean | Std. deviation | Skewness | Kurtosis | Missing |
|---|---:|---:|---:|---:|---:|---:|---:|
| NO₂ | 0* | 0* | 0* | 0* | 0.868 | 0.390 | 148 |
| CO | 0.016 | 0.043 | 0.030 | 0.004 | 0.335 | 0.524 | 157 |
| SO₂ | -0.001 | 0.001 | 0* | 0* | 0.143 | 2.342 | 104 |

> **Catatan:** tanda `*` menunjukkan bahwa nilai terlihat sebagai `0` karena pembulatan pada tampilan Statistics View. Hal tersebut tidak berarti seluruh nilai aslinya benar-benar nol.

Khusus NO₂, nilai pada data asli berada pada skala yang sangat kecil, yaitu sekitar `10⁻⁵`. Jika tampilan statistik menggunakan jumlah digit desimal yang terbatas, nilai tersebut dapat terlihat sebagai `0`.

Hal yang sama perlu diperhatikan pada beberapa statistik SO₂.

---

## 2.9 Interpretasi Statistik Dasar

### 2.9.1 Minimum dan Maksimum

Nilai **minimum** menunjukkan nilai terendah yang ditemukan pada data valid, sedangkan nilai **maksimum** menunjukkan nilai tertinggi.

Contohnya pada CO:

```text
Minimum = 0.016
Maximum = 0.043
```

Artinya, berdasarkan data valid yang tersedia, nilai CO berada pada rentang tersebut.

Untuk NO₂ dan SO₂, interpretasi minimum dan maksimum harus mempertimbangkan skala angka dan pembulatan pada Statistics View.

---

### 2.9.2 Mean

**Mean** atau rata-rata dihitung dari jumlah seluruh nilai valid dibagi jumlah data valid.

Secara matematis:

```text
Mean = Σx / n
```

dengan:

- `Σx` = jumlah seluruh nilai data valid;
- `n` = jumlah data valid.

Data `NULL` tidak termasuk dalam perhitungan nilai rata-rata.

---

### 2.9.3 Median

**Median** merupakan nilai tengah setelah data valid diurutkan.

Jika jumlah data genap:

```text
Median = (nilai tengah 1 + nilai tengah 2) / 2
```

Jika jumlah data ganjil:

```text
Median = nilai tengah
```

Median berguna sebagai ukuran pemusatan yang relatif tidak terlalu dipengaruhi oleh nilai ekstrem.

Pada workflow ini, perhitungan median diaktifkan melalui opsi:

```text
Calculate median values (computationally expensive)
```

---

### 2.9.4 Standard Deviation

**Standard deviation** atau standar deviasi digunakan untuk melihat seberapa jauh data menyebar dari nilai rata-ratanya.

Secara sederhana:

- standar deviasi kecil → data cenderung lebih dekat dengan rata-rata;
- standar deviasi besar → data memiliki penyebaran yang lebih besar.

Standar deviasi perlu dibaca bersama mean agar karakteristik penyebaran data dapat dipahami dengan lebih baik.

---

## 2.10 Jumlah Data dan Missing Values

Setiap variabel memiliki total **366 baris**, tetapi jumlah nilai valid berbeda.

| Polutan | Total Baris | Data Valid | Missing |
|---|---:|---:|---:|
| NO₂ | 366 | 218 | 148 |
| CO | 366 | 209 | 157 |
| SO₂ | 366 | 262 | 104 |

Jumlah missing dapat dihitung dengan:

```text
Missing = Total Baris - Data Valid
```

Contoh untuk NO₂:

```text
366 - 218 = 148
```

Contoh untuk CO:

```text
366 - 209 = 157
```

Contoh untuk SO₂:

```text
366 - 262 = 104
```

Hal ini menunjukkan bahwa SO₂ memiliki data valid paling banyak, sedangkan CO memiliki jumlah data missing paling banyak.

---

## 2.11 Persentase Data Missing

Persentase missing digunakan untuk mengetahui seberapa besar bagian data yang tidak tersedia.

Rumus:

```text
Persentase Missing = (Jumlah Missing / Total Data) × 100%
```

Hasilnya:

| Polutan | Missing | Persentase Missing |
|---|---:|---:|
| NO₂ | 148 | 40,44% |
| CO | 157 | 42,90% |
| SO₂ | 104 | 28,42% |

### Interpretasi

Berdasarkan hasil tersebut:

- **NO₂** memiliki sekitar 40,44% data missing.
- **CO** memiliki sekitar 42,90% data missing.
- **SO₂** memiliki sekitar 28,42% data missing.

Dengan demikian, SO₂ memiliki kelengkapan data paling baik dibandingkan NO₂ dan CO dalam dataset ini.

Data missing tidak langsung dihapus pada tahap ini karena kondisi tersebut merupakan bagian dari karakteristik dataset yang perlu diketahui sebelum menentukan metode penanganan missing value.

---

## 2.12 Analisis Skewness

**Skewness** digunakan untuk melihat tingkat kemencengan atau ketidaksimetrisan distribusi data.

Hasil yang diperoleh:

| Polutan | Skewness |
|---|---:|
| NO₂ | 0.868 |
| CO | 0.335 |
| SO₂ | 0.143 |

Ketiga nilai tersebut bernilai positif.

Secara umum, skewness positif menunjukkan bahwa distribusi data memiliki kecenderungan ekor yang lebih panjang ke arah kanan.

Perbandingan nilai:

```text
NO₂ > CO > SO₂
```

NO₂ memiliki nilai skewness paling besar, sehingga distribusinya menunjukkan kemencengan positif yang paling kuat dibandingkan CO dan SO₂.

SO₂ memiliki nilai paling dekat dengan nol, sehingga distribusinya relatif lebih simetris dibandingkan dua polutan lainnya.

Interpretasi skewness tetap perlu dilakukan bersama pemeriksaan distribusi data dan jumlah data valid.

---

## 2.13 Analisis Kurtosis

**Kurtosis** digunakan untuk menggambarkan karakteristik ekor distribusi dan tingkat konsentrasi data dibandingkan distribusi normal, tergantung definisi kurtosis yang digunakan oleh perangkat lunak.

Hasil yang diperoleh:

| Polutan | Kurtosis |
|---|---:|
| NO₂ | 0.390 |
| CO | 0.524 |
| SO₂ | 2.342 |

SO₂ memiliki nilai kurtosis paling tinggi.

Hal ini menunjukkan bahwa distribusi SO₂ memiliki karakteristik ekor atau konsentrasi nilai yang lebih kuat dibandingkan NO₂ dan CO.

Karena interpretasi kurtosis dapat bergantung pada definisi yang digunakan oleh software, hasil ini sebaiknya digunakan sebagai indikasi karakteristik distribusi dan tidak berdiri sendiri sebagai kesimpulan akhir.

---

## 2.14 Pemeriksaan NaN dan Infinity

Selain missing value, Statistics View juga dapat digunakan untuk memeriksa nilai khusus seperti:

- `NaN` (Not a Number);
- `+∞` (positive infinity);
- `-∞` (negative infinity).

Hasil pemeriksaan:

| Polutan | NaN | +∞ | -∞ |
|---|---:|---:|---:|
| NO₂ | 0 | 0 | 0 |
| CO | 0 | 0 | 0 |
| SO₂ | 0 | 0 | 0 |

Hasil tersebut menunjukkan bahwa tidak ditemukan nilai `NaN`, `+∞`, maupun `-∞` pada ketiga variabel polutan.

Perlu dibedakan antara `NULL` dan `NaN`:

- **NULL** berarti nilai tidak tersedia/kosong.
- **NaN** merupakan nilai khusus yang menunjukkan hasil numerik yang bukan angka valid.

Dalam dataset ini terdapat `NULL`, tetapi tidak terdapat `NaN` maupun infinity berdasarkan hasil Statistics View.

---

## 2.15 Ringkasan Hasil Analisis

Ringkasan hasil pengolahan KNIME dapat ditampilkan sebagai berikut:

| Aspek | NO₂ | CO | SO₂ |
|---|---:|---:|---:|
| Total baris | 366 | 366 | 366 |
| Data valid | 218 | 209 | 262 |
| Missing | 148 | 157 | 104 |
| Missing (%) | 40,44% | 42,90% | 28,42% |
| Skewness | 0.868 | 0.335 | 0.143 |
| Kurtosis | 0.390 | 0.524 | 2.342 |
| NaN | 0 | 0 | 0 |
| +∞ | 0 | 0 | 0 |
| -∞ | 0 | 0 | 0 |

Dari tabel tersebut dapat dilihat bahwa:

1. Dataset memiliki 366 tanggal untuk setiap polutan.
2. Jumlah data valid berbeda karena terdapat missing value.
3. SO₂ memiliki jumlah data valid paling banyak.
4. CO memiliki jumlah missing paling banyak.
5. NO₂ memiliki skewness paling tinggi.
6. SO₂ memiliki kurtosis paling tinggi.
7. Tidak terdapat NaN maupun nilai infinity.

---

## 2.16 Catatan Penting tentang Data Missing

Data missing yang ditemukan tidak langsung dihapus pada tahap ini.

Keputusan tersebut dilakukan karena menghapus data secara langsung dapat mengurangi jumlah observasi dan berpotensi mengubah karakteristik time series.

Sebelum menentukan metode penanganan missing value, perlu dipertimbangkan:

- jumlah missing;
- posisi missing berdasarkan tanggal;
- pola missing;
- karakteristik masing-masing polutan;
- tujuan analisis berikutnya.

Oleh karena itu, tahap selanjutnya dapat digunakan untuk melakukan pemeriksaan lebih lanjut terhadap pola data dan menentukan metode pengolahan missing value yang sesuai.

---

## 2.17 Dokumentasi Workflow

Untuk dokumentasi laporan, workflow KNIME sebaiknya ditampilkan dengan urutan node:

```text
PostgreSQL Connector
        ↓
DB Table Selector
        ↓
DB Reader
        ↓
Statistics
```

Dokumentasi dapat dilengkapi dengan:

1. Screenshot konfigurasi PostgreSQL Connector.
2. Screenshot pemilihan tabel `public.air_quality`.
3. Screenshot workflow KNIME secara keseluruhan.
4. Screenshot Statistics View.
5. Screenshot hasil statistik yang menampilkan missing value.

Screenshot digunakan sebagai bukti visual bahwa proses pengolahan benar-benar dilakukan menggunakan KNIME.

> **Catatan:** Screenshot dapat ditambahkan setelah workflow dan hasil analisis sudah final. Dokumentasi teks tidak bergantung pada screenshot sehingga pembahasan tetap dapat dibaca tanpa gambar.

---

## 2.18 Kesimpulan

Pengolahan data kualitas udara menggunakan **KNIME Analytics Platform** berhasil dilakukan melalui empat node utama, yaitu:

1. **PostgreSQL Connector**
2. **DB Table Selector**
3. **DB Reader**
4. **Statistics**

KNIME berhasil terhubung dengan database PostgreSQL Aiven dan membaca tabel `public.air_quality` yang berisi **366 baris data** untuk periode 31 Agustus 2025 sampai 31 Agustus 2026.

Hasil Statistics View menunjukkan bahwa jumlah data valid berbeda untuk setiap polutan. NO₂ memiliki 218 data valid, CO memiliki 209 data valid, dan SO₂ memiliki 262 data valid. Dengan demikian, terdapat masing-masing 148, 157, dan 104 data missing.

Dari sisi distribusi, NO₂ memiliki nilai skewness paling tinggi yaitu **0.868**, sedangkan SO₂ memiliki nilai skewness paling dekat dengan nol yaitu **0.143**. Untuk kurtosis, SO₂ memiliki nilai paling tinggi yaitu **2.342**.

Pemeriksaan nilai khusus juga menunjukkan bahwa tidak terdapat **NaN**, **+∞**, maupun **-∞** pada data polutan.

Dengan demikian, tahap pengolahan menggunakan KNIME telah menghasilkan gambaran awal mengenai jumlah data, kelengkapan data, serta karakteristik statistik distribusi NO₂, CO, dan SO₂. Hasil ini dapat digunakan sebagai dasar untuk pembahasan **rumus statistik dan contoh perhitungan** pada tahap berikutnya.
