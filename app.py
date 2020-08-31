from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

line_bot_api = LineBotApi('9w6xDK60z7Y5pJ7PoeTGCbFPEKuKONA2tq4kpbB4BApZ8cgbc1+3zzBtK0aV1JpLKkO26A67nkNFhMcv2js6C/pkbpqMJirUesGtpWjMde1stSza08NkTef/8sYIno7IDf8tfAFLt0Uux1uOLSp2QwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e683235c8e38f945d628c6855db7f711')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    logging.debug(f"raw msg:{body}")
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@app.route("/",methods=["GET"])
def main_page():
    logging.info("main page")
    return "meow~"
    

rem_item = []
def add_rem(item:str):
    global rem_item
    rem_item.append(item)

def remove_rem(idx:int):
    rem_item.pop(index=idx)
def list_rem()->str:
    if  len(rem_item) == 0:
        return "沒東西啦 臭ㄐㄐ"
    else:
        s = "剩下這些(OuO):\n"
        for i in range(len(rem_item)):
            s += f"{i}:{rem_item[i]}\n"
        return s

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text)
    logging.info(f"receive message:{msg}")
    
    if msg[:3] == "@肥皂":
        msg = msg[3:]
        if msg == "吃藥":
            line_bot_api.leave_group(event.source.group_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()