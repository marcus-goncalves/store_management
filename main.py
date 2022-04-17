from fastapi import Depends, FastAPI
from utils import oauth, db
from routers import provider

app = FastAPI()
app.include_router(oauth.router)
app.include_router(provider.router)


@app.get("/users")
def read_current_user(check: str = Depends(oauth.authentication)) -> dict:
    with db.DBConnection() as conn:
        test = conn.test
        print(test)
    return {"message": "success!"}
