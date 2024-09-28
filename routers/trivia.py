from fastapi import APIRouter

from random import randint

router = APIRouter()

trivias = [
    {"title": "dupa", "content": "pieprzyć"},
    {"title": "dupa1", "content": "pieprzyć"},
    {"title": "dupa2", "content": "pieprzyć"}
]

@router.get("/")
def getTrivia():
    return trivias[randint(0, len(trivias)-1)]
