#(©) @RknDeveloper ✨


from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums
from pyrogram.errors import UserNotParticipant
from database import add_user, add_group
from configs import rkn1
import random, asyncio
import os



#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.command("start"))
async def op(bot, m :Message):
    try:
        await bot.get_chat_member(rkn1.UPDATECHANNEL_ID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("─※ ·Hᴇʟᴘ· ※─", callback_data = "help")
                    ],[
                InlineKeyboardButton("𖣘 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url="https://t.me/RknDeveloper"),
                InlineKeyboardButton("⚘ Sᴜᴘᴘᴏʀᴛ ⚘", url="https://t.me/RknDeveloperSupport")
                ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url="https://t.me/Rkn_Auto-Request-Approve-bot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url="https://t.me/Rkn_Auto-Request-Approve-bot?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]])            
    
            add_user(m.from_user.id)
            await m.reply_photo(photo=rkn1.RKN_PIC, caption="**🦊 Hᴇʟʟᴏ {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @RknDeveloper__**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
            
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ 💁‍♂️", url="https://t.me/Rkn_Auto-Request-Approve-bot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 Hello {}!\n**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🥀 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🥀", url=f"https://t.me/RknDeveloper")],[
                    InlineKeyboardButton("𖤍 Tʀʏ Aɢᴀɪɴ ༗", "rkndeveloper")
                ]
            ]
        )
        await m.reply_text("**rknDeveloper.**".format(rkn1.UPDATE_CHANNEL), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
