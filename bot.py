
from pyrogram import Client
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
import random, asyncio
import os, sys
from config import rkn


app = Client(
    "approver",
    api_id=rkn.API_ID,
    api_hash=rkn.API_HASH,
    bot_token=rkn.BOT_TOKEN
)

print("RknDeveloper Bot Is Live ✨")
app.run()
