from fastapi import FastAPI
from app.routers import items

app = FastAPI()
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"Hello": "Safado"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

