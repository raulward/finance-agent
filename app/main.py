from fastapi import FastAPI
from app.api.v1.stock import stock_router

app = FastAPI()

app.include_router(stock_router)

@app.get("/")
def root_site():
    return {"message": "ok"}
