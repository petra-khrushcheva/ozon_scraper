from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src import scraper
from src.core import get_session
from src.products import services

from src.products.schemas import Product, ProductsCount

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", status_code=status.HTTP_200_OK)
async def start_scraping(
    input: ProductsCount,
    session: AsyncSession = Depends(get_session),
):
    """
    Запуск задачи на парсинг N товаров. Количество товаров
    принимается в теле запроса в параметре products_count, по умолчанию
    10 (если значение не было передано), максимум 50.
    """
    return await scraper.start_scraping(
        products_count=input.products_count, session=session
    )


@router.get("/", response_model=List[Product])
async def get_products(session: AsyncSession = Depends(get_session)):
    """
    Получение списка товаров последнего парсинга.
    """
    return await services.get_last_scraping_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: int, session: AsyncSession = Depends(get_session)
):
    """
    Получение товара по айди.
    """
    return await services.get_product(product_id=product_id, session=session)
