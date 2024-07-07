import math
import strings
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi




def get_youtube_video_id(url):
    try:
        if "youtube" in url or "youtu.be" in url:
            return YouTube(url).video_id
    except:
        return None

def get_youtube_video_thumbnail(video_id):
    return f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"

def get_video_transcript(vid_id):
    try:
        transcript = YouTubeTranscriptApi.list_transcripts(vid_id)
        translated_transcript = transcript.find_transcript(strings.LANGUAGE_SHORTCODES).translate('en')
        return translated_transcript.fetch()
    except:
        return None
    

# split the transcript in chunks
def get_video_transcript_chunks(transcript, segment_duration=2000):
    segments = []
    current_segment = {'text': '', 'start': 0, 'duration': 0}

    for item in transcript:
        text = item['text']
        start = item['start']
        duration = math.ceil(item['duration'])

        if current_segment['duration'] + duration <= segment_duration:
            current_segment['text'] += text + " "
            current_segment['duration'] += duration
        else:
            segments.append(current_segment)
            current_segment = {'text': text + ' ', 'start': start, 'duration': duration}

    if current_segment['text']:
        segments.append(current_segment)

    return segments


# def create_temp_file(content, filename = 'untitled'):
#     temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.html', prefix=filename, encoding='utf8', delete=False)
#     temp_file.write(content)
#     temp_file.flush()
#     html_file_path = temp_file.name
#     return html_file_path, temp_file

# def create_mindmap_pdf(content):
#     file_path, temp_file = create_temp_file(strings.MINDMAP_HTML_DATA.replace('[MINDMAP_DATA]',content),filename= 'mindmap' )
#     pdf = converter.__get_pdf_from_html(f'file:///{file_path}',timeout=2,install_driver=True,print_options={"landscape":True,"preferCSSPageSize":True})
#     temp_file.close()
#     return pdf

# def create_notes_pdf(content):
#     markdown_html =  markdown.markdown(content)
#     file_path, temp_file = create_temp_file(markdown_html,filename='notes' )
#     #pdf = converter.__get_pdf_from_html(f'file:///{file_path}',timeout=2,install_driver=True,print_options={"potrait":True,"preferCSSPageSize":True})
#     temp_file.close()
#     return ''
