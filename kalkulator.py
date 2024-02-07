import streamlit as st

# Header
st.header('Habibah :sparkles:')

# Subheader
st.subheader('Plot')

# Membuat dua kolom
c1, c2 = st.columns(2)

# Kolom pertama
with c1:
    x = st.number_input('Suhu', value=100)

# Kolom kedua
with c2:
    unit = st.selectbox('Unit', ('C', 'F', 'R', 'K'), key='k1')

# Menampilkan hasil input
st.write(x, unit)

st.caption('Copyright © Habibah Nur Wahidah 2024')
