import os
from dotenv import load_dotenv

load_dotenv("config.env")

#API
API_ID = int(os.getenv("API_ID", 209235))
API_HASH = os.getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")

#Req
DELAY = int(os.getenv("DELAY", 15))
WAKTU = int(os.getenv("WAKTU", 100))
MESSAGE_LINK = os.getenv("MESSAGE_LINK", None)

#STRING
STRING = os.getenv("STRING", None)
