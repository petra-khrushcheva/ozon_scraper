from fastapi import HTTPException, status

from src.products import services


async def get_product_by_id(product_id, session):
    """Получение товара по айди"""
    product = await services.get_product(
        product_id=product_id, session=session
    )
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Продукта с id {product_id} в базе нет.",
    )


async def get_last_scraping_products(session):
    """Получение списка товаров последнего парсинга"""
    products = await services.get_last_scraping_products(session=session)
    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Парсинга еще не было",
        )
    return products
