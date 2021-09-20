# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram import Client, filters
from pyrogram.types import *

FayasNoushad = Client(
    "Calculator Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
<b>Hello {}, I am a simple calculator telegram bot. Send me /calculator.

Made by @KOT_BOTS</b>
"""
START_BUTTONS = InlineKeyboardMarkup( [[
        InlineKeyboardButton('📢Updates', url='https://t.me/KOT_BOTS'),
        InlineKeyboardButton('💥Support', url='https://t.me/KOT_REPORS'),
        InlineKeyboardButton('♻️Source', url='https://t.me/KOT_FREE_DE_LA_HOYA_OFF_YT')
        ]]
    )
CALCULATE_TEXT = "Made by @KOT_FREE_DE_LA_HOYA_OFF"
CALCULATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("🄳🄴🄻", callback_data="DEL"),
        InlineKeyboardButton("🄰🄲", callback_data="AC"),
        InlineKeyboardButton("(", callback_data="("),
        InlineKeyboardButton(")", callback_data=")")
        ],[
        InlineKeyboardButton("⑦", callback_data="7"),
        InlineKeyboardButton("⑧", callback_data="8"),
        InlineKeyboardButton("⑨", callback_data="9"),
        InlineKeyboardButton("÷", callback_data="/")
        ],[
        InlineKeyboardButton("④", callback_data="4"),
        InlineKeyboardButton("⑤", callback_data="5"),
        InlineKeyboardButton("⑥", callback_data="6"),
        InlineKeyboardButton("Ⓧ︎", callback_data="*")
        ],[
        InlineKeyboardButton("①", callback_data="1"),
        InlineKeyboardButton("②", callback_data="2"),
        InlineKeyboardButton("③", callback_data="3"),
        InlineKeyboardButton("-", callback_data="-"),
        ],[
        InlineKeyboardButton(".", callback_data="."),
        InlineKeyboardButton("⓪", callback_data="0"),
        InlineKeyboardButton("=", callback_data="="),
        InlineKeyboardButton("+", callback_data="+"),
        ]]
    )

@FayasNoushad.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@FayasNoushad.on_message(filters.private & filters.command(["calc", "calculate", "calculator"]))
async def calculate(bot, update):
    await update.reply_text(
        text=CALCULATE_TEXT,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

@FayasNoushad.on_callback_query()
async def cb_data(bot, update):
        data = update.data
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            message_text = '' if CALCULATE_TEXT in message_text else message_text
            if data == "=":
                text = float(eval(message_text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await update.message.edit_text(
                text=f"{text}\n\n{CALCULATE_TEXT}",
                disable_web_page_preview=True,
                reply_markup=CALCULATE_BUTTONS
            )
        except Exception as error:
            print(error)

@FayasNoushad.on_inline_query()
async def inline(bot, update):
    data = update.query
    data = data.replace(" ", "")
    data = data.replace("×", "*")
    data = data.replace("÷", "*")
    if len(data) == 0:
        try:
            answers = [
                InlineQueryResultArticle(
                    title="Calculator",
                    description=f"New calculator",
                    input_message_content=InputTextMessageContent(
                        text=CALCULATE_TEXT,
                        disable_web_page_preview=True
                    ),
                    reply_markup=CALCULATE_BUTTONS
                )
            ]
            await bot.answer_inline_query(
                inline_query_id=update.chat.id,
                results=answers
            )
        except Exception as error:
            print(error)
    else:
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            text = float(eval(message_text))
            answers = [
                InlineQueryResultArticle(
                    title="Answer",
                    description=f"",
                    input_message_content=InputTextMessageContent(
                        text=f"{data} = {text}",
                        disable_web_page_preview=True
                    )
                )
            ]
            await bot.answer_inline_query(
                inline_query_id=update.chat.id,
                results=answers
            )
        except:
            pass

FayasNoushad.run()
