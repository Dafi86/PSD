---
title: "Week 4 — Clustering Data Fitur TSFEL"
description: "Persiapan data, standardisasi, PCA, Elbow Method, K-Means, evaluasi clustering, visualisasi, dan profiling."
---

# Week 4 — Clustering Data Fitur TSFEL

## Tujuan

Pada Week 4 dilakukan proses **clustering** terhadap data hasil ekstraksi fitur **TSFEL** untuk tiga polutan, yaitu **NO₂, CO, dan SO₂**.

Tahapan analisis pada dokumen ini dibatasi pada:

1. Persiapan dan validasi data.
2. Pengambilan 68 fitur TSFEL.
3. Standardisasi menggunakan `StandardScaler`.
4. Analisis PCA dan cumulative explained variance.
5. Elbow Method untuk K=2–10.
6. Evaluasi K-Means menggunakan Silhouette, Davies-Bouldin, dan Calinski-Harabasz.
7. Pengujian PCA 1–36 terhadap K=2–10.
8. Clustering menggunakan seluruh 68 fitur.
9. Perbandingan PCA dan seluruh 68 fitur.
10. Visualisasi dan profiling cluster.
11. Implementasi Python serta output terminal.


## 1. Persiapan Data untuk Clustering

### 1.1 Tujuan

Pada tahap ini data hasil ekstraksi fitur TSFEL dipersiapkan sebelum digunakan untuk proses clustering. Data yang digunakan terdiri dari tiga jenis polutan, yaitu **NO₂, CO, dan SO₂**.

Masing-masing data memiliki:

-  37 data/observasi 
-  71 kolom 
-  3 kolom identitas: 
  - `id` 
  - `nama` 
  - `daerah` 
-  68 fitur hasil ekstraksi TSFEL 

Karena data NO₂, CO, dan SO₂ memiliki struktur data dan ID yang tidak sepenuhnya sama, proses clustering dilakukan **secara terpisah untuk masing-masing polutan**.

Data yang digunakan:

```
```

```
Data_Satu_Kelas/
├── ekstraksi_fitur_no2.csv
├── ekstraksi_fitur_co.csv
└── ekstraksi_fitur_so2.csv
```

Pada proses ini seluruh data tetap digunakan. Tidak ada data yang dihapus, termasuk data yang memiliki nilai ekstrem. Nilai ekstrem akan diperlakukan sebagai bagian dari karakteristik data dan dianalisis melalui hasil clustering.

---

### 1.2 Pemeriksaan Data

```
```

```
import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path("E:/PSD/Data_Satu_Kelas")

files = {
    "NO2": DATA_DIR / "ekstraksi_fitur_no2.csv",
    "CO": DATA_DIR / "ekstraksi_fitur_co.csv",
    "SO2": DATA_DIR / "ekstraksi_fitur_so2.csv"
}

for nama_polutan, file in files.items():

    df = pd.read_csv(file)

    print("=" * 60)
    print(f"POLUTAN : {nama_polutan}")
    print("Ukuran data :", df.shape)

    print("Missing value :", df.isna().sum().sum())
    print("Infinity :", np.isinf(df.select_dtypes(include=np.number)).sum().sum())
    print("Duplikat :", df.duplicated().sum())

    fitur = [
        kolom for kolom in df.columns
        if kolom not in ["id", "nama", "daerah"]
    ]

    print("Jumlah fitur :", len(fitur))
```

### 1.3 Output

Output pemeriksaan menunjukkan:

```
```

```
============================================================
POLUTAN : NO2
Ukuran data : (37, 71)
Missing value : 0
Infinity : 0
Duplikat : 0
Jumlah fitur : 68

============================================================
POLUTAN : CO
Ukuran data : (37, 71)
Missing value : 0
Infinity : 0
Duplikat : 0
Jumlah fitur : 68

============================================================
POLUTAN : SO2
Ukuran data : (37, 71)
Missing value : 0
Infinity : 0
Duplikat : 0
Jumlah fitur : 68
```

### 1.4 Mengambil 68 Fitur

```
```

```
kolom_identitas = ["id", "nama", "daerah"]

fitur = [
    kolom for kolom in df.columns
    if kolom not in kolom_identitas
]

X = df[fitur].copy()

print("Jumlah fitur :", len(fitur))
print("Ukuran X :", X.shape)
```

Output:

```
```

```
Jumlah fitur : 68
Ukuran X : (37, 68)
```

### 1.5 Pembahasan

Data sudah memiliki 68 fitur hasil ekstraksi TSFEL. Kolom identitas tidak digunakan sebagai variabel clustering karena kolom tersebut hanya berfungsi sebagai informasi mengenai data.

Dengan demikian, input utama untuk clustering adalah matriks:

```
```

```
37 observasi × 68 fitur
```

### Kesimpulan

Data sudah siap digunakan untuk proses standardisasi. Seluruh 37 observasi tetap dipertahankan dan 68 fitur digunakan sebagai variabel clustering.

---

## 2. Standardisasi Data dengan StandardScaler

## 2.1 Konsep

Standardisasi dilakukan agar setiap fitur memiliki skala yang relatif sama. Hal ini penting karena K-Means menggunakan jarak antar data dalam menentukan cluster.

Standardisasi menggunakan metode **Z-Score**:

```math
z = \frac{x-\mu}{\sigma}
```

Keterangan:

- `x` = nilai asli 
- `\mu` = rata-rata 
- `\sigma` = standar deviasi 
- `z` = nilai setelah standardisasi 

---

## 2.2 Code

```
```

```
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler

DATA_DIR = Path("E:/PSD/Data_Satu_Kelas")
OUTPUT_DIR = Path("E:/PSD/clustering/hasil")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

files = {
    "NO2": DATA_DIR / "ekstraksi_fitur_no2.csv",
    "CO": DATA_DIR / "ekstraksi_fitur_co.csv",
    "SO2": DATA_DIR / "ekstraksi_fitur_so2.csv"
}

kolom_identitas = ["id", "nama", "daerah"]

for polutan, file in files.items():

    df = pd.read_csv(file)

    fitur = [
        kolom for kolom in df.columns
        if kolom not in kolom_identitas
    ]

    X = df[fitur].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    df_scaled = pd.DataFrame(
        X_scaled,
        columns=fitur
    )

    print("=" * 60)
    print(f"POLUTAN : {polutan}")
    print("Data awal :", X.shape)
    print("Data setelah standardisasi :", df_scaled.shape)
    print("Rata-rata :", round(df_scaled.mean().mean(), 6))
    print("Std :", round(df_scaled.std().mean(), 6))
```

