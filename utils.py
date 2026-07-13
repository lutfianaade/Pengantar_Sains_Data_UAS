import pandas as pd 
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Membaca dataset CSV.
    """

    df = pd.read_csv(file_path)

    print("=" * 30)
    print("DATASET BERHASIL DIMUAT")
    print("=" * 30)

    print("\n5 Data Pertama")
    print(df.head())

    return df 

#membuat fungsi check_data
def check_data(df):
    """
    Menampilkan informasi dataset.
    """

    print("\n" + "=" * 30)
    print("INFORMASI DATASET")
    print("=" * 30)

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

    print(df.isnull().sum())

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

    print("\n" + "=" * 30)
    print("STATISTIK DATA")
    print("=" * 30)

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

    plt.figure(figsize=(7,5))

    plt.bar(
        churn.index,
        churn.values,
        color=["steelblue", "tomato"]
    )

    plt.title("Jumlah Pelanggan Churn", fontsize=14)
    plt.xlabel("Status Churn")
    plt.ylabel("Jumlah Pelanggan")

    plt.tight_layout()
    plt.savefig("grafik_bar_churn.png")
    plt.show()

def bar_chart(df):
    contract = df["Contract"].value_counts()

    plt.figure(figsize=(7,5))

    plt.bar(contract.index, contract.values)

    plt.title("Jumlah Pelanggan Berdasarkan Jenis Kontrak")
    plt.xlabel("Jenis Kontrak")
    plt.ylabel("Jumlah Pelanggan")

    plt.tight_layout()
    plt.savefig("grafik_bar_contract.png")
    plt.show()

def boxplot(df):
    """Membuat Boxplot MonthlyCharges berdasarkan Churn"""
    plt.figure(figsize=(7,5))

    plt.boxplot(
    [
        df[df["Churn"]=="No"]["MonthlyCharges"],
        df[df["Churn"]=="Yes"]["MonthlyCharges"]
    ],
    tick_labels=["No","Yes"] 
    )
    
    plt.title("Monthly Charges Berdasarkan Churn")
    plt.xlabel("Status Churn")
    plt.ylabel("Monthly Charges")

    plt.tight_layout()

    plt.savefig("grafik_boxplot.png")
    plt.show()

def histogram(df):

    plt.figure(figsize=(8,5))

    plt.hist(
        df["MonthlyCharges"],
        bins=15,
        edgecolor="white"
    )

    plt.title("Distribusi Monthly Charges")
    plt.xlabel("Monthly Charges")
    plt.ylabel("Jumlah Pelanggan")

    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("grafik_histogram.png")
    plt.show()
