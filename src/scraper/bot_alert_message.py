from aiogram import Bot

from src.core import settings


async def send_alert(products_count: int):
    """
    Оповещение в телеграм о завершении парсинга,
    запущеного через POST v1/products/.
    """
    bot = Bot(token=settings.bot_token.get_secret_value())
    await bot.send_message(
        chat_id=settings.chat_id,
        text=(
            "Задача на парсинг товаров с сайта Ozon завершена. "
            f"Сохранено: {products_count} товаров"
        ),
    )
