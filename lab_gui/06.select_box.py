import streamlit as st

select=st.selectbox('선택박스', ['A', 'B', 'C'])
st.text(select)