#(©) @RknDeveloper ✨


from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant
from RknDeveloper.untils.database import add_user, add_group
from configs import rkn1
import random, asyncio
import os



gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]


# Main Process _ _ _ _ _ Users Send Massage 🥀__🥀 Please 😢 Give Credit

@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(bot, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await bot.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await bot.send_video(kk.id,img, "**Hello {}!\nWelcome To {}\n\n__Pᴏᴡᴇʀᴅ Bʏ : @RknDeveloper__**".format(m.from_user.mention, m.chat.title), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url="https://t.me/Rkn_Auto_acceptsjoinrequestsbot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url="https://t.me/Rkn_AutoRequestApprovebot?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]])            )
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    

# Start Massage _____ # Please 😢 Give Credit 

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
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url="https://t.me/Rkn_AutoRequestApprovebot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url="https://t.me/Rkn_AutoRequestApprovebot?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]])            
    
            add_user(m.from_user.id)
            await m.reply_photo(photo=rkn1.RKN_PIC, caption="**🦊 Hᴇʟʟᴏ {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @RknDeveloper__**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
            
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Pʀɪᴠᴀᴛᴇ", url="https://t.me/Rkn_AutoRequestApprovebot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**❣️ Hᴇʟʟᴏ {}!\n\nWʀɪᴛᴇ Mᴇ Pʀɪᴠᴀᴛᴇ Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs.**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🥀 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🥀", url=f"https://t.me/RknDeveloper")],[
                    InlineKeyboardButton("𖤍 Tʀʏ Aɢᴀɪɴ ༗", "rkn_developer")
                ]
            ]
        )
        await m.reply_text("**💞 Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ!. Iғ Yᴏᴜ Jᴏɪɴᴇᴅ Cʟɪᴄᴋ Tʀʏ Aɢᴀɪɴ Bᴜᴛᴛᴏɴ Tᴏ Cᴏɴғɪʀᴍ. 🥀**".format(rkn1.UPDATE_CHANNEL), reply_markup=key)

