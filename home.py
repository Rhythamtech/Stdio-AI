import os
import streamlit as st
from utils import *

custom_css = """
            <style>
                
                div[data-testid="stVerticalBlock"]{
                    width: 80vv;
                    margin-left: auto;
                    margin-right: auto;
                    text-align: center;
                }  
                
                div[data-testid="stImage"]{
                    margin:auto;
                }
                         
                </style>
            """            

current_page()

signin_page = st.Page("signin.py", title="Sign Up", icon=":material/person_add:",url_path='signup')
login_page = st.Page("login.py", title="Log in", icon=":material/login:",url_path='login')
settings_page = st.Page("settings.py", title="Settings", icon=":material/settings:")
dasboard_page = st.Page("dashboard.py", title="Dashboard", icon=":material/dashboard:",url_path='dashboard')
video_processing_page = st.Page("notes.py", title="Video Processing", icon=":material/memory_alt:")
 
def home_page():
    st.markdown( custom_css ,unsafe_allow_html=True)

    st.title("Write YouTube Video notes With AI")
    st.markdown("#### :grey[Effortlessly Writing YouTube Video Notes with AI Assistance]")
    st.markdown("\n")

    button_cols = st.columns([10,6,6,10],vertical_alignment='center')

    button_cols[1].button("Get Started", key="get-started",use_container_width = True,type="primary")
    button_cols[2].button("Watch Tutorial  ▶️", key="watch-tutorial",use_container_width = True)

    st.markdown("###\n\n ##### :grey[WHAT WE ACHIEVED 😎]")
    #st.image("download.svg",width=420)
    st.html("""            
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}

/* Float four columns side by side */
.column {
  float: left;
  width: 25%;
  padding: 0 5px;
}

.row {margin: 0 -5px;}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive columns */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
    display: block;
    margin-bottom: 10px;
  }
}

/* Style the counter cards */
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  padding: 16px;
  border: 1px solid;
  border-radius: 8px;
  text-align: center;
}

.fa {font-size:50px;}
</style>


<div class="row">
  <div class="column">
    <div class="card">
      <h3>30+</h3>
      <p>Active Users</p>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <h3>100+</h3>
      <p>Videos Processed</p>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
      <h3>70+</h3>
      <p>Notes Saved</p>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
      <h3>40+</h3>
      <p>Mindmap Saved</p>
    </div>
  </div>
</div>


            """)

    if st.session_state.get("get-started"):
        current_page("login_page")
        st.rerun()

if st.session_state.current_page == "login_page":
  st.navigation([login_page]).run()
elif st.session_state.current_page == 'signup_page':
  st.navigation([signin_page]).run()
elif st.session_state.current_page == 'dashboard_page':
  st.navigation([dasboard_page]).run()
elif st.session_state.current_page == 'video_processing_page':
  st.navigation([video_processing_page]).run()
else:
  home_page()



    
    
    
