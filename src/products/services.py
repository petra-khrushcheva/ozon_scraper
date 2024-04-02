from uuid import UUID

from sqlalchemy import desc, select
from sqlalchemy.orm import joinedload
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models import (
    Product,
    ProductScrapingAssociation,
    ScrapingEvent,
)


async def get_last_scraping_products(session: AsyncSession):
    last_scraping = (await session.execute(
        select(ScrapingEvent).order_by(desc(ScrapingEvent.id)).limit(1)
    )).scalar_one_or_none()
    if last_scraping is not None:
        stmt = (
            select(
                ProductScrapingAssociation.discount,
                ProductScrapingAssociation.price,
                Product.name,
                Product.description,
                Product.image_url,
            )
            .where(ProductScrapingAssociation.scraping_id == last_scraping.id)
            .options(joinedload(ProductScrapingAssociation.product))
        )
        result: Result = await session.execute(stmt)
        return result.unique().scalars().all()


async def get_product(product_id: UUID, session: AsyncSession):
    result: Result = await session.get(Product, product_id)
    return result.scalar_one_or_none()
