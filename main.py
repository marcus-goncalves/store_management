from fastapi import FastAPI
from utils import oauth
from routers import product, provider

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
app.include_router(product.router)