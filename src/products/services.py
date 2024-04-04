from uuid import UUID

from sqlalchemy import and_, desc, func, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models import (Product, ProductScrapingAssociation,
                                 ScrapingEvent)


async def get_last_scraping_products(session: AsyncSession):
    """Получение списка товаров последнего парсинга"""
    last_scraping = (
        await session.execute(
            select(ScrapingEvent).order_by(desc(ScrapingEvent.id)).limit(1)
        )
    ).scalar_one_or_none()
    if last_scraping is not None:
        stmt = (
            select(
                ProductScrapingAssociation.discount,
                ProductScrapingAssociation.price,
                Product.name,
                Product.image_url,
                Product.slug,
            )
            .select_from(ProductScrapingAssociation)
            .join(ProductScrapingAssociation.product)
            .where(ProductScrapingAssociation.scraping_id == last_scraping.id)
        )
        result: Result = await session.execute(stmt)
        return result.unique().all()
    return None


async def get_product(product_id: UUID, session: AsyncSession):
    """Получение одного товара и его последней цены"""
    result: Result = await session.get(Product, product_id)
    subq = (
        select(func.max(ProductScrapingAssociation.scraping_id))
        .where(ProductScrapingAssociation.product_id == product_id)
        .scalar_subquery()
    )
    stmt = (
        select(
            ProductScrapingAssociation.discount,
            ProductScrapingAssociation.price,
            Product.name,
            Product.image_url,
            Product.slug,
        )
        .select_from(ProductScrapingAssociation)
        .join(ProductScrapingAssociation.product)
        .where(
            and_(ProductScrapingAssociation.scraping_id == subq),
            ProductScrapingAssociation.product_id == product_id,
        )
    )
    result: Result = await session.execute(stmt)
    return result.one_or_none()
