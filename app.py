import streamlit as st


menu = st.sidebar.selectbox('메뉴', options=['식단 기록하기','기록 확인하기','통계보기','회원가입'])

if menu == '기록 확인하기':
    col1, col2, col3 = st.columns(3)
    with col1:
        emp_uid = st.empty()
        uid = emp_uid.text_input('아이디')
    with col2:
        search = st.button('검색')
        init = st.button('초기화')

    if search:

        if uid is None or len(uid) < 5:
            st.warning('아이디를 확인하세요!')
            st.stop()

        if check_uid(uid) == 0:
            st.warning('존재하지 않는 아이디입니다!')
            st.stop()

        cur.execute(f"SELECT "
                    f"u.uname, u.uid, u.upw, u.ubd, u.ugender, p.im_name "
                    f"FROM users as u, photos as p "
                    f"WHERE u.uid='{uid}'")
        res = cur.fetchone()
        df = pd.DataFrame(res,
                          index=['이름','아이디','비밀번호','생일','성별','사진'],
                          columns=['내용'])
        st.dataframe(df)
        st.image(os.path.join(save_dir, res[5]))

    if init:
        uid = None
        search = None
        uid = emp_uid.text_input('아이디', key=2)