## 2.3 Output

Hasil standardisasi mempertahankan ukuran data:

```
```

```
NO2
Data awal : (37, 68)
Data setelah standardisasi : (37, 68)

CO
Data awal : (37, 68)
Data setelah standardisasi : (37, 68)

SO2
Data awal : (37, 68)
Data setelah standardisasi : (37, 68)
```

Rata-rata hasil standardisasi berada sangat dekat dengan 0.

### 2.4 Pembahasan

Standardisasi tidak mengubah jumlah data maupun jumlah fitur. Perubahan hanya terjadi pada skala nilai setiap fitur.

Tahap ini diperlukan sebelum PCA dan K-Means karena beberapa fitur TSFEL memiliki skala yang berbeda.

### Kesimpulan

Ketiga data polutan telah distandardisasi dan siap digunakan untuk reduksi dimensi menggunakan PCA.

---

## 3. Reduksi Dimensi dengan PCA

## 3.1 Konsep PCA

**Principal Component Analysis (PCA)** digunakan untuk mengurangi jumlah dimensi data dengan membentuk komponen baru yang mewakili variasi data.

Data awal mempunyai:

```
```

```
37 observasi × 68 fitur
```

Karena jumlah observasi hanya 37, jumlah maksimum komponen PCA yang valid setelah proses centering adalah:

```math
\min(n-1,p)
```

```math
\min(37-1,68)=36
```

Jadi pada penelitian ini jumlah maksimum komponen PCA adalah **36**, bukan 37.

---

## 3.2 Code PCA

```
```

```
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

DATA_DIR = Path("E:/PSD/Data_Satu_Kelas")
OUTPUT_DIR = Path("E:/PSD/clustering/hasil")

files = {
    "NO2": DATA_DIR / "ekstraksi_fitur_no2.csv",
    "CO": DATA_DIR / "ekstraksi_fitur_co.csv",
    "SO2": DATA_DIR / "ekstraksi_fitur_so2.csv"
}

kolom_identitas = ["id", "nama", "daerah"]

for polutan, file in files.items():

    df = pd.read_csv(file)

    fitur = [
        kolom for kolom in df.columns
        if kolom not in kolom_identitas
    ]

    X = df[fitur]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    max_pca = min(
        X_scaled.shape[0] - 1,
        X_scaled.shape[1]
    )

    pca = PCA(n_components=max_pca)
    X_pca = pca.fit_transform(X_scaled)

    explained = pca.explained_variance_ratio_
    cumulative = explained.cumsum()

    hasil = pd.DataFrame({
        "PCA": range(1, max_pca + 1),
        "Explained_Variance": explained,
        "Cumulative_Variance": cumulative
    })

    output = OUTPUT_DIR / polutan
    output.mkdir(parents=True, exist_ok=True)

    hasil.to_csv(
        output / f"{polutan}_pca_variance.csv",
        index=False
    )

    plt.figure(figsize=(10, 6))
    plt.plot(
        range(1, max_pca + 1),
        cumulative,
        marker="o"
    )

    plt.xlabel("Jumlah Komponen PCA")
    plt.ylabel("Cumulative Explained Variance")
    plt.title(f"Cumulative Explained Variance PCA - {polutan}")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        output / f"{polutan}_pca_variance.png",
        dpi=300
    )

    plt.show()

    print("=" * 60)
    print(polutan)
    print("Jumlah komponen maksimum :", max_pca)
    print("PCA 1 :", round(cumulative[0], 6))
    print("PCA 5 :", round(cumulative[4], 6))
    print("PCA 10 :", round(cumulative[9], 6))
    print("PCA 20 :", round(cumulative[19], 6))
    print("PCA 36 :", round(cumulative[35], 6))
```

## 3.3 Output PCA

### NO₂

```
```

```
Jumlah komponen maksimum : 36
PCA 1  : 0.458151
PCA 5  : 0.862886
PCA 10 : 0.956579
PCA 20 : 0.996338
PCA 36 : 1.000000
```

### CO

```
```

```
Jumlah komponen maksimum : 36
PCA 1  : 0.539550
PCA 5  : 0.904670
PCA 10 : 0.970289
PCA 20 : 0.998887
PCA 36 : 1.000000
```

### SO₂

```
```

```
Jumlah komponen maksimum : 36
PCA 1  : 0.530483
PCA 5  : 0.914009
PCA 10 : 0.976745
PCA 20 : 0.998543
PCA 36 : 1.000000
```

## 3.4 Gambar PCA

### NO₂



Path:

```
```

```
E:\PSD\clustering\hasil\NO2\NO2_pca_variance.png
```

Markdown:

```
```

```
![Cumulative Variance PCA NO2](../clustering/hasil/NO2/NO2_pca_variance.png)
```

### CO



Path:

```
```

```
E:\PSD\clustering\hasil\CO\CO_pca_variance.png
```

Markdown:

```
```

```
![Cumulative Variance PCA CO](../clustering/hasil/CO/CO_pca_variance.png)
```

### SO₂



Path:

```
```

```
E:\PSD\clustering\hasil\SO2\SO2_pca_variance.png
```

Markdown:

```
```

```
![Cumulative Variance PCA SO2](../clustering/hasil/SO2/SO2_pca_variance.png)
```

## 3.5 Pembahasan

PCA1 menjelaskan sekitar:

-  NO₂ = 45,82% 
-  CO = 53,96% 
-  SO₂ = 53,05% 

Sedangkan sampai PCA20, informasi yang dipertahankan sudah mendekati 100%.

