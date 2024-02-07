import streamlit as st

# Header
st.header('Habibah:sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)

with c1:
  x = st.number_input('Suhu',value=100)
  st.write('=>:')
with c2:
  satuan = st.selectbox
    ('C', 'F', 'R', 'K'),key='k1')

sr.write(x,' ',satuan,'= ',' ')

st.caption('Copyright © Habibah Nur Wahidah 2024')
