from utils import (
    load_data,
    check_data,
    clean_data,
    statistics_summary,
    save_summary_to_txt,
    bar_chart,
    scatter_plot,
    correlation_heatmap
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
    scatter_plot(df)
    correlation_heatmap(df)

    print("\n" + "=" * 60)
    print("SEMUA PROSES BERHASIL DIJALANKAN")
    print("Output yang dihasilkan:")
    print("- hasil_analisis.txt")
    print("- grafik_bar_churn.png")
    print("- grafik_scatter.png")
    print("- grafik_heatmap.png")
    print("=" * 60)


if __name__ == "__main__":
    main()