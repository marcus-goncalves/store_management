from fastapi import Depends, FastAPI
from utils import oauth, db
from routers import provider

app = FastAPI(
    title="Store management",
    version="1.0.0",
    contact={
        "name": "Marcus Gonçalves",
        "email": "nvrrox@gmail.com"
    }
)

app.include_router(oauth.router)
app.include_router(provider.router)
