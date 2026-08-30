# 4. Sumber Polutan

## 4.1 Pendahuluan

Partikulat udara merupakan salah satu komponen penting dalam analisis kualitas udara. Pada project ini, parameter yang dianalisis adalah **PM1, PM2.5, dan PM10**.

Konsentrasi partikulat di udara dapat dipengaruhi oleh berbagai sumber, baik yang berasal dari aktivitas manusia maupun sumber alami.

Identifikasi sumber polutan dilakukan untuk memberikan konteks terhadap data yang dianalisis. Dengan mengetahui sumber yang berpotensi menghasilkan partikulat, perubahan konsentrasi PM1, PM2.5, dan PM10 dapat lebih mudah diinterpretasikan pada tahap analisis berikutnya.

Namun, pada project ini tidak dilakukan pengukuran langsung terhadap sumber emisi tertentu. Oleh karena itu, pembahasan sumber polutan digunakan sebagai **informasi pendukung** dan bukan sebagai bukti bahwa suatu sumber tertentu secara langsung menyebabkan nilai konsentrasi pada dataset.

---

## 4.2 Jenis Partikulat yang Dianalisis

Terdapat tiga parameter partikulat yang digunakan dalam dataset:

| Parameter | Ukuran Partikel | Nama Variabel |
|---|---|---|
| PM1 | ≤ 1 µm | `pm1_ug_m3` |
| PM2.5 | ≤ 2,5 µm | `pm2p5_ug_m3` |
| PM10 | ≤ 10 µm | `pm10_ug_m3` |

Ketiga parameter memiliki ukuran partikel yang berbeda.

Secara umum, partikulat yang berukuran lebih kecil dapat berasal dari proses pembakaran dan proses atmosfer, sedangkan partikulat berukuran lebih besar juga dapat berasal dari debu dan material yang tersuspensi kembali ke udara.

---

## 4.3 Sumber Polutan dari Transportasi

Transportasi merupakan salah satu sumber partikulat yang dapat berasal dari aktivitas kendaraan bermotor.

Sumber partikulat dari transportasi dapat berasal dari:

- emisi pembakaran bahan bakar kendaraan;
- emisi gas buang kendaraan;
- keausan ban;
- keausan rem;
- debu jalan yang kembali tersuspensi akibat pergerakan kendaraan.

Aktivitas kendaraan yang tinggi dapat meningkatkan jumlah partikulat di udara, terutama pada wilayah dengan kepadatan lalu lintas yang tinggi.

Di Kabupaten Lamongan, aktivitas transportasi dapat menjadi salah satu faktor yang perlu diperhatikan ketika menginterpretasikan perubahan konsentrasi partikulat.

Namun, dataset yang digunakan dalam project ini tidak memiliki variabel jumlah kendaraan atau volume lalu lintas. Oleh karena itu, hubungan langsung antara lalu lintas dan konsentrasi partikulat tidak dapat dibuktikan hanya menggunakan dataset ini.

---

## 4.4 Sumber Polutan dari Aktivitas Industri

Aktivitas industri juga dapat menjadi salah satu sumber partikulat udara.

Partikulat dapat dihasilkan dari berbagai aktivitas industri seperti:

- proses pembakaran;
- penggunaan bahan bakar;
- proses produksi;
- pengolahan material;
- aktivitas pemindahan bahan;
- dan proses industri lainnya.

Besarnya kontribusi aktivitas industri terhadap konsentrasi partikulat bergantung pada jenis industri, teknologi yang digunakan, bahan bakar, sistem pengendalian emisi, serta kondisi atmosfer.

Dalam project ini, informasi mengenai lokasi dan intensitas aktivitas industri tidak menjadi variabel utama dataset. Oleh karena itu, aktivitas industri hanya digunakan sebagai salah satu kemungkinan sumber polutan.

---

## 4.5 Sumber Polutan dari Pembakaran

Pembakaran dapat menghasilkan partikulat dalam jumlah tertentu.

Sumber pembakaran dapat berasal dari:

- pembakaran bahan bakar;
- pembakaran biomassa;
- pembakaran sampah;
- pembakaran terbuka;
- dan aktivitas lainnya yang menghasilkan asap.

Proses pembakaran dapat menghasilkan partikulat berukuran kecil yang dapat berkontribusi terhadap konsentrasi PM1 dan PM2.5.

