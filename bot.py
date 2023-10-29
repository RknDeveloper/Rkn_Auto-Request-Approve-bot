#(©) @RknDeveloper

import logging
import logging.config
from aiohttp import web
from configs import rkn1
from pyrogram import Client
from RknDeveloper.web_support import web_server

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
 

class Bot(Client):

    def __init__(self):
        super().__init__(
            "approver",
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
       app = web.AppRunner(await web_server())
       await app.setup()
       bind_address = "0.0.0.0"
       await web.TCPSite(app, bind_address, rkn1.PORT).start()
       logging.info(f"{me.first_name} ✅✅ BOT started successfully ✅✅")

       for id in rkn1.ADMIN:
            try:
                await self.send_message(id, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
            except:
                pass

    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped 🙄")
        
bot = Bot()
bot.run()
