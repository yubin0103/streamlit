import streamlit as st
import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()

st.subheader('회원가입')

with st.form('my_form', clear_on_submit=True):
    st.info('다음 양식을 모두 입력 후 제출하세요!')
    uid = st.text_input('이름', max_chars=12)
    uname = st.text_input('ID', max_chars=10)
    upw = st.text_input('PW', type='password')
    upw_chk = st.text_input('비밀번호 확인', type='password')
    ubd = st.date_input('생년월일')
    ugender = st.radio('성별', options=['남','여'], horizontal=True)

    submitted = st.form_submit_button('완료')
    if submitted:
        st.success(f'{uname} {uid} {upw} {ubd} {ugender}')
        cur.execute(f"INSERT INTO users VALUES ("
                    f"'{uname}','{uid}','{upw}',"
                    f"'{ubd}','{ugender}')")
        con.commit()


