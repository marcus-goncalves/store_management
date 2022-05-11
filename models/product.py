from enum import Enum
from pydantic import BaseModel, Field, constr
from typing import List, Optional
from datetime import datetime

class ProductSize(str, Enum):
    P: str = "P"
    M: str = "M"
    G: str = "G"
    GG: str = "GG"


class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")
    product_name: constr(max_length=50)
    stock_price: float
    quantity: int = 1
    size: ProductSize | int
    provider_name: constr(max_length=50)
    active: bool | None = True
    created_at: Optional[datetime] = datetime.now()
    updated_at: datetime = datetime.now()

class PaginatedProducts(BaseModel):
    data: List[Product] = None
    page_size: int
    page: int
    pages: int