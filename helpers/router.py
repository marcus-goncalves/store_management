from fastapi import APIRouter


router = APIRouter(
    prefix='/healthcheck',
    tags=['HealthCheck'])


@router.get('')
async def ping() -> str:
    return {"message": "pong"}
