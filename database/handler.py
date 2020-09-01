import os
import psycopg2
import logging
DATABASE_URL = os.getenv("DATABASE_URL" , "error")
conn:psycopg2.extensions.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True
cursor:psycopg2.extensions.cursor = conn.cursor()
logging.basicConfig(level=logging.DEBUG)

def init():
    logging.info(f"db url:{DATABASE_URL}")
    global conn
    global cursor
    
    cmd = '''
    CREATE TABLE IF NOT EXISTS sticky_note(
        id serial PRIMARY KEY,
        ctx text
    );
    INSERT INTO sticky_note(ctx) VALUES('test string');
    '''
    cursor.execute(cmd)
