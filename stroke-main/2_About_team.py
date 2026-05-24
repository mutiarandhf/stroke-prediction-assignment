import streamlit as st
from pathlib import Path

# Ambil root project
BASE_DIR = Path(__file__).resolve().parent.parent

st.title("👥 Our Team")
st.divider()

st.subheader("Anggota Tim")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(str(BASE_DIR / "assets" / "daffa.jpeg"), use_container_width=True)
    st.markdown("**Muhammad Daffa**")
    st.caption("NPM: 2506704941")

with col2:
    st.image(str(BASE_DIR / "assets" / "mutiara.jpeg"), use_container_width=True)
    st.markdown("**Mutiara Dewi Nadhifa**")
    st.caption("NPM: 2506704992")

with col3:
    st.image(str(BASE_DIR / "assets" / "sindi.jpeg"), use_container_width=True)
    st.markdown("**Sindi Novelia**")
    st.caption("NPM: 2506562343")

st.divider()
st.subheader("Dosen Pembimbing")

col_prof, col_info = st.columns([1, 2])

with col_prof:
    st.image(str(BASE_DIR / "assets" / "prof al.jpg"), use_container_width=True)

with col_info:
    st.markdown("**Prof. Alhadi Bustamam, S.Si., M.Kom., Ph.D**")
    st.caption("Dosen Pembimbing")
    st.caption("Mata kuliah Komputasi dan Sains Data")

st.divider()

st.subheader("Technology")
st.markdown("""
- Python
- Streamlit
- Random Forest
- Scikit-learn
""")