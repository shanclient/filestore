#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about": 
        await query.message.edit_text(
            text = f"<b>🧑🏻‍💻 Bot Creator :</b> <a href='https://t.me/Ruban9124'> Ruban </a>\n Want to earn money 500 per day using bot🤑 \n Contact @Ruban9124",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(" 😊 Contact  ", url="https://t.me/Ruban9124")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
