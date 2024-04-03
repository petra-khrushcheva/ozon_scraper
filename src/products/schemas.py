from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated


class ProductsCount(BaseModel):
    products_count: Annotated[int, Field(10, strict=True, gt=0, le=50)]


class ProductRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    price: int
    image_url: str
    discount: str | None = None


class ProductCreate(ProductRead):
    id: int
    slug: str
