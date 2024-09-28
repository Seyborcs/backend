from typing import Union

from fastapi import FastAPI

from .routers import db_test, events, trivia

app = FastAPI()

app.include_router(
    db_test.router,
    prefix="/db_test"
)

app.include_router(
    events.router,
    prefix="/events"
)

app.include_router(
    trivia.router,
    prefix="/trivia"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
