from fastapi import APIRouter

router = APIRouter()

@router.get("/aaa")
def print1():
    return {"a": "a"}

@router.get("/bbb")
def print2():
    return {"b": "b"}
