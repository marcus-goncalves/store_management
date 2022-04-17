from fastapi import APIRouter, Depends, status
from entities.provider import Provider
from utils import oauth

router = APIRouter(
    prefix="/provider",
    tags=["Providers"],
    dependencies=[Depends(oauth.authentication)],
    responses={
        201: {"description": "Created"},
        400: {"description": "Invalid body"},
        401: {"description": "Unauthorized"}
    }
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_provider(provider: Provider):
    return provider


@router.get("/{company_name}", status_code=status.HTTP_200_OK)
async def get_provider(company_name: str) -> dict:
    return {"company_test": company_name}


@router.put("/{company_name}", status_code=status.HTTP_202_ACCEPTED)
async def update_provider(company_name: str, provider: Provider) -> dict:
    return {"company_changed": company_name, "new_provider": provider}


@router.delete("/{company_name}", status_code=status.HTTP_200_OK)
async def delete_provider(company_name: str):
    return {"company": company_name}
