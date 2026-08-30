# Penambangan Sains Data

## Analisis Kualitas Udara di Lamongan

**Nama:** Ahmad Dafi Zidni Alfarisi  
**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Penambangan Sains Data (PSD)  
**Universitas:** Universitas Trunojoyo Madura

---

## Deskripsi Project

Project ini merupakan tugas mata kuliah **Penambangan Sains Data** yang berfokus pada pemahaman kualitas udara di wilayah Lamongan.

Pada tahap pertama, analisis difokuskan pada:

1. Business Understanding
2. Data Understanding
3. Eksplorasi awal dataset
4. Pemeriksaan kualitas data

Tahap analisis lanjutan akan dilakukan pada pertemuan berikutnya sesuai materi yang diberikan.

---

# 1. Business Understanding

## Latar Belakang

Kualitas udara merupakan salah satu faktor yang dapat memengaruhi lingkungan dan kehidupan masyarakat. Konsentrasi partikulat di udara dapat berubah dari waktu ke waktu dan dipengaruhi oleh berbagai aktivitas maupun kondisi lingkungan.

Oleh karena itu, diperlukan pemahaman terhadap data kualitas udara pada suatu wilayah untuk mengetahui karakteristik dan perubahan konsentrasi polutan dari waktu ke waktu.

Wilayah yang dipilih dalam project ini adalah **Lamongan, Jawa Timur**.

## Tujuan

Tujuan dari project ini adalah:

> Mengetahui dan memahami kondisi kualitas udara di wilayah Lamongan berdasarkan data konsentrasi partikulat udara.

Secara khusus, tahap pertama bertujuan untuk:

- memahami dataset kualitas udara;
- mengetahui periode dan cakupan data;
- memahami setiap fitur yang tersedia;
- mengetahui satuan pengukuran;
- mengeksplorasi karakteristik data;
- menemukan nilai yang tidak wajar;
- mengetahui adanya missing value;
- mengetahui adanya data duplikat;
- mengidentifikasi outlier pada data.

## Manfaat

Project ini diharapkan memberikan beberapa manfaat:

### 1. Pemahaman kondisi udara

Data dapat digunakan untuk melihat bagaimana konsentrasi partikulat berubah selama periode pengamatan.

### 2. Identifikasi kondisi tidak normal

Eksplorasi data dapat membantu menemukan nilai yang sangat tinggi, sangat rendah, atau tidak wajar.

### 3. Dasar analisis selanjutnya

Dataset yang telah dipahami dan diperiksa dapat menjadi dasar untuk analisis lebih lanjut pada pertemuan berikutnya.

### 4. Pembelajaran Penambangan Sains Data

Project ini menjadi latihan dalam proses memperoleh, memahami, membersihkan, mengeksplorasi, dan menganalisis data lingkungan.

---

# 2. Data Understanding

## Wilayah Pengamatan

Wilayah yang digunakan dalam project adalah:

| Keterangan | Informasi |
|---|---|
| Wilayah | Lamongan |
| Provinsi | Jawa Timur |
| Latitude | -7.2 |
| Longitude | 112.4 |
| Tools wilayah | GeoJSON.io |

Koordinat tersebut digunakan untuk menentukan lokasi pengambilan data kualitas udara.

Batas wilayah pengamatan dibuat menggunakan **GeoJSON** sebagai bagian dari proses pembatasan wilayah data.

## Sumber Data

Data kualitas udara diperoleh dari:

**Copernicus Atmosphere Monitoring Service (CAMS)**

Dataset yang digunakan berasal dari data kualitas udara atmosfer dan kemudian diekstraksi menjadi format CSV untuk proses analisis.

## Periode Data

Data yang digunakan mencakup sekitar satu tahun:

**29 Agustus 2025 – 29 Agustus 2026**

Periode tersebut memenuhi kebutuhan tugas untuk menggunakan data minimal satu tahun.

---

# 3. Dataset

