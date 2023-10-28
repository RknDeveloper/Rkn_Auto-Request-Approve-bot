from configs import rkn1
from pyrogram import Client, filters
from RknDeveloper.untils.database import add_user
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_callback_query(filters.regex("rkn_developer"))
async def chk(bot, cb : CallbackQuery):
    try:
        await bot.get_chat_member(kn1.UPDATECHANNEL_ID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("─※ ·Hᴇʟᴘ· ※─", callback_data = "help")
                    ],[
                InlineKeyboardButton("𖣘 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url="https://t.me/RknDeveloper"),
                InlineKeyboardButton("⚘ Sᴜᴘᴘᴏʀᴛ ⚘", url="https://t.me/RknDeveloperSupport")
                ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url="https://t.me/Rkn_Auto_acceptsjoinrequestsbot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url="https://t.me/Rkn_Auto_acceptsjoinrequestsbot?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]])            
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 Hᴇʟʟᴏ {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @RknDeveloper__**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
            
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️🙅‍♂️")
