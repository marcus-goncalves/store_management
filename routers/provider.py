from fastapi import APIRouter, Depends, status
from models.provider import Provider, PaginatedProviders
from utils import oauth
from typing import List

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
             status_code=status.HTTP_201_CREATED,
             response_model_include={"provider_name"}
             )
async def create_provider(provider: Provider) -> Provider:
    ...


@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=PaginatedProviders
            )
async def read_providers(
        page_size: int = 10,
        page: int = 1) -> PaginatedProviders:
    ...


@router.put("/{provider_name}",
            status_code=status.HTTP_202_ACCEPTED,
            response_model=Provider
            )
async def update_provider(provider_name: str, provider: Provider) -> Provider:
    return {"provider_changed": provider_name, "new_provider": provider}


@router.delete("/{provider_name}",
               status_code=status.HTTP_200_OK,
               response_model_include={"provider_name"}
               )
async def delete_provider(provider_name: str):
    return {"provider": provider_name}
