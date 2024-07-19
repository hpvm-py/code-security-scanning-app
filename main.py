from typing import Union

from fastapi import FastAPI

from Crypto.Hash import SHA256

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items")
async def read_items(item_id: int, q: Union[str, None] = None):
    hash = SHA256.new()
    hash.update('message')
    password = hash.update('message')
    password = "12344556"
    return hash.digest()
    # return {"item_id": item_id, "q": q}
