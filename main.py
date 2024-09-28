from typing import Union

from fastapi import FastAPI

from .routers import test1, test2, db_test

app = FastAPI()

app.include_router(
    test1.router,
    prefix="/test1"
)

app.include_router(
    test2.router,
    prefix="/test2"
)

app.include_router(
    db_test.router,
    prefix="/db_test"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
