from flask import Flask, request, abort, make_response
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
from farm.handler import (
    DataCenterAuthFailure,
    farm_notify_receiver_handler
)
from ntr.handler import (
    ntr_handler
)
from time import sleep
from os import getenv
import traceback, sys
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

line_bot_api = LineBotApi(getenv("LINE_BOT_API"))
handler = WebhookHandler(getenv("WEBHOOK_HANDLER"))
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
    return "meow~~v1.5"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text)
    logging.info(f"receive message:{msg}")
    if msg[:3] == "@肥皂":
        msg = msg[3:]
        cmd_proc.parse(event,msg)

@app.route("/farm_notify", methods=['POST'])
def data_center_notification():
    data = request.get_json()
    try:
        farm_notify_receiver_handler(data["DATA_CENTER_TOKEN"] ,data["farm_token"], data["msg"], line_bot_api)
    except IndexError:
        return "can not found specify target", 404, {'Content-Type': 'application/json'}
    except DataCenterAuthFailure:
        abort(403)
    return 'OK'

@app.route("/push_ntr", methods=['POST'])
def ntr_msg():
    data = request.get_json()
    if not ntr_handler(data, line_bot_api):
        abort(403)
    return 'OK'

if __name__ == "__main__":
    #farm_notify_receiver_handler('ko_no_data_center_da', TextMessage(text="just a test") , line_bot_api)
    pass