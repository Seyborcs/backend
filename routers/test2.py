from fastapi import APIRouter

router = APIRouter()

@router.get("/ccc")
def print1():
    return {"c": "c"}

@router.get("/ddd")
def print2():
    return {"d": "d"}
