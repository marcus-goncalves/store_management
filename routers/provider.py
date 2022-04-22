from fastapi import APIRouter, Depends, status
from utils import oauth

from models.provider import Provider, PaginatedProviders
import controllers.provider as controller

router = APIRouter(
    prefix="/provider",
    tags=["Providers"],
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
             status_code=status.HTTP_201_CREATED
             )
def create_provider(provider: Provider) -> None:
    controller.insert_provider(provider)


@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=PaginatedProviders
            )
async def read_providers(
        page_size: int = 10,
        page: int = 1) -> PaginatedProviders:

    data = controller.get_all_providers(page_size, page)
    return data


@router.put("/{id}",
            status_code=status.HTTP_202_ACCEPTED,
            response_model=Provider
            )
def update_provider(id: str, provider: Provider) -> Provider:
    res = controller.update_provider(id, provider)
    return res


@router.delete("/{id}",
               status_code=status.HTTP_200_OK
               )
def delete_provider(id: str):
    controller.delete_provider(id)
