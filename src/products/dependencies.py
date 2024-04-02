from fastapi import HTTPException, status

from src.products import services


async def get_product_by_id(product_id, session):
    product = await services.get_product(
        product_id=product_id, session=session
    )
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no product with id {product_id}",
    )


async def get_last_scraping_products(session):
    products = await services.get_last_scraping_products(session=session)
    if products is not None:
        return products
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="There was no scraping yet",
    )
