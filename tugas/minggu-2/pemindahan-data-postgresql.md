# 1. Pemindahan Data ke PostgreSQL Aiven

## 1.1 Latar Belakang

Data time series kualitas udara Kabupaten Lamongan pada awalnya tersimpan dalam format **Comma-Separated Values (CSV)**. Format CSV cukup praktis untuk penyimpanan dan pertukaran data, tetapi untuk proses pengolahan dan analisis yang lebih terstruktur, data perlu dipindahkan ke dalam sebuah sistem manajemen basis data.

Pada tahap ini digunakan **PostgreSQL pada Aiven** sebagai basis data terpusat. PostgreSQL dipilih karena mendukung pengelolaan data tabular secara terstruktur, bahasa SQL untuk pengambilan dan pemeriksaan data, serta dapat digunakan sebagai sumber data yang terhubung dengan perangkat lunak analisis seperti **KNIME**.

Proses pemindahan data dilakukan melalui beberapa tahapan, yaitu:

1. Menyiapkan database PostgreSQL pada Aiven.
2. Membuat tabel `air_quality`.
3. Menyesuaikan struktur tabel dengan struktur file CSV.
4. Mengimpor data CSV menggunakan **pgAdmin 4**.
5. Melakukan verifikasi jumlah data yang berhasil masuk.
6. Memastikan data siap digunakan sebagai sumber proses analisis di KNIME.

---

## 1.2 Persiapan Database

Database yang digunakan adalah **PostgreSQL yang disediakan melalui Aiven**.

**Nama database:**

```text
defaultdb
```

**Schema:**

```text
public
```

**Nama tabel:**

```text
air_quality
```

Sehingga nama tabel secara lengkap adalah:

```text
public.air_quality
```

Database ini digunakan sebagai tempat penyimpanan data kualitas udara yang sebelumnya berada pada file CSV.

File sumber data yang digunakan adalah:

```text
data_lamongan_clean(1).csv
```

File tersebut berisi **1.464 baris data** dan memiliki enam variabel utama yang akan dimasukkan ke dalam tabel PostgreSQL.

### Struktur Data Sumber

| No. | Kolom | Tipe Data PostgreSQL | Keterangan |
|---:|---|---|---|
| 1 | `valid_time` | TIMESTAMP | Waktu pengamatan |
| 2 | `latitude` | DOUBLE PRECISION | Koordinat lintang |
| 3 | `longitude` | DOUBLE PRECISION | Koordinat bujur |
| 4 | `pm1_ug_m3` | DOUBLE PRECISION | Konsentrasi PM1 dalam µg/m³ |
| 5 | `pm2p5_ug_m3` | DOUBLE PRECISION | Konsentrasi PM2.5 dalam µg/m³ |
| 6 | `pm10_ug_m3` | DOUBLE PRECISION | Konsentrasi PM10 dalam µg/m³ |

Selain enam variabel yang berasal dari CSV, tabel PostgreSQL memiliki satu kolom tambahan yaitu `id`.

Kolom `id` digunakan sebagai identitas unik untuk setiap baris data dan nilainya dibuat secara otomatis oleh PostgreSQL.

---

## 1.3 Perancangan Struktur Tabel

Sebelum melakukan import data, struktur tabel perlu dibuat terlebih dahulu. Struktur tabel dibuat agar tipe data pada PostgreSQL sesuai dengan karakteristik masing-masing kolom pada file CSV.

Tabel yang digunakan adalah:

```text
public.air_quality
```

Struktur tabel terdiri dari tujuh kolom, yaitu:

- `id`
- `valid_time`
- `latitude`
- `longitude`
- `pm1_ug_m3`
- `pm2p5_ug_m3`
- `pm10_ug_m3`

Kolom `id` tidak berasal dari file CSV. Kolom tersebut dibuat pada sisi database untuk memberikan identitas unik pada setiap record.

---

## 1.4 Pembuatan Tabel PostgreSQL

Tabel `air_quality` dibuat menggunakan perintah SQL berikut:

```sql
CREATE TABLE air_quality (
    id SERIAL PRIMARY KEY,
    valid_time TIMESTAMP NOT NULL,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    pm1_ug_m3 DOUBLE PRECISION,
    pm2p5_ug_m3 DOUBLE PRECISION,
    pm10_ug_m3 DOUBLE PRECISION
);
```

### Penjelasan Perintah SQL

#### 1. `id SERIAL PRIMARY KEY`

