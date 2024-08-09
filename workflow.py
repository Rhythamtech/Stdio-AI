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

        #saveSvgButton {
            position: absolute;
            right: 200px;
            bottom: 20px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js" integrity="sha512-qZvrmS2ekKPF2mSznTQsxqPgnpkI4DNTlrdUmTzrDgektczlKNRRhy5X5AAOnx5S09ydFYWWNSfcEqDTTHgtNA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.2/html2pdf.bundle.min.js" integrity="sha512-MpDFIChbcXl2QgipQrt1VcPHMldRILetapBl5MPCA9Y8r7qvlwx1/Mc9hNTzY+kS5kX6PdoDq41ws1HiVNLdZA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<button id="saveSvgButton">Save as SVG</button>
<button id="downloadButton">Download Mindmap</button>

<script>
   document.getElementById('downloadButton').addEventListener('click', function () {
    var element = document.querySelector('.markmap svg');
    var opt = {
      margin:       0,
      filename:     'markmap.pdf',
      html2canvas:  { scale: 10, useCORS: true },  // Increase scale for higher resolution and allow cross-origin images
      jsPDF:        {
                        unit: 'in',
                        format: 'A4',
                        orientation: 'landscape',
                        compress: true,
                        dpi: 300  // Set DPI for better quality
                    }
    };

    // Apply CSS to enhance text clarity
    element.style.fontSmooth = 'always';
    element.style.webkitFontSmoothing = 'antialiased';
    element.style.mozOsxFontSmoothing = 'grayscale';

    // Generate the PDF
    html2pdf().set(opt).from(element).save();
  });


        document.getElementById('saveSvgButton').addEventListener('click', function () {
            var svgElement = document.querySelector('.markmap svg');

            if (!svgElement) {
                console.error('SVG element not found');
                return;
            }

            var svgData = new XMLSerializer().serializeToString(svgElement);
            var svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
            var svgUrl = URL.createObjectURL(svgBlob);
            var downloadLink = document.createElement('a');
            downloadLink.href = svgUrl;
            downloadLink.download = 'markmap.svg';
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);
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


    #print(f"Markdown: \n{mindmap_html}")
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
    
