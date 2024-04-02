from aiogram import Bot

from src.bot import bot
from src.core import settings


async def send_alert(products_count: int, bot: Bot = bot):
    bot.send_message(
        chat_id=settings.chat_id,
        text=("Задача на парсинг товаров с сайта Ozon завершена. "
              f"Сохранено: {products_count} товаров")
    )