Kolom `id` digunakan sebagai identitas unik setiap record.

Tipe `SERIAL` memungkinkan PostgreSQL memberikan nilai angka secara otomatis ketika data baru dimasukkan. Sementara itu, `PRIMARY KEY` memastikan bahwa setiap nilai `id` bersifat unik dan tidak boleh kosong.

Contoh nilai yang dihasilkan:

```text
1
2
3
4
...
1464
```

Dengan demikian, kolom `id` tidak perlu disediakan pada file CSV.

#### 2. `valid_time TIMESTAMP NOT NULL`

Kolom `valid_time` menyimpan waktu ketika pengamatan dilakukan.

Tipe `TIMESTAMP` digunakan karena data memiliki informasi tanggal dan waktu. Constraint `NOT NULL` digunakan untuk memastikan setiap record memiliki informasi waktu pengamatan.

Kolom ini penting karena data yang dianalisis merupakan **data time series**.

#### 3. `latitude DOUBLE PRECISION`

Kolom `latitude` menyimpan koordinat lintang lokasi pengamatan.

Tipe `DOUBLE PRECISION` digunakan karena koordinat geografis dapat memiliki nilai desimal dengan tingkat ketelitian yang cukup tinggi.

#### 4. `longitude DOUBLE PRECISION`

Kolom `longitude` menyimpan koordinat bujur lokasi pengamatan.

Sama seperti `latitude`, tipe `DOUBLE PRECISION` digunakan untuk mempertahankan nilai desimal koordinat.

#### 5. `pm1_ug_m3 DOUBLE PRECISION`

Kolom `pm1_ug_m3` menyimpan konsentrasi partikel **PM1**.

Satuan yang digunakan adalah:

```text
µg/m³
```

atau mikrogram per meter kubik.

#### 6. `pm2p5_ug_m3 DOUBLE PRECISION`

Kolom `pm2p5_ug_m3` menyimpan konsentrasi **PM2.5** dalam satuan µg/m³.

PM2.5 merupakan salah satu parameter penting dalam analisis kualitas udara karena merepresentasikan partikel berukuran sangat kecil yang dapat berada di udara.

#### 7. `pm10_ug_m3 DOUBLE PRECISION`

Kolom `pm10_ug_m3` menyimpan konsentrasi **PM10** dalam satuan µg/m³.

Parameter ini digunakan bersama PM1 dan PM2.5 untuk melihat kondisi konsentrasi partikulat pada lokasi pengamatan.

---

## 1.5 Kesesuaian Struktur CSV dengan PostgreSQL

Struktur kolom pada file CSV disesuaikan dengan struktur tabel PostgreSQL.

Pemetaan kolom dilakukan sebagai berikut:

| Kolom CSV | Kolom PostgreSQL | Tipe Data | Keterangan |
|---|---|---|---|
| `valid_time` | `valid_time` | TIMESTAMP | Waktu pengamatan |
| `latitude` | `latitude` | DOUBLE PRECISION | Lintang |
| `longitude` | `longitude` | DOUBLE PRECISION | Bujur |
| `pm1_ug_m3` | `pm1_ug_m3` | DOUBLE PRECISION | PM1 |
| `pm2p5_ug_m3` | `pm2p5_ug_m3` | DOUBLE PRECISION | PM2.5 |
| `pm10_ug_m3` | `pm10_ug_m3` | DOUBLE PRECISION | PM10 |

Kolom `id` tidak dipetakan dari CSV karena dibuat otomatis oleh PostgreSQL.

Dengan pemetaan tersebut, jumlah kolom yang diambil dari CSV adalah **enam kolom**, sedangkan tabel PostgreSQL memiliki **tujuh kolom** termasuk kolom `id`.

---

## 1.6 Import Data CSV Menggunakan pgAdmin 4

Setelah tabel berhasil dibuat, tahap berikutnya adalah memasukkan data dari file CSV ke dalam tabel PostgreSQL.

Proses import dilakukan menggunakan **pgAdmin 4**.

File yang digunakan:

```text
data_lamongan_clean(1).csv
```

Tabel tujuan:

```text
public.air_quality
```

### Pengaturan Import

Pengaturan yang digunakan pada proses import adalah:

| Pengaturan | Nilai |
|---|---|
| Format | CSV |
| Header | Yes |
| Delimiter | `,` |
| Quote | `"` |
| Escape | `"` |

### Penjelasan Pengaturan

**Format CSV**

