import os
import psycopg2
import logging
DATABASE_URL = os.getenv("DATABASE_URL" , "error")
conn:psycopg2.extensions.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True
cursor:psycopg2.extensions.cursor = conn.cursor()
logging.basicConfig(level=logging.DEBUG)

def init():
    global conn
    global cursor
    
    cmd = '''
    CREATE TABLE IF NOT EXISTS sticky_note(
        id SERIAL PRIMARY KEY,
        ctx TEXT
    );
    CREATE TABLE IF NOT EXISTS farm_users(
        farm_token TEXT PRIMARY KEY,
        user_line_id TEXT
    );
    '''
    cursor.execute(cmd)
