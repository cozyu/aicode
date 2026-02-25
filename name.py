import streamlit as st
import pandas as pd

st.title('나의 첫 데이터 앱')

name = st.text_input('이름을 입력하세요:')
if name:
    st.write(f'반갑습니다, {name}님!')

data = pd.DataFrame({'숫자': [1, 2, 3], '값': [10, 20, 30]})
st.line_chart(data)