Karena jumlah data hanya 37 observasi, jumlah maksimum komponen PCA yang dapat digunakan adalah 36.

### Kesimpulan

PCA dapat digunakan untuk mengurangi dimensi data dari 68 fitur menjadi maksimal 36 komponen. Selanjutnya seluruh PCA1 sampai PCA36 akan diuji terhadap K-Means.

---

## 4. Analisis Jumlah Cluster dengan Elbow Method

## 4.1 Konsep

Elbow Method digunakan untuk melihat perubahan **inertia** ketika jumlah cluster `K` ditambah.

Inertia menunjukkan jumlah kuadrat jarak setiap data terhadap centroid cluster-nya.

Semakin kecil nilai inertia, semakin dekat data dengan centroid. Namun inertia akan selalu menurun ketika jumlah cluster bertambah, sehingga Elbow Method digunakan untuk mencari titik perubahan yang relatif signifikan.

---

## 4.2 Code

```
```

```
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

DATA_DIR = Path("E:/PSD/Data_Satu_Kelas")
OUTPUT_DIR = Path("E:/PSD/clustering/hasil")

files = {
    "NO2": DATA_DIR / "ekstraksi_fitur_no2.csv",
    "CO": DATA_DIR / "ekstraksi_fitur_co.csv",
    "SO2": DATA_DIR / "ekstraksi_fitur_so2.csv"
}

kolom_identitas = ["id", "nama", "daerah"]

for polutan, file in files.items():

    df = pd.read_csv(file)

    fitur = [
        kolom for kolom in df.columns
        if kolom not in kolom_identitas
    ]

    X = df[fitur]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    hasil = []

    for k in range(2, 11):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)

        hasil.append({
            "K": k,
            "Inertia": model.inertia_
        })

    hasil_df = pd.DataFrame(hasil)

    folder = OUTPUT_DIR / polutan
    folder.mkdir(parents=True, exist_ok=True)

    hasil_df.to_csv(
        folder / f"{polutan}_elbow.csv",
        index=False
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        hasil_df["K"],
        hasil_df["Inertia"],
        marker="o"
    )

    plt.xlabel("Jumlah Cluster (K)")
    plt.ylabel("Inertia")
    plt.title(f"Elbow Method - {polutan}")
    plt.xticks(range(2, 11))
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        folder / f"{polutan}_elbow.png",
        dpi=300
    )

    plt.show()

    print(f"\n{polutan}")
    print(hasil_df)
```

## 4.3 Output NO₂

```
```

```
K    Inertia
2    1326.578705
3    1001.281921
4     811.798641
5     655.789824
6     578.312417
7     504.989692
8     458.598752
9     424.658844
10    373.027966
```

### Gambar



Path:

```
```

```
E:\PSD\clustering\hasil\NO2\NO2_elbow.png
```

---

## 4.4 Output CO

```
```

```
K    Inertia
2    1123.800303
3     660.214101
4     509.373825
5     413.889526
6     361.351576
7     315.868398
8     272.854136
9     239.322559
10    221.039012
```

### Gambar



Path:

```
```

```
E:\PSD\clustering\hasil\CO\CO_elbow.png
```

---

## 4.5 Output SO₂

```
```

```
K    Inertia
2    1210.459866
3     691.644801
4     525.289021
5     413.678733
6     335.555572
7     301.063800
8     267.415808
9     239.817616
10    230.171524
```

### Gambar



Path:

```
```

```
E:\PSD\clustering\hasil\SO2\SO2_elbow.png
```

## 4.6 Pembahasan

Elbow Method menunjukkan bahwa inertia terus menurun ketika jumlah cluster bertambah. Oleh karena itu, penentuan jumlah cluster tidak hanya dilakukan berdasarkan Elbow Method.

Untuk memastikan kualitas cluster digunakan:

-  Silhouette Score 
-  Davies-Bouldin Index 
-  Calinski-Harabasz Index 

### Kesimpulan

Elbow Method digunakan sebagai analisis awal jumlah cluster. Penentuan K selanjutnya diperkuat menggunakan beberapa metrik evaluasi clustering.

---

## 5. Evaluasi K-Means Clustering

## 5.1 Metrik Evaluasi

Tiga metrik digunakan:

### Silhouette Score

Nilainya berada pada rentang -1 sampai 1.

Semakin mendekati 1 menunjukkan pemisahan cluster yang semakin baik.

### Davies-Bouldin Index

Semakin kecil nilainya semakin baik.

### Calinski-Harabasz Index

Semakin besar nilainya semakin baik.

---

## 5.2 Code

```
```

```
import pandas as pd
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

DATA_DIR = Path("E:/PSD/Data_Satu_Kelas")
OUTPUT_DIR = Path("E:/PSD/clustering/hasil")

files = {
    "NO2": DATA_DIR / "ekstraksi_fitur_no2.csv",
    "CO": DATA_DIR / "ekstraksi_fitur_co.csv",
    "SO2": DATA_DIR / "ekstraksi_fitur_so2.csv"
}

kolom_identitas = ["id", "nama", "daerah"]

for polutan, file in files.items():

    df = pd.read_csv(file)

    fitur = [
        kolom for kolom in df.columns
        if kolom not in kolom_identitas
    ]

    X = df[fitur]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    hasil = []

    for k in range(2, 11):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        labels = model.fit_predict(X_scaled)

        hasil.append({
            "K": k,
            "Silhouette": silhouette_score(
                X_scaled,
                labels
            ),
            "Davies_Bouldin": davies_bouldin_score(
                X_scaled,
                labels
            ),
            "Calinski_Harabasz": calinski_harabasz_score(
                X_scaled,
                labels
            ),
            "Inertia": model.inertia_
        })

    hasil_df = pd.DataFrame(hasil)

    folder = OUTPUT_DIR / polutan
    folder.mkdir(parents=True, exist_ok=True)

    hasil_df.to_csv(
        folder / f"{polutan}_evaluasi_cluster.csv",
        index=False
    )

    print("\n", "=" * 70)
    print(polutan)
    print(hasil_df.to_string(index=False))
```

---

## 5.3 Hasil NO₂

