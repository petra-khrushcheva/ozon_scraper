from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.bot.router import router
from src.core import settings

bot = Bot(
    token=settings.bot_token.get_secret_value(), parse_mode=ParseMode.HTML
)

dp = Dispatcher()
dp.include_router(router)
