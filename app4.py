import streamlit as st
from gtts import gTTS

st.title('Text to Speech :musical_note:')
text=st.text_area('Enter Text')
if text:
    tts=gTTS(text, lang='ru')
    tts.save('ses.mp3')
    ses=open('ses.mp3','rb')
    st.audio(ses.read())