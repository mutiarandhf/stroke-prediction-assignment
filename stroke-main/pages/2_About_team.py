import streamlit as st

st.title("👥 Our Team")
st.divider()

st.subheader("Anggota Tim")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/daffa.jpeg", use_container_width=True)
    st.markdown("**Muhammad Daffa**")
    st.caption("NPM: 2506704941")

with col2:
    st.image("assets/mutiara.jpeg", use_container_width=True)
    st.markdown("**Mutiara Dewi Nadhifa**")
    st.caption("NPM: 2506704992")

with col3:
    st.image("assets/sindi.jpeg", use_container_width=True)
    st.markdown("**Sindi Novelia**")
    st.caption("NPM: 2506562343")

st.divider()
st.subheader("Dosen Pembimbing")

col_prof, col_info = st.columns([1, 2])  # kolom foto lebih kecil dari kolom info

with col_prof:
    st.image("assets/prof al.jpg", use_container_width=True)

with col_info:
    st.markdown("**Prof. Alhadi Bustamam, S.Si., M.Kom., Ph.D**")
    st.caption("Dosen Pembimbing")
    st.caption("\nMata kuliah Komputasi dan Sains Data")

st.divider()

st.subheader("Technology")
st.markdown("""
- Python
- Streamlit
- Random Forest
- Scikit-learn
""")