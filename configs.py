from os import path, getenv
import os

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:rkndeveloperDEhdhyjjvjjftSEW")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "RknDeveloper")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1001819787652"))
    ADMIN = list(map(int, getenv("ADMIN").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/e846f9375e9d4f4975ce4.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","")
    
rkn1 = Config()
