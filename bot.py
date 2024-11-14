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

# extra imports
import time, os, logging, logging.config
from aiohttp import web
from datetime import datetime
from pytz import timezone

# pyrogram imports
from pyrogram import Client, __version__
from pyrogram.raw.all import layer

# bots imports
from RknDeveloper.web_support import web_server
from configs import rkn1

# logging print 
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
 

class Bot(Client):
    def __init__(self):
        super().__init__(
            "auto-approver",
            api_id=rkn1.API_ID,
            api_hash=rkn1.API_HASH,
            bot_token=rkn1.BOT_TOKEN,
            plugins=dict(root='RknDeveloper')
             )
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = rkn1.BOT_UPTIME
        
        if rkn1.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()
            bind_address = "0.0.0.0"
            await web.TCPSite(app, bind_address, rkn1.PORT).start()
            
        logging.info(f"{me.first_name} Restarted.....")
        logging.info(rkn1.LOGO)
        
        for id in rkn1.ADMIN:
            try:
                await self.send_message(id, f"**__{me.first_name}  Restarted......__**")
            except: pass
            
        if rkn1.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(rkn1.LOG_CHANNEL, f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Iꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")
                
    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped 🙄")
        
bot = Bot()
bot.run()


# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