| K | Silhouette | Davies-Bouldin | Calinski-Harabasz |
|---:|---:|---:|---:|
| 2                                          | 0.745489 | 0.163103 | 29.428895 |
| 3                                          | 0.190722 | 1.125673 | 24.460850 |
| 4                                          | 0.204530 | 0.999696 | 22.089486 |
| 5                                          | 0.216606 | 0.846203 | 21.790032 |
| 6                                          | 0.185596 | 0.949480 | 19.980313 |
| 7                                          | 0.161947 | 1.028688 | 19.178711 |
| 8                                          | 0.166889 | 0.986332 | 17.917511 |
| 9                                          | 0.151594 | 1.200741 | 16.626744 |
| 10                                         | 0.172124 | 0.867316 | 16.639278 |

Pada 68 fitur, K=2 mempunyai Silhouette tertinggi dan Davies-Bouldin terendah.

---

## 5.4 Hasil CO

| K | Silhouette | Davies-Bouldin | Calinski-Harabasz |
|---:|---:|---:|---:|
| 2                                          | 0.795494 | 0.124689 | 39.902098 |
| 3                                          | 0.697034 | 0.159113 | 44.926881 |
| 4                                          | 0.342517 | 0.694459 | 40.936316 |
| 5                                          | 0.184501 | 0.927503 | 38.485834 |
| 6                                          | 0.153812 | 0.984529 | 35.064522 |
| 7                                          | 0.161337 | 0.880005 | 33.069652 |
| 8                                          | 0.142490 | 0.841078 | 32.373252 |
| 9                                          | 0.150055 | 0.858393 | 31.672196 |
| 10                                         | 0.145469 | 0.807706 | 29.641297 |

Silhouette dan Davies-Bouldin menunjukkan K=2, sedangkan Calinski-Harabasz memiliki nilai tertinggi pada K=3.

---

## 5.5 Hasil SO₂

| K | Silhouette | Davies-Bouldin | Calinski-Harabasz |
|---:|---:|---:|---:|
| 2                                          | 0.789366 | 0.127864 | 35.609528 |
| 3                                          | 0.708469 | 0.151285 | 43.022138 |
| 4                                          | 0.392088 | 0.533434 | 40.137562 |
| 5                                          | 0.406057 | 0.473969 | 39.225053 |
| 6                                          | 0.135855 | 0.879872 | 38.920395 |
| 7                                          | 0.126801 | 0.959841 | 35.556182 |
| 8                                          | 0.099564 | 1.002946 | 33.689077 |
| 9                                          | 0.120845 | 0.801750 | 32.139584 |
| 10                                         | 0.092438 | 1.125461 | 28.828438 |

Silhouette dan Davies-Bouldin menunjukkan K=2, sedangkan Calinski-Harabasz memiliki nilai tertinggi pada K=3.

## 5.6 Pembahasan

Berdasarkan 68 fitur:

-  NO₂ menunjukkan K=2 pada Silhouette dan Davies-Bouldin. 
-  CO menunjukkan K=2 pada Silhouette dan Davies-Bouldin, sedangkan CH menunjukkan K=3. 
-  SO₂ menunjukkan K=2 pada Silhouette dan Davies-Bouldin, sedangkan CH menunjukkan K=3. 

Karena tidak semua metrik selalu memberikan nilai K yang sama, hasil clustering perlu dilihat bersama dengan visualisasi dan konteks analisis.

---

## 6. Analisis PCA 1–36 dan K-Means

## 6.1 Tujuan

Tahap ini digunakan untuk mengetahui bagaimana perubahan jumlah komponen PCA memengaruhi hasil clustering.

Karena maksimal PCA adalah 36, maka diuji:

```
```

```
PCA 1
PCA 2
PCA 3
...
PCA 36
```

Untuk setiap PCA dilakukan pengujian K:

```
```

```
K = 2 sampai 10
```

---

## 6.2 Code

```
```

```
import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

DATA_DIR = Path("E:/PSD/Data_Satu_Kelas")
OUTPUT_DIR = Path("E:/PSD/clustering/hasil")

files = {
    "NO2": DATA_DIR / "ekstraksi_fitur_no2.csv",
    "CO": DATA_DIR / "ekstraksi_fitur_co.csv",
    "SO2": DATA_DIR / "ekstraksi_fitur_so2.csv"
}

kolom_identitas = ["id", "nama", "daerah"]

for polutan, file in files.items():

    df = pd.read_csv(file)

    fitur = [
        kolom for kolom in df.columns
        if kolom not in kolom_identitas
    ]

    X = df[fitur]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    max_pca = min(
        X_scaled.shape[0] - 1,
        X_scaled.shape[1]
    )

    semua_hasil = []

    for n_pca in range(1, max_pca + 1):

        pca = PCA(n_components=n_pca)
        X_pca = pca.fit_transform(X_scaled)

        variance = pca.explained_variance_ratio_.sum()

        for k in range(2, 11):

            model = KMeans(
                n_clusters=k,
                random_state=42,
                n_init=10
            )

            labels = model.fit_predict(X_pca)

            semua_hasil.append({
                "PCA": n_pca,
                "K": k,
                "Cumulative_Variance": variance,
                "Silhouette": silhouette_score(
                    X_pca,
                    labels
                ),
                "Davies_Bouldin": davies_bouldin_score(
                    X_pca,
                    labels
                ),
                "Calinski_Harabasz": calinski_harabasz_score(
                    X_pca,
                    labels
                )
            })

    hasil = pd.DataFrame(semua_hasil)

    folder = OUTPUT_DIR / polutan
    folder.mkdir(parents=True, exist_ok=True)

    hasil.to_csv(
        folder / f"{polutan}_PCA_1_36_K_2_10.csv",
        index=False
    )

    print(f"{polutan} selesai.")
```

## 6.3 Hasil Terbaik Berdasarkan Silhouette

### NO₂

```
```

```
PCA       : 1
K         : 2
Silhouette: 0.962038
DB        : 0.007346
CH        : 8857.149772
Variance  : 0.458151
```

### CO

```
```