Menunjukkan bahwa sumber data yang digunakan memiliki format Comma-Separated Values.

**Header: Yes**

Baris pertama file CSV berisi nama kolom. Oleh karena itu, baris pertama tidak dianggap sebagai record data.

Contoh header:

```text
valid_time,latitude,longitude,pm1_ug_m3,pm2p5_ug_m3,pm10_ug_m3
```

**Delimiter: `,`**

Tanda koma digunakan sebagai pemisah antar kolom.

**Quote: `"`**

Tanda petik ganda digunakan sebagai karakter pembungkus nilai apabila diperlukan.

**Escape: `"`**

Karakter escape digunakan untuk menangani tanda petik yang terdapat di dalam nilai CSV.

---

## 1.7 Kolom yang Diimport

Kolom yang dimasukkan dari file CSV adalah:

```text
valid_time
latitude
longitude
pm1_ug_m3
pm2p5_ug_m3
pm10_ug_m3
```

Sedangkan kolom:

```text
id
```

tidak diikutsertakan dalam proses import.

Hal tersebut dilakukan karena PostgreSQL akan menghasilkan nilai `id` secara otomatis berdasarkan mekanisme `SERIAL`.

Secara konseptual, proses import dapat digambarkan sebagai berikut:

```text
data_lamongan_clean(1).csv
            |
            v
     Proses Import CSV
            |
            v
     public.air_quality
            |
            +--> id dibuat otomatis PostgreSQL
            |
            +--> valid_time
            +--> latitude
            +--> longitude
            +--> pm1_ug_m3
            +--> pm2p5_ug_m3
            +--> pm10_ug_m3
```

---

## 1.8 Pemeriksaan Setelah Import

Setelah proses import selesai, perlu dilakukan pemeriksaan untuk memastikan data telah berhasil masuk ke database.

Pemeriksaan pertama dilakukan dengan menghitung jumlah baris pada tabel.

Query yang digunakan:

```sql
SELECT COUNT(*) AS jumlah_data
FROM public.air_quality;
```

Hasil yang diperoleh:

```text
jumlah_data
-----------
1464
```

Hasil tersebut menunjukkan bahwa tabel `public.air_quality` memiliki **1.464 baris data**.

Jumlah tersebut sesuai dengan jumlah data pada file CSV, sehingga dapat disimpulkan bahwa seluruh record telah berhasil dimasukkan ke PostgreSQL.

---

## 1.9 Pemeriksaan Sampel Data

Selain menghitung jumlah baris, data dapat diperiksa secara langsung menggunakan query:

```sql
SELECT *
FROM public.air_quality
LIMIT 10;
```

Query tersebut digunakan untuk menampilkan sepuluh record pertama dari tabel.

Pemeriksaan ini bertujuan untuk memastikan bahwa:

1. Data telah masuk ke tabel yang benar.
2. Kolom memiliki nama yang sesuai.
3. Nilai `id` telah dibuat secara otomatis.
4. Nilai waktu tersimpan pada kolom `valid_time`.
5. Koordinat tersimpan pada kolom `latitude` dan `longitude`.
6. Nilai PM1, PM2.5, dan PM10 tersimpan pada kolom yang sesuai.

---

## 1.10 Pemeriksaan Struktur Tabel

Struktur tabel juga dapat diperiksa melalui PostgreSQL untuk memastikan tipe data yang digunakan sudah sesuai.

Secara konseptual, struktur tabel yang diharapkan adalah:

| Kolom | Tipe | Constraint |
|---|---|---|
| `id` | SERIAL / integer | PRIMARY KEY |
| `valid_time` | TIMESTAMP | NOT NULL |
| `latitude` | DOUBLE PRECISION | - |
| `longitude` | DOUBLE PRECISION | - |
| `pm1_ug_m3` | DOUBLE PRECISION | - |
| `pm2p5_ug_m3` | DOUBLE PRECISION | - |
| `pm10_ug_m3` | DOUBLE PRECISION | - |

Struktur tersebut memungkinkan data numerik kualitas udara disimpan sebagai tipe numerik sehingga dapat digunakan untuk operasi statistik dan analisis lebih lanjut.

---

## 1.11 Pemeriksaan Data Time Series

Karena data yang digunakan merupakan data time series, kolom `valid_time` menjadi salah satu kolom penting yang perlu diperiksa.

Data dapat diurutkan berdasarkan waktu menggunakan query:

```sql
SELECT *
FROM public.air_quality
ORDER BY valid_time
LIMIT 10;
```

