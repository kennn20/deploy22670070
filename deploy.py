import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Analisis Dataset Game Terlaris")

# Upload atau load dataset
@st.cache_data
def load_data():
    return pd.read_csv("bestSelling_games.csv")

df = load_data()

# Tampilkan beberapa baris pertama
st.subheader("Tampilan Awal Dataset")
st.dataframe(df.head())

# Statistik ringkas
st.subheader("Statistik Ringkas")
st.write(df.describe())

# Pilihan untuk filter
st.subheader("Filter Berdasarkan Platform")
platforms = df['Platform'].dropna().unique()
selected_platform = st.selectbox("Pilih Platform", options=platforms)

filtered_df = df[df['Platform'] == selected_platform]
st.write(f"Jumlah game pada platform {selected_platform}: {filtered_df.shape[0]}")
st.dataframe(filtered_df)

# Visualisasi Penjualan berdasarkan Tahun
st.subheader("Visualisasi Penjualan per Tahun")
if 'Year' in df.columns and 'Global_Sales' in df.columns:
    sales_per_year = df.groupby('Year')['Global_Sales'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=sales_per_year, x='Year', y='Global_Sales', ax=ax)
    ax.set_title("Total Penjualan Global per Tahun")
    ax.set_ylabel("Penjualan (juta unit)")
    st.pyplot(fig)
else:
    st.warning("Kolom 'Year' atau 'Global_Sales' tidak ditemukan di dataset.")

# Footer
st.markdown("---")
st.markdown("Dibuat dengan ❤️ menggunakan Streamlit")

