import streamlit as st
from textblob import TextBlob

st.title('Sentiment Analyzer')
text=st.text_area('Enter Text')
if text:
    polarity=TextBlob(text).sentiment.polarity
    if polarity>0.10:
        sentiment='Positive'
    elif polarity<-0.10:
        sentiment=' Negative'
    else:
        sentiment='Neutral'

    st.write("the sentiment is: ", sentiment)