Query tersebut menampilkan data berdasarkan urutan waktu dari yang paling awal.

Untuk melihat rentang waktu data, dapat digunakan query:

```sql
SELECT
    MIN(valid_time) AS waktu_awal,
    MAX(valid_time) AS waktu_akhir
FROM public.air_quality;
```

Query tersebut digunakan untuk mengetahui periode pengamatan yang terdapat di dalam database.

---

## 1.12 Pemeriksaan Nilai Kosong

Sebelum data digunakan untuk analisis di KNIME, pemeriksaan nilai kosong atau `NULL` juga penting dilakukan.

Contoh query untuk memeriksa jumlah nilai kosong pada masing-masing parameter adalah:

```sql
SELECT
    COUNT(*) FILTER (WHERE valid_time IS NULL) AS null_valid_time,
    COUNT(*) FILTER (WHERE latitude IS NULL) AS null_latitude,
    COUNT(*) FILTER (WHERE longitude IS NULL) AS null_longitude,
    COUNT(*) FILTER (WHERE pm1_ug_m3 IS NULL) AS null_pm1,
    COUNT(*) FILTER (WHERE pm2p5_ug_m3 IS NULL) AS null_pm2p5,
    COUNT(*) FILTER (WHERE pm10_ug_m3 IS NULL) AS null_pm10
FROM public.air_quality;
```

Pemeriksaan ini dapat digunakan untuk mengetahui apakah terdapat data yang kosong pada masing-masing kolom.

Khusus kolom `valid_time`, tabel telah menggunakan `NOT NULL`, sehingga setiap record harus memiliki waktu pengamatan.

---

## 1.13 Pemeriksaan Data Duplikat

Pemeriksaan duplikasi juga dapat dilakukan, khususnya apabila satu kombinasi waktu dan lokasi seharusnya hanya memiliki satu record.

Contoh query:

```sql
SELECT
    valid_time,
    latitude,
    longitude,
    COUNT(*) AS jumlah
FROM public.air_quality
GROUP BY
    valid_time,
    latitude,
    longitude
HAVING COUNT(*) > 1;
```

Query tersebut menampilkan kombinasi waktu dan lokasi yang muncul lebih dari satu kali.

Pemeriksaan ini dapat membantu memastikan kualitas data sebelum digunakan untuk analisis time series.

---

## 1.14 Verifikasi Jumlah Data

Berdasarkan proses import dan verifikasi yang telah dilakukan, diperoleh jumlah data sebagai berikut:

| Keterangan | Jumlah |
|---|---:|
| Jumlah baris pada file CSV | 1.464 |
| Jumlah baris pada PostgreSQL | 1.464 |
| Kolom dari CSV | 6 |
| Kolom tambahan PostgreSQL | 1 (`id`) |
| Total kolom tabel PostgreSQL | 7 |

Jumlah data pada file CSV dan database memiliki nilai yang sama, yaitu **1.464 baris**.

Hal tersebut menunjukkan bahwa proses pemindahan data telah berhasil dilakukan.

---

## 1.15 PostgreSQL sebagai Sumber Data KNIME

Setelah data berhasil disimpan dan diverifikasi pada PostgreSQL Aiven, database dapat digunakan sebagai sumber data untuk proses analisis menggunakan **KNIME**.

Alur pengolahan data secara umum adalah:

```text
File CSV
   |
   v
PostgreSQL Aiven
   |
   v
public.air_quality
   |
   v
Koneksi Database
   |
   v
KNIME
   |
   v
Data Cleaning / Preprocessing
   |
   v
Analisis Statistik
   |
   v
Visualisasi / Interpretasi
```

Dengan menggunakan PostgreSQL sebagai sumber data, KNIME tidak perlu menjadikan file CSV sebagai sumber utama. Data dapat diambil langsung dari database melalui koneksi PostgreSQL.

Hal ini juga membuat penyimpanan data menjadi lebih terstruktur dan memudahkan penggunaan data yang sama untuk beberapa tahap analisis.

---

## 1.16 Keuntungan Penggunaan PostgreSQL Aiven

Penggunaan PostgreSQL Aiven memberikan beberapa keuntungan dalam pengelolaan dataset kualitas udara, antara lain:

### 1. Penyimpanan Data Terstruktur

Data disimpan dalam bentuk tabel dengan tipe data yang jelas. Hal ini membuat setiap variabel memiliki format yang sesuai dengan karakteristik datanya.

