from fastapi import APIRouter, Depends, status
from utils import oauth
from typing import List

from models.product import PaginatedProducts, Product
import controllers.product as controller

router = APIRouter(
    prefix="/products",
    tags=["Produtos"],
    dependencies=[Depends(oauth.authentication)],
    responses={
        200: {"description": "Request OK"},
        201: {"description": "Created"},
        202: {"description": "Update accepted"},
        400: {"description": "Invalid body"},
        401: {"description": "Unauthorized"},
        404: {"description": "Data not found"}
    }
)

@router.post("/",
             name="Cadastrar um produto",
             status_code=status.HTTP_201_CREATED
             )
def create_products(products: List[Product]) -> None:
    controller.insert_products(products)

@router.get("/{product_name}",
            name="Buscar um produto pelo Nome",
            status_code=status.HTTP_200_OK)
def get_product(product_name: str) -> None:
    return status.HTTP_501_NOT_IMPLEMENTED

@router.get("/",
            name="Buscar todos os produtos",
            status_code=status.HTTP_200_OK,
            response_model=PaginatedProducts)
def read_products(page_size: int = 10, page: int = 1) -> PaginatedProducts:
    res = controller.get_all_products()
    return res

@router.put("/{id_product}",
            name="Atualizar um produto pelo Id",
            status_code=status.HTTP_202_ACCEPTED,
            response_model=Product)
def update_product(id_product: str) -> None:
    return status.HTTP_501_NOT_IMPLEMENTED

@router.delete("/{id_product}",
               name="Excluir um produto pelo Id",
               status_code=status.HTTP_200_OK)
def delete_product(id_product: str) -> None:
    return status.HTTP_501_NOT_IMPLEMENTED
