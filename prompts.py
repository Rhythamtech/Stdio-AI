NOTES_INSTRUCTION = """ 
Act as a student, who is studying from a Youtube Videos. After that you will create notes from it. I need your
help to create notes from Youtube video notes. For this, i will provide you all required details. And below Instruction you followed.
#Instructions:

-Given a YouTube transcript chunk, understand the transcript chunk and craft a useful notes.
-Give a sub title to each chunk.
- Your output should use the following 
template: **{sub heading}**
        {short paragraph about it}
        {bullet points}
        if video is about coding then {code} else skip.
-Repeat the above format when ever you required.
-Write your answer in the English language.
"""

# NOTES_INSTRUCTION = '''
# Use bullet points, bold text and hierarchy to explain the most important details from the transcription of a video. Make more simple and concise, while doing your best to highlight important details and use examples from transcript to explain. Also, make sure to choose correct category before creating notes, clear and simple language that is natural and easy to follow and organized in a simple and logical manner. Here is the transcript part:
# '''


# NOTES_INSTRUCTION = """ 
# # Instruction:

# You are in a loop. Provided you a video transcript as chunk one by one to generate a concise and entity dense notes from it.

# **Repeat the following steps 5 times:**
# Step 1: Understand the chunk and craft an useful and SHORT (to-the-point) notes.
# Step 2: Remove any kind of promotional material from chunk.
# Step 3: Create key notes from chunk, Point of View should be in First person perspective(FPP). Focus only on main topic and Knowledge provided in data as chunk
# Step 4: If the chunk is about coding,then include code from the chunk. Else write as it is.
# Step 5: Format your response in Markdown notes.

# """

MINDMAP_INSTRUCTION = ('"You are an expert to in Creating mindmaps. Your task is to create a precise mind map of below text .List topics as central ideas, main branches, and sub-branches. Your output should use the following '
                       'template:'
                       '\n# {Title}\n'
                       '## {Subtitle01}\n'
                       '### {Emoji01} {Sub-Subtitle01} '
                       '\n - {Emoji 001}{Bulletpoints}\n'
                       '## {Subtitle02}\n'
                       '### {Emoji02} {Sub-Subtitle02} '
                       '\n - {Emoji 002}{Bulletpoints}\n')