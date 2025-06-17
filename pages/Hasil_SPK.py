import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Hasil SPK", layout="wide")

# Judul dengan warna sage
st.markdown("""
<h1 style='color: #d3b497;'>Hasil Perhitungan SPK - WP</h1>
""", unsafe_allow_html=True)
# Cek data
if "alternatif_data" not in st.session_state or not st.session_state.alternatif_data:
    st.warning("Silakan masukkan data terlebih dahulu di halaman Input Data.")
    st.stop()

# Skala konversi
def skala_harga_sewa(nilai):
    if nilai <= 100_000_000:
        return 5
    elif nilai <= 125_000_000:
        return 4
    elif nilai <= 150_000_000:
        return 3
    elif nilai <= 175_000_000:
        return 2
    else:
        return 1

def skala_aksesibilitas(nilai):
    if nilai <= 0.5:
        return 5
    elif nilai <= 1.0:
        return 4
    elif nilai <= 1.5:
        return 3
    elif nilai <= 2.0:
        return 2
    else:
        return 1

def skala_luas_tempat(nilai):
    if nilai > 300:
        return 5
    elif nilai >= 201:
        return 4
    elif nilai >= 151:
        return 3
    elif nilai >= 101:
        return 2
    else:
        return 1

# Bobot dan tipe
bobot = [5, 4, 4, 5, 3]
tipe_kriteria = ['cost', 'cost', 'benefit', 'cost', 'benefit']
total_bobot = sum(bobot)
w = [b / total_bobot for b in bobot]
w_signed = [w[i] * (-1 if tipe_kriteria[i] == 'cost' else 1) for i in range(len(w))]

# DataFrame
df = pd.DataFrame(st.session_state.alternatif_data, columns=["Alternatif", "C1_HargaSewa", "C2_Jarak", "C3_Kepadatan", "C4_Kompetitor", "C5_Luas"])
df["C1"] = df["C1_HargaSewa"].apply(skala_harga_sewa)
df["C2"] = df["C2_Jarak"].apply(skala_aksesibilitas)
df["C3"] = df["C3_Kepadatan"]
df["C4"] = df["C4_Kompetitor"]
df["C5"] = df["C5_Luas"].apply(skala_luas_tempat)

# Hitung WP
nilai_kriteria = df[["C1", "C2", "C3", "C4", "C5"]].values
S = np.prod(np.power(nilai_kriteria, w_signed), axis=1)
V = S / np.sum(S)

# Hasil
df["Skor S"] = S
df["Skor V"] = V
df["Rank"] = df["Skor V"].rank(ascending=False).astype(int)
df = df.sort_values("Skor V", ascending=False).reset_index(drop=True)

st.markdown("### Ranking Alternatif")
st.dataframe(df[["Alternatif", "Skor V", "Rank"]])

best = df.loc[0, "Alternatif"]
st.success(f"✅ Lokasi terbaik adalah: **{best}**")
