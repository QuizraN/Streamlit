import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(layout='wide')

if __name__ == "__main__":
    st.title("Stramlit Demo Application")
    # data_point =st.slider('Select a value', min_value=0, max_value=10)
    # st.write("The Selcted value is:",data_point)
    components.iframe("https://docs.google.com/presentation/d/1fkKdCXsdglEok_gjy7-eJa1i2WDUgMSQZdtNA1YcJlc/edit?usp=sharing", width=1700, height=1000)
    st.balloons()
    