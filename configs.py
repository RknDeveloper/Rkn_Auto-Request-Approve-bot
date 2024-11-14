# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To (https://github.com/JayMahakal98)
# Update Channel @Digital_Botz & @DigitalBotz_Support

"""
Apache License 2.0
Copyright (c) 2022 @RknDeveloper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/RknDeveloper
Repo Link : https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot
License Link : https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot/blob/main/LICENSE
"""

from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:rkndeveloperDEhdhyjjvjjftSEW")
 
    FORCE_SUB = int(getenv("FORCE_SUB", "-1001819787652"))
    ADMIN = list(map(int, getenv("ADMIN", "6151758586").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002120760645"))
    
    # database configs
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/e846f9375e9d4f4975ce4.jpg")
    
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4 https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4 https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4 https://telegra.ph/file/293cc10710e57530404f8.mp4 https://telegra.ph/file/506898de518534ff68ba0.mp4 https://telegra.ph/file/dae0156e5f48573f016da.mp4 https://telegra.ph/file/3e2871e714f435d173b9e.mp4 https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4 https://telegra.ph/file/876edfcec678b64eac480.mp4 https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4 https://telegra.ph/file/b4834b434888de522fa49.mp4").split()

    LOGO = """
╔═╗╔╦╗╔═╦╗  ╔══╗╔═╗╔╗─╔╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╗
║╬║║╔╝║║║║  ╚╗╗║║╦╝║╚╦╝║║╦╝║║─║║║║╬║║╦╝║╬║
║╗╣║╚╗║║║║  ╔╩╝║║╩╗╚╗║╔╝║╩╗║╚╗║║║║╔╝║╩╗║╗╣
╚╩╝╚╩╝╚╩═╝  ╚══╝╚═╝─╚═╝─╚═╝╚═╝╚═╝╚╝─╚═╝╚╩╝
──────────  ──────────────────────────────"""

rkn1 = Config()


# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