```
PCA       : 1
K         : 2
Silhouette: 0.948900
DB        : 0.016955
CH        : 1749.430762
Variance  : 0.539550
```

### SO₂

```
```

```
PCA       : 1
K         : 2
Silhouette: 0.925296
DB        : 0.030963
CH        : 366.002229
Variance  : 0.530483
```

## 6.4 Pembahasan

Hasil evaluasi menunjukkan PCA1 dengan K=2 menghasilkan Silhouette paling tinggi untuk ketiga polutan.

Namun PCA1 hanya menjelaskan:

-  NO₂ = 45,82% 
-  CO = 53,96% 
-  SO₂ = 53,05% 

Sehingga nilai Silhouette yang tinggi pada PCA1 perlu dipahami sebagai kualitas pemisahan pada ruang satu dimensi tersebut, bukan berarti seluruh informasi 68 fitur hanya terdiri dari satu komponen.

### Kesimpulan

PCA1-K2 menghasilkan pemisahan cluster yang sangat jelas berdasarkan Silhouette, tetapi analisis tetap dibandingkan dengan hasil 68 fitur agar tidak hanya bergantung pada satu representasi data.

---

## 7. Clustering Menggunakan 68 Fitur

## 7.1 Konsep

Selain menggunakan PCA, clustering juga dilakukan langsung menggunakan seluruh 68 fitur TSFEL yang telah distandardisasi.

Alurnya:

```
```

```
68 Fitur TSFEL
       ↓
StandardScaler
       ↓
K-Means
       ↓
Evaluasi Cluster
```

---

## 7.2 Code

```
```

```
import pandas as pd
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

DATA_DIR = Path("E:/PSD/Data_Satu_Kelas")

files = {
    "NO2": DATA_DIR / "ekstraksi_fitur_no2.csv",
    "CO": DATA_DIR / "ekstraksi_fitur_co.csv",
    "SO2": DATA_DIR / "ekstraksi_fitur_so2.csv"
}

kolom_identitas = ["id", "nama", "daerah"]

for polutan, file in files.items():

    df = pd.read_csv(file)

    fitur = [
        kolom for kolom in df.columns
        if kolom not in kolom_identitas
    ]

    X = df[fitur]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    for k in [2]:

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        labels = model.fit_predict(X_scaled)

        print("=" * 60)
        print(polutan)
        print("Jumlah fitur :", len(fitur))
        print("Jumlah cluster :", k)
        print(
            "Silhouette :",
            silhouette_score(X_scaled, labels)
        )
        print(
            "Davies-Bouldin :",
            davies_bouldin_score(X_scaled, labels)
        )
        print(
            "Calinski-Harabasz :",
            calinski_harabasz_score(X_scaled, labels)
        )
```

## 7.3 Output

### NO₂

```
```

```
Jumlah fitur : 68
Jumlah cluster : 2
Silhouette : 0.745489
Davies-Bouldin : 0.163103
Calinski-Harabasz : 29.428895
```

### CO

```
```

```
Jumlah fitur : 68
Jumlah cluster : 2
Silhouette : 0.795494
Davies-Bouldin : 0.124689
Calinski-Harabasz : 39.902098
```

### SO₂

```
```

```
Jumlah fitur : 68
Jumlah cluster : 2
Silhouette : 0.789366
Davies-Bouldin : 0.127864
Calinski-Harabasz : 35.609528
```

### Kesimpulan

Clustering menggunakan 68 fitur menghasilkan pemisahan cluster yang cukup jelas berdasarkan nilai Silhouette, dengan K=2 menjadi konfigurasi yang menghasilkan Silhouette tertinggi pada ketiga polutan.

---

## 8. Perbandingan PCA dan 68 Fitur

## 8.1 Hasil Perbandingan

| Polutan | Metode | K | Silhouette | Davies-Bouldin |
|---|---|---:|---:|---:|
| NO₂                                    | PCA1     | 2 | 0.962038 | 0.007346 |
| NO₂                                    | 68 Fitur | 2 | 0.745489 | 0.163103 |
| CO                                     | PCA1     | 2 | 0.948900 | 0.016955 |
| CO                                     | 68 Fitur | 2 | 0.795494 | 0.124689 |
| SO₂                                    | PCA1     | 2 | 0.925296 | 0.030963 |
| SO₂                                    | 68 Fitur | 2 | 0.789366 | 0.127864 |

## 8.2 Code Perbandingan

```
```

```
import pandas as pd

data = [
    ["NO2", "PCA1", 2, 0.962038, 0.007346],
    ["NO2", "68 Fitur", 2, 0.745489, 0.163103],

    ["CO", "PCA1", 2, 0.948900, 0.016955],
    ["CO", "68 Fitur", 2, 0.795494, 0.124689],

    ["SO2", "PCA1", 2, 0.925296, 0.030963],
    ["SO2", "68 Fitur", 2, 0.789366, 0.127864]
]

df = pd.DataFrame(
    data,
    columns=[
        "Polutan",
        "Metode",
        "K",
        "Silhouette",
        "Davies_Bouldin"
    ]
)

print(df)
```

## 8.3 Pembahasan

Dari hasil pengujian, nilai Silhouette pada PCA1 lebih tinggi dibandingkan penggunaan langsung 68 fitur.

Namun, PCA1 hanya mempertahankan sekitar 46–54% variasi data. Oleh karena itu hasil PCA1 dan hasil 68 fitur tidak dapat dianggap sebagai hal yang sama.

PCA digunakan untuk melihat struktur data pada ruang yang lebih sederhana, sedangkan 68 fitur digunakan untuk mempertahankan seluruh fitur hasil ekstraksi.

### Kesimpulan

Kedua pendekatan digunakan sebagai pembanding:

```
```

```
PCA → melihat struktur data setelah reduksi dimensi
68 fitur → menggunakan seluruh fitur TSFEL
```

---

## 9. Scatter Plot dan Persebaran Cluster

## 9.1 Tujuan

Scatter plot digunakan untuk melihat persebaran data berdasarkan cluster yang telah terbentuk.

Visualisasi dilakukan berdasarkan hasil clustering yang mengikuti struktur analisis pada referensi.

