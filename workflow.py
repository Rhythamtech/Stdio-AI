from main import * 
import streamlit as st
from pytube import YouTube
from prompts import NOTES_INSTRUCTION, MINDMAP_INSTRUCTION
from llm import stream_chat,non_stream_chat
import streamlit.components.v1 as components



def markmap(data):
    data = str(data)

    markdown_style = '''
        <style>
            svg {
            
                width: 100%;
                height: 100vh;
            }
        </style>'''

    markdown_html = f'''
         {markdown_style}
        <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader@latest"></script>
        <div class='markmap'>
---
markmap:
    maxWidth: 300
---
{data}
        </div>
    '''
    #print(f"Markdown: \n{markdown_html}")
    components.html(markdown_html)
 
    
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
                chunk_data = f" {f'-**Title of YouTube** {video_title}' if index==0 else ''}\n- **({chunk_seq})** \nTranscript-{chunk_text}"
                st.write_stream(stream_chat(NOTES_INSTRUCTION, chunk_data))
        return ''
    else:
        st.toast(f"Unable to fetch transcript for {st.session_state.video_id}")
        return None

def mindmap_workflow():    
    mindmap_text  = non_stream_chat(MINDMAP_INSTRUCTION, st.session_state.notes)
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
    markmap(mindmap_text)
    st.session_state["workflow_completed"] = True
    return mindmap_text
    
