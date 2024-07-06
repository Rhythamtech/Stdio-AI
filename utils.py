import streamlit as st
from streamlit_cookies_controller import CookieController

APP_NAME    = "Stdioai_Cookies_based_Authication"
COOKIE_NAME  = f"{APP_NAME}_authentication_cookie"
controller  = CookieController()

def required_authentication(page_name):
    st.write(controller.getAll())
    
    if controller.get(COOKIE_NAME) == None:
        st.session_state.current_page = 'login_page'
    else:
        cookie_username = controller.get(COOKIE_NAME)["username"]
        cookie_password = controller.get(COOKIE_NAME)["password"]
        
        if cookie_username == None or cookie_password == None:
            st.session_state.current_page = 'login_page'
        else:
            if cookie_username == "admin" and cookie_password == "admin":
                st.write(f"Welcome {cookie_username}")
            else:
                st.session_state.current_page = 'login_page'

def store_authentication_data(username,password):
    controller.set(COOKIE_NAME, {"username":"admin","password":"admin","current_page":st.session_state.current_page})

def remove_authentication_data():
    controller.remove(COOKIE_NAME)
    controller.set(COOKIE_NAME, {"username":None,"password":None,"current_page":"home_page"})
    
def current_page(page=None):
    cookies  = controller.get(COOKIE_NAME)
    if cookies == None and page == None:
        st.session_state.current_page = 'home_page'
        controller.set(COOKIE_NAME, {"username":None,"password":None,"current_page":st.session_state.current_page})

    elif page == None:
        st.session_state.current_page = controller.get(COOKIE_NAME)["current_page"]
        return st.session_state.current_page
        
    else:
        existing_cookies = controller.get(COOKIE_NAME)
        existing_cookies["current_page"] = page
        controller.set(COOKIE_NAME,existing_cookies)
        st.session_state.current_page = page
        
def display_cookies():
    st.write(controller.get(COOKIE_NAME))
    