Pembakaran terbuka juga berpotensi menghasilkan campuran berbagai jenis partikulat dan gas yang kemudian dapat mengalami perubahan di atmosfer.

---

## 4.6 Sumber Polutan dari Aktivitas Pertanian

Kabupaten Lamongan memiliki aktivitas pertanian yang cukup luas. Aktivitas pertanian dapat berkontribusi terhadap partikulat melalui beberapa proses.

Contohnya:

- pengolahan tanah;
- aktivitas kendaraan pertanian;
- perpindahan material;
- debu dari lahan;
- pembakaran sisa tanaman;
- dan aktivitas pertanian lainnya.

Debu dari permukaan tanah dapat berkontribusi terhadap partikulat berukuran lebih besar, sedangkan proses pembakaran biomassa dapat menghasilkan partikulat yang lebih halus.

Pada dataset yang digunakan, tidak terdapat variabel khusus mengenai aktivitas pertanian. Oleh karena itu, pengaruh aktivitas pertanian tidak dapat dihitung secara langsung.

---

## 4.7 Debu Jalan dan Debu Permukaan

Debu jalan merupakan salah satu sumber partikulat yang dapat meningkat akibat aktivitas kendaraan dan angin.

Partikel yang berada di permukaan jalan dapat kembali tersuspensi ke udara ketika mendapatkan gangguan mekanis.

Beberapa faktor yang dapat memengaruhi resuspensi debu antara lain:

- jumlah kendaraan;
- kecepatan kendaraan;
- kondisi permukaan jalan;
- kondisi cuaca;
- dan kelembapan permukaan.

Sumber ini lebih berkaitan dengan partikulat yang berukuran relatif lebih besar, meskipun sebagian partikel yang lebih kecil juga dapat ikut tersuspensi.

---

## 4.8 Sumber Alami

Selain aktivitas manusia, partikulat juga dapat berasal dari sumber alami.

Contoh sumber alami antara lain:

- debu tanah;
- material permukaan;
- aerosol laut;
- aktivitas atmosfer;
- dan partikel alami lainnya.

Kontribusi sumber alami dapat berubah berdasarkan kondisi cuaca, arah angin, kelembapan, dan kondisi lingkungan.

Karena data yang digunakan berasal dari sistem pemodelan atmosfer, keberadaan partikulat dalam dataset dapat merupakan hasil dari berbagai proses emisi dan transportasi atmosfer.

---

## 4.9 Pengaruh Kondisi Meteorologi

Kondisi meteorologi memiliki peran penting terhadap konsentrasi partikulat di atmosfer.

Beberapa faktor meteorologi yang dapat memengaruhi konsentrasi partikulat antara lain:

### 1. Angin

Angin dapat menyebabkan partikulat berpindah dari satu lokasi ke lokasi lainnya.

Kecepatan dan arah angin dapat memengaruhi proses:

- penyebaran;
- transportasi;
- dan pengenceran partikulat.

### 2. Hujan

Hujan dapat membantu menghilangkan sebagian partikulat dari atmosfer melalui proses deposisi basah.

Kondisi setelah hujan dapat menyebabkan konsentrasi partikulat berbeda dibandingkan kondisi kering.

### 3. Suhu

Suhu dapat memengaruhi kondisi atmosfer dan proses pembentukan maupun penyebaran polutan.

### 4. Kelembapan

Kelembapan dapat memengaruhi karakteristik aerosol dan kondisi atmosfer.

Pada dataset awal CAMS tersedia berbagai variabel atmosfer. Namun, dataset utama yang digunakan pada project ini difokuskan pada PM1, PM2.5, dan PM10.

---

## 4.10 Hubungan Sumber Polutan dengan PM1, PM2.5, dan PM10

Secara umum, berbagai sumber dapat menghasilkan ukuran partikulat yang berbeda.

| Sumber | PM1 | PM2.5 | PM10 |
|---|:---:|:---:|:---:|
| Pembakaran | ✓ | ✓ | ✓ |
| Emisi kendaraan | ✓ | ✓ | ✓ |
| Aktivitas industri | ✓ | ✓ | ✓ |
| Pembakaran biomassa | ✓ | ✓ | ✓ |
| Debu jalan |  | ✓ | ✓ |
| Debu tanah |  | ✓ | ✓ |
| Aktivitas pertanian |  | ✓ | ✓ |
| Sumber alami | ✓ | ✓ | ✓ |

