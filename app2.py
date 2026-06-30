import streamlit as st
import pickle

st.title('Tecrübe yazılı ve mülakata göre maaş tahmini :heavy_dollar_sign:')
model=pickle.load(open('maas.pkl', 'rb'))

tecrube=st.number_input('tecrube',1,10)
yazili=st.number_input('yazili',1,10)
mulakat=st.number_input('Mulakat',1,10)
if st.button('tahmin et'):
    tahmin = model.predict([[tecrube, yazili, mulakat]])
    tahmin=round(tahmin[0][0])
    st.success(f'Yapay zekanın tahmin ettiği maaş:$ {tahmin}')