### 2. Pengelolaan Data Menggunakan SQL

PostgreSQL memungkinkan proses pemeriksaan dan pengolahan data menggunakan SQL, seperti:

- menghitung jumlah data;
- mengambil data berdasarkan waktu;
- melakukan penyaringan data;
- menghitung statistik;
- memeriksa nilai kosong;
- memeriksa data duplikat;
- mengurutkan data.

### 3. Data Terpusat

Data disimpan pada satu database sehingga dapat digunakan oleh aplikasi atau proses analisis yang membutuhkan sumber data yang sama.

### 4. Mendukung Analisis Time Series

Kolom `valid_time` menggunakan tipe `TIMESTAMP`, sehingga data dapat diurutkan dan dikelompokkan berdasarkan waktu untuk kebutuhan analisis time series.

### 5. Integrasi dengan KNIME

PostgreSQL dapat digunakan sebagai sumber data untuk workflow KNIME sehingga proses analisis dapat dilakukan secara lebih terstruktur.

---

## 1.17 Contoh Query Pengambilan Data

Untuk mengambil seluruh data:

```sql
SELECT *
FROM public.air_quality;
```

Untuk mengambil kolom tertentu:

```sql
SELECT
    valid_time,
    latitude,
    longitude,
    pm1_ug_m3,
    pm2p5_ug_m3,
    pm10_ug_m3
FROM public.air_quality;
```

Untuk mengambil data berdasarkan urutan waktu:

```sql
SELECT *
FROM public.air_quality
ORDER BY valid_time;
```

Untuk mengambil data dengan konsentrasi PM10 tertentu, misalnya lebih dari 50 µg/m³:

```sql
SELECT *
FROM public.air_quality
WHERE pm10_ug_m3 > 50;
```

Query-query tersebut dapat menjadi dasar untuk proses eksplorasi data sebelum data diteruskan ke KNIME.

---

## 1.18 Dokumentasi Hasil Pemindahan Data

Hasil akhir dari proses pemindahan data dapat dirangkum sebagai berikut:

```text
Sumber Data
    |
    +-- data_lamongan_clean(1).csv
    |
    +-- 1.464 baris
    |
    +-- 6 kolom data utama
            |
            v
PostgreSQL Aiven
    |
    +-- Database: defaultdb
    |
    +-- Schema: public
    |
    +-- Table: air_quality
    |
    +-- 7 kolom termasuk id
            |
            v
Verifikasi
    |
    +-- COUNT(*) = 1.464
    |
    +-- Data siap digunakan
            |
            v
KNIME
    |
    +-- Preprocessing
    +-- Analisis statistik
    +-- Visualisasi
```

---

# 2. Kesimpulan

Data time series kualitas udara Kabupaten Lamongan yang sebelumnya tersimpan dalam file `data_lamongan_clean(1).csv` telah dipindahkan ke database **PostgreSQL Aiven**.

Database yang digunakan adalah `defaultdb`, dengan tabel `public.air_quality`. Tabel tersebut memiliki tujuh kolom, yaitu `id`, `valid_time`, `latitude`, `longitude`, `pm1_ug_m3`, `pm2p5_ug_m3`, dan `pm10_ug_m3`.

Enam kolom utama berasal dari file CSV, sedangkan kolom `id` ditambahkan pada sisi PostgreSQL sebagai identitas unik setiap record. Kolom `id` menggunakan `SERIAL PRIMARY KEY` sehingga nilainya dapat dibuat secara otomatis oleh PostgreSQL.

Proses import dilakukan menggunakan **pgAdmin 4** dengan format CSV, menggunakan header, delimiter koma, serta quote dan escape berupa tanda petik ganda.

Berdasarkan proses verifikasi menggunakan query:

```sql
SELECT COUNT(*) AS jumlah_data
FROM public.air_quality;
```

diperoleh hasil:

```text
jumlah_data
-----------
1464
```

Hasil tersebut sesuai dengan jumlah baris pada file sumber, yaitu **1.464 data**. Dengan demikian, proses pemindahan data dari file CSV ke PostgreSQL Aiven dapat dinyatakan berhasil.

Database PostgreSQL selanjutnya dapat digunakan sebagai sumber data terpusat untuk proses analisis menggunakan **KNIME**, termasuk tahap pemeriksaan kualitas data, preprocessing, analisis statistik, analisis time series, serta visualisasi data kualitas udara Kabupaten Lamongan.
