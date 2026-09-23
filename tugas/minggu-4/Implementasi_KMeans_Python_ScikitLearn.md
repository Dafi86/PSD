

```
# Implementasi K-Means dengan Python (Scikit-Learn)

## Daftar Isi

1. [Evaluasi Jumlah Cluster dengan Elbow Method](#11-evaluasi-jumlah-cluster-dengan-elbow-method)
2. [Visualisasi Scatter Plot dan Profiling Cluster](#12-visualisasi-scatter-plot-dan-profiling-cluster)
3. [Ringkasan Hasil Python](#13-ringkasan-hasil-python)
4. [Alur Kerja (Workflow) Clustering KNIME](#2-alur-kerja-workflow-clustering-knime)
5. [Interpretasi Hasil Clustering (Scatter Plot KNIME)](#3-interpretasi-hasil-clustering-scatter-plot-knime)
6. [Kesimpulan](#kesimpulan)
7. [Catatan Penting untuk File Gambar](#catatan-penting-untuk-file-gambar)

---

Pada tahap ini dilakukan proses clustering menggunakan algoritma **K-Means** dengan Python dan Scikit-Learn.

Data yang digunakan merupakan data hasil ekstraksi **68 fitur TSFEL** dari tiga polutan, yaitu:

- NO₂
- CO
- SO₂

Masing-masing data polutan terdiri dari **37 data** dengan **68 fitur TSFEL**.

Kolom `id`, `nama`, dan `daerah` digunakan sebagai identitas data sehingga tidak digunakan dalam proses perhitungan clustering.

Alur proses yang digunakan adalah:

```text
Data 68 Fitur TSFEL
        ↓
StandardScaler
        ↓
PCA 37
        ↓
Elbow Method
        ↓
K-Means
        ↓
Scatter Plot
        ↓
Profiling Cluster
```

---

## 1.1 Evaluasi Jumlah Cluster dengan Elbow Method

### Pengertian

**Elbow Method** digunakan untuk melihat perubahan nilai inertia ketika jumlah cluster ditambah.

Pada tahap ini digunakan beberapa nilai K, yaitu:



```
K = 2 sampai K = 10
```

Nilai inertia akan semakin kecil ketika jumlah cluster bertambah. Grafik Elbow digunakan sebagai salah satu pertimbangan untuk melihat jumlah cluster yang digunakan pada proses K-Means.

Sebelum proses clustering, data dilakukan standardisasi menggunakan `StandardScaler`.

Selanjutnya data direduksi menggunakan PCA menjadi **37 komponen**, sesuai dengan instruksi tugas.

### Kode Python



```
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


# =========================
# Membaca data
# =========================

df = pd.read_csv(
    "Data_Satu_Kelas/ekstraksi_fitur_no2.csv"
)


# =========================
# Memisahkan fitur
# =========================

fitur = df.drop(
    ["id", "nama", "daerah"],
    axis=1
)


# =========================
# Standardisasi
# =========================

scaler = StandardScaler()

fitur_scaled = scaler.fit_transform(fitur)


# =========================
# PCA 37
# =========================

pca = PCA(n_components=37)

fitur_pca = pca.fit_transform(
    fitur_scaled
)


# =========================
# Elbow Method
# =========================

inertia = []

for k in range(2, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(fitur_pca)

    inertia.append(
        kmeans.inertia_
    )


# =========================
# Menampilkan hasil
# =========================

for k, nilai in zip(
    range(2, 11),
    inertia
):

    print(
        f"K={k} : {nilai:.6f}"
    )


# =========================
# Membuat grafik
# =========================

plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 11),
    inertia,
    marker="o"
)

plt.xlabel("Jumlah Cluster (K)")
plt.ylabel("Inertia")

plt.title(
    "Elbow Method - NO₂"
)

plt.grid(True)

plt.tight_layout()

