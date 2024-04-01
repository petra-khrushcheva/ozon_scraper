from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import get_session
from src.products import services

# from src.products.dependencies import ...
from src.products.schemas import Product, ProductsCount
from src import scraper

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", status_code=status.HTTP_200_OK)
async def start_scraping(
    input: ProductsCount,
    session: AsyncSession = Depends(get_session),
):
    """
    POST /v1/products/: Запуск задачи на парсинг N товаров. Количество товаров
    должно приниматься в теле запроса в параметре products_count, по умолчанию
    10 (если значение не было передано), максимум 50.
    """
    return await scraper.start_scraping()


@router.get("/", response_model=List[Product])
async def get_products(session: AsyncSession = Depends(get_session)):
    """
    • GET /v1/products/: Получение списка товаров.
    """
    return await services.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: UUID, session: AsyncSession = Depends(get_session)
):
    """
    • GET /v1/products/{product_id}/: Получение товара по айди.
    """
    return await services.get_product(session=session)
