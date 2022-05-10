from fastapi import HTTPException, status
from typing import List

from models.product import Product, PaginatedProducts, ProductSize

def insert_products(products: List[Product]) -> None:
    try:
        return status.HTTP_501_NOT_IMPLEMENTED
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"invalid data - {err}")

def get_all_products(page_size: int = 10, page: int = 1) -> PaginatedProducts:
    start: int = (page -1) * page_size
    end: int = start + page_size

    products = [{"product_name": "Mark", "stock_price": 0, "size": ProductSize.P, "provider_name": "uni duni te"}]

    pages = round(len(products) / page_size, 0)
    output = {
        "data": products[start:end],
        "page_size": page_size,
        "page": page,
        "pages": pages
    }

    res = PaginatedProducts(**output)
    return res