plt.show()
```

Kode yang sama digunakan untuk CO dan SO₂ dengan mengganti nama file CSV.

### Output Terminal NO₂



```
K=2 : 1326.578705
K=3 : 1001.281921
K=4 : 811.798641
K=5 : 655.789824
K=6 : 578.312417
K=7 : 504.989692
K=8 : 458.598752
K=9 : 424.658844
K=10 : 373.027966
```

### Output Terminal CO



```
K=2 : 1123.800303
K=3 : 660.214101
K=4 : 509.373825
K=5 : 413.889526
K=6 : 361.351576
K=7 : 315.868398
K=8 : 272.854136
K=9 : 239.322559
K=10 : 221.039012
```

### Output Terminal SO₂



```
K=2 : 1210.459866
K=3 : 691.644801
K=4 : 525.289021
K=5 : 413.678733
K=6 : 335.555572
K=7 : 301.063800
K=8 : 267.415808
K=9 : 239.817616
K=10 : 230.171524
```

### Grafik Elbow NO₂

![Elbow Method NO2](image/NO2_elbow.png)

### Grafik Elbow CO

![Elbow Method CO](image/CO_elbow.png)

### Grafik Elbow SO₂

![Elbow Method SO2](image/SO2_elbow.png)

### Pembahasan

Dari hasil Elbow Method dapat dilihat bahwa nilai inertia mengalami penurunan ketika jumlah cluster bertambah.

Elbow Method digunakan sebagai salah satu pertimbangan dalam menentukan jumlah cluster. Selanjutnya proses clustering dilakukan menggunakan konfigurasi cluster yang digunakan pada tahap visualisasi dan profiling.

---

## 1.2 Visualisasi Scatter Plot dan Profiling Cluster

Setelah proses evaluasi jumlah cluster, dilakukan clustering menggunakan K-Means.

Pada tahap ini digunakan konfigurasi:

| Polutan | Jumlah Cluster |
|---|---:|
| NO₂ | 6 |
| CO | 4 |
| SO₂ | 6 |

Data terlebih dahulu dilakukan standardisasi dan PCA menjadi 37 komponen.

Setelah itu K-Means digunakan untuk memberikan label cluster pada setiap data.

Hasil cluster kemudian digunakan untuk membuat **Scatter Plot** berdasarkan daerah dan melakukan **profiling** untuk melihat daerah yang terdapat pada setiap cluster.

---

### NO₂

Pada data NO₂ digunakan:



```
PCA = 37
K = 6
```

### Kode



```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


# =========================
# Membaca data
# =========================

df = pd.read_csv(
    "Data_Satu_Kelas/ekstraksi_fitur_no2.csv"
)


# =========================
# Identitas dan fitur
# =========================

identitas = df[
    ["id", "nama", "daerah"]
]

fitur = df.drop(
    ["id", "nama", "daerah"],
    axis=1
)


# =========================
# Standardisasi
# =========================

scaler = StandardScaler()

fitur_scaled = scaler.fit_transform(
    fitur
)


# =========================
# PCA 37
# =========================

pca = PCA(
    n_components=37
)

fitur_pca = pca.fit_transform(
    fitur_scaled
)


# =========================
# K-Means
# =========================

kmeans = KMeans(
    n_clusters=6,
    random_state=42,
    n_init=10
)

cluster = kmeans.fit_predict(
    fitur_pca
)


# =========================
# Menambahkan cluster
# =========================

hasil = identitas.copy()

hasil["Cluster"] = cluster


# =========================
# Scatter Plot
# =========================

plt.figure(
    figsize=(15, 7)
)

sns.scatterplot(
    data=hasil,
    x="daerah",
    y="Cluster",
    hue="Cluster",
    palette="tab10",
    s=100
)

plt.title(
    "Scatter Plot Persebaran Daerah per Cluster (NO₂)"
)

plt.xlabel("Daerah")
plt.ylabel("Cluster")

plt.xticks(
    rotation=90
)

plt.grid(True)

plt.tight_layout()

plt.show()


# =========================
# Profiling
# =========================

profil = (
    hasil
    .groupby(
        ["Cluster", "daerah"]
    )
    .size()
    .reset_index(
        name="Jumlah"
    )
)


# =========================
# Top 3 daerah
# =========================

