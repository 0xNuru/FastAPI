from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

fake_items_db = [{"item_name": "foo"}, {
    "item_name": "bar"}, {"item_name": "baz"}]


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# using Predefined values in path
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):

    if model_name is model_name.alexnet:
        return {"model_name": model_name, "message": "Who even knows what alexnet is?"}
    if model_name is model_name.lenet:
        return {"model_name": model_name, "message": "something about lenet"}
    return {"model_name": model_name, "message": "This is just resnet!"}


# Path parameters containing paths
@app.get("/files/{file_path: path}")
async def get_file(file_path: str):
    return {"file_path": file_path}


# Query Parameters
@app.get("/items/")
async def read_item(start: int = 0, limit: int = 10, step: int = 1):
    return fake_items_db[start:limit:step]


# optional query parameters
@app.get("/items/{item_id}")
async def read_item_by_id(item_id, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
