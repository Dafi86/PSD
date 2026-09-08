# 4. Sumber Polutan

## 4.1 Pendahuluan

Polutan udara dapat berasal dari berbagai aktivitas yang menghasilkan emisi ke atmosfer. Sumber polutan dapat berasal dari aktivitas manusia maupun proses alami.

Dalam proyek ini, polutan yang dianalisis adalah:

- **NO₂ (Nitrogen Dioxide)**
- **CO (Carbon Monoxide)**
- **SO₂ (Sulfur Dioxide)**

Pemahaman mengenai sumber masing-masing polutan diperlukan agar perubahan nilai yang terdapat dalam dataset dapat diinterpretasikan dengan lebih baik.

Perlu diperhatikan bahwa data yang digunakan dalam proyek ini merupakan data pengamatan berbasis satelit. Oleh karena itu, data tersebut digunakan untuk melihat pola dan perubahan polutan pada wilayah penelitian, bukan untuk secara langsung menentukan sumber emisi tertentu.

---

## 4.2 Sumber Polutan NO₂

Nitrogen Dioxide (NO₂) merupakan salah satu gas yang berkaitan erat dengan proses pembakaran pada suhu tinggi.

Sumber antropogenik NO₂ umumnya berkaitan dengan aktivitas pembakaran bahan bakar.

Beberapa sumber NO₂ antara lain:

### 1. Transportasi

Kendaraan bermotor menghasilkan emisi dari proses pembakaran bahan bakar. Emisi kendaraan dapat menjadi salah satu sumber nitrogen oksida (NOₓ) yang kemudian berkaitan dengan keberadaan NO₂ di atmosfer.

Contohnya:

- sepeda motor;
- mobil;
- kendaraan barang;
- kendaraan umum.

### 2. Aktivitas Industri

Proses industri yang menggunakan pembakaran bahan bakar dapat menghasilkan emisi nitrogen oksida.

Besarnya emisi bergantung pada jenis proses, bahan bakar, teknologi, serta kondisi operasional yang digunakan.

### 3. Pembangkit Energi

Pembakaran bahan bakar pada pembangkit energi juga dapat menghasilkan nitrogen oksida.

Sumber tersebut terutama berkaitan dengan proses pembakaran bahan bakar pada temperatur tinggi.

### 4. Pembakaran Terbuka

Pembakaran biomassa atau material lainnya secara terbuka juga dapat menghasilkan berbagai jenis gas dan partikulat, termasuk senyawa nitrogen oksida.

---

## 4.3 Sumber Polutan CO

Carbon Monoxide (CO) merupakan gas yang terutama terbentuk dari proses pembakaran yang tidak sempurna.

Sumber CO dapat berasal dari berbagai aktivitas pembakaran.

### 1. Kendaraan Bermotor

Kendaraan bermotor merupakan salah satu sumber CO yang umum.

Pembakaran bahan bakar pada mesin kendaraan dapat menghasilkan CO terutama ketika proses pembakaran tidak berlangsung secara sempurna.

### 2. Pembakaran Biomassa

Pembakaran biomassa seperti sisa tanaman, kayu, atau material organik dapat menghasilkan CO.

Pembakaran yang tidak sempurna dapat meningkatkan pembentukan karbon monoksida.

### 3. Pembakaran Bahan Bakar

Berbagai aktivitas yang menggunakan bahan bakar dapat menghasilkan CO apabila terjadi pembakaran yang tidak sempurna.

Contohnya dapat berupa penggunaan bahan bakar untuk kegiatan rumah tangga, transportasi, maupun aktivitas lainnya.

### 4. Aktivitas Industri

Beberapa proses industri yang melibatkan pembakaran juga dapat menghasilkan emisi CO.

Jumlah emisi bergantung pada jenis industri, bahan bakar, proses pembakaran, dan teknologi pengendalian emisi.

---

## 4.4 Sumber Polutan SO₂

Sulfur Dioxide (SO₂) merupakan gas yang terutama berkaitan dengan pembakaran bahan bakar yang mengandung sulfur serta beberapa proses industri.

Sumber SO₂ antara lain:

### 1. Pembakaran Bahan Bakar Fosil

Bahan bakar fosil yang mengandung sulfur dapat menghasilkan SO₂ ketika dibakar.

Contohnya:

- batu bara;
- minyak;
- bahan bakar fosil lainnya.

### 2. Pembangkit Energi