Tabel tersebut digunakan sebagai gambaran umum mengenai kemungkinan sumber partikulat.

Tabel tersebut **bukan hasil pengukuran kontribusi sumber polutan di Kabupaten Lamongan**. Dataset yang digunakan tidak menyediakan informasi source apportionment, sehingga kontribusi masing-masing sumber tidak dapat dihitung secara langsung.

---

## 4.11 Ringkasan Sumber Polutan

Berdasarkan pembahasan di atas, sumber yang berpotensi berhubungan dengan keberadaan partikulat di wilayah penelitian dapat dikelompokkan menjadi dua kategori.

### Sumber Antropogenik

Sumber yang berkaitan dengan aktivitas manusia:

- transportasi;
- aktivitas industri;
- pembakaran bahan bakar;
- pembakaran terbuka;
- aktivitas pertanian;
- dan aktivitas permukiman.

### Sumber Alami

Sumber yang berasal dari proses alami:

- debu tanah;
- aerosol alami;
- material permukaan;
- dan proses atmosfer.

---

## 4.12 Keterbatasan Identifikasi Sumber Polutan

Identifikasi sumber polutan pada project ini memiliki beberapa keterbatasan.

Dataset utama hanya memiliki informasi:

- waktu;
- latitude;
- longitude;
- PM1;
- PM2.5;
- PM10.

Dataset tidak memiliki informasi langsung mengenai:

- jumlah kendaraan;
- lokasi industri;
- jumlah pembakaran;
- luas lahan terbakar;
- volume emisi;
- arah dan kecepatan angin pada dataset utama;
- atau kontribusi masing-masing sumber emisi.

Oleh karena itu, project ini tidak melakukan **source apportionment** atau perhitungan kontribusi setiap sumber polutan.

Pembahasan sumber polutan digunakan untuk memberikan konteks ketika melakukan interpretasi hasil eksplorasi data.

---

## 4.13 Tujuan Identifikasi Sumber Polutan

Identifikasi sumber polutan dilakukan untuk mendukung analisis pada tahap berikutnya.

Informasi ini dapat membantu ketika ditemukan:

- peningkatan konsentrasi PM;
- penurunan konsentrasi PM;
- nilai ekstrem;
- pola tertentu berdasarkan waktu;
- atau perbedaan karakteristik PM1, PM2.5, dan PM10.

Sebagai contoh, apabila ditemukan peningkatan konsentrasi partikulat pada periode tertentu, hasil tersebut dapat dibahas dengan mempertimbangkan kemungkinan faktor aktivitas manusia maupun kondisi lingkungan.

Namun, interpretasi tersebut tetap harus dibedakan antara **indikasi** dan **bukti kausal**.

---

## 4.14 Alur Identifikasi Sumber Polutan

```text
Data PM1, PM2.5, PM10
          ↓
Identifikasi Karakteristik Partikulat
          ↓
Identifikasi Sumber Antropogenik
          ↓
Transportasi
          ↓
Industri
          ↓
Pembakaran
          ↓
Pertanian
          ↓
Identifikasi Sumber Alami
          ↓
Debu / Aerosol Alami
          ↓
Pertimbangan Kondisi Meteorologi
          ↓
Interpretasi Hasil Eksplorasi Data
```

---

## 4.15 Kesimpulan

PM1, PM2.5, dan PM10 dapat berasal dari berbagai sumber, baik sumber antropogenik maupun sumber alami.

Sumber antropogenik yang berpotensi menghasilkan partikulat meliputi transportasi, aktivitas industri, pembakaran, aktivitas pertanian, serta aktivitas manusia lainnya.

Sementara itu, sumber alami dapat berasal dari debu tanah, material permukaan, aerosol alami, dan proses atmosfer.

Selain sumber emisi, kondisi meteorologi juga dapat memengaruhi penyebaran dan konsentrasi partikulat di atmosfer.

Pada project ini, identifikasi sumber polutan digunakan sebagai informasi pendukung untuk memahami data kualitas udara Kabupaten Lamongan. Karena dataset tidak memiliki informasi kontribusi emisi masing-masing sumber, project ini tidak melakukan perhitungan kontribusi sumber polutan secara langsung.

Hasil identifikasi sumber polutan selanjutnya dapat digunakan sebagai konteks dalam melakukan **Eksplorasi Data** dan interpretasi pola **PM1, PM2.5, dan PM10** berdasarkan waktu.