Untuk visualisasi/profiling digunakan:

-  NO₂ → K=6 
-  CO → K=4 
-  SO₂ → K=6 

**Catatan:** K tersebut digunakan untuk mengikuti struktur visualisasi referensi. Hasil evaluasi metrik sebelumnya menunjukkan K=2 sebagai konfigurasi dengan Silhouette tertinggi pada 68 fitur.

---

## 9.2 Code

```
```

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

DATA_DIR = Path("E:/PSD/Data_Satu_Kelas")
OUTPUT_DIR = Path("E:/PSD/clustering/hasil")

files = {
    "NO2": DATA_DIR / "ekstraksi_fitur_no2.csv",
    "CO": DATA_DIR / "ekstraksi_fitur_co.csv",
    "SO2": DATA_DIR / "ekstraksi_fitur_so2.csv"
}

k_values = {
    "NO2": 6,
    "CO": 4,
    "SO2": 6
}

kolom_identitas = ["id", "nama", "daerah"]

for polutan, file in files.items():

    df = pd.read_csv(file)

    fitur = [
        kolom for kolom in df.columns
        if kolom not in kolom_identitas
    ]

    X = df[fitur]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    k = k_values[polutan]

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = model.fit_predict(X_scaled)

    folder = OUTPUT_DIR / polutan
    folder.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        folder / f"{polutan}_hasil_cluster_K{k}.csv",
        index=False
    )

    plt.figure(figsize=(15, 7))

    sns.scatterplot(
        data=df,
        x="daerah",
        y="Cluster",
        hue="Cluster",
        palette="tab10",
        s=100
    )

    plt.xticks(rotation=90)
    plt.title(
        f"Scatter Plot Persebaran Daerah per Cluster ({polutan})"
    )
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        folder / f"{polutan}_scatter_cluster_K{k}.png",
        dpi=300
    )

    plt.show()
```

---

## 9.3 Hasil NO₂

Cluster yang terbentuk:

```
```

```
Cluster 0 : 1 data
Cluster 1 : 13 data
Cluster 2 : 1 data
Cluster 3 : 2 data
Cluster 4 : 4 data
Cluster 5 : 16 data
```

Gambar:



Path:

```
```

```
E:\PSD\clustering\hasil\NO2\NO2_scatter_cluster_K6.png
```

---

## 9.4 Hasil CO

```
```

```
Cluster 0 : 31 data
Cluster 1 : 1 data
Cluster 2 : 1 data
Cluster 3 : 4 data
```

Gambar:



Path:

```
```

```
E:\PSD\clustering\hasil\CO\CO_scatter_cluster_K4.png
```

---

## 9.5 Hasil SO₂

```
```

```
Cluster 0 : 3 data
Cluster 1 : 14 data
Cluster 2 : 1 data
Cluster 3 : 1 data
Cluster 4 : 17 data
Cluster 5 : 1 data
```

Gambar:



Path:

```
```

```
E:\PSD\clustering\hasil\SO2/SO2_scatter_cluster_K6.png
```

---

## 10. Profiling Hasil Cluster

## 10.1 Tujuan

Profiling dilakukan untuk mengetahui daerah yang berada pada masing-masing cluster.

Proses dilakukan dengan menghitung jumlah data berdasarkan kombinasi:

```
```

```
Cluster + daerah
```

---

## 10.2 Code

```
```

```
import pandas as pd
from pathlib import Path

INPUT_DIR = Path("E:/PSD/clustering/hasil")

files = {
    "NO2": "NO2_hasil_cluster_K6.csv",
    "CO": "CO_hasil_cluster_K4.csv",
    "SO2": "SO2_hasil_cluster_K6.csv"
}

OUTPUT_DIR = Path("E:/PSD/clustering/profiling")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for polutan, filename in files.items():

    file = INPUT_DIR / polutan / filename

    df = pd.read_csv(file)

    profiling = (
        df.groupby(["Cluster", "daerah"])
        .size()
        .reset_index(name="Jumlah")
    )

    profiling = profiling.sort_values(
        ["Cluster", "Jumlah"],
        ascending=[True, False]
    )

    profiling.to_csv(
        OUTPUT_DIR / f"{polutan}_profiling_daerah_lengkap.csv",
        index=False
    )

    top3 = (
        profiling
        .groupby("Cluster")
        .head(3)
    )

    top3.to_csv(
        OUTPUT_DIR / f"{polutan}_top3_daerah_per_cluster.csv",
        index=False
    )

    print("=" * 60)
    print(polutan)
    print(top3)
```

---

## 10.3 Contoh Hasil NO₂

```
```

```
Cluster 0
Warudoyong, Kota Sukabumi

Cluster 1
Bangkalan Kota, Bangkalan
Gresik Kota, Gresik
Kamal, Bangkalan

Cluster 2
Kamal, Banyuajuh

Cluster 3
Cerme, Gresik
Kec Kalianget, Sumenep

Cluster 4
Kota Sumenep
Labang, Bangkalan
Sreseh, Sampang

Cluster 5
Kwanyar, Bangkalan
Asemrowo, Surabaya
Bandung, Jogoroto, Jombang
```

## 10.4 Contoh Hasil CO

```
```

```
Cluster 0
Kwanyar, Bangkalan
Asemrowo, Surabaya
Bandung, Jogoroto, Jombang

Cluster 1
Kamal, Banyuajuh

Cluster 2
Kamal, Bangkalan

Cluster 3
Cerme, Gresik
Kec Kalianget, Sumenep
Wonoayu
```

## 10.5 Contoh Hasil SO₂

```
```

```
Cluster 0
Kec Bangkalan, Kab Bangkalan
Tanah Merah, Bangkalan
Warudoyong, Kota Sukabumi

Cluster 1
Asemrowo, Surabaya
Bandung, Jogoroto, Jombang
Baron Nganjuk

Cluster 2
Kamal, Banyuajuh

Cluster 3
Kamal, Bangkalan

Cluster 4
Banyu Ajuh, Perumnas, Kamal
Cerme, Gresik
Gresik Kota, Gresik

