# 1. Pemindahan Data ke PostgreSQL Aiven

## Pendahuluan

Pada tahap ini, data **time series kualitas udara Kecamatan Kalitengah, Kabupaten Lamongan** dipindahkan dari file CSV ke database **PostgreSQL** yang disediakan oleh **Aiven**.

Data yang digunakan merupakan data polutan **NO₂, CO, dan SO₂** dengan rentang waktu **31 Agustus 2025 sampai 31 Agustus 2026**.

Tujuan pemindahan data ke database adalah:

1. Menyimpan data secara lebih terstruktur.
2. Memudahkan pengelolaan dan pemeriksaan data.
3. Menyiapkan data agar dapat digunakan dalam proses analisis menggunakan **KNIME**.
4. Memastikan data dapat diakses kembali melalui query SQL.

---

## 1.1 Persiapan Database PostgreSQL Aiven

Database PostgreSQL yang digunakan berasal dari layanan **Aiven**.

Informasi koneksi database:

| Komponen | Keterangan |
|---|---|
| Database | `defaultdb` |
| Schema | `public` |
| Table | `air_quality` |
| Host | `pg-1af3ba92-analisis-time-series.a.aivencloud.com` |
| Port | `15751` |
| User | `avnadmin` |
| SSL Mode | `require` |

> **Catatan keamanan:** Password database tidak ditampilkan dalam dokumentasi ini untuk menjaga keamanan akun dan kredensial database.

---

## 1.2 Membuat Tabel `air_quality`

Setelah database PostgreSQL siap digunakan, dibuat tabel bernama `air_quality`.

Struktur tabel dibuat menggunakan perintah SQL berikut:

```sql
CREATE TABLE public.air_quality (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    no2 DOUBLE PRECISION,
    co DOUBLE PRECISION,
    so2 DOUBLE PRECISION
);
```

### Penjelasan kolom

| Kolom | Tipe Data | Fungsi |
|---|---|---|
| `id` | `SERIAL` | Nomor identitas setiap baris data |
| `date` | `DATE` | Tanggal pengamatan |
| `no2` | `DOUBLE PRECISION` | Nilai konsentrasi NO₂ |
| `co` | `DOUBLE PRECISION` | Nilai konsentrasi CO |
| `so2` | `DOUBLE PRECISION` | Nilai konsentrasi SO₂ |

Kolom `id` digunakan sebagai **primary key**, sehingga setiap baris memiliki identitas yang berbeda.

Kolom `date` menggunakan tipe `DATE` karena data yang digunakan merupakan data pengamatan berdasarkan tanggal.

Sementara itu, kolom `no2`, `co`, dan `so2` menggunakan `DOUBLE PRECISION` agar dapat menyimpan nilai numerik dengan angka desimal.

---

## 1.3 Struktur Database

Struktur penyimpanan data di PostgreSQL adalah sebagai berikut:

```text
defaultdb
└── public
    └── air_quality
        ├── id
        ├── date
        ├── no2
        ├── co
        └── so2
```

Keterangan:

- `defaultdb` merupakan database yang digunakan.
- `public` merupakan schema PostgreSQL.
- `air_quality` merupakan tabel yang menyimpan data kualitas udara.
- `id`, `date`, `no2`, `co`, dan `so2` merupakan kolom di dalam tabel.

---

## 1.4 Pemindahan Data dari CSV

Data hasil pengolahan time series sebelumnya disimpan dalam file:

```text
polutan_kalitengah_timeseries.csv
```

File CSV tersebut kemudian digunakan sebagai sumber data untuk mengisi tabel:

```text
public.air_quality
```

Data mencakup periode:

```text
31 Agustus 2025
```

sampai:

```text
31 Agustus 2026
```

Periode tersebut mencakup **366 tanggal kalender**, termasuk tanggal awal dan tanggal akhir.

### Data missing

Tidak semua tanggal memiliki nilai yang valid untuk setiap polutan. Beberapa nilai kosong disimpan sebagai `NULL`.

Jumlah data yang tersedia adalah:

| Polutan | Data Valid | Data Missing |
|---|---:|---:|
| NO₂ | 218 | 148 |
| CO | 209 | 157 |
| SO₂ | 262 | 104 |

Data missing tetap dipertahankan karena merupakan bagian dari kondisi data hasil pengambilan data. Nilai kosong tersebut nantinya dapat diperiksa dan dianalisis pada tahap pengolahan data berikutnya.

---

## 1.5 Pemeriksaan Data

Setelah proses pemindahan data selesai, dilakukan beberapa pemeriksaan untuk memastikan bahwa data berhasil masuk ke PostgreSQL dan memiliki jumlah serta rentang tanggal yang sesuai.

### 1.5.1 Mengecek jumlah baris data

Query yang digunakan:

```sql
SELECT COUNT(*)
FROM public.air_quality;
```

Hasil:

```text
366
```

Hasil tersebut menunjukkan bahwa terdapat **366 baris data** yang tersimpan di dalam tabel `air_quality`.

