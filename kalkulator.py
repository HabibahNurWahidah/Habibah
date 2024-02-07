import streamlit as st

# Header
st.header('Habibah :sparkles:')

# Subheader
st.subheader('Plot')

# Membuat dua kolom
c1, c2, c3= st.columns(3)

# Kolom pertama
with c1:
    x = st.number_input('Masukkan angka pertama', value=100)

# Kolom kedua
with c2:
    unit = st.selectbox('Unit', ('C', 'F', 'R', 'K'), key='k1')


# Menampilkan hasil input
st.write(x, unit)

st.caption('Copyright © Habibah Nur Wahidah 2024')
