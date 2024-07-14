from main import * 
import streamlit as st
from pytube import YouTube
from prompts import NOTES_INSTRUCTION, MINDMAP_INSTRUCTION
from llm import stream_chat,non_stream_chat
import streamlit.components.v1 as components



def markmap(data):
    st.markdown('''
              <style>
                  [data-testid="stIFrame"]{
                          height: 70vh;
                          border: 1px solid;
                          border-radius: 12px;
                          background-color: #dddddd;
                      }
              </style>
             ''',unsafe_allow_html=True)
    data = str(data)
    
    download_button_html = """
     <style>
      #downloadButton {
        position: absolute;
        right: 20px;
        bottom: 20px;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
      }
    </style>
    <script src="https://raw.githack.com/eKoopmans/html2pdf/master/dist/html2pdf.bundle.js"></script>
    <button id="downloadButton">Download Mindmap</button>
    <script>
      document.getElementById('downloadButton').addEventListener('click', function () {
        var element = document.querySelector('.markmap svg');
        var opt = {
          margin:       0,
          filename:     'markmap.pdf',
          html2canvas:  { scale: 4},  // Increase scale for higher resolution
          jsPDF:        {
                            unit: 'in', format: 'A4',
                            orientation: 'landscape'
                        }
        };

        // Generate the PDF
        html2pdf().set(opt).from(element).save()
      });

    </script>
"""

    mindmap_html = f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Markmap</title>
    <style>
      svg.markmap {{
        width: 100%;
        height: 100vh;
      }}
    </style>
    <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader@0.16"></script>
  </head>
  <body>
    <div class="markmap">
      <script type="text/template">
---
markmap:
    maxWidth: 300
---
{data}
      </script>
    </div>
    {download_button_html}
  </body>
</html>
'''


    #print(f"Markdown: \n{markdown_html}")
    st.caption("Before download, Zoom out the mindmap and fit inside the frame.")
    components.html(mindmap_html)
 
    
def notes_workflow():
    youtube_video_id = st.session_state.video_id
    transcript  =  get_video_transcript(youtube_video_id)
    

    if transcript is not None:
        chunks = get_video_transcript_chunks(transcript)
        
        # Processing each chunk and display response
        total_chunks_count = len(chunks)
        video_title = YouTube("https://www.youtube.com/watch?v=" + str(st.session_state.video_id)).title
        st.session_state.notes = ''

        for index, chunk in enumerate(chunks):
                current_index = index + 1
                chunk_text = chunk['text']
                chunk_seq = f"{current_index}/{total_chunks_count}"
               # chunk_data = f" {f'-**Title of YouTube** {video_title}' if index==0 else ''}\n- **({chunk_seq})** \nTranscript-{chunk_text}"
                chunk_data = f"\n Transcript-{chunk_text}"
                st.write_stream(stream_chat(NOTES_INSTRUCTION, chunk_data))
        return ''
    else:
        st.toast(f"Unable to fetch transcript for {st.session_state.video_id}")
        return None

def mindmap_workflow():    
    mindmap_text  = non_stream_chat(MINDMAP_INSTRUCTION, st.session_state.notes)
    markmap(mindmap_text)
    st.session_state["workflow_completed"] = True
    return mindmap_text
    
