import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent

@st.cache_resource
def load_artifacts():
    return (
        joblib.load(APP_DIR / "rf_stroke_model.pkl"),
        joblib.load(APP_DIR / "encoding_maps.pkl"),
        joblib.load(APP_DIR / "feature_names.pkl"),
    )

rf_model, encoding_maps, feature_names = load_artifacts()

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f0f4ff 0%, #faf8f5 50%, #e8f4fd 100%);
}
.stButton button {
    background-color: #1a237e;
    color: white;
    border-radius: 12px;
    padding: 14px 28px;
    border: none;
    font-size: 16px;
    font-weight: 600;
}
.stButton button:hover {
    background-color: #1565c0;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.title("🧠 Prediksi Risiko Stroke")
st.write("Isi data diri dan kesehatan kamu di bawah ini, lalu klik tombol prediksi.")
st.divider()

# =====================================================
# INPUT FORM
# =====================================================
col1, col2 = st.columns(2)

with col1:
    age               = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=30)
    avg_glucose_level = st.number_input("Kadar Glukosa Rata-rata (mg/dL)", min_value=50.0, max_value=300.0, value=90.0)
    bmi               = st.number_input("BMI", min_value=10.0, max_value=60.0, value=24.0)

with col2:
    work_type      = st.selectbox("Jenis Pekerjaan", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
    smoking_status = st.selectbox("Status Merokok", ["never smoked", "formerly smoked", "smokes", "Unknown"])

st.divider()

# =====================================================
# TOMBOL PREDIKSI
# =====================================================
if st.button("🔍 Prediksi Sekarang", use_container_width=True):

    with st.spinner("🧠 Menganalisis data kesehatan Anda..."):
        time.sleep(1.5)

    data_pasien = {
        'age'              : age,
        'avg_glucose_level': avg_glucose_level,
        'bmi'              : bmi,
        'work_type'        : work_type,
        'smoking_status'   : smoking_status,
    }

    # =====================================================
    # PREPROCESSING
    # =====================================================
    processed = {}
    for feat in feature_names:
        val = data_pasien[feat]
        if feat in encoding_maps:
            key = str(val).strip().lower()
            enc_map = encoding_maps[feat]
            if key not in enc_map:
                st.error(f"❌ Nilai '{val}' untuk fitur '{feat}' tidak ada di encoding map.")
                st.write("Nilai yang tersedia:", list(enc_map.keys()))
                st.stop()
            processed[feat] = enc_map[key]
        else:
            processed[feat] = float(val)

    input_df    = pd.DataFrame([processed])[feature_names]
    pred        = rf_model.predict(input_df)[0]
    prob        = rf_model.predict_proba(input_df)[0]
    prob_stroke = round(prob[1] * 100, 2)
    prob_aman   = round(prob[0] * 100, 2)

    # =====================================================
    # TAMPILKAN HASIL
    # =====================================================
    st.divider()
    st.subheader("📋 Hasil Prediksi")

    col_a, col_b = st.columns(2)
    col_a.metric("Probabilitas Tidak Stroke", f"{prob_aman}%")
    col_b.metric("Probabilitas Stroke", f"{prob_stroke}%")

    st.write("")
    st.write("**Probabilitas Risiko Stroke:**")
    st.progress(int(prob_stroke), text=f"{prob_stroke}%")

    st.divider()

    # =====================================================
    # HASIL & REKOMENDASI
    # =====================================================
    if pred == 1:
        if prob_stroke >= 75:
            st.error("🔴 RISIKO TINGGI — Anda berisiko terkena stroke.")
            with st.container(border=True):
                st.markdown("### 🏥 Rekomendasi")
                st.write("Risiko stroke Anda tergolong **tinggi**. Segera ambil tindakan:")
                st.markdown("""
                - Segera konsultasi ke dokter atau spesialis saraf
                - Kontrol tekanan darah secara rutin
                - Hindari rokok dan alkohol sepenuhnya
                - Kurangi makanan tinggi garam, lemak, dan gula
                - Minum obat sesuai resep dokter secara teratur
                """)
        else:
            st.warning("🟡 RISIKO SEDANG — Waspadai kondisi kesehatan Anda.")
            with st.container(border=True):
                st.markdown("### ⚠️ Rekomendasi")
                st.write("Risiko stroke Anda tergolong **sedang**. Lakukan langkah pencegahan:")
                st.markdown("""
                - Konsultasi ke dokter untuk pemeriksaan lebih lanjut
                - Pantau tekanan darah dan kadar gula secara berkala
                - Mulai olahraga ringan minimal 30 menit per hari
                - Jaga pola makan seimbang dan hindari stres berlebihan
                - Kurangi konsumsi rokok jika masih merokok
                """)
    else:
        if prob_stroke < 25:
            st.success("🟢 RISIKO RENDAH — Anda tidak terindikasi stroke.")
            with st.container(border=True):
                st.markdown("### ✅ Rekomendasi")
                st.write("Risiko stroke Anda tergolong **rendah**. Namun tetap jaga pola hidup sehat:")
                st.markdown("""
                - Olahraga teratur minimal 3x seminggu
                - Pola makan seimbang
                - Cek kesehatan rutin setidaknya 1x setahun
                - Kelola stres dengan baik
                - Istirahat cukup 7-8 jam per hari
                """)
        else:
            st.warning("🟡 RISIKO SEDANG — Tidak terindikasi stroke, namun tetap pantau kesehatan.")
            with st.container(border=True):
                st.markdown("### ⚠️ Rekomendasi")
                st.write("Risiko stroke Anda **cukup perlu diwaspadai**. Beberapa saran:")
                st.markdown("""
                - Periksakan kesehatan secara rutin ke dokter
                - Jaga berat badan ideal dan hindari obesitas
                - Batasi konsumsi makanan berlemak dan tinggi gula
                - Aktif bergerak dan hindari gaya hidup sedentari
                - Pantau tekanan darah dan kadar gula darah secara berkala
                """)

    st.caption("⚕️ Hasil ini bersifat prediktif, bukan diagnosis medis resmi.")