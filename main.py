from ast import If
from fastapi import FastAPI
from helpers import router as helper

app = FastAPI()

app.include_router(helper.router)
