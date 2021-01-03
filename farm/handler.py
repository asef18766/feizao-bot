from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import TextMessage
from database.handler import cursor
import logging

DATA_CENTER_TOKEN = "ko_no_data_center_da"
LINE_BOT_CLIENT_TOKEN = "ko_no_linebot_da"

class DataCenterAuthFailure(Exception):
    pass

def data_center_auth(func):
    def wrapper(*args, **kwargs):
        if DATA_CENTER_TOKEN in args:
            return func(*args, **kwargs)
        elif  "data_center_token" in kwargs.keys() and kwargs["data_center_token"] == DATA_CENTER_TOKEN:
            return func(*args, **kwargs)
        raise DataCenterAuthFailure()
    return wrapper

def query_farm_exist(farm_token:str)->bool:
    return True

def register_farm(user_id:str , farm_token:str):
    # post and check if farm exsist
    if not query_farm_exist(farm_token):
        raise Exception("farm not exsist !!")

    # add user info to db
    cmd = '''
    INSERT INTO farm_users (farm_token, user_line_id) VALUES (%s,%s);
    '''
    cursor.execute(cmd,(farm_token,user_id,))

@data_center_auth
def farm_token_to_line_id(data_center_token:str ,farm_token:str)->str:
    cmd = '''
    SELECT user_line_id FROM farm_users WHERE farm_token = (%s);
    '''
    cursor.execute(cmd,(farm_token,))
    return cursor.fetchall()[0][0]

@data_center_auth
def farm_notify_receiver_handler(data_center_token:str , farm_token:str , msg:str , bot_api:LineBotApi):
   user_id = farm_token_to_line_id(data_center_token ,farm_token)
   logging.info(f"sending msg {msg} to target {user_id}")
   bot_api.push_message(user_id,TextMessage(text=msg))