Cluster 5
Wonoayu
```

### Pembahasan

Profiling menunjukkan bahwa beberapa daerah muncul sebagai anggota cluster tertentu berdasarkan karakteristik 68 fitur TSFEL.

Data dengan karakteristik yang berbeda dapat membentuk cluster yang lebih kecil. Hal tersebut tidak langsung berarti data tersebut salah, tetapi menunjukkan adanya perbedaan karakteristik pada ruang fitur.

---

## 11. Implementasi Clustering dengan Python

## 11.1 Alur Python

Seluruh proses clustering menggunakan Python dilakukan melalui tahapan:

```
```

```
Data
 ↓
Validasi
 ↓
68 Fitur TSFEL
 ↓
StandardScaler
 ↓
PCA
 ↓
Evaluasi K
 ↓
K-Means
 ↓
Scatter Plot
 ↓
Profiling
```

Script utama yang digunakan:

```
```

```
E:\PSD\clustering\clustering_final.py
```

---

## 11.2 Menjalankan Program

```
```

```
cd E:\PSD

python clustering\clustering_final.py
```

## 11.3 Output Terminal

Program menghasilkan informasi seperti:

```
```

```
============================================================
POLUTAN : NO2
Jumlah data : 37
Jumlah fitur : 68
Missing value : 0
Infinity : 0
Duplicate : 0

PCA maksimum : 36

Evaluasi K-Means selesai.
Hasil clustering disimpan.

============================================================
POLUTAN : CO
Jumlah data : 37
Jumlah fitur : 68
Missing value : 0
Infinity : 0
Duplicate : 0

PCA maksimum : 36

Evaluasi K-Means selesai.
Hasil clustering disimpan.

============================================================
POLUTAN : SO2
Jumlah data : 37
Jumlah fitur : 68
Missing value : 0
Infinity : 0
Duplicate : 0

PCA maksimum : 36

Evaluasi K-Means selesai.
Hasil clustering disimpan.
```

## 11.4 File Hasil

Contoh hasil:

```
```

```
clustering/
└── hasil/
    ├── NO2/
    │   ├── NO2_elbow.png
    │   ├── NO2_pca_variance.png
    │   ├── NO2_evaluasi_cluster.csv
    │   ├── NO2_PCA_1_36_K_2_10.csv
    │   ├── NO2_hasil_cluster.csv
    │   └── NO2_scatter_pca.png
    │
    ├── CO/
    │   ├── CO_elbow.png
    │   ├── CO_pca_variance.png
    │   ├── CO_evaluasi_cluster.csv
    │   ├── CO_PCA_1_36_K_2_10.csv
    │   ├── CO_hasil_cluster.csv
    │   └── CO_scatter_pca.png
    │
    └── SO2/
        ├── SO2_elbow.png
        ├── SO2_pca_variance.png
        ├── SO2_evaluasi_cluster.csv
        ├── SO2_PCA_1_36_K_2_10.csv
        ├── SO2_hasil_cluster.csv
        └── SO2_scatter_pca.png
```

---

## 14. Kesimpulan Clustering

## 14.1 Kesimpulan Data

Data yang digunakan terdiri dari 37 observasi untuk masing-masing polutan dengan 68 fitur TSFEL.

```
```

```
NO₂ : 37 × 68
CO  : 37 × 68
SO₂ : 37 × 68
```

Tidak terdapat missing value, infinity, maupun duplikasi yang mengganggu proses clustering.

---

## 14.2 Kesimpulan PCA

Jumlah maksimum komponen PCA adalah 36 karena jumlah observasi hanya 37.

Hasil cumulative variance:

| Polutan | PCA 1 | PCA 5 | PCA 10 | PCA 20 |
|---|---:|---:|---:|---:|
| NO₂                           | 45,82% | 86,29% | 95,66% | 99,63% |
| CO                            | 53,96% | 90,47% | 97,03% | 99,89% |
| SO₂                           | 53,05% | 91,40% | 97,67% | 99,85% |

---

## 14.3 Kesimpulan K-Means 68 Fitur

Pada penggunaan seluruh 68 fitur, hasil evaluasi menunjukkan:

| Polutan | K | Silhouette | Davies-Bouldin |
|---|---:|---:|---:|
| NO₂                              | 2 | 0.745489 | 0.163103 |
| CO                               | 2 | 0.795494 | 0.124689 |
| SO₂                              | 2 | 0.789366 | 0.127864 |

K=2 memberikan Silhouette tertinggi dan Davies-Bouldin terendah untuk ketiga polutan.

Untuk CO dan SO₂, Calinski-Harabasz memiliki nilai tertinggi pada K=3, sehingga terdapat sedikit perbedaan hasil antar-metrik.

---

## 14.4 Kesimpulan PCA + K-Means

Pada pengujian PCA1 sampai PCA36 dan K=2 sampai K=10, konfigurasi dengan Silhouette tertinggi adalah:

| PolutanPCAKSilhouette |      |   |          |
| --------------------- | ---- | - | -------- |
| NO₂                   | PCA1 | 2 | 0.962038 |
| CO                    | PCA1 | 2 | 0.948900 |
| SO₂                   | PCA1 | 2 | 0.925296 |

Namun PCA1 hanya mempertahankan sekitar 46–54% variasi data. Oleh karena itu, hasil PCA1 digunakan sebagai salah satu sudut pandang analisis, sedangkan hasil 68 fitur tetap dipertahankan sebagai analisis utama dengan seluruh fitur TSFEL.

---

## 14.5 Kesimpulan Akhir

Berdasarkan seluruh proses, tahapan clustering yang dilakukan adalah:

```
```

```
37 Data
    ↓
68 Fitur TSFEL
    ↓
Validasi Data
    ↓
StandardScaler
    ↓
PCA 1–36
    ↓
Evaluasi K = 2–10
    ↓
K-Means
    ↓
Silhouette
Davies-Bouldin
Calinski-Harabasz
    ↓
Scatter Plot
    ↓
Profiling Cluster
    ↓
Perbandingan PCA dan 68 Fitur
    ↓
