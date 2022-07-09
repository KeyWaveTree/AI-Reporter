import streamlit as st

click=st.sidebar.button('버튼')
st.text(click)

if st.sidebar.button('버튼'):
    st.text("클릭")