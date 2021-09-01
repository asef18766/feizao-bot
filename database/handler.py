import logging
from . import conn, cursor

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
    CREATE TABLE IF NOT EXISTS maple_pt(
        id serial PRIMARY KEY,
        pt int,
        record_date DATE NOT NULL DEFAULT CURRENT_DATE,
    );
    CREATE TABLE IF NOT EXISTS auth_role(
        user_line_id TEXT,
        role TEXT
    );
    '''
    cursor.execute(cmd)
