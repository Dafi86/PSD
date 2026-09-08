import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Lokasi data
data_path = Path("tugas/data/polutan_kalitengah_timeseries.csv")
output_dir = Path("tugas/data")

# Baca data
df = pd.read_csv(data_path)
df["date"] = pd.to_datetime(df["date"])

# Daftar polutan
pollutants = {
    "NO2": "NO₂",
    "CO": "CO",
    "SO2": "SO₂",
}

# Buat grafik masing-masing polutan
for column, label in pollutants.items():
    plt.figure(figsize=(12, 5))

    plt.plot(
        df["date"],
        df[column],
        linewidth=1.5
    )

    plt.title(f"Time Series {label} Kecamatan Kalitengah")
    plt.xlabel("Tanggal")
    plt.ylabel(f"Konsentrasi {label}")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_path = output_dir / f"timeseries_{column}_Kalitengah.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"Berhasil dibuat: {output_path}")

print("\nSemua grafik selesai dibuat.")
