import streamlit as st

st.set_page_config(
    page_title = "Heart Attack Prediction",
    page_icon="🧊",
    layout = "wide"
)

st.title('Heart Disease Prediction')
url = "https://www.linkedin.com/in/akhmad-fadhil/"

i, ii, iii = st.columns(3)
with ii:
    st.image('heart.jpg', caption='Healthy heart', width=500)

# with st.container(border=True):
    # st.markdown(
    #     """
    #     Penyakit jantung adalah penyebab utama kematian bagi masyarakat di Amerika. Penyakit tersebut diderita hampir oleh seluruh ras yang ada di Amerika seperti Afrika-Amerika, 
    #     Indian Amerika, dan penduduk asli Alaska, serta kulit putih. Studi terbaru dari Centers of Disease Control and Prevention (CDC) menunjukkan bahwa hamper separuh penduduk 
    #     Amerika (47%) memiliki setidaknya 1 dari 3 faktor resiko utama penyakit jantung. Faktor resiko utama tersebut antara lain:
    #     - Tekanan darah tinggi
    #     - Kolesterol tinggi
    #     - Merokok
    #     """)
    # st.markdown(
    #     """
    #     Selain itu, indikator lain yang yang dapat menyebabkan penyakit jantung antara lain status diabetes, obesitas (BMI tinggi), kurang aktivitas fisik, atau terlalu banyak 
    #     minum alkohol. 
    #     \nOleh karena itu, mengidentifikasi dan mencegah faktor yang memiliki dampak terbesar terhadap penyakit jantung sangat penting untuk meminimalisir kematian. 
    #     Dalam konteks ini, faktor yang akan dianalisis yaitu perilaku kesehatan untuk mencari insight yang dapat dilitindaklanjuti sehingga mengurangi penderita penyakit jantung. 
    #     """)
        