Dataset hasil ekstraksi memiliki:

- **1.464 baris**
- **6 kolom**

Kolom yang digunakan adalah:

| Fitur | Keterangan |
|---|---|
| `valid_time` | Waktu pengamatan data |
| `latitude` | Koordinat lintang lokasi |
| `longitude` | Koordinat bujur lokasi |
| `pm1_ug_m3` | Konsentrasi PM1 |
| `pm2p5_ug_m3` | Konsentrasi PM2.5 |
| `pm10_ug_m3` | Konsentrasi PM10 |

---

# 4. Pemahaman Fitur Polutan

## PM1

PM1 merupakan partikulat dengan diameter aerodinamis kurang dari atau sama dengan **1 mikrometer**.

Partikel dengan ukuran sangat kecil seperti PM1 dapat berasal dari proses pembakaran dan aktivitas yang menghasilkan partikel halus.

## PM2.5

PM2.5 merupakan partikulat dengan diameter aerodinamis kurang dari atau sama dengan **2,5 mikrometer**.

PM2.5 dapat berasal dari berbagai sumber seperti:

- kendaraan bermotor;
- pembakaran bahan bakar;
- aktivitas industri;
- pembakaran biomassa;
- proses pembentukan partikulat sekunder di atmosfer.

Karena ukurannya kecil, PM2.5 menjadi salah satu parameter penting dalam analisis kualitas udara.

## PM10

PM10 merupakan partikulat dengan diameter aerodinamis kurang dari atau sama dengan **10 mikrometer**.

Sumber PM10 dapat berasal dari:

- debu jalan;
- aktivitas konstruksi;
- tanah dan material permukaan;
- aktivitas industri;
- pembakaran;
- transportasi.

---

# 5. Eksplorasi Awal Data

Eksplorasi awal dilakukan untuk mengetahui karakteristik dataset sebelum melakukan analisis lebih lanjut.

Hal yang diperiksa meliputi:

- jumlah baris dan kolom;
- tipe data;
- periode pengamatan;
- nilai minimum;
- nilai maksimum;
- nilai rata-rata;
- missing value;
- data duplikat;
- nilai negatif;
- outlier;
- distribusi data.

Hasil eksplorasi lengkap ditampilkan pada notebook:

**01 Data Understanding**

---

# 6. Pemeriksaan Data

Berdasarkan pemeriksaan awal, ditemukan beberapa nilai yang perlu diperhatikan terutama pada variabel partikulat.

Untuk PM10 ditemukan nilai:

- **Minimum:** sekitar `-44.03`
- **Maksimum:** sekitar `164.67`
- **Jumlah outlier:** `22`

Nilai negatif pada konsentrasi partikulat secara fisik perlu diperiksa karena konsentrasi massa partikulat tidak seharusnya bernilai negatif.

Nilai tersebut **tidak langsung dihapus pada tahap ini**, tetapi dicatat sebagai temuan pada proses Data Understanding untuk ditangani pada tahap Data Preparation.

---

# 7. Kesimpulan Minggu Pertama

Pada tahap pertama, dataset kualitas udara wilayah Lamongan telah berhasil diperoleh dan dipahami.

Dataset mencakup periode **29 Agustus 2025 sampai 29 Agustus 2026** dengan parameter utama:

- PM1
- PM2.5
- PM10

Dataset terdiri dari **1.464 baris dan 6 kolom**.

Eksplorasi awal juga menemukan adanya nilai yang tidak wajar, termasuk nilai negatif dan beberapa outlier pada data partikulat.

Temuan tersebut akan menjadi dasar untuk tahap berikutnya, yaitu **Data Preparation dan analisis lanjutan** sesuai materi pertemuan berikutnya.

> **Catatan:** Project ini pada tahap Minggu 1 difokuskan pada Business Understanding dan Data Understanding. Analisis lanjutan tidak dimasukkan agar sesuai dengan materi dan instruksi tugas pertemuan pertama.
EOF