top3 = (
    profil
    .sort_values(
        ["Cluster", "Jumlah"],
        ascending=[True, False]
    )
    .groupby("Cluster")
    .head(3)
)

print(top3)
```

### Hasil Scatter Plot NO₂

![Scatter Cluster NO2](image/NO2_scatter_cluster_K6.png)

### Profiling NO₂

Hasil profiling digunakan untuk melihat daerah yang terdapat pada masing-masing cluster.

Beberapa hasil yang diperoleh antara lain:



```
Cluster 0
Warudoyong, Kota Sukabumi

Cluster 1
Bangkalan Kota, Gresik Kota, Kamal

Cluster 2
Kamal, Banyuajuh

Cluster 3
Cerme, Kalianget

Cluster 4
Kota Sumenep, Labang, Sreseh

Cluster 5
Kwanyar, Asemrowo, Bandung
```

Profiling ini membantu melihat isi dari setiap cluster berdasarkan daerah.

---

### CO

Pada data CO digunakan:



```
PCA = 37
K = 4
```

Kode yang digunakan sama seperti NO₂, dengan mengganti file menjadi:



```
df = pd.read_csv(
    "Data_Satu_Kelas/ekstraksi_fitur_co.csv"
)
```

dan jumlah cluster:



```
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)
```

Judul grafik:



```
plt.title(
    "Scatter Plot Persebaran Daerah per Cluster (CO)"
)
```

### Hasil Scatter Plot CO

![Scatter Cluster CO](image/CO_scatter_cluster_K6.png)

> Nama file gambar CO masih menggunakan nama `K6` pada repository, tetapi konfigurasi clustering yang digunakan adalah **K=4**. Nama file tidak mengubah hasil clustering.

### Profiling CO

Hasil profiling menunjukkan:



```
Cluster 0
Kwanyar, Asemrowo, Bandung

Cluster 1
Kamal, Banyuajuh

Cluster 2
Kamal, Bangkalan

Cluster 3
Cerme, Kalianget, Wonoayu
```

---

### SO₂

Pada data SO₂ digunakan:



```
PCA = 37
K = 6
```

File data:



```
df = pd.read_csv(
    "Data_Satu_Kelas/ekstraksi_fitur_so2.csv"
)
```

K-Means:



```
kmeans = KMeans(
    n_clusters=6,
    random_state=42,
    n_init=10
)
```

Judul:



```
plt.title(
    "Scatter Plot Persebaran Daerah per Cluster (SO₂)"
)
```

### Hasil Scatter Plot SO₂

![Scatter Cluster SO2](image/SO2_scatter_cluster_K6.png)

### Profiling SO₂

Hasil profiling menunjukkan:



```
Cluster 0
Kec Bangkalan, Tanah Merah, Warudoyong

Cluster 1
Asemrowo, Bandung, Baron Nganjuk

Cluster 2
Kamal, Banyuajuh

Cluster 3
Kamal, Bangkalan

Cluster 4
Banyu Ajuh, Cerme, Gresik Kota

Cluster 5
Wonoayu
```

Profiling digunakan untuk melihat daerah yang masuk ke masing-masing cluster.

---

## 1.3 Ringkasan Hasil Python

Hasil proses clustering Python dapat diringkas sebagai berikut:

| Polutan | Data | Fitur TSFEL | PCA | K |
|---|---:|---:|---:|---:|
| NO₂ | 37 | 68 | 37 | 6 |
| CO | 37 | 68 | 37 | 4 |
| SO₂ | 37 | 68 | 37 | 6 |

Dari proses tersebut, data berhasil diproses menggunakan StandardScaler, PCA, dan K-Means.

Hasil clustering Python selanjutnya digunakan sebagai pembanding ketika proses clustering dilakukan menggunakan KNIME.

---

# 2. Alur Kerja (Workflow) Clustering KNIME

Setelah proses menggunakan Python, clustering dilakukan kembali menggunakan **KNIME**.

Tujuannya adalah untuk melakukan proses yang sama menggunakan workflow visual sehingga setiap tahapan dapat dilihat dengan jelas.

Alur workflow yang digunakan adalah:



```
Database
    ↓
