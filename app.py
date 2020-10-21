from flask import Flask, request, abort
from pics import imgur
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage,
)
import logging
from cmds.root import FeizaoRoot
from database.handler import init

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

line_bot_api = LineBotApi('9w6xDK60z7Y5pJ7PoeTGCbFPEKuKONA2tq4kpbB4BApZ8cgbc1+3zzBtK0aV1JpLKkO26A67nkNFhMcv2js6C/pkbpqMJirUesGtpWjMde1stSza08NkTef/8sYIno7IDf8tfAFLt0Uux1uOLSp2QwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e683235c8e38f945d628c6855db7f711')
cmd_proc = FeizaoRoot(line_bot_api)
init()

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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text)
    logging.info(f"receive message:{msg}")
    if msg[:3] == "@肥皂":
        msg = msg[3:]
        cmd_proc.parse(event,msg)

@app.route("/farm_notify", methods=['POST'])
def data_center_notification():
    pass

if __name__ == "__main__":
    print(imgur.upload("/home/asef18766/下載/5288fd6deca7eb9f1fa3f61fb065c0c2.png"))