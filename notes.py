from utils import *
import streamlit as st
from workflow import *
from database import *
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.bottom_container import bottom

st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"/>',
    unsafe_allow_html=True,
)
    
def hide_magic_button():
    st.markdown("""
                <style>
                button[data-testid="baseButton-secondary"]{
                    display: none;
                }
                </style>
                """,unsafe_allow_html=True)

def go_back():
    current_page('dashboard_page')
    st.rerun()
    
def saving_to_cloud(video_id,mindmap,notes):
    st.toast("Saving...",icon="👽")
    save_data(video_id,mindmap,notes)
    current_page('dashboard_page')
    

def bottom_layout(video_id,mindmap,notes):
    try :
        st.markdown("""
                    <style>
                    div [data-testid="stBottomBlockContainer"]{
                      padding-top: 3px;  
                    }
                    </style>    
                    """,unsafe_allow_html=True)

        cols = st.columns([8,4.5,4.5,8],gap="small",vertical_alignment="center")

        with cols[1]:
            with stylable_container(
                        key="gradient-button",
                        css_styles=r"""
                            button{
                                padding: 1rem;
                                position: relative;
                                background: linear-gradient(to right, red, purple);
                                padding: 3px;
                            }
                            """,
                    ):
                st.button("✨ **Re-generate** ",use_container_width=True,type="primary")

        with cols[2]:
            st.button("**Save to Cloud** 📁",use_container_width=True,type="primary",on_click=saving_to_cloud,args=(video_id,mindmap,notes))
                
    
    except Exception as e:
        st.error("Oops!! We are under Maintenance Mode 👷‍♂️. **STAY CONNECTED**")
        

# page UI starts from here...    

with stylable_container(
        key="icon-button",
        css_styles=r"""
            button div:before {
                font-family: 'Font Awesome 5 Free';
                content: '\F104';
                display: inline-block;
                padding: 1px;
                vertical-align: center;
                font-weight: 900;
            }
            """,
    ):
       if st.button("",type="primary"):
           go_back()
           
if "video_id" not in st.session_state :
    go_back()

st.title(YouTube("https://www.youtube.com/watch?v=" + str(st.session_state.video_id)).title)
mindmap_data = ''

if st.button("Click for AI Magic ✨"):
    
    if "workflow_completed" not in st.session_state:
        st.session_state["workflow_completed"] =  False
    else:
        st.session_state["workflow_completed"] =  False
        
    try:
        hide_magic_button()  
        data  = fetch_notes(video_id = st.session_state.video_id)
        
        if data == None:
            if notes_workflow() is not None:
                with st.spinner("Generating MindMap..."):
                    st.title("🧠 Mindmap")
                    mindmap_data = mindmap_workflow()
            else:
                st.write("```Unable to fetch transcript for " + str(st.session_state.video_id)+"```")
        else:
            st.write(data[0][0])
            st.title("🧠 Mindmap")
            markmap(data[0][1])
            st.session_state["workflow_completed"] = True
        
        
        if st.session_state["workflow_completed"] and data == None:
            with bottom():
                bottom_layout(st.session_state.video_id,mindmap_data,st.session_state.notes)
        
    except Exception as e:
        st.error("Oops!! We are under Maintenance Mode 👷‍♂️. **STAY CONNECTED**")
        