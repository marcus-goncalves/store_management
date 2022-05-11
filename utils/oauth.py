import secrets
from dotenv import dotenv_values
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

env = dotenv_values("./.env")
authentication = OAuth2PasswordBearer(tokenUrl="/oauth/me")

router = APIRouter(
    prefix="/oauth",
    tags=["oauth"],
    include_in_schema=False)


@router.post("/me")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    username = secrets.compare_digest(
        form.username, env["HTTP_LOGIN"])
    pwd = secrets.compare_digest(form.password, env["HTTP_PWD"])
    if not (username and pwd):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return {"access_token": env["HTTP_TOKEN"], "token_type": "bearer"}
