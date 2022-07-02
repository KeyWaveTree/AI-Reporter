import streamlit as st
text=st.text_input('텍스트 입력기')
number=st.text_input('숫자 입력기', format='%6f')
st.text(text)
st.text(number)