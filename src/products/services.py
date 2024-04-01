from uuid import UUID

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models import Product
from src.products.schemas import Product, ProductsCount


async def get_products(session: AsyncSession):
    pass


async def get_product(product_id: UUID, session: AsyncSession):
    pass
