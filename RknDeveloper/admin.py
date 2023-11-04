import os, sys
from pyrogram import Client, filters
from RknDeveloper.untils.database import all_users, all_groups
from configs import rkn1
from pyrogram.types import Message


@Client.on_message(filters.command("rknusers") & filters.user(rkn1.ADMIN))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
✨ Cʜᴀᴛs Sᴛᴀᴛs ✨
🙋‍♂️ Tᴏᴛᴀʟ Usᴇʀs : `{xx}`
👥 Tᴏᴛᴀʟ Gʀᴏᴜᴘs : `{x}`
🚧 Tᴏᴛᴀʟ Usᴇʀs & Gʀᴏᴜᴘs : `{tot}` """)

@Client.on_message(filters.command("restart") & filters.user(rkn1.ADMIN))
async def restart_bot(b, m):
    rknz = await m.reply_text("🔄__Rᴇꜱᴛᴀʀᴛɪɴɢ.....__")
    await rknz.edit(f"🐾 Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ Cᴏᴍᴘʟᴇᴛᴇ 🐾")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
