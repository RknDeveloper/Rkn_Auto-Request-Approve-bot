from os import path, getenv
import os, time 
from pyrogram.types import BotCommand

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:rkndeveloperDEhdhyjjvjjftSEW")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "RknDeveloper")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1001819787652"))
    ADMIN = list(map(int, getenv("ADMIN", "6151758586").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002120760645"))
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/e846f9375e9d4f4975ce4.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Rkn_AutoRequestApprovebot")
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4 https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4 https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4 https://telegra.ph/file/293cc10710e57530404f8.mp4 https://telegra.ph/file/506898de518534ff68ba0.mp4 https://telegra.ph/file/dae0156e5f48573f016da.mp4 https://telegra.ph/file/3e2871e714f435d173b9e.mp4 https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4 https://telegra.ph/file/876edfcec678b64eac480.mp4 https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4 https://telegra.ph/file/b4834b434888de522fa49.mp4").split()

    LOGO = """
╔═╗╔╦╗╔═╦╗  ╔══╗╔═╗╔╗─╔╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╗
║╬║║╔╝║║║║  ╚╗╗║║╦╝║╚╦╝║║╦╝║║─║║║║╬║║╦╝║╬║
║╗╣║╚╗║║║║  ╔╩╝║║╩╗╚╗║╔╝║╩╗║╚╗║║║║╔╝║╩╗║╗╣
╚╩╝╚╩╝╚╩═╝  ╚══╝╚═╝─╚═╝─╚═╝╚═╝╚═╝╚╝─╚═╝╚╩╝
──────────  ──────────────────────────────"""

rkn1 = Config()


# Commond Automatic Set 📐
#(©) @RknDeveloper Repo - https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot 
# Please Don't Remove Credit 🙏
async def set_commands(app):
    COMMANDS = [
        BotCommand("start", "Used to start the bot."),
        BotCommand("help", "Displays the help command."),
        BotCommand("about", "Displays information about the bot."),
        BotCommand("method", "Sets your preferred method."),
        BotCommand("shortener_api", "Sets the shortener API."),
        BotCommand("mdisk_api", "Sets the mDisk API."),
        BotCommand("header", "Sets the header."),
        BotCommand("footer", "Sets the footer."),
        BotCommand("username", "Sets the username to replace others."),
        BotCommand("banner_image", "Sets the banner image."),
        BotCommand("me", "Displays information about the bot."),
        BotCommand("base_site", "Changes the base site."),
        BotCommand("include_domain", "Sets the included domain."),
        BotCommand("exclude_domain", "Sets the excluded domain."),
        BotCommand("stats", "Displays statistics of the server and bot."),
        BotCommand("batch", "Converts link for multiple posts (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("logs", "Sends the log messages (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("restart", "Restarts or re-deploys the server (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("ban", "Bans users (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("unban", "Unbans users (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("info", "Gets user info (Aᴅᴍɪɴ Oɴʟʏ)."),
    ]

    await app.set_bot_commands(COMMANDS)
