# 1. Business Understanding

## 1.1 Latar Belakang

Kualitas udara merupakan salah satu aspek penting dalam kondisi lingkungan karena berkaitan dengan aktivitas manusia dan kondisi lingkungan di suatu wilayah. Keberadaan polutan di atmosfer dapat berasal dari berbagai aktivitas, seperti transportasi, pembakaran bahan bakar, aktivitas industri, serta pembakaran biomassa.

Pemantauan polutan udara diperlukan untuk mengetahui bagaimana kondisi udara berubah dari waktu ke waktu. Data pengamatan yang dikumpulkan secara berkala dapat digunakan untuk melihat pola, perubahan, serta kecenderungan kondisi polusi udara pada suatu wilayah.

Dalam proyek ini, wilayah yang menjadi objek pengamatan adalah **Kecamatan Kalitengah, Kabupaten Lamongan, Jawa Timur**.

Data polutan diperoleh dari pengamatan satelit **Sentinel-5P/TROPOMI** melalui layanan data atmosfer dan kemudian diproses untuk memperoleh nilai pengamatan polutan pada wilayah Kecamatan Kalitengah.

Polutan yang digunakan dalam proyek ini meliputi:

- **NO₂ (Nitrogen Dioxide)**
- **CO (Carbon Monoxide)**
- **SO₂ (Sulfur Dioxide)**

Dataset yang digunakan memiliki fitur `date` sebagai penanda waktu serta tiga fitur polutan, yaitu `NO2`, `CO`, dan `SO2`.

Data tersebut dikumpulkan dalam rentang waktu **31 Agustus 2025 sampai 31 Agustus 2026**. Berdasarkan rentang tersebut, dataset memiliki **366 tanggal kalender** yang dapat digunakan untuk melakukan analisis perubahan polutan berdasarkan waktu.

Namun, tidak semua fitur polutan memiliki data pada setiap tanggal. Berdasarkan hasil pemeriksaan awal dataset, terdapat missing values pada NO₂, CO, dan SO₂. Oleh karena itu, kondisi kelengkapan data juga menjadi bagian penting yang perlu diperhatikan dalam proses analisis.

Melalui analisis data tersebut, diharapkan dapat diperoleh gambaran mengenai pola perubahan polutan udara di Kecamatan Kalitengah serta menjadi dasar untuk melakukan analisis lebih lanjut terhadap kondisi kualitas udara berdasarkan data yang tersedia.

---

## 1.2 Tujuan Bisnis

Tujuan utama dari pengumpulan dan analisis data polutan di Kecamatan Kalitengah adalah memperoleh informasi yang dapat digunakan untuk memahami kondisi dan perubahan polusi udara berdasarkan data pengamatan selama satu tahun.

Tujuan tersebut meliputi beberapa aspek berikut.

### 1. Pemantauan Kondisi Lingkungan

Data polutan dapat digunakan untuk memantau perubahan kondisi lingkungan di Kecamatan Kalitengah.

Dengan melihat nilai NO₂, CO, dan SO₂ dari waktu ke waktu, dapat diketahui bagaimana nilai masing-masing polutan berubah selama periode pengamatan.

Pemantauan berdasarkan data historis dapat membantu memberikan gambaran kondisi lingkungan berdasarkan data yang tersedia.

Pada proyek ini, hasil analisis digunakan untuk memberikan gambaran perubahan nilai polutan dan bukan untuk menetapkan kondisi kesehatan udara secara langsung.

---

### 2. Identifikasi Tren dan Pola

Data time series memungkinkan dilakukan identifikasi terhadap pola perubahan polutan.

Analisis dapat digunakan untuk mengetahui:

- periode ketika nilai polutan meningkat;
- periode ketika nilai polutan menurun;
- perubahan nilai polutan dari waktu ke waktu;
- pola perubahan masing-masing jenis polutan;
- periode dengan nilai polutan relatif tinggi atau rendah;
- perbedaan pola perubahan antarpolutan.

Informasi tersebut dapat digunakan untuk memahami karakteristik temporal polutan pada wilayah penelitian.

---

### 3. Pemahaman Terhadap Perubahan Data

Data historis polutan dapat digunakan untuk memahami bagaimana nilai polutan berubah pada periode pengamatan.

Dengan melakukan pemantauan terhadap perubahan nilai polutan secara berkala, periode yang menunjukkan perubahan nilai dapat lebih mudah diidentifikasi.

Pada proyek ini, analisis difokuskan pada pemahaman data dan perubahan historis. Sistem peringatan otomatis maupun sistem prediksi bukan merupakan bagian dari implementasi proyek saat ini.

Hasil analisis dapat menjadi dasar apabila pada penelitian selanjutnya ingin dilakukan pengembangan berupa pemantauan berkala, prediksi, atau sistem peringatan.

---

### 4. Evaluasi Kondisi Berdasarkan Data Historis

Hasil analisis data dapat digunakan sebagai informasi pendukung untuk mengevaluasi perubahan kondisi polutan berdasarkan data historis.

