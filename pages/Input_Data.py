import streamlit as st
import pandas as pd

st.set_page_config(page_title="Input Data", layout="wide")

# Judul dengan warna sage
st.markdown("""
<h1 style='color: #b3d4b8;'>Input Data Alternatif Lokasi</h1>
""", unsafe_allow_html=True)

st.markdown("""
Masukkan data dari beberapa alternatif lokasi coffee shop.  
Nilai seperti harga sewa, jarak, dan luas akan dikonversi otomatis ke skala.
""")

if "alternatif_data" not in st.session_state:
    st.session_state.alternatif_data = []

jumlah = st.number_input("Masukkan jumlah alternatif:", min_value=1, value=3, step=1)

st.session_state.alternatif_data = []
for i in range(jumlah):
    with st.expander(f"Alternatif {i+1}", expanded=False):
        nama = st.text_input(f"Nama Lokasi {i+1}", f"Lokasi {i+1}")
        c1 = st.number_input(f"Harga Sewa (Rp) - Lokasi {i+1}", min_value=0, value=100_000_000, step=1_000_000)
        c2 = st.number_input(f"Jarak ke Kampus (km) - Lokasi {i+1}", min_value=0.0, step=0.1)
        c3 = st.number_input(f"Kepadatan Mahasiswa - Lokasi {i+1}", min_value=0, value=100)
        c4 = st.number_input(f"Jumlah Kompetitor - Lokasi {i+1}", min_value=0, value=3)
        c5 = st.number_input(f"Luas Tempat (m²) - Lokasi {i+1}", min_value=0, value=150)
        st.session_state.alternatif_data.append([nama, c1, c2, c3, c4, c5])

if st.session_state.alternatif_data:
    df_preview = pd.DataFrame(
        st.session_state.alternatif_data,
        columns=["Alternatif", "Harga Sewa", "Jarak", "Kepadatan", "Kompetitor", "Luas"]
    )

    # Subjudul preview dengan warna coklat
    st.markdown("""
    <h3 style='color: #d3b497;'>Preview Data</h3>
    """, unsafe_allow_html=True)

    st.dataframe(df_preview)
