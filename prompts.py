NOTES_INSTRUCTION = """ 
#Instructions:
-You are an expert in understanding the YouTube Transcript Chunks.
-Given a YouTube transcript chunk and Youtube Video title as topic reference, understand the transcript chunk and craft a useful notes.
-Give a sub title to each chunk.
-Format your response in Markdown. Split paragraphs with more than two sentences into multiple chunks separated by a newline, and use bullet points to improve clarity.
-Write your answer in the English language.


"""

MINDMAP_INSTRUCTION = ('"You are an expert to in Creating mindmaps. Your task is to create a precise mind map of below text .List topics as central ideas, main branches, and sub-branches. Your output should use the following '
                       'template:'
                       '\n# {Title}\n'
                       '## {Subtitle01}\n'
                       '### {Emoji01} {Sub-Subtitle01} '
                       '\n - {Emoji 001}{Bulletpoints}\n'
                       '## {Subtitle02}\n'
                       '### {Emoji02} {Sub-Subtitle02} '
                       '\n - {Emoji 002}{Bulletpoints}\n')