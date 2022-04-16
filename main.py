import secrets
from fastapi import Depends, FastAPI, HTTPException, Security, status
from utils import oauth

app = FastAPI()


@app.get("/users/me")
def read_current_user(username: str = Depends(oauth.authenticate)) -> dict:
    return {"username": username}
