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
                
                div[data-testid="stImage"]{
                    margin:auto;
                }
                         
                </style>
            """
            
st.markdown( custom_css ,unsafe_allow_html=True)
with st.container():
    st.subheader("&nbsp;&nbsp;&nbsp; Hello Again!")
    st.markdown("**Welcome back you've been misssed!**")
    email = st.text_input(label="Enter you Email", placeholder= "mypersonalmail@yourdomain.com",value="admin")
    password = st.text_input(label="Enter you super secret password", placeholder='****************',type='password',value="admmin")
    
    if st.button("Log In", type='primary',use_container_width=True):
        store_authentication_data(email,password)
        current_page(page='dashboard_page')
        st.rerun()
        
    st.caption('New user? Click here to sign up')
    
    if st.button("Sign Up", type='secondary',use_container_width=True):
        current_page('signup_page')
        st.rerun()