import streamlit as st
from utils import *
custom_css = """
            <style>
                
                div[data-testid="stVerticalBlock"]{
                    width: 44vh;
                    margin-left: auto;
                    margin-right: auto;
                    text-align: center;
                }  
                         
                </style>
            """
                     
st.markdown(custom_css ,unsafe_allow_html=True)
with st.container():
    st.header("&nbsp;&nbsp;&nbsp;&nbsp; WELCOME")
    st.markdown("&nbsp; **J O I N - U S - T O D A Y 🎈**")  
    email = st.text_input(label="Enter you Email", placeholder= "mypersonalmail@yourdomain.com",value="admin")
    password = st.text_input(label="Enter you super secret password", placeholder='****************',type='password',value="admin")
    
    if st.button("Sign Up", type='primary',use_container_width=True):
        store_authentication_data(email,password)
        current_page(page='dashboard_page')
        st.rerun()
        
    st.caption('Existing user? Click here to Login')
    
    if st.button("Log In", type='secondary',use_container_width=True):
        current_page('login_page')
        st.rerun() 