import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(
    page_title="Game Terlaris",
    page_icon="🎮",
    layout="wide"
)

# Gaya CSS tambahan untuk mempercantik tampilan
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .hero {
        text-align: center;
        padding: 3rem 1rem;
        background-color: #0e1117;
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 3em;
        margin-bottom: 0.2em;
    }
    .hero p {
        font-size: 1.2em;
        color: #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
    <div class="hero">
        <h1>🎮 Analisis Game Terlaris</h1>
        <p>Temukan insight menarik dari ribuan data game populer!</p>
    </div>
""", unsafe_allow_html=True)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("bestSelling_games.csv")
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['release_year'] = df['release_date'].dt.year
    return df

df = load_data()

# Seksi 1 - Ringkasan Dataset
with st.container():
    st.subheader("🔍 Ringkasan Dataset")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Contoh Data:")
        st.dataframe(df.head())

    with col2:
        st.write("Statistik Ringkas:")
        st.write(df.describe())

# Seksi 2 - Visualisasi per Tahun
with st.container():
    st.subheader("📈 Visualisasi Unduhan Estimasi per Tahun Rilis")
    if 'release_year' in df.columns and 'estimated_downloads' in df.columns:
        downloads_per_year = df.groupby('release_year')['estimated_downloads'].sum().reset_index()
        downloads_per_year = downloads_per_year.dropna()

        fig, ax = plt.subplots(figsize=(12, 5))
        sns.lineplot(data=downloads_per_year, x='release_year', y='estimated_downloads', ax=ax)
        ax.set_title("Total Unduhan Estimasi per Tahun Rilis", fontsize=14)
        ax.set_ylabel("Estimasi Unduhan")
        ax.set_xlabel("Tahun Rilis")
        st.pyplot(fig)
    else:
        st.warning("Kolom 'release_year' atau 'estimated_downloads' tidak ditemukan.")

# Seksi 3 - Ekspander Detail
with st.expander("📂 Lihat Seluruh Data dan Detail Kolom"):
    st.write("Jumlah entri:", df.shape[0])
    st.write("Kolom dataset:")
    st.write(df.columns.tolist())
    st.dataframe(df)

# Footer
st.markdown("---")
st.markdown("<center>Dibuat dengan ❤️ menggunakan Streamlit | Dataset: Game Terlaris</center>", unsafe_allow_html=True)
