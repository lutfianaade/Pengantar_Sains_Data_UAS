import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Membaca dataset CSV.
    """

    df = pd.read_csv(file_path)

    print("=" * 60)
    print("DATASET BERHASIL DIMUAT")
    print("=" * 60)

    print("\n5 Data Pertama")
    print(df.head())

    return df 

#membuat fungsi check_data
def check_data(df):
    """
    Menampilkan informasi dataset.
    """

    print("\n" + "=" * 60)
    print("INFORMASI DATASET")
    print("=" * 60)

    print(df.info())

    print("\nUkuran Dataset")
    print(f"Jumlah Baris  : {df.shape[0]}")
    print(f"Jumlah Kolom  : {df.shape[1]}")

    print("\nMissing Value")

    print(df.isnull().sum())

    print("\nJumlah Data Duplikat")

    print(df.duplicated().sum())

def clean_data(df):
    """
    Membersihkan dataset.
    """

    # Mengganti spasi kosong menjadi NaN
    df["TotalCharges"] = df["TotalCharges"].replace(" ", pd.NA)

    # Mengubah TotalCharges menjadi numerik
    df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
    )

    # Mengisi missing value dengan median
    median_total = df["TotalCharges"].median()

    df["TotalCharges"] = df["TotalCharges"].fillna(median_total)

    print("\nCleaning selesai.")

    return df


def statistics_summary(df):
    """
    Menampilkan statistik dasar.
    """

    print("\n" + "=" * 60)
    print("STATISTIK DATA")
    print("=" * 60)

    print(df.describe())

def save_summary_to_txt(df):
    """
    Menyimpan hasil analisis ke file txt.
    """

    with open(
        "hasil_analisis.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("HASIL ANALISIS DATASET TELCO CUSTOMER CHURN\n")

        file.write("=" * 60)

        file.write("\n\n")

        file.write(
            f"Jumlah Baris : {df.shape[0]}\n"
        )

        file.write(
            f"Jumlah Kolom : {df.shape[1]}\n\n"
        )

        file.write("STATISTIK DESKRIPTIF\n\n")

        file.write(str(df.describe(include="all")))

        file.write("\n\n")

        file.write(
            "JUMLAH PELANGGAN BERDASARKAN CHURN\n\n"
        )

        file.write(
            str(
                df["Churn"].value_counts()
            )
        )

    print("\nFile TXT berhasil dibuat.")

def bar_chart(df):
    """
    Membuat grafik jumlah pelanggan berdasarkan status Churn.
    """

    churn = df["Churn"].value_counts()

    plt.figure(figsize=(6,5))

    plt.bar(
        churn.index,
        churn.values
    )

    plt.title("Jumlah Pelanggan Churn")
    plt.xlabel("Status Churn")
    plt.ylabel("Jumlah Pelanggan")

    plt.tight_layout()

    plt.savefig("grafik_bar_churn.png")

    plt.show()

def scatter_plot(df):
    """
    Scatter Plot antara Tenure dan Monthly Charges.
    """

    plt.figure(figsize=(8,6))

    plt.scatter(
        df["tenure"],
        df["MonthlyCharges"],
        alpha=0.4,      # membuat titik transparan
        s=15            # ukuran titik lebih kecil
    )

    plt.title("Hubungan Tenure dengan Monthly Charges")

    plt.xlabel("Tenure (Bulan)")

    plt.ylabel("Monthly Charges")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("grafik_scatter.png")

    plt.show()

def correlation_heatmap(df):
    """
    Membuat Heatmap Korelasi.
    """

    corr = df.corr(numeric_only=True)

    plt.figure(figsize=(12,8))

    plt.imshow(
        corr,
        cmap="coolwarm",
        interpolation="nearest"
    )

    plt.colorbar()

    plt.xticks(
        range(len(corr.columns)),
        corr.columns,
        rotation=90
    )

    plt.yticks(
        range(len(corr.columns)),
        corr.columns
    )

    plt.title("Heatmap Korelasi")

    plt.tight_layout()

    plt.savefig("grafik_heatmap.png")

    plt.show()