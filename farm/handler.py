from linebot import (
    LineBotApi, WebhookHandler
)
from database.handler import cursor
DATA_CENTER_TOKEN = "ko_no_data_center_da"

def data_center_auth(func):
    def wrapper(*args, **kwargs):
        if kwargs["token"] == DATA_CENTER_TOKEN:
            return func(*args, **kwargs)
        raise Exception("data center auth failed")
    return wrapper

def register_farm(user_id:str , farm_token:str):
    pass

@data_center_auth
def farm_token_to_line_id(farm_token:str)->str:
    pass

@data_center_auth
def farm_notify_receiver_handler(farm_token:str , msg:str , bot_api:LineBotApi):
   pass