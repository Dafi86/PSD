# Klasifikasi Tutupan Lahan Provinsi Jawa Timur Berbasis Citra Sentinel-2 Menggunakan Machine Learning

**Aplikasi dashboard:** [Klasifikasi Tutupan Lahan Jawa Timur](https://24-027klasifikasijawatimur.streamlit.app/)  
**Repositori proyek:** [GitHub – 24-027_klasifikasijawatimur](https://github.com/Dafi86/24-027_klasifikasijawatimur)  
**Wilayah kajian:** Provinsi Jawa Timur, Indonesia

> **Catatan dokumentasi:** Dokumen ini diperbarui dengan membaca notebook Google Colab serta berkas evaluasi (`classification_report.csv`, `confusion_matrix.csv`, dan `evaluasi_model.csv`). Angka dataset, poligon, split, dan periode citra merujuk pada kode/output notebook yang tersimpan; sumber asal dan proses validasi poligon masih perlu dikonfirmasi dari data referensi.

## 1. Ringkasan

Proyek ini mengembangkan dashboard untuk klasifikasi tutupan lahan di Provinsi Jawa Timur menggunakan fitur spektral citra Sentinel-2 dan model machine learning. Dashboard proyek menyediakan konteks untuk melihat hasil klasifikasi, evaluasi model, serta prediksi tutupan lahan.

Model membedakan enam kelas: **Sawah, Bangunan, Mangrove, Lahan Hijau, Laut, dan Danau/Ranu**. Berdasarkan laporan evaluasi yang dilampirkan, model memperoleh akurasi keseluruhan **82,34%** pada **6.404 sampel uji**, dengan **macro F1-score 0,7882**. Hasil tiap kelas tidak seragam; kelas Bangunan memiliki F1-score tertinggi, sementara Laut merupakan kelas dengan F1-score terendah.

## 2. Latar Belakang

Tutupan lahan menggambarkan penutupan biofisik pada permukaan bumi yang dapat diamati, termasuk melalui interpretasi citra penginderaan jauh. Informasi tutupan lahan berguna sebagai salah satu masukan untuk memahami kondisi lingkungan dan persebaran objek di suatu wilayah.

Citra satelit menyediakan informasi spektral yang dapat diolah menjadi fitur untuk membedakan jenis permukaan. Namun, karakteristik spektral antarkelas dapat saling tumpang tindih. Karena itu, hasil klasifikasi perlu dievaluasi menggunakan data uji dan metrik yang sesuai, bukan hanya dilihat dari peta hasil prediksi.

## 3. Tujuan

Tujuan proyek ini adalah:
1. Mengklasifikasikan tutupan lahan di Provinsi Jawa Timur ke dalam enam kelas yang ditetapkan dalam proyek.
2. Memanfaatkan band spektral Sentinel-2 dan indeks spektral sebagai fitur masukan model.
3. Menyajikan hasil klasifikasi dan evaluasi melalui dashboard berbasis web.
4. Mengidentifikasi kelas yang telah dikenali dengan baik dan kelas yang masih sering tertukar berdasarkan laporan evaluasi.

## 4. Wilayah Kajian dan Kelas

Wilayah kajian adalah Provinsi Jawa Timur. Enam kelas yang digunakan dalam proyek adalah:

| Kelas | Deskripsi ringkas |
|---|---|
| Sawah | Area persawahan |
| Bangunan | Area terbangun |
| Mangrove | Area vegetasi mangrove |
| Lahan Hijau | Kelas lahan bervegetasi yang didefinisikan sebagai “Lahan Hijau” dalam proyek |
| Laut | Area laut |
| Danau/Ranu | Area danau atau ranu |

Definisi operasional dan aturan pelabelan rinci setiap kelas perlu mengikuti data referensi/label yang digunakan saat membangun dataset. Aturan tersebut belum disertakan dalam berkas evaluasi.

## 5. Data dan Fitur

### 5.1 Sumber citra

Proyek menggunakan fitur yang berkaitan dengan citra Sentinel-2. Rentang tanggal akuisisi, produk Sentinel-2 yang dipakai, tingkat pemrosesan, metode masking awan, resolusi, serta sumber label belum dijelaskan dalam berkas yang tersedia dan perlu dicantumkan untuk memastikan proses dapat direplikasi.

### 5.2 Fitur masukan model

Fitur yang tercatat untuk model adalah:

| Fitur | Keterangan |
|---|---|
| B02 | Band spektral Sentinel-2 |
| B03 | Band spektral Sentinel-2 |
| B04 | Band spektral Sentinel-2 |
| B08 | Band spektral Sentinel-2 |
| B11 | Band spektral Sentinel-2 |
| NDVI | Indeks vegetasi |
| NDWI | Indeks air |
| MNDWI | Indeks air termodifikasi |
| NDBI | Indeks area terbangun |

Rumus, skala nilai, proses normalisasi, serta penanganan data hilang harus disesuaikan dengan implementasi yang benar-benar digunakan dalam kode proyek. Jangan menganggap langkah-langkah tersebut dilakukan apabila belum diverifikasi.

## 6. Metode Klasifikasi

Metadata proyek yang tersedia mengidentifikasi estimator sebagai **ExtraTreesClassifier**. Dengan demikian, dokumentasi ini menyebut model sebagai Extra Trees, bukan XGBoost. Nama berkas model yang berbeda tidak cukup untuk menentukan algoritma; jenis estimator yang dimuat oleh model menjadi acuan yang lebih relevan.

Secara umum, Extra Trees merupakan metode ensemble yang menggabungkan banyak pohon keputusan. Namun, parameter aktual—misalnya jumlah pohon, kedalaman maksimum, kriteria pemisahan, random state, dan bobot kelas—belum tersedia pada berkas yang dilampirkan.

Alur kerja tingkat tinggi proyek:

1. Menyiapkan citra dan data label tutupan lahan.
2. Mengambil nilai band dan menghitung/menyediakan indeks spektral.
3. Membentuk tabel fitur untuk kelas target.
4. Melatih model klasifikasi dan menguji prediksi pada data uji.
5. Menghitung metrik evaluasi dan matriks kebingungan.
6. Menyajikan hasil melalui dashboard Streamlit.

Langkah-langkah tersebut merupakan gambaran umum alur klasifikasi. Rincian pelaksanaan dan pembagian dataset perlu diverifikasi dengan kode proyek.

## 7. Evaluasi Model

Evaluasi berikut ditranskripsikan dari `classification_report.csv` dan `confusion_matrix.csv` yang diberikan.

### 7.1 Metrik keseluruhan

| Metrik | Nilai |
|---|---:|
| Akurasi | 0,823392 (82,34%) |
| Macro precision | 0,792728 |
| Macro recall | 0,791763 |
| Macro F1-score | 0,788203 |
| Jumlah sampel uji | 6.404 |

Akurasi menunjukkan proporsi seluruh prediksi yang benar. Macro F1-score menghitung F1 setiap kelas lalu merata-ratakannya tanpa memberi bobot berdasarkan jumlah sampel tiap kelas. Selisih antara akurasi dan macro F1 menunjukkan bahwa performa perlu dilihat per kelas, bukan hanya melalui satu angka keseluruhan.

### 7.2 Metrik per kelas

| Kelas | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Sawah | 0,8992 | 0,7783 | 0,8344 | 1.800 |
| Bangunan | 0,9324 | 0,9165 | 0,9244 | 1.581 |
| Mangrove | 0,8363 | 0,8191 | 0,8276 | 923 |
| Lahan Hijau | 0,7219 | 0,9517 | 0,8210 | 1.200 |
| Laut | 0,5547 | 0,4650 | 0,5059 | 600 |
| Danau/Ranu | 0,8119 | 0,8200 | 0,8159 | 300 |

**Interpretasi utama:**

- **Bangunan** menunjukkan F1-score tertinggi (0,9244), dengan precision dan recall sama-sama tinggi pada data uji.
- **Sawah** memiliki precision tinggi (0,8992), tetapi recall 0,7783. Ini berarti sebagian sampel Sawah aktual tidak teridentifikasi sebagai Sawah.
- **Lahan Hijau** memiliki recall sangat tinggi (0,9517), tetapi precision lebih rendah (0,7219). Model menangkap sebagian besar sampel Lahan Hijau aktual, namun sejumlah prediksi Lahan Hijau berasal dari kelas lain.
- **Laut** memiliki F1-score terendah (0,5059), recall 0,4650, dan precision 0,5547. Kelas ini menjadi prioritas untuk pemeriksaan data dan perbaikan model.
- **Mangrove** dan **Danau/Ranu** memiliki F1-score masing-masing 0,8276 dan 0,8159. Untuk Danau/Ranu, jumlah sampel uji relatif lebih kecil (300), sehingga evaluasi tambahan dapat membantu menilai kestabilan metriknya.

### 7.3 Matriks kebingungan

Baris menunjukkan kelas aktual dan kolom menunjukkan kelas prediksi.

| Aktual \ Prediksi | Sawah | Bangunan | Mangrove | Lahan Hijau | Laut | Danau/Ranu |
|---|---:|---:|---:|---:|---:|---:|
| Sawah | 1.401 | 39 | 102 | 179 | 67 | 12 |
| Bangunan | 108 | 1.449 | 0 | 8 | 16 | 0 |
| Mangrove | 6 | 1 | 756 | 89 | 66 | 5 |
| Lahan Hijau | 11 | 3 | 22 | 1.142 | 22 | 0 |
| Laut | 32 | 61 | 24 | 164 | 279 | 40 |
| Danau/Ranu | 0 | 1 | 0 | 0 | 53 | 246 |

Pola kekeliruan yang menonjol:
- Dari **600 sampel Laut**, 279 diprediksi benar sebagai Laut. Kekeliruan terbesar adalah Laut diprediksi sebagai Lahan Hijau (164 sampel), kemudian Bangunan (61 sampel).
- Dari **1.800 sampel Sawah**, 1.401 diprediksi benar; kekeliruan terbanyak adalah menjadi Lahan Hijau (179) dan Mangrove (102).
- Dari **923 sampel Mangrove**, 756 diprediksi benar dan 89 diprediksi sebagai Lahan Hijau.
- Dari **300 sampel Danau/Ranu**, 246 diprediksi benar dan 53 diprediksi sebagai Laut.

Kekeliruan ini menunjukkan kelas yang perlu ditinjau, tetapi matriks kebingungan saja tidak menjelaskan penyebabnya. Penyebab potensial—seperti kemiripan spektral, kualitas label, kondisi citra, atau ketidakseimbangan kelas—perlu diperiksa menggunakan data dan proses pemodelan asli.

## 8. Pembahasan dan Rekomendasi

Berdasarkan berkas evaluasi, performa model cukup baik secara keseluruhan, tetapi belum merata pada keenam kelas. Beberapa tindak lanjut yang layak diuji adalah:

1. **Audit sampel Laut dan Lahan Hijau.** Periksa sampel yang tertukar, lokasi spasialnya, kualitas label, serta apakah citra dan label berasal dari periode yang sebanding.
2. **Periksa kelas Mangrove dan Sawah.** Tinjau contoh yang diprediksi sebagai Lahan Hijau untuk memahami apakah terdapat tumpang tindih definisi atau karakteristik spektral.
3. **Evaluasi data dan pembagian uji.** Pastikan data uji terpisah dari data pelatihan dan validasi. Untuk data spasial, pertimbangkan pemisahan berdasarkan lokasi agar skor tidak terlalu optimistis akibat sampel yang berdekatan.
4. **Bandingkan eksperimen secara terukur.** Uji parameter model, fitur, atau strategi penanganan kelas secara terpisah, kemudian bandingkan macro F1 dan metrik per kelas.
5. **Laporkan ketidakpastian.** Bila hasil akan digunakan untuk pengambilan keputusan, sertakan batasan data, tanggal citra, skala spasial, dan validasi tambahan.

Rekomendasi tersebut merupakan usulan untuk eksperimen lanjutan, bukan klaim bahwa eksperimen tersebut sudah dilakukan.

## 9. Batasan

Dokumentasi dan tiga CSV evaluasi belum menyediakan informasi mengenai:
- tanggal/periode citra dan produk Sentinel-2 yang digunakan;
- sumber dan proses pembuatan label;
- jumlah sampel sebelum pemisahan data serta proporsi train/validation/test;
- parameter lengkap ExtraTreesClassifier;
- prosedur prapemrosesan, masking awan, dan perhitungan indeks;
- validasi geografis independen dan ketidakpastian spasial.

Informasi tersebut perlu ditambahkan dari kode, catatan eksperimen, atau sumber data asli sebelum dokumen digunakan sebagai laporan penelitian final.

## 10. Aplikasi

Dashboard dapat diakses melalui:

- **Aplikasi Streamlit:** https://24-027klasifikasijawatimur.streamlit.app/
- **Repositori GitHub:** https://github.com/Dafi86/24-027_klasifikasijawatimur

Nama menu dan fitur pada dashboard sebaiknya dicocokkan dengan versi aplikasi yang aktif saat laporan diterbitkan.

## Daftar Pustaka

European Space Agency. (n.d.). *Sentinel-2*. https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2

Badan Pusat Statistik. (2023). *Metadata variabel statistik: Penutupan lahan*. https://sirusa.web.bps.go.id/metadata/variabel/5f468298-8f40-9d3d-65e6-0ab06da7cc7e

Geurts, P., Ernst, D., & Wehenkel, L. (2006). Extremely randomized trees. *Machine Learning, 63*, 3–42. https://doi.org/10.1007/s10994-006-6226-1

Scikit-learn developers. (n.d.). *ExtraTreesClassifier*. https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html

Klasifikasi Tutupan Lahan Jawa Timur. (n.d.). *Dashboard aplikasi*. https://24-027klasifikasijawatimur.streamlit.app/

## Lampiran: Berkas Evaluasi

Angka evaluasi dalam dokumen ini berasal dari berkas berikut yang disediakan bersama proyek:
- `classification_report.csv`
- `confusion_matrix.csv`
- `evaluasi_model.csv`

Berkas `evaluasi_model.csv` berisi pasangan label aktual (`y_true`) dan prediksi (`y_pred`) sebanyak 6.404 baris. Jika dilakukan analisis lanjutan dari berkas ini, hasilnya perlu dihitung ulang dari pasangan tersebut dan dicocokkan dengan laporan evaluasi di atas.

## 11. Penguatan Data Understanding

Bagian ini memisahkan informasi yang sudah terverifikasi dari berkas evaluasi dan informasi yang masih harus ditelusuri dari dataset atau kode sumber.

### 11.1 Informasi yang sudah terverifikasi

- **Jumlah sampel evaluasi/uji:** 6.404 baris pada `evaluasi_model.csv`, dengan kolom `y_true` dan `y_pred`.
- **Jumlah kelas target:** 6, yaitu Sawah, Bangunan, Mangrove, Lahan Hijau, Laut, dan Danau/Ranu.
- **Jumlah fitur model:** 9, yaitu B02, B03, B04, B08, B11, NDVI, NDWI, MNDWI, dan NDBI.
- **Model:** metadata proyek yang tersedia mengidentifikasi estimator sebagai `ExtraTreesClassifier`.
- **Metrik evaluasi:** akurasi 0,823392 dan macro F1-score 0,788203.

Jumlah 6.404 adalah jumlah sampel yang dievaluasi, bukan bukti jumlah seluruh dataset sebelum pembagian training dan testing. CSV evaluasi tidak memuat identitas polygon, geometri, koordinat, atau asal-usul sampel.

### 11.2 Distribusi sampel evaluasi per kelas

| Kelas | Jumlah sampel uji | Proporsi dari 6.404 |
|---|---:|---:|
| Sawah | 1.800 | 28,11% |
| Bangunan | 1.581 | 24,69% |
| Mangrove | 923 | 14,41% |
| Lahan Hijau | 1.200 | 18,74% |
| Laut | 600 | 9,37% |
| Danau/Ranu | 300 | 4,68% |
| **Total** | **6.404** | **100%** |

Distribusi ini hanya menggambarkan sampel evaluasi yang ada di laporan, bukan komposisi keseluruhan data mentah atau data training.

### 11.3 Informasi polygon yang harus dilengkapi

Berkas evaluasi yang tersedia belum menunjukkan polygon apa yang digunakan. Untuk menjelaskan bagian ini secara benar, periksa dataset asli, notebook, atau kode preprocessing dan catat:

1. **Peran polygon:** apakah polygon digunakan sebagai sampel berlabel untuk setiap kelas, sebagai batas administrasi Jawa Timur, atau keduanya.
2. **Sumber polygon:** digitasi manual, shapefile/GeoJSON dari sumber tertentu, atau dataset tutupan lahan lain.
3. **Jumlah polygon:** jumlah fitur polygon seluruhnya dan jumlah per kelas.
4. **Sebaran spasial:** kabupaten/kota atau koordinat lokasi sampel per kelas.
5. **Atribut label:** nama kolom yang menyimpan kelas dan bagaimana label dipetakan ke enam kelas model.
6. **Hubungan polygon dengan sampel:** apakah setiap polygon menghasilkan satu sampel, banyak piksel/sampel, atau statistik agregat.
7. **Pencegahan kebocoran data:** apakah sampel dari polygon/lokasi yang sama bisa masuk ke data training dan testing sekaligus.

Jangan menyebut jumlah polygon, nama lokasi polygon, sumber label, atau rasio training/testing sebelum memverifikasinya dari data/kode asli.

### 11.4 Data Understanding: pertanyaan dan jawaban yang aman

**T: Berapa jumlah datanya?**  
J: “File evaluasi berisi 6.404 sampel uji. Jumlah keseluruhan dataset dan jumlah data training perlu saya cocokkan dengan proses pembentukan dataset serta pembagian train-test.”

**T: Ada berapa kelas?**  
J: “Ada enam kelas target: Sawah, Bangunan, Mangrove, Lahan Hijau, Laut, dan Danau/Ranu.”

**T: Fitur apa yang digunakan?**  
J: “Model menggunakan sembilan fitur, yaitu lima band Sentinel-2—B02, B03, B04, B08, dan B11—serta empat indeks spektral: NDVI, NDWI, MNDWI, dan NDBI.”

**T: Polygon apa saja yang digunakan?**  
J: “CSV evaluasi tidak menyimpan geometri atau identitas polygon. Saya perlu merujuk kembali ke dataset sumber atau kode preprocessing untuk memastikan polygon sampel, jumlahnya, sumbernya, dan sebarannya per kelas.”

**T: Apakah 6.404 itu total seluruh data?**  
J: “Belum tentu. Angka 6.404 adalah jumlah sampel yang tercatat pada evaluasi. Jumlah seluruh dataset sebelum pemisahan data tidak bisa disimpulkan dari file ini saja.”

### 11.5 Checklist sebelum presentasi

- [ ] Catat total sampel sebelum train-test split.
- [ ] Catat jumlah sampel training, validation (jika ada), dan testing.
- [ ] Pastikan rasio atau metode pembagian dataset.
- [ ] Temukan file polygon asli (misalnya SHP, GeoJSON, atau GeoPackage) atau kode yang membuatnya.
- [ ] Hitung total polygon dan polygon per kelas.
- [ ] Catat sumber label dan metode penentuan label.
- [ ] Catat periode citra Sentinel-2 dan langkah preprocessing yang benar-benar digunakan.
- [ ] Pastikan sampel dari polygon/lokasi yang sama tidak menyebabkan kebocoran antara training dan testing.

Checklist ini perlu dilengkapi dari sumber data dan kode asli sebelum dokumentasi dipakai sebagai laporan final.


## 12. Pembaruan Data Understanding berdasarkan notebook Google Colab

**Bagian ini memperbarui bagian 11** setelah notebook `klasifikasi_tutupan_lahan_jatim_colab.ipynb` diperiksa. Angka di bawah berasal dari kode dan output yang tersimpan di notebook. Pastikan output tersebut berasal dari run yang sama dengan model yang dipakai dashboard.

### 12.1 Sumber dan cakupan data citra

- **Sumber citra:** hasil ekspor Google Earth Engine dari koleksi `COPERNICUS/S2_SR_HARMONIZED` (Sentinel-2 Level-2A).
- **Periode yang dikonfigurasi:** 1 Juni–2 Juli 2026 (inklusif).
- **Pemilihan dan masking pada proses ekspor sebelumnya:** scene dengan tutupan awan kurang dari 30%; masker SCL mengecualikan kelas 0, 1, 3, 8, 9, 10, dan 11.
- **Input notebook:** 43 GeoTIFF yang sudah ada di Google Drive; notebook pelatihan ini membaca hasil ekspor tersebut, bukan mengunduh ulang citra.
- **Grid analisis:** 43 fitur grid unik, CRS `EPSG:4326`, geometri valid pada output yang tersimpan.
- **Resolusi target raster:** 10 m. Perlu diingat bahwa band B11 memiliki resolusi asli 20 m dan disesuaikan ke grid 10 m melalui resampling; ini tidak berarti detail asli B11 menjadi 10 m.

### 12.2 Sampel poligon referensi

Notebook mencatat sampel referensi pada GeoPackage `sampel_tutupan_lahan_jatim.gpkg`, dengan kolom label `kelas` dan identitas `polygon_id`. Catatan notebook menyebut poligon referensi harus disiapkan/didigitasi atau berasal dari sumber yang dapat dipertanggungjawabkan; notebook ini sendiri tidak membuktikan sumber eksternal atau metode digitasi yang digunakan.

| Kelas | Poligon referensi awal | Poligon dengan piksel fitur valid | Piksel fitur hasil ekstraksi |
|---|---:|---:|---:|
| Sawah | 20 | 20 | 6.300 |
| Bangunan | 40 | 40 | 12.332 |
| Mangrove | 17 | 16 | 4.385 |
| Lahan Hijau | 11 | 11 | 4.200 |
| Laut | 19 | 6 | 2.403 |
| Danau/Ranu | 14 | 14 | 4.200 |
| **Total** | **121** | **107** | **33.820** |

**Cara membaca angka ini:**
- **121** adalah jumlah objek poligon referensi yang tercatat sebelum ekstraksi fitur.
- **107** adalah jumlah poligon unik yang benar-benar menghasilkan piksel fitur valid. Untuk Mangrove, satu poligon tidak menghasilkan fitur valid; untuk Laut, hanya 6 dari 19 poligon yang menghasilkan fitur valid dalam raster yang diproses.
- **33.820** adalah jumlah baris/piksel sampel setelah ekstraksi fitur dan penyaringan nilai tidak valid. Angka ini bukan jumlah poligon dan bukan jumlah seluruh piksel citra Jawa Timur.
- Ekstraksi dibatasi maksimum 300 piksel acak per poligon per tile. Karena satu poligon dapat memotong lebih dari satu tile, jumlah piksel tidak sama dengan jumlah poligon dikali 300 secara sederhana.

### 12.3 Pembagian training, validation, dan testing

Output notebook menunjukkan pembagian berdasarkan **kelompok `polygon_id`**, bukan pembagian piksel acak yang mengizinkan piksel dari poligon sama tersebar ke beberapa set. Tidak ditemukan overlap antarkelompok pada output yang tersimpan.

| Set | Jumlah piksel | Jumlah poligon |
|---|---:|---:|
| Training | 21.331 | 65 |
| Validation | 6.085 | 21 |
| Testing | 6.404 | 21 |
| **Total** | **33.820** | **107** |

Proporsi berdasarkan jumlah piksel sekitar **63,07% training**, **18,00% validation**, dan **18,94% testing**. Persentase ini bukan rasio split yang ditentukan langsung atas setiap piksel; pembagian dilakukan pada kelompok poligon sehingga jumlah piksel per set mengikuti isi poligon.

Distribusi per kelas pada output split:

| Kelas | Piksel training | Piksel validation | Piksel testing | Poligon training | Poligon validation | Poligon testing |
|---|---:|---:|---:|---:|---:|---:|
| Sawah | 3.600 | 900 | 1.800 | 11 | 3 | 6 |
| Bangunan | 8.866 | 1.885 | 1.581 | 27 | 7 | 6 |
| Mangrove | 2.562 | 900 | 923 | 9 | 3 | 4 |
| Lahan Hijau | 2.100 | 900 | 1.200 | 5 | 3 | 3 |
| Laut | 1.203 | 600 | 600 | 3 | 2 | 1 |
| Danau/Ranu | 3.000 | 900 | 300 | 10 | 3 | 1 |
| **Total** | **21.331** | **6.085** | **6.404** | **65** | **21** | **21** |

Perhatian: kelas Laut dan Danau/Ranu masing-masing hanya memiliki satu poligon pada set testing menurut output notebook. Walaupun jumlah piksel test-nya ratusan, piksel dalam satu poligon tidak sama dengan ratusan lokasi independen. Ini membatasi seberapa jauh hasil evaluasi dapat digeneralisasi ke lokasi lain. Penambahan poligon test independen, terutama untuk kelas-kelas tersebut, akan memperkuat evaluasi.

### 12.4 Fitur yang digunakan

Model menerima sembilan fitur:
- **Band reflektansi:** B02 (Blue), B03 (Green), B04 (Red), B08 (NIR), B11 (SWIR1).
- **Indeks spektral:** NDVI, NDWI, MNDWI, NDBI.

Rumus yang tercantum dalam notebook:
- `NDVI = (B08 − B04) / (B08 + B04)`
- `NDWI = (B03 − B08) / (B03 + B08)`
- `MNDWI = (B03 − B11) / (B03 + B11)`
- `NDBI = (B11 − B08) / (B11 + B08)`

Piksel dengan fitur tidak valid/NaN dikeluarkan dari dataset fitur.

### 12.5 Pemilihan model dan evaluasi

Notebook membandingkan Random Forest, Extra Trees, SVM RBF, dan HistGradientBoosting. Pemilihan kandidat dilakukan menggunakan akurasi validation tertinggi, dengan Macro F1 sebagai pemecah seri. Output memilih **Extra Trees**.

| Model | Dataset pemilihan | Akurasi | Macro F1 |
|---|---|---:|---:|
| Extra Trees | Validation | 0,8600 | 0,8442 |
| Random Forest | Validation | 0,8212 | 0,7776 |
| SVM RBF | Validation | 0,8099 | 0,8019 |
| HistGradientBoosting | Validation | 0,8003 | 0,7567 |

Setelah pemilihan model, metrik test Extra Trees yang tercatat adalah:
- **Akurasi:** 0,823392 (82,34%)
- **Balanced accuracy / macro recall:** 0,791763
- **Macro precision:** 0,792728
- **Macro F1:** 0,788203
- **Weighted F1:** 0,821488

Jumlah sampel testing 6.404 pada notebook konsisten dengan jumlah baris dalam `evaluasi_model.csv` dan total support pada classification report yang diberikan. Namun, untuk presentasi, sebaiknya pastikan berkas evaluasi dan model dashboard memang diekspor dari run notebook yang sama.

### 12.6 Jawaban singkat untuk pertanyaan presentasi

**“Berapa jumlah data yang digunakan?”**  
“Notebook mengekstrak 33.820 sampel piksel berfitur dari 121 poligon referensi awal. Dari jumlah itu, 107 poligon menghasilkan fitur valid. Dataset dibagi berbasis poligon menjadi 21.331 sampel training, 6.085 validation, dan 6.404 testing.”

**“Ada berapa poligon?”**  
“Ada 121 poligon referensi awal. Setelah ekstraksi dan pemeriksaan fitur valid, 107 poligon digunakan dalam dataset fitur.”

**“Mengapa jumlah poligon valid lebih sedikit?”**  
“Tidak semua poligon menghasilkan piksel valid yang beririsan dengan raster input. Perbedaan paling besar ada pada kelas Laut: 19 poligon awal, tetapi 6 poligon menghasilkan fitur valid.”

**“Bagaimana mencegah data bocor antara training dan testing?”**  
“Pembagian dilakukan berdasarkan `polygon_id`, sehingga piksel dari satu poligon tidak dibagi ke training, validation, dan testing sekaligus. Output notebook mencatat overlap antarkelompok nol.”

**“Apakah hasil test sepenuhnya mewakili semua wilayah Jawa Timur?”**  
“Belum tentu. Jumlah sampel piksel test besar, tetapi beberapa kelas hanya diwakili satu poligon pada test. Karena itu, evaluasi independen tambahan pada lebih banyak poligon/lokasi akan memperkuat klaim generalisasi.”

### 12.7 Hal yang masih perlu dikonfirmasi

- Sumber asal dan prosedur pembuatan/validasi setiap poligon referensi belum dapat dipastikan hanya dari notebook; notebook menyatakan file sampel disediakan sebagai input.
- Perlu memastikan hasil evaluasi yang ditampilkan dashboard berasal dari versi model dan run notebook yang sama.
- Periode citra yang tertulis adalah periode konfigurasi ekspor; notebook menggunakan TIFF yang sudah tersedia. Untuk audit penuh, simpan metadata ekspor GEE dan identitas scene yang membentuk TIFF.