```

Seluruh observasi tetap digunakan dalam proses analisis. Data dengan karakteristik ekstrem tidak dihapus karena masih merupakan bagian dari data penelitian. Perbedaan karakteristik tersebut justru dapat terlihat melalui hasil pembentukan cluster.

---

# Daftar Path Gambar Week 4

Supaya nanti kamu gampang memasukkan gambar ke materi, ini kumpulan path-nya:

### NO₂

```
```

```
E:\PSD\clustering\hasil\NO2\NO2_elbow.png
E:\PSD\clustering\hasil\NO2\NO2_pca_variance.png
E:\PSD\clustering\hasil\NO2\NO2_scatter_pca.png
E:\PSD\clustering\hasil\NO2\NO2_scatter_daerah_cluster.png
E:\PSD\clustering\hasil\NO2\NO2_scatter_PCA_K2_final.png
E:\PSD\clustering\hasil\NO2\NO2_scatter_cluster_K6.png
```

### CO

```
```

```
E:\PSD\clustering\hasil\CO\CO_elbow.png
E:\PSD\clustering\hasil\CO\CO_pca_variance.png
E:\PSD\clustering\hasil\CO\CO_scatter_pca.png
E:\PSD\clustering\hasil\CO\CO_scatter_daerah_cluster.png
E:\PSD\clustering\hasil\CO\CO_scatter_PCA_K2_final.png
E:\PSD\clustering\hasil\CO\CO_scatter_cluster_K4.png
```

### SO₂

```
```

```
E:\PSD\clustering\hasil\SO2\SO2_elbow.png
E:\PSD\clustering\hasil\SO2\SO2_pca_variance.png
E:\PSD\clustering\hasil\SO2\SO2_scatter_pca.png
E:\PSD\clustering\hasil\SO2\SO2_scatter_daerah_cluster.png
E:\PSD\clustering\hasil\SO2\SO2_scatter_PCA_K2_final.png
E:\PSD\clustering\hasil\SO2\SO2_scatter_cluster_K6.png
```

### Untuk Markdown Jupyter Book

Format umumnya:

```
```

```
![Judul Gambar](../clustering/hasil/NO2/NO2_elbow.png)
```




### 11.4 Output Terminal

Contoh output terminal yang tercantum pada materi:

```text
============================================================
POLUTAN: NO2
============================================================
Data       : 37
Features   : 68
Missing    : 0
Infinity   : 0
Duplicate  : 0
PCA max    : 36
Evaluasi   : selesai

============================================================
POLUTAN: CO
============================================================
Data       : 37
Features   : 68
Missing    : 0
Infinity   : 0
Duplicate  : 0
PCA max    : 36
Evaluasi   : selesai

============================================================
POLUTAN: SO2
============================================================
Data       : 37
Features   : 68
Missing    : 0
Infinity   : 0
Duplicate  : 0
PCA max    : 36
Evaluasi   : selesai
```

Output tersebut menunjukkan bahwa ketiga dataset berhasil diproses dengan **37 observasi**, **68 fitur**, tidak memiliki missing value, infinity, atau duplicate berdasarkan validasi, dan proses dapat dilanjutkan sampai evaluasi.

> **Catatan:** Jika output terminal asli memiliki format/baris tambahan, gunakan output asli tersebut pada dokumentasi final. Jangan menambahkan angka yang tidak benar-benar dihasilkan program.

## 12. Kesimpulan

Data yang dianalisis terdiri dari tiga polutan, yaitu **NO₂, CO, dan SO₂**. Masing-masing dataset memiliki **37 observasi dan 68 fitur TSFEL** yang digunakan untuk proses clustering. Hasil validasi menunjukkan tidak terdapat missing value, infinity, maupun duplicate.

Sebelum clustering, seluruh fitur distandardisasi menggunakan `StandardScaler`. Setelah itu dilakukan PCA dengan maksimum **36 komponen**, sesuai dengan:

\[
\min(n-1,p)=\min(37-1,68)=36
\]

Cumulative explained variance menunjukkan bahwa pada PCA20 variasi yang dipertahankan mencapai sekitar **99,63% untuk NO₂, 99,89% untuk CO, dan 99,85% untuk SO₂**.

Pada evaluasi K-Means menggunakan seluruh 68 fitur, **K=2** memiliki Silhouette tertinggi dan Davies-Bouldin terendah untuk ketiga polutan pada hasil yang terdokumentasi. Untuk CO dan SO₂, Calinski-Harabasz memiliki nilai tertinggi pada K=3, sehingga hasil clustering perlu dibaca menggunakan ketiga metrik secara bersama-sama.

Pengujian PCA1–PCA36 dengan K=2–K=10 menunjukkan bahwa kombinasi **PCA1 dan K=2** menghasilkan Silhouette tertinggi untuk masing-masing polutan. Namun, PCA1 hanya menjelaskan sekitar **45,82% NO₂, 53,96% CO, dan 53,05% SO₂**, sehingga hasil PCA1 dipahami sebagai evaluasi pada representasi satu dimensi dan tetap dibandingkan dengan hasil clustering menggunakan seluruh 68 fitur.

Visualisasi dan profiling digunakan untuk melihat distribusi cluster dan daerah yang berada di dalam cluster. Konfigurasi visualisasi yang digunakan pada materi adalah **K=6 untuk NO₂, K=4 untuk CO, dan K=6 untuk SO₂** sebagai referensi visualisasi/profiling.

Alur utama Week 4:

```text
Data NO₂ / CO / SO₂
        ↓
Validasi Data
        ↓
68 Fitur TSFEL
        ↓
StandardScaler
        ↓
PCA 1–36
        ↓
Elbow Method K=2–10
        ↓
K-Means K=2–10
        ↓
Silhouette + Davies-Bouldin + Calinski-Harabasz
        ↓
Perbandingan PCA dan 68 Fitur
        ↓
Visualisasi
        ↓
Profiling Cluster
```

> **Batas pembahasan:** Penerapan menggunakan KNIME tidak termasuk dalam dokumen ini dan akan dibuat pada patch/dokumentasi tersendiri.
