import re
import time

import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.alert_message import send_alert
from src.products import (
    Product,
    ProductScrapingAssociation,
    ScrapingEvent,
    schemas,
)

URL = "https://www.ozon.ru/seller/1/products/"


def get_page_data(url) -> str:
    with uc.Chrome() as driver:
        driver.get(url)
        time.sleep(6)
        return driver.page_source


def parse_page_data(products_count: int) -> list[schemas.ProductCreate]:
    products = []
    page_number = 1
    html = get_page_data(url=f"{URL}?page={page_number}")
    soup = BeautifulSoup(html, "lxml")
    product_cards = soup.find_all("div", class_="wi3")
    while len(products) < products_count:
        for product in product_cards:
            if len(products) < products_count:
                products.append(
                    schemas.ProductCreate(
                        id=product.find(
                            "a", class_=re.compile("^xi3 tile-hover-target")
                        )
                        .get("href")
                        .split("/")[2]
                        .split("-")[-1],
                        name=re.sub(
                            " +",
                            " ",
                            product.find("span", class_="tsBody500Medium")
                            .get_text()
                            .replace("\n", ""),
                        ),
                        price="".join(
                            (
                                product.find(
                                    "span",
                                    class_=(
                                        "c300-a1 tsHeadline500Medium c300-c0"
                                    ),
                                ).get_text()[:-2]
                            ).split()
                        ),
                        image_url=product.find("img", class_="ix1 b900-a").get(
                            "src"
                        ),
                        discount=product.find(
                            "span",
                            class_=(
                                "tsBodyControl400Small c300-a2 c300-a7 c300-b1"
                            ),
                        )
                        .get_text()
                        .strip()[1:-1],
                        slug=product.find(
                            "a", class_=re.compile("^xi3 tile-hover-target")
                        )
                        .get("href")
                        .split("/")[2],
                    )
                )
        page_number += 1
    return products


async def save_products_to_db(
    products: list[schemas.ProductCreate],
    products_count: int,
    session: AsyncSession,
):
    new_scraping = ScrapingEvent(products_count=products_count)
    session.add(new_scraping)
    for product_card in products:
        product = await session.get(Product, product_card.id)
        if not product:
            product = Product(
                **{
                    key: value
                    for key, value in product_card.model_dump().items()
                    if key in Product.__mapper__.column_attrs.keys()
                }
            )
        product_scraped = ProductScrapingAssociation(
            product=product,
            scraping=new_scraping,
            price=product_card.price,
            discount=product_card.discount,
        )
        session.add_all([product, product_scraped])
    await session.commit()


async def start_scraping(session: AsyncSession, products_count: int = 10):
    products = parse_page_data(products_count=products_count)
    await save_products_to_db(
        products=products, products_count=products_count, session=session
    )
    await send_alert(products_count=products_count)
