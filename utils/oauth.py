import secrets
from dotenv import dotenv_values
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

authentication = HTTPBasic()
env = dotenv_values('./.env')


def authenticate(credentials: HTTPBasicCredentials = Depends(authentication)) -> str:
    username = secrets.compare_digest(
        credentials.username, env['HTTP_LOGIN'])
    pwd = secrets.compare_digest(credentials.password, env['HTTP_PWD'])
    if not (username and pwd):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return credentials.username
