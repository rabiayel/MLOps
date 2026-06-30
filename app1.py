import streamlit as st
import pandas as pd
import plotly.express as px
st.title('MLOps Streamlit App :balloon:')


df = pd.read_csv('prog_languages_data.csv')


st.radio('Medeni Durum', ('Evli', 'Bekar', 'Dul', 'Nisanlı'))
st.selectbox('Bildiğiniz Programlama Dilleri', ['C++', 'Python', 'Java', 'Asp', 'C', 'Q#'])
st.multiselect('Bildiğiniz Programlama Dilleri', ['C++', 'Python', 'Java', 'Asp', 'C', 'Q#'])


st.write(df)

fig = px.pie(df, values='Sum')
st.plotly_chart(fig)


fig2 = px.bar(df, x = 'lang' , y='Sum')
st.plotly_chart(fig2)



st.divider()

st.text_input('Adınızı Giriniz')
st.file_uploader('Dosya Yükleyin')


st.write('Merhaba')

st.error('Hatalı')

st.text_area('Mesajınızı Girin')
st.time_input('Saat Sec')
st.date_input('Tarih Seç')

st.camera_input('Kamera')
st.balloons()

st.video('secret_of_success.mp4')

st.image('image_02.jpg')