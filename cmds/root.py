from cq_notify.user import cq_create_token, cq_register_user, query_line_id
from os import getenv
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    TextMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    URIAction
)
from linebot.models.events import MessageEvent
from linebot.models.sources import SourceUser

from pics.handler import (
    get_pics,
    pics_resp
)
from sticky_note.handler import (
    add_rem,remove_rem,list_rem
)
import logging , traceback
from farm.handler import register_farm

ADMIN = getenv("HISUKURIFU", "")

class FeizaoRoot():
    methods = []
    line_bot_api:LineBotApi = None

    def cmd_吃藥(self,event:MessageEvent,cmdline:str):
        try:
                self.line_bot_api.leave_group(event.source.group_id)
        except AttributeError:
            pass
        try:
            self.line_bot_api.leave_room(event.source.room_id)
        except AttributeError:
            pass
    def cmd_幫我記(self,event:MessageEvent,cmdline:str):
        add_rem(cmdline)
        self.line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text="賀歐")
        )

    def cmd_我忘了啥(self,event:MessageEvent,cmdline:str):
        self.line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=list_rem())
        )

    def cmd_忘了(self,event:MessageEvent,cmdline:str):
        remove_rem(int(cmdline))
        self.line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text="賀歐")
        )
    def cmd_註冊農場(self,event:MessageEvent,cmdline:str):
        register_farm(event.source.user_id, cmdline)

        self.line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text="ok惹~~")
        )

    def cmd_發錢(self,event:MessageEvent,cmdline:str):
        self.line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text="您收到了紅包訊息！",
                template=ButtonsTemplate(
                    type="buttons",
                    thumbnail_image_url="https://i.imgur.com/X2Ty7qW.png",
                    title='LINE Pay紅包',
                    text='肥皂發了數個紅包到聊天室。先搶先贏，立即打開紅包！',
                    actions=[
                        URIAction(
                            label='查看紅包狀態',
                            uri='https://www.youtube.com/watch?v=072tU1tamd0'
                        )
                    ]
                )
            )
        )
    def cmd_克魯生成(self,event:MessageEvent,cmdline:str):
        logging.warning(f"src {event.source} try to generate token")
        
        if (event.source.user_id != ADMIN):
            self.line_bot_api.reply_message(
                event.reply_token,
                TextMessage(text="だが断る")
            )
        else:
            self.line_bot_api.reply_message(
                event.reply_token,
                TextMessage(text=cq_create_token())
            )
    def cmd_克魯註冊(self,event:MessageEvent,cmdline:str):
        try:
            user_token = cmdline
            logging.info(f"receive cq register token {user_token}")
            line_id = query_line_id(user_token)
            if line_id != "NULL":
                self.line_bot_api.reply_message(
                    event.reply_token,
                    TextMessage(text="だが断る")
                )
                return
            
            cq_register_user(user_token, event.source.user_id)
            self.line_bot_api.reply_message(
                event.reply_token,
                TextMessage(text="done ~~ please check your client ~~ OuO")
            )
        except Exception as e:
            self.line_bot_api.reply_message(
                event.reply_token,
                TextMessage(text="だが 断る")
            )
            raise e
    def __init__(self , line_bot_api:LineBotApi):
        self.line_bot_api = line_bot_api
        for func in dir(self):
            if func[:4] == "cmd_":
                self.methods.append(func)
                logging.info(f"command {func} successfully register")
                
    def parse(self,event,cmdline:str):
        findcmd = False
        for i in range(1,5):
            if f"cmd_{cmdline[:i]}" in self.methods:
                try:
                    getattr(self,f"cmd_{cmdline[:i]}")(event,cmdline[i:])
                    findcmd = True
                except Exception as e:
                    logging.error(traceback.format_exc())
                break
        if not findcmd:
            self.line_bot_api.reply_message(
                reply_token = event.reply_token,
                messages = pics_resp(get_pics("exception"))
            )
            