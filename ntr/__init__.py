from os import getenv
import logging
NTR_TOKEN = getenv("NTR_TOKEN", "test_token")
if NTR_TOKEN == "test_token":
    logging.warning("current is using testing NTR_TOKEN, please change it to prevent being NTR!!")