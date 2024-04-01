from aiogram import Bot

from src.core import settings


async def send_alert(bot: Bot, count: int = 10):
    bot.send_message(chat_id=settings.chat_id, text="")
