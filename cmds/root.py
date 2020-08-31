from linebot import (
    LineBotApi, WebhookHandler
)
from pics.handler import (
    get_pics,
    pics_resp
)

class FeizaoRoot():
    methods = []
    line_bot_api:LineBotApi = None

    def cmd_吃藥(self,event,cmdline:str):
        try:
                self.line_bot_api.leave_group(event.source.group_id)
        except AttributeError:
            pass
        try:
            self.line_bot_api.leave_room(event.source.room_id)
        except AttributeError:
            pass

    def __init__(self , line_bot_api:LineBotApi):
        self.line_bot_api = line_bot_api
        for func in dir(self):
            if func[:4] == "cmd_":
                self.methods.append(func)
    
    def parse(self,event,cmdline:str):
        findcmd = False
        for i in range(1,5):
            if f"cmd_{cmdline[:i]}" in self.methods:
                getattr(self,f"cmd_{cmdline[:i]}")(event,cmdline[i:])
                findcmd = True
                break
        if not findcmd:
            self.line_bot_api.reply_message(
                reply_token = event.reply_token,
                messages = pics_resp(get_pics("exception"))
            )
            