DB Table Selector
    ↓
DB Reader
    ↓
Normalizer
    ↓
PCA
    ↓
K-Means
    ↓
Scatter Plot
```

### Fungsi setiap node

| Node | Fungsi |
|---|---|
| DB Table Selector | Memilih tabel polutan dari database |
| DB Reader | Membaca data dari database |
| Normalizer | Melakukan standardisasi data |
| PCA | Melakukan reduksi dimensi menjadi 37 komponen |
| K-Means | Membagi data menjadi beberapa cluster |
| Scatter Plot | Menampilkan persebaran hasil cluster |

### Workflow KNIME



Workflow tersebut digunakan untuk data NO₂, CO, dan SO₂.

Perbedaan jumlah cluster yang digunakan adalah:



```
NO₂ → K=6
CO  → K=4
SO₂ → K=6
```

---

# 3. Interpretasi Hasil Clustering (Scatter Plot KNIME)

Setelah proses K-Means selesai, hasil clustering ditampilkan menggunakan Scatter Plot.

Scatter Plot digunakan untuk melihat persebaran data berdasarkan cluster.

Pada visualisasi ini:



```
Sumbu X → Daerah
Sumbu Y → Cluster
Warna   → Cluster
```

Dengan visualisasi tersebut, daerah yang berada pada cluster yang sama dapat dilihat dengan lebih mudah.

---

## 3.1 Hasil Clustering NO₂

Data NO₂ menggunakan:



```
K = 6
```

Hasil Scatter Plot:

![Scatter Plot KNIME NO2](image/NO2_scatter_daerah_cluster.png)

Hasil tersebut menunjukkan persebaran daerah berdasarkan enam cluster.

---

## 3.2 Hasil Clustering CO

Data CO menggunakan:



```
K = 4
```

Hasil Scatter Plot:

![Scatter Plot KNIME CO](image/CO_scatter_daerah_cluster.png)

Hasil tersebut menunjukkan persebaran daerah berdasarkan empat cluster.

---

## 3.3 Hasil Clustering SO₂

Data SO₂ menggunakan:



```
K = 6
```

Hasil Scatter Plot:

![Scatter Plot KNIME SO2](image/SO2_scatter_daerah_cluster.png)

Hasil tersebut menunjukkan persebaran daerah berdasarkan enam cluster.

---

## Kesimpulan

Berdasarkan proses yang telah dilakukan, data 68 fitur TSFEL berhasil digunakan untuk proses clustering menggunakan Python dan KNIME.

Tahapan yang dilakukan terdiri dari:



```
68 Fitur TSFEL
      ↓
StandardScaler
      ↓
PCA 37
      ↓
Elbow Method
      ↓
K-Means
      ↓
Scatter Plot
      ↓
Profiling
```

Hasil clustering Python digunakan sebagai dasar untuk membandingkan proses yang dilakukan menggunakan KNIME.

Jumlah cluster yang digunakan pada tahap visualisasi adalah:

- **NO₂ = 6 cluster** 
- **CO = 4 cluster** 
- **SO₂ = 6 cluster** 

Dengan menggunakan Scatter Plot, hasil pembagian data ke dalam cluster dapat dilihat berdasarkan daerah sehingga lebih mudah untuk dilakukan interpretasi.



```

## Catatan Penting untuk File Gambar

Di materi final ini **semua gambar sudah menggunakan format yang benar**:

```md
!![Nama gambar](image/nama-file.png)
```

bukan:



```
![Nama gambar](image/nama-file.png)
```

dan **bukan**:



```
!![Nama gambar](image/image/nama-file.png)
```

Jadi tidak akan diarahkan sebagai link download selama file PNG-nya memang ada di folder:



```
tugas/minggu-4/image/
```

Untuk workflow:



```
!![Workflow Clustering KNIME](image/knime/workflow-clustering.png)
```

kalau ternyata file workflow kamu sebenarnya berada langsung di `image/` dan bukan `image/knime/`, path-nya perlu disesuaikan dengan lokasi file sebenarnya.