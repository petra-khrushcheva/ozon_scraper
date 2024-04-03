from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    image_url: Mapped[str]
    slug: Mapped[str] = mapped_column(String(200))


class ScrapingEvent(Base):
    __tablename__ = "scraping_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    products_count: Mapped[int]


class ProductScrapingAssociation(Base):
    __tablename__ = "product_scraping_association"
    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "scraping_id",
            name="unique_product_scraping",
        ),
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )
    scraping_id: Mapped[int] = mapped_column(
        ForeignKey("scraping_events.id", ondelete="CASCADE"), nullable=False
    )
    price: Mapped[int]
    discount: Mapped[str | None]

    product: Mapped["Product"] = relationship()
    scraping: Mapped["ScrapingEvent"] = relationship()
