from os import getenv

imgur_cfg = {
    "id":getenv("IMGUR_ID"),
    "secret":getenv("IMGUR_SECRET"),
    "access_token":getenv("IMGUR_ACCESS_TOKEN"),
    "refresh_token":getenv("IMGUR_REFRESH_TOKEN")
}