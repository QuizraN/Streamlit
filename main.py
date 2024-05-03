import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')

if __name__ == "__main__":
    st.title("BC Demo Application")
    components.iframe("https://docs.google.com/presentation/d/1fkKdCXsdglEok_gjy7-eJa1i2WDUgMSQZdtNA1YcJlc/edit?usp=sharing",width=1700, height=1000)