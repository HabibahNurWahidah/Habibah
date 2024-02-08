import streamlit as st

st.header('Habibah :heart:')
st.subheader('Suhu')

def konversiSuhu(suhu):
    drjt = int(suhu[:-1])
    inputan = suhu[-1]

if inputan.upper()=="C":
    hasil1 = float((9*drjt)/5+32)
    hasil2 = float(drjt+273.15)
    hasil3 = float(4/5*drjt)
    jenisX = "Celcius"
    jenis1 = "Farenheit"
    jenis2 = "Kelvin"
    jenis3 = "Reamur"
    print(drjt,jenisX,"=","{:.1f}".
format(hasil1),jenis1)
    print(drjt,jenisX,"=","{:.1f}".
format(hasil2),jenis2)
    print(drjt,jenisX,"=","{:.1f}".
format(hasil3),jenis3) 

elif inputan.upper()=="F":
    hasil1 = float((djrt-32)*5/9)
    hasil2 = float(((djrt-32)*5/9)+273.15)
    hasil3 = float(4/9*(djrt-32))
    jenisX = "Farenheit"
    jenis1 = "Celcius"
    jenis2 = "Kelvin"
    jenis3 = "Reamur"
    print(drjt,jenisX,"=","{:.1f}".
format(hasil1),jenis1)
    print(drjt,jenisX,"=","{:.1f}".
format(hasil2),jenis2)
    print(drjt,jenisX,"=","{:.1f}".
format(hasil3),jenis3)

elif inputan.upper()=="K":
    hasil1 = float(djrt-273.15)
    hasil2 = float(((djrt-273.15)*9/5)+32)
    hasil3 = float(4/5*(djrt-273))
    jenisX = "Kelvin"
    jenis1 = "Celcius"
    jenis2 = "Farenheit"
    jenis3 = "Reamur"
    print(drjt,jenisX,"=","{:.1f}".
format(hasil1),jenis1)
    print(drjt,jenisX,"=","{:.1f}".
format(hasil2),jenis2)
    print(drjt,jenisX,"=","{:.1f}".
format(hasil3),jenis3)

elif inputan.upper()=="R":
    hasil1 = float((5/4)*drjt)
    hasil2 = float((9/4*drjt)+32)
    hasil3 = float((5/4*drjt)+273)
    jenisX = "Reamur"
    jenis1 = "Celcius"
    jenis2 = "Farenheit"
    jenis3 = "Kelvin"
    print(drjt,jenisX,"=","{:.1f}".
format(hasil1),jenis1)
    print(drjt,jenisX,"=","{:.1f}".
format(hasil2),jenis2)
    print(drjt,jenisX,"=","{:.1f}".
format(hasil3),jenis3)

    else:
    print("Inputan tidak sesuai! Perhatikan penulisan input")
i=0
print("Program Konversi Suhu")
while i==0:
    temp=input("/nMasukan suhu =")
    konversiSuhu(temp)

lagi=int(input("Hitung lagi?(1=iya) atau (0=tidak)="))
if(lagi==1):
    i=0
elif(lagi!=1):
    i=1

    
