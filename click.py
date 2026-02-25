import streamlit as st

st.title("나의 첫 웹 앱")
st.write("반가워요! Streamlit으로 만든 사이트입니다.")

if st.button("클릭해보세요"):
    st.success("버튼을 누르셨군요!")
