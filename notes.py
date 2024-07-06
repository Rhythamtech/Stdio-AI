import uuid
from utils import *
import streamlit as st
from workflow import *
from pytube import YouTube
import streamlit.components.v1 as components
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
               
def download_base64_file(b64, download_filename):
    id_link = '_'+str(uuid.uuid4())
    components.html(
        f"""          
        
     <html>
    <head>
    <title>Start Auto Download file</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script>
    $('<a href="data:application/octet-stream;base64,{b64}" download="{download_filename}">')[0].click()
    </script>
    </head>
    </html>                           """)  
      
@st.experimental_fragment
def download_form_container(notes,mindmap):
    
    cols = st.columns([8,2,1.07],vertical_alignment='bottom')
    selection =  cols[1].selectbox("Download: ",["Notes as .pdf","Mindmap as .pdf"],index=None,)

    with cols[2]:
        if selection == "Notes as .pdf":
            base64_notes = create_notes_pdf(content=notes)
            st.download_button("Download",
                                   data = base64_notes,
                                   type='primary',
                                 file_name=f"video_notes_{st.session_state.video_id}.pdf",
                                 mime = "application/octet-stream", )

        elif selection == "Mindmap as .pdf":
            base64_mindmap = create_mindmap_pdf(content=mindmap)
            stylable_container.download_button("Download",
                                   data = base64_mindmap,
                                 file_name=f"video_mindmap_{st.session_state.video_id}.pdf",
                                 type='primary',
                                 mime = "application/octet-stream", )


with stylable_container(
        key="container_with_border",
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
    hide_magic_button()  
    if notes_workflow() is not None:
        with st.spinner("Generating MindMap..."):
            st.title("🧠 Mindmap")
            mindmap_data = mindmap_workflow()
    else:
        st.write("```Unable to fetch transcript for " + str(st.session_state.video_id)+"```")
        pass

    if st.session_state.workflow_completed:
        with bottom():
            download_form_container(notes=st.session_state.notes,mindmap=mindmap_data)
    