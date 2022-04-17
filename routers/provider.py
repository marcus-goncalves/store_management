from fastapi import APIRouter, Depends, status
from entities.provider import Provider
from utils import oauth

router = APIRouter(
    prefix="/provider",
    tags=["provider"],
    dependencies=[Depends(oauth.authentication)],
    responses={
        201: {"description": "Created"},
        400: {"description": "Invalid body"}
    }
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_provider(provider: Provider):
    print(provider)
    return provider
