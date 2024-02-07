import streamlit as st

# Header
st.header('Habibah :sparkles:')

# Subheader
st.subheader('Plot')

# Membuat dua kolom
c1, c2, c3= st.columns(3)

# Kolom pertama
with c1:
    num1 = st.number_input('Masukkan angka pertama', value=1)

# Kolom kedua
with c2:
    unit = st.selectbox('Pilih Unit', ('+', '-', 'x', '/'))

# Kolom ketiga
with c3:
    num2 = st.number_input('Masukkan angka kedua', value=1)
def calculate(num1, num2, unit):
    if unit == '+':
        result = num1 + num2
    elif unit == '-':
        result = num1-num2
    elif unit == 'x':
        result = num1*num2
    elif unit == '/':
        if num2 !=0: #Menghindari pembagian dengan nol
            result = num1/num2
        else :
            result = "Error:Pembagian dengan nol"
            return result
            
result = calculate(num1,num2,unit)
st.write('Hasil:',result)

st.caption('Copyright © Habibah Nur Wahidah 2024')
