from itertools import product
from fastapi import HTTPException, status
from typing import List

from models.product import Product, PaginatedProducts, ProductSize
import repositories.product as repo

def insert_product(product: Product) -> None:
    try:
        repo.insert(product.dict())
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"invalid data - {err}")

def get_all_products(page_size: int = 10, page: int = 1) -> PaginatedProducts:
    start: int = (page -1) * page_size
    end: int = start + page_size

    products = repo.read_all()

    pages = round(len(products) / page_size, 0)
    if pages == 0:
        pages = 1

    output = {
        "data": products[start:end],
        "page_size": page_size,
        "page": page,
        "pages": pages
    }

    res = PaginatedProducts(**output)
    return res

def update_product(id: str, new_product: Product) -> Product:
    data = repo.update(id, new_product.dict())
    res = Product(**data)

    return res

def delete_product(id: str) -> None:
    repo.delete(id)