Jumlah ini sesuai dengan jumlah tanggal kalender pada periode 31 Agustus 2025 sampai 31 Agustus 2026.

---

### 1.5.2 Mengecek rentang tanggal

Untuk memastikan tanggal paling awal dan paling akhir, digunakan query:

```sql
SELECT
    MIN(date) AS tanggal_awal,
    MAX(date) AS tanggal_akhir
FROM public.air_quality;
```

Hasil:

```text
2025-08-31 sampai 2026-08-31
```

Hasil tersebut menunjukkan bahwa data telah mencakup periode pengamatan yang diharapkan.

---

### 1.5.3 Mengecek jumlah data valid setiap polutan

Untuk mengetahui jumlah nilai yang tersedia pada setiap polutan, digunakan fungsi `COUNT()`:

```sql
SELECT
    COUNT(no2) AS no2_valid,
    COUNT(co) AS co_valid,
    COUNT(so2) AS so2_valid
FROM public.air_quality;
```

Hasil:

| Polutan | Data Valid |
|---|---:|
| NO₂ | 218 |
| CO | 209 |
| SO₂ | 262 |

Pada PostgreSQL, `COUNT(nama_kolom)` hanya menghitung nilai yang **tidak NULL**. Oleh karena itu, hasil query tersebut dapat digunakan untuk mengetahui jumlah data valid pada masing-masing polutan.

Perbedaan jumlah data valid terjadi karena tidak semua tanggal memiliki hasil pengamatan yang tersedia untuk setiap polutan.

---

### 1.5.4 Mengecek data secara langsung

Untuk melihat beberapa baris data yang telah tersimpan, dapat digunakan query:

```sql
SELECT *
FROM public.air_quality
ORDER BY date
LIMIT 10;
```

Query tersebut menampilkan maksimal 10 data pertama berdasarkan urutan tanggal.

Pemeriksaan ini berguna untuk memastikan bahwa:

- data berhasil masuk ke tabel;
- tanggal tersimpan dengan benar;
- nilai polutan tersimpan sebagai data numerik;
- nilai yang tidak tersedia tetap ditampilkan sebagai `NULL`.

---

## 1.6 Contoh Data

Beberapa contoh data yang terdapat pada tabel `air_quality` adalah:

| ID | Tanggal | NO₂ | CO | SO₂ |
|---:|---|---:|---:|---:|
| 1 | 2025-08-31 | 0.00003774 | 0.02549803 | 0.00027628 |
| 2 | 2025-09-01 | 0.00003116 | 0.02842947 | -0.00016491 |
| 3 | 2025-09-02 | NULL | 0.02262214 | NULL |
| 4 | 2025-09-03 | 0.00002038 | 0.02528949 | -0.000108 |
| 5 | 2025-09-04 | 0.00005897 | 0.02827020 | 0.00005221 |

Dari contoh tersebut terlihat bahwa tidak semua tanggal memiliki nilai untuk seluruh polutan.

Sebagai contoh, pada **2 September 2025**, nilai NO₂ dan SO₂ tidak tersedia sehingga disimpan sebagai `NULL`, sedangkan nilai CO masih tersedia.

---

## 1.7 Verifikasi Hasil Pemindahan

Secara umum, proses pemindahan data dianggap berhasil apabila beberapa kondisi berikut terpenuhi:

| Pemeriksaan | Hasil |
|---|---|
| Tabel `air_quality` berhasil dibuat | Berhasil |
| Jumlah baris | 366 |
| Tanggal awal | 2025-08-31 |
| Tanggal akhir | 2026-08-31 |
| Data valid NO₂ | 218 |
| Data valid CO | 209 |
| Data valid SO₂ | 262 |
| Data `NULL` dipertahankan | Ya |

Dengan hasil tersebut, database PostgreSQL Aiven telah siap digunakan sebagai sumber data untuk tahap pengolahan berikutnya.

---

## 1.8 Kesimpulan

Pada tahap ini, data **time series kualitas udara Kecamatan Kalitengah, Kabupaten Lamongan** berhasil dipindahkan dari file CSV ke database PostgreSQL Aiven.

Data disimpan pada:

```text
defaultdb
└── public
    └── air_quality
```

Tabel `air_quality` memiliki **366 baris data** yang mencakup periode **31 Agustus 2025 sampai 31 Agustus 2026**.

Jumlah data valid berbeda pada setiap polutan, yaitu:

- **NO₂:** 218 data valid dan 148 data missing.
- **CO:** 209 data valid dan 157 data missing.
- **SO₂:** 262 data valid dan 104 data missing.

Nilai yang tidak tersedia tetap disimpan sebagai `NULL` agar kondisi data asli tidak berubah. Dengan demikian, data telah tersimpan secara terstruktur di PostgreSQL dan siap digunakan sebagai sumber data untuk proses analisis menggunakan **KNIME** pada tahap berikutnya.
