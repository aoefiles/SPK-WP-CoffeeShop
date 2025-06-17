import streamlit as st

st.set_page_config(page_title="SPK Coffee Shop", layout="wide")

# Judul berwarna sage
st.markdown("""
<h1 style='text-align: center; color: #b3d4b8;'>
    SPK Coffee Shop - Metode Weighted Product
</h1>
""", unsafe_allow_html=True)

st.markdown("""
Selamat datang di aplikasi Sistem Pendukung Keputusan (SPK) untuk menentukan lokasi optimal cabang <b>coffee shop</b> menggunakan metode <b>Weighted Product (WP)</b>.

<hr style='border: 1px solid #eee;'>

<h3 style='color: #d3b497;'>Kriteria Penilaian:</h3>
""", unsafe_allow_html=True)

st.markdown("""
| Kode | Kriteria              | Tipe     |
|------|------------------------|----------|
| C1   | Harga Sewa (Rp)        | Cost     |
| C2   | Aksesibilitas (km)     | Cost     |
| C3   | Kepadatan Mahasiswa    | Benefit  |
| C4   | Jumlah Kompetitor      | Cost     |
| C5   | Luas Tempat (m²)       | Benefit  |
""")

st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# Subjudul metode
st.markdown("""
<h3 style='color: #d3b497;'>Tentang Metode Weighted Product (WP)</h3>

<p>Metode ini menghitung skor untuk setiap alternatif berdasarkan bobot dan jenis kriteria. Berikut adalah tahapan perhitungannya:</p>
""", unsafe_allow_html=True)

# Gambar rumus dengan subjudul numerik dan ukuran sedang
st.subheader("1. Normalisasi Bobot")
st.image("normalisasi.png", caption="Rumus Normalisasi Bobot", width=300)

st.subheader("2. Perhitungan Vektor S")
st.image("vektorS.png", caption="Rumus Perhitungan Vektor S", width=300)

st.subheader("3. Perhitungan Vektor V")
st.image("vektorV.png", caption="Rumus Perhitungan Vektor V", width=300)

st.markdown("""
<hr style='border: 1px solid #eee;'>
Silakan lanjut ke tab <b>Input Data</b> untuk mulai menilai alternatif lokasi.
""", unsafe_allow_html=True)
