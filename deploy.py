import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Analisis Dataset Game Terlaris")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("bestSelling_games.csv")
    # Konversi kolom tanggal
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['release_year'] = df['release_date'].dt.year
    return df

df = load_data()

# Tampilkan beberapa baris pertama
st.subheader("Tampilan Awal Dataset")
st.dataframe(df.head())

# Statistik ringkas
st.subheader("Statistik Ringkas")
st.write(df.describe())

# Visualisasi Estimated Downloads berdasarkan Tahun Rilis
st.subheader("Visualisasi Unduhan Estimasi per Tahun Rilis")
if 'release_year' in df.columns and 'estimated_downloads' in df.columns:
    downloads_per_year = df.groupby('release_year')['estimated_downloads'].sum().reset_index()
    downloads_per_year = downloads_per_year.dropna()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=downloads_per_year, x='release_year', y='estimated_downloads', ax=ax)
    ax.set_title("Total Unduhan Estimasi per Tahun Rilis")
    ax.set_ylabel("Estimasi Unduhan")
    ax.set_xlabel("Tahun Rilis")
    st.pyplot(fig)
else:
    st.warning("Kolom 'release_year' atau 'estimated_downloads' tidak ditemukan.")

# Footer
st.markdown("---")
st.markdown("Pangeran Genuk")
