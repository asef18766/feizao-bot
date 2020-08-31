import json
import random
from linebot.models import (
    ImageSendMessage
)
def get_pics(types:str)->str:
    with open("pics/list.json" , "r") as fp:
        urls = json.loads(fp.read())[types]
        return random.choice(urls)

def pics_resp(url:str)->ImageSendMessage:
    return ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    )