Data yang dikumpulkan selama satu tahun memberikan gambaran yang dapat digunakan untuk membandingkan kondisi antarperiode.

Evaluasi tersebut dapat membantu:

- melihat perubahan nilai polutan;
- membandingkan kondisi pada waktu yang berbeda;
- mengetahui periode dengan nilai relatif tinggi;
- mengetahui periode dengan nilai relatif rendah;
- memahami karakteristik data yang tersedia.

Evaluasi dalam proyek ini dilakukan berdasarkan nilai dan pola yang terdapat pada dataset.

---

### 5. Menjadi Dasar Analisis Selanjutnya

Hasil pemahaman terhadap dataset dapat digunakan sebagai dasar untuk tahap analisis berikutnya.

Sebelum melakukan analisis yang lebih lanjut, perlu diketahui terlebih dahulu struktur, kelengkapan, distribusi, dan karakteristik data.

Oleh karena itu, Business Understanding menjadi dasar untuk menentukan arah analisis pada tahap:

- Data Understanding;
- Eksplorasi Data;
- Data Preparation;
- analisis pola dan tren.

---

## 1.3 Pertanyaan Utama Analisis

Berdasarkan tujuan proyek, beberapa pertanyaan utama yang ingin dijawab melalui proses analisis data adalah:

1. Bagaimana perubahan nilai NO₂ di Kecamatan Kalitengah selama periode pengamatan?
2. Bagaimana perubahan nilai CO di Kecamatan Kalitengah selama periode pengamatan?
3. Bagaimana perubahan nilai SO₂ di Kecamatan Kalitengah selama periode pengamatan?
4. Apakah terdapat pola kenaikan atau penurunan nilai polutan pada periode tertentu?
5. Pada periode kapan nilai masing-masing polutan relatif tinggi atau rendah?
6. Bagaimana perbedaan pola perubahan antara NO₂, CO, dan SO₂?
7. Bagaimana kondisi kelengkapan data pada masing-masing fitur polutan?
8. Apakah terdapat karakteristik data, seperti missing values atau nilai negatif, yang perlu diperhatikan sebelum analisis lanjutan?

Pertanyaan tersebut menjadi acuan dalam proses Data Understanding dan Eksplorasi Data.

---

## 1.4 Ruang Lingkup

Ruang lingkup proyek ini dibatasi pada pengumpulan, pemeriksaan, dan analisis data polutan udara di Kecamatan Kalitengah, Kabupaten Lamongan, Jawa Timur.

Data yang dianalisis meliputi:

- fitur waktu `date`;
- NO₂ (`NO2`);
- CO (`CO`);
- SO₂ (`SO2`).

Wilayah penelitian dibatasi berdasarkan wilayah Kecamatan Kalitengah.

Periode pengamatan yang digunakan adalah:

**31 Agustus 2025 – 31 Agustus 2026.**

Dataset memiliki total **366 tanggal kalender** dalam periode tersebut.

Analisis difokuskan pada:

- pemeriksaan struktur dataset;
- pemeriksaan kualitas dan kelengkapan data;
- eksplorasi karakteristik data;
- analisis statistik deskriptif;
- visualisasi perubahan polutan;
- identifikasi pola dan tren berdasarkan waktu.

---

## 1.5 Batasan Proyek

Agar analisis tetap sesuai dengan tujuan proyek, terdapat beberapa batasan yang perlu diperhatikan.

### 1. Terbatas pada Tiga Jenis Polutan

Analisis hanya menggunakan tiga fitur polutan yang tersedia dalam dataset, yaitu:

- NO₂;
- CO;
- SO₂.

Polutan lain yang tidak terdapat dalam dataset tidak dianalisis dalam proyek ini.

---

### 2. Terbatas pada Wilayah Kecamatan Kalitengah

Analisis hanya dilakukan pada wilayah Kecamatan Kalitengah, Kabupaten Lamongan.

Hasil analisis tidak digunakan untuk menggambarkan kondisi seluruh Kabupaten Lamongan atau wilayah lain di luar batas penelitian.

---

### 3. Terbatas pada Periode Data yang Digunakan

Periode analisis hanya mencakup data dari:

**31 Agustus 2025 sampai 31 Agustus 2026.**

Kesimpulan yang diperoleh hanya menggambarkan karakteristik data pada periode tersebut.

---

### 4. Tidak Menentukan Sumber Emisi Secara Langsung

Walaupun masing-masing polutan memiliki sumber emisi yang secara umum diketahui, proyek ini tidak melakukan analisis untuk menentukan sumber emisi secara langsung.

Perubahan nilai polutan dalam dataset tidak langsung dikaitkan dengan aktivitas tertentu tanpa data pendukung tambahan.

---

### 5. Tidak Digunakan sebagai Penetapan Status Kesehatan Udara

Nilai yang terdapat pada dataset digunakan untuk analisis perubahan dan karakteristik polutan.

Proyek ini tidak secara langsung digunakan untuk menetapkan kategori kesehatan udara atau status kualitas udara berdasarkan standar tertentu.

