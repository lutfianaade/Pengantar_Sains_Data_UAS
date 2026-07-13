from utils import (
    load_data,
    check_data,
    clean_data,
    statistics_summary,
    save_summary_to_txt,
    bar_chart,
    boxplot,
    histogram
)


def main():
    # Lokasi dataset
    file_path = "dataset/Telco-Customer-Churn.csv"

    # Load dataset
    df = load_data(file_path)

    # Cek kondisi dataset
    check_data(df)

    # Data cleaning
    df = clean_data(df)

    # Statistik deskriptif
    statistics_summary(df)

    # Simpan hasil analisis ke file TXT
    save_summary_to_txt(df)

    # Visualisasi
    bar_chart(df)
    boxplot(df)
    histogram(df)

    print("\n" + "=" * 60)
    print("SEMUA PROSES BERHASIL DIJALANKAN")
    print("Output yang dihasilkan:")
    print("- hasil_analisis.txt")
    print("- grafik_bar_churn.png")
    print("- grafik_bar_contract.png")
    print("- grafik_boxplot.png")
    print("- grafik_histogram.png")
    print("=" * 60)


if __name__ == "__main__":
    main()