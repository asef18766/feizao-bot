import logging
from linebot.models.messages import TextMessage
from database import cursor
from linebot import LineBotApi
from pics.handler import pics_resp
import secrets

class CQUserAuthFailure(Exception):
    pass

def query_line_id(user_token:str)->str:
    logging.debug(f"querying line id with token {user_token}")
    cmd = '''
    SELECT user_line_id FROM cq_users WHERE user_token = (%s);
    '''
    cursor.execute(cmd, (user_token,))
    return cursor.fetchall()[0][0]

def cq_user_auth(user_token:str):
    line_id = query_line_id(user_token)
    if line_id:
        return line_id
    raise CQUserAuthFailure()

def send_user_notify(line_id:str, pic_url:str, line_bot_api:LineBotApi):
    line_bot_api.push_message(line_id, pics_resp(pic_url))
    line_bot_api.push_message(line_id, TextMessage(text="your cq is in danger...OAO"))

def cq_create_token()->str:
    user_token = secrets.token_bytes(8).hex()
    cmd = '''
    INSERT INTO cq_users (user_token, user_line_id) VALUES (%s, %s);
    '''
    cursor.execute(cmd, (user_token, "NULL",))
    return user_token

def cq_register_user(user_token:str, line_id:str):
    cmd = '''
    UPDATE cq_users
    SET
    user_line_id = (%s)
    WHERE
    user_token = (%s);
    '''
    cursor.execute(cmd, (line_id, user_token,))
