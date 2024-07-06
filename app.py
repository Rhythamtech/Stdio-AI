import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed",layout='wide')


if "is_user_authenticated" not in st.session_state:
    st.session_state.is_user_authenticated = False
    
is_user_authenticated = st.session_state.is_user_authenticated 

home_page = st.Page("home.py", title="Home", icon=":material/home:")
pg = st.navigation([home_page])
pg.run()