Untuk melakukan penilaian tersebut diperlukan metode, satuan, dan standar pembanding yang sesuai.

---

### 6. Tidak Membangun Sistem Prediksi atau Peringatan Otomatis

Proyek pada tahap ini berfokus pada pemahaman dan eksplorasi data.

Sistem prediksi, machine learning, maupun peringatan dini otomatis belum menjadi bagian dari implementasi utama.

Namun, hasil analisis dapat digunakan sebagai dasar untuk pengembangan proyek pada tahap berikutnya.

---

## 1.6 Output yang Diharapkan

Output yang diharapkan dari tahap Business Understanding adalah:

1. Menentukan tujuan pengumpulan dan analisis data polutan.
2. Menentukan wilayah penelitian.
3. Menentukan jenis polutan yang akan dianalisis.
4. Menentukan periode pengamatan.
5. Menentukan pertanyaan utama analisis.
6. Menentukan ruang lingkup dan batasan proyek.
7. Menentukan kebutuhan analisis terhadap data.
8. Menentukan informasi yang diharapkan dari hasil analisis.

Secara umum, hasil analisis diharapkan dapat memberikan gambaran mengenai:

- perubahan NO₂;
- perubahan CO;
- perubahan SO₂;
- pola perubahan berdasarkan waktu;
- karakteristik masing-masing fitur;
- kondisi kelengkapan data;
- periode dengan nilai relatif tinggi dan rendah.

---

## 1.7 Kebutuhan Analisis

Untuk mencapai tujuan proyek, data perlu dianalisis melalui beberapa tahapan.

### Tahap 1 — Data Understanding

Tahap ini digunakan untuk memahami:

- struktur dataset;
- jumlah baris dan kolom;
- nama fitur;
- tipe data;
- periode pengamatan;
- jumlah data valid;
- missing values;
- nilai minimum dan maksimum;
- karakteristik khusus pada data.

---

### Tahap 2 — Eksplorasi Data

Tahap eksplorasi dilakukan untuk melihat:

- distribusi nilai polutan;
- pola perubahan data;
- tren berdasarkan waktu;
- perbandingan antarperiode;
- karakteristik masing-masing fitur;
- kemungkinan hubungan perubahan antarpolutan.

---

### Tahap 3 — Data Preparation

Tahap pengolahan data dilakukan apabila diperlukan berdasarkan hasil pemeriksaan sebelumnya.

Beberapa kondisi yang perlu diperhatikan antara lain:

- missing values;
- nilai negatif;
- format tanggal;
- konsistensi tipe data.

Penanganan data dilakukan berdasarkan hasil pemeriksaan dan kebutuhan analisis.

---

## 1.8 Indikator Keberhasilan Analisis

Analisis dianggap memenuhi tujuan awal apabila dapat memberikan informasi yang jelas mengenai:

1. struktur dan karakteristik dataset;
2. periode pengamatan;
3. jumlah data yang tersedia;
4. kondisi missing values;
5. perubahan nilai NO₂ dari waktu ke waktu;
6. perubahan nilai CO dari waktu ke waktu;
7. perubahan nilai SO₂ dari waktu ke waktu;
8. pola atau tren yang dapat diamati dari data;
9. karakteristik data yang perlu diperhatikan dalam tahap berikutnya.

Dengan demikian, keberhasilan proyek tidak hanya dilihat dari hasil visualisasi, tetapi juga dari kemampuan analisis dalam menjelaskan kondisi dan karakteristik dataset secara jelas.

---

## 1.9 Kesimpulan Business Understanding

Berdasarkan tahap Business Understanding, proyek ini berfokus pada pemantauan dan analisis perubahan data polutan udara di Kecamatan Kalitengah, Kabupaten Lamongan.

Dataset yang digunakan terdiri dari empat fitur utama, yaitu `date`, `NO2`, `CO`, dan `SO2`.

Fitur `date` digunakan sebagai penanda waktu, sedangkan NO₂, CO, dan SO₂ digunakan untuk menggambarkan nilai tiga jenis polutan yang diamati.

Periode pengamatan berlangsung selama satu tahun, yaitu dari **31 Agustus 2025 sampai 31 Agustus 2026**, dengan total **366 tanggal kalender**.

Tujuan utama analisis adalah memahami bagaimana nilai masing-masing polutan berubah berdasarkan waktu, mengidentifikasi pola atau tren, serta memahami karakteristik dan kualitas data sebelum dilakukan analisis yang lebih lanjut.

Analisis dibatasi pada wilayah Kecamatan Kalitengah dan tiga jenis polutan yang tersedia dalam dataset. Proyek ini tidak bertujuan untuk menentukan sumber emisi secara langsung, menetapkan status kesehatan udara, maupun membangun sistem prediksi atau peringatan otomatis.

Tahap selanjutnya adalah **Data Understanding**, yaitu memahami sumber, struktur, karakteristik, kelengkapan, serta kondisi data yang telah dikumpulkan.
