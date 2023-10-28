#(©) @RknDeveloper

from pyrogram.types import Message
from pyrogram import filters, Client, errors
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from RknDeveloper.untils.database import all_users, all_groups, users, remove_user
from configs import rkn1
import random, asyncio
import os


@Client.on_message(filters.command("broadcast") & filters.user(rkn1.ADMIN))
async def bcast(_, m : Message):
    allusers = users
    rknz = await m.reply_text("`🥀 Bʀᴏᴀᴅᴄᴀꜱᴛ Sᴛᴀʀᴛᴇᴅ...!`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "broadcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "broadcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await rknz.edit(f"✅Sᴜᴄᴄᴇssғᴜʟʟ Tᴏ `{success}` Usᴇʀs.\n❌ Fᴀɪʟᴅ Tᴏ `{failed}` Usᴇʀs.\n👾 Fᴏᴜɴᴅ `{blocked}` Bʟᴏᴄᴋᴇᴅ Usᴇʀs \n👻 Fᴏᴜɴᴅ `{deactivated}` Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ Usᴇʀs.")



@Client.on_message(filters.command("fd_broadcast") & filters.user(rkn1.ADMIN))
async def fcast(_, m : Message):
    allusers = users
    rknz = await m.reply_text("`🥀 Bʀᴏᴀᴅᴄᴀꜱᴛ Sᴛᴀʀᴛᴇᴅ...!`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fd_broadcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fd_broadcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await rknz.edit(f"✅Sᴜᴄᴄᴇssғᴜʟʟ Tᴏ `{success}` Usᴇʀs.\n❌ Fᴀɪʟᴅ Tᴏ `{failed}` Usᴇʀs.\n👾 Fᴏᴜɴᴅ `{blocked}` Bʟᴏᴄᴋᴇᴅ Usᴇʀs \n👻 Fᴏᴜɴᴅ `{deactivated}` Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ Usᴇʀs.")

