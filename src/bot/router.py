from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hlink

from src.core import async_session
from src.products.services import get_last_scraping_products

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):  # а так тексты переносить вообще можно???
    await message.answer(
        text="Этот бот присылает вам уведомления о завершении парсинга товаров"
        " с сайта Ozon. Вы можете посмотреть результаты последнего парсинга по"
        " команде /Список_товаров"
    )


@router.message(Command("Список_товаров"))
async def product_list_handler(message: Message):
    with async_session() as session:
        products = await get_last_scraping_products(session=session)
    if products is not None:
        text = ""
        number = 1
        for product in products:
            product_link = hlink(
                title=product.name,
                url=f'https://www.ozon.ru/product/{product.slug}'
            )
            line = f"{hbold(number)}. {product_link}\n"
            text += line
            number += 1
        message.answer(text=text)
    message.answer(text="Парсинга еще не было")
