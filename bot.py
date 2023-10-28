#(©) @RknDeveloper

from configs import rkn1
from pyrogram import Client 

app = Client(
    "approver",
    api_id=rkn1.API_ID,
    api_hash=rkn1.API_HASH,
    bot_token=rkn1.BOT_TOKEN,
    plugins=dict(root='RknDeveloper')
)


print("Rkn_Auto-Request-Approve-bot ✅✅ BOT started successfully ✅✅")
app.run()
