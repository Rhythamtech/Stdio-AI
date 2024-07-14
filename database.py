import os
import sqlitecloud
from dotenv import load_dotenv

load_dotenv()

db_name = "stdioai_db"
connection_str = f"sqlitecloud://cj0892jlsk.sqlite.cloud:8860?apikey={os.environ.get("SQLITE_API_KEY")}"

def save_data(video_id,mindmap_data,notes):
    conn = sqlitecloud.connect(connection_str)
    conn.execute(f"USE DATABASE {db_name}") 
    
    sql = '''
        INSERT INTO STDIO_GENERATED_VIDEO_DATA (video_id, markmap_text, video_notes)
        VALUES (?,?,?);
    '''
    
    cur =  conn.cursor()
    cur.execute(sql,(video_id,mindmap_data,notes))

    conn.close()
    return "data inserted"

def fetch_notes(video_id):
    conn = sqlitecloud.connect(connection_str)
    conn.execute(f"USE DATABASE {db_name}") 
    
    sql = f'''
        SELECT video_notes,markmap_text FROM "STDIO_GENERATED_VIDEO_DATA"
        WHERE video_id = '{video_id}';
    '''
    cur =  conn.execute(sql)
    data  = cur.fetchall()
    conn.close()
    
    if data == []:
        return None
    else:
        return data
    
    
     


def fetch_all_notes():
    conn = sqlitecloud.connect(connection_str)
    conn.execute(f"USE DATABASE {db_name}") 
    
    sql = '''
    SELECT id,video_id,markmap_text,video_notes FROM "STDIO_GENERATED_VIDEO_DATA"
    '''
    cur =  conn.execute(sql)
    result  = cur.fetchall()
    conn.close()
    return result



    
    
    

