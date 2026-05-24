import streamlit as st
import time

st.set_page_config(
    page_title="Stroke Prediction",
    page_icon="🧠",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
/* Background utama */
.stApp {
    background: linear-gradient(135deg, #f0f4ff 0%, #faf8f5 50%, #e8f4fd 100%);
}

/* Hero title */
h1 {
    text-align: center;
    color: #1a237e;
    font-size: 56px;
    font-weight: 800;
}

/* Subtitle */
h2 {
    text-align: center;
    color: #1565c0;
    font-size: 32px;
}

p {
    text-align: center;
    color: #4B5563;
    font-size: 18px;
}

/* Tombol */
.stButton button {
    background-color: #1a237e;
    color: white;
    border-radius: 12px;
    padding: 14px 28px;
    border: none;
    font-size: 16px;
    font-weight: 600;
    transition: 0.3s;
}
.stButton button:hover {
    background-color: #1565c0;
    transform: translateY(-2px);
}

/* Kartu statistik */
.stat-card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(26, 35, 126, 0.1);
    border-top: 4px solid #1565c0;
    margin: 8px 0;
}
.stat-number {
    font-size: 42px;
    font-weight: 800;
    color: #1a237e;
    margin: 0;
}
.stat-label {
    font-size: 14px;
    color: #6B7280;
    margin: 4px 0 0 0;
}

/* Kartu container */
.info-card {
    background: white;
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    height: 100%;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================
st.markdown("""
# 🧠 Stroke Prediction

## Sistem Prediksi Risiko Stroke dengan Machine Learning

Deteksi dini risiko stroke menggunakan teknologi kecerdasan buatan
untuk membantu pencegahan dan penanganan yang lebih baik.
""")

st.write("")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔍 Coba Prediksi Sekarang", use_container_width=True):
        st.switch_page("pages/1_Prediksi_stroke.py")
with col2:
    if st.button("📖 Pelajari Lebih Lanjut", use_container_width=True):
        st.switch_page("pages/2_About_team.py")

st.divider()

# =====================================================
# STATISTIK FAKTA STROKE
# =====================================================
st.markdown("<h2 style='text-align:center; color:#1a237e;'>📊 Fakta Stroke di Indonesia</h2>", unsafe_allow_html=True)
st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='stat-card'>
        <p class='stat-number'>1 dari 4</p>
        <p class='stat-label'>orang dewasa berusia di atas 25 tahun akan mengalami stroke</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='stat-card'>
        <p class='stat-number'>330rb+</p>
        <p class='stat-label'>kematian akibat stroke per tahun di Indonesia</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='stat-card'>
        <p class='stat-number'>80%</p>
        <p class='stat-label'>kasus stroke sebenarnya dapat dicegah</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='stat-card'>
        <p class='stat-number'>#2</p>
        <p class='stat-label'>penyebab kematian tertinggi di dunia</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# TENTANG PROJECT
# =====================================================
st.markdown("<h2 style='text-align:center; color:#1a237e;'>Tentang Project</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Project ini bertujuan untuk mengembangkan sistem prediksi risiko stroke yang dapat membantu tenaga medis dan masyarakat dalam deteksi dini</p>", unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 📌 Latar Belakang")
        st.write("")
        st.write(
            "Stroke merupakan salah satu penyebab kematian tertinggi di Indonesia. "
            "Deteksi dini faktor risiko stroke sangat penting untuk pencegahan dan "
            "penanganan yang lebih efektif."
        )
        st.write(
            "Dengan memanfaatkan teknologi machine learning, kami mengembangkan sistem "
            "yang dapat memprediksi risiko stroke berdasarkan berbagai parameter kesehatan."
        )

with col2:
    with st.container(border=True):
        st.markdown("### 💻 Teknologi yang Digunakan")
        st.write("")
        st.markdown("""
        • Python & Scikit-learn untuk model ML  
        • Streamlit untuk frontend  
        • Random Forest, LR & SVM untuk klasifikasi  
        • Pandas & NumPy untuk data processing  
        """)