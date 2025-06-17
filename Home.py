import streamlit as st

st.set_page_config(
    page_title="SPK Lokasi Coffee Shop",
    layout="wide"
)


# Gambar header
st.image("header.jpg", use_container_width=True)

# Konten utama di tengah
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<h1 style='text-align: center; color: #b3d4b8;'>SPK Lokasi Coffee Shop</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align: center; font-size: 18px; color: #b3d4b8;'>
        Aplikasi <b style='color:#d3b497;'>Sistem Pendukung Keputusan (SPK)</b> berbasis 
        <b style='color:#d3b497;'>Weighted Product (WP)</b><br>
        untuk membantu menentukan lokasi terbaik pembukaan <i>coffee shop</i> di Yogyakarta.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align: center; font-size: 16px; color: black; background-color: #c6915f; padding: 10px; border-radius: 10px;'>
        Gunakan menu di sidebar untuk memulai:
        <br>
        • Input data alternatif<br>
        • Lihat hasil perhitungan<br>
        • Ranking lokasi terbaik
    </p>
    """, unsafe_allow_html=True)
