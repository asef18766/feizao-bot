import os
import psycopg2
import logging

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a feizao-bot').read()[:-1]
logging.info(f"db url:{DATABASE_URL}")
conn:psycopg2.extensions.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor:psycopg2.extensions.cursor = conn.cursor()
def init():
    cmd = '''
    CREATE TABLE IF NOT EXISTS sticky_note(
        id serial PRIMARY KEY,
        ctx text
    );
    '''
    cursor.execute(cmd)
    conn.commit()

def query_single_col(table:str , col:str)->list:
    cmd ='''
    SELECT (%s) from (%s); 
    '''
    cursor.execute(cmd , (col,table))
    return cursor.fetchall()