Pembangkit listrik yang menggunakan bahan bakar dengan kandungan sulfur dapat menghasilkan emisi SO₂.

Besarnya emisi dipengaruhi oleh jenis bahan bakar dan teknologi pengendalian emisi yang digunakan.

### 3. Aktivitas Industri

Beberapa proses industri dapat menghasilkan SO₂, terutama proses yang menggunakan bahan bakar atau bahan baku yang mengandung sulfur.

### 4. Proses Pembakaran

Aktivitas pembakaran yang menggunakan material dengan kandungan sulfur juga dapat menghasilkan SO₂.

---

## 4.5 Sumber Polutan Berdasarkan Aktivitas

Secara umum, sumber polutan yang dibahas dalam proyek dapat dirangkum sebagai berikut:

| Sumber Aktivitas | NO₂ | CO | SO₂ |
|---|:---:|:---:|:---:|
| Kendaraan bermotor | ✓ | ✓ | ✓ |
| Pembakaran bahan bakar | ✓ | ✓ | ✓ |
| Aktivitas industri | ✓ | ✓ | ✓ |
| Pembangkit energi | ✓ | ✓ | ✓ |
| Pembakaran biomassa | ✓ | ✓ | - |
| Pembakaran terbuka | ✓ | ✓ | - |

Tabel tersebut menunjukkan bahwa satu aktivitas dapat menghasilkan lebih dari satu jenis polutan.

Namun, kontribusi masing-masing sumber terhadap konsentrasi polutan dapat berbeda tergantung pada jenis aktivitas, intensitas aktivitas, kondisi atmosfer, dan faktor lingkungan lainnya.

---

## 4.6 Hubungan Sumber Polutan dengan Data

Informasi mengenai sumber polutan digunakan sebagai dasar dalam memahami pola yang terdapat pada dataset.

Sebagai contoh, peningkatan nilai suatu polutan pada periode tertentu dapat menjadi indikasi yang perlu diteliti lebih lanjut. Namun, peningkatan tersebut tidak dapat langsung disimpulkan berasal dari satu sumber tertentu hanya berdasarkan data polutan.

Hal tersebut disebabkan oleh beberapa faktor yang dapat memengaruhi konsentrasi polutan di atmosfer, seperti:

- kondisi meteorologi;
- arah dan kecepatan angin;
- proses transportasi polutan;
- kondisi atmosfer;
- intensitas sumber emisi;
- perubahan aktivitas manusia.

Oleh karena itu, analisis pada proyek ini berfokus pada **pola dan perubahan data polutan berdasarkan waktu**, bukan menentukan sumber emisi secara langsung.

---

## 4.7 Sumber Polutan dan Wilayah Penelitian

Wilayah penelitian adalah **Kecamatan Kalitengah, Kabupaten Lamongan**.

Informasi mengenai sumber polutan pada bagian ini digunakan sebagai pengetahuan umum untuk membantu menginterpretasikan data yang diperoleh dari pengamatan satelit.

Tidak semua sumber polutan yang disebutkan dapat dipastikan terdapat atau menjadi sumber utama di Kecamatan Kalitengah.

Penentuan sumber emisi spesifik di wilayah penelitian membutuhkan data tambahan, seperti:

- data lalu lintas;
- data aktivitas industri;
- data penggunaan bahan bakar;
- data pembakaran terbuka;
- data meteorologi;
- data inventarisasi emisi.

Data tersebut tidak termasuk dalam dataset utama proyek ini.

---

## 4.8 Kesimpulan

NO₂, CO, dan SO₂ dapat berasal dari berbagai sumber aktivitas.

NO₂ banyak berkaitan dengan proses pembakaran dan emisi kendaraan, CO terutama berkaitan dengan pembakaran yang tidak sempurna, sedangkan SO₂ berkaitan dengan pembakaran bahan bakar yang mengandung sulfur dan beberapa aktivitas industri.

Pemahaman mengenai sumber polutan dapat membantu dalam menginterpretasikan perubahan data yang diperoleh dari pengamatan satelit.

Namun, data polutan saja belum cukup untuk menentukan sumber emisi secara spesifik. Oleh karena itu, pada proyek ini informasi sumber polutan digunakan sebagai konteks pendukung untuk analisis data.

Tahap selanjutnya adalah **Eksplorasi Data**, yaitu melakukan analisis dan visualisasi terhadap dataset polutan Kecamatan Kalitengah.
