from typing_extensions import Annotated

from pydantic import BaseModel, ConfigDict, Field


class ProductsCount(BaseModel):
    products_count: Annotated[int, Field(10, strict=True, gt=0, le=50)]


class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    price: float
    description: str
    image_url: str
    discount: str | None = None
