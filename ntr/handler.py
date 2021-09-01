from . import NTR_TOKEN
from linebot import (
    LineBotApi
)
from linebot.models import (
    TextMessage
)
def ntr_handler(data:dict, linebot_api:LineBotApi)->bool:
    if "NTR_TOKEN" in data and data["NTR_TOKEN"] == NTR_TOKEN:
        linebot_api.broadcast(TextMessage(text=data['txt']))
        return True
    
    return False