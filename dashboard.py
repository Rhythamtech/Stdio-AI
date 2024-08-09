import time
from main import * 
from utils import *
from pytube import YouTube
import streamlit as st
from streamlit_extras.row import row 
from streamlit_extras.stylable_container import stylable_container

st.markdown("""
            <style>
            div[data-testid="collapsedControl"]{
                display: none;
            }
            
         img {
             border-radius: 12px;
             width: 100%;
             margin-top: 4px;
             }
             
             div[data-testid="stVerticalBlockBorderWrapper"]{
                     border-radius: 1rem;
             }
             
             button[aria-label="Close"]{
                    padding-bottom: 10%;
             }         
            </style>
            """,unsafe_allow_html=True)


if "video_id" not in st.session_state:
    st.session_state["video_id"] = ""

def proceed_button_click():
    st.session_state.current_page = 'video_processing_page'
        
def  button_click():
    st.toast("Button Clicked")

def hide_dailog_form():
    st.html("""
            <style>
            div[data-testid="stForm"] {
                display: none;
                padding: 0px;
            } 
            div[data-testid="element-container"] > button {
                display: none;
            }
            </style>
            """)    
    
@st.experimental_dialog(" ")
def popup_dialog():
    with st.form("video_url_form",border=False):
        video_url = st.text_input("Paste your Youtube Video URL:",placeholder="https://www.youtube.com/watch?v=dQw4w9 ")    
        submitted = st.form_submit_button("Submit",use_container_width= True)
    
    if submitted:
        if video_url == "":
            st.error("Please enter a valid URL or Missing URL")
        else:
            video_id = get_youtube_video_id(video_url)
            if video_id == None:
                st.warning("'Oops! 🫣 I think you forgot to enter a valid YouTube URL. Please try again.")
            else:
                with st.spinner("Please wait while we process your video."):
                    current_page('video_processing_page')
                    st.session_state.video_id = video_id
                    st.rerun()
                    
top_title =st.columns([2.5,6,10],vertical_alignment="center")       
if top_title[0].button("👋Logout"):
    remove_authentication_data()
    st.rerun()

top_title[1].markdown("### **My Notes & Mindmaps**")
st.write("Stop!! watching long video tutorials  and start creating notes using AI")

#Overview
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
  width: 33.2%;
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
    margin-bottom: 7px;
  }
}

/* Style the counter cards */
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  padding: 10px;
  border: 1px solid;
  border-radius: 8px;
}

.fa {font-size:50px;}
</style>

<div class="row">
  <div class="column">
    <div class="card">
    <p>Videos</p>
      <h3>110</h3>
    </div>
  </div>

  <div class="column">
    <div class="card">
    <p>Notes Downloads</p>
      <h3>55</h3>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
    <p>Mindmap Downloads</p>
      <h3>10</h3>
    </div>
  </div>
  
</div>

        """)

total_no_of_data = 15
total_no_of_rows = int(total_no_of_data/4) 
top_row = row([4,7,2.3],vertical_align='center')


# with top_row.container():
#     with stylable_container(
#         key="container_with_border",
#         css_styles=r"""
#             button {
#                 height: 150px;
#                 border-color: #00ffff00;
#             }
#             """,
#     ):
#          if st.button(" **[+] Create new notes**",type="primary",use_container_width=True):
#             popup_dialog()

with top_row.container():
    st.markdown("##### Previous Notes & Mindmaps")   
top_row.empty()

if top_row.button("Create new notes",type="primary",use_container_width=True):
    popup_dialog()

            


# Shimmer effect
st.html("""
        <style>
        article{
	width: 100%;
	position: relative;
	padding: 20px;
	box-sizing: border-box;
}

article .line{
	width: 100%;
	height: 20px;
	background: #dce7c8;
	margin: 20px 0;
	border-radius: 5px;
}

article .shimmer{
	position: absolute;
	top: 0;
	left: 0;
	width: 50%;
	height: 100%;

	background: linear-gradient(100deg,
	rgba(255,255,255,0) 20%,
	rgba(255,255,255,0.5) 50%,
	rgba(255,255,255,0) 80%);

	animation: shimmer 2s infinite linear;
}

@keyframes shimmer{
	from {
		transform: translateX(-200%);
	}
	to{
		transform: translateX(200%);
	}
}

        </style>
        <div>
		<article>
			<div class="line"></div>
			<div class="line"></div>
			<div class="line"></div>
			<div class="line"></div>
			<div class="line"></div>
			<div class="shimmer"></div>
		</article>
	</div>


        """)
# with st.spinner("Please wait while we fetch your previous notes and mindmaps."):     
#     cols = st.columns(4)
#     rows = st.columns(4)*total_no_of_rows
#     grid =[cell for cell in cols+rows]
#     if total_no_of_data == 0:
#         st.write(" :grey[```No Data Found```]")
#     else:
#         for i in range(total_no_of_data):
#             with grid[i].container(border=True):
#                 st.image("https://img.youtube.com/vi/CUUP-fUmA3A/mqdefault.jpg", use_column_width=True)
#                 title_col = st.columns([8,2])
#                 title_col[0].markdown(f"##### {YouTube("https://www.youtube.com/watch?v=" + str(st.session_state.video_id)).title}")
#                 with title_col[1]:
#                     st.button("✏️",key=f"jsms{i}")    
#                 st.markdown(":grey[Write YouTube Video Notes :blue[With AI]]")