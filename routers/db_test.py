from fastapi import APIRouter
from ..utils import db
from ..utils.point import Point

router = APIRouter()

@router.get("/all")
def get_all():
    return db.get_all()

@router.post("/insert")
def add_point(lon: str, lat: str):
    db.insert(Point.create(lon, lat))
    return {}

@router.get("/search_proximity")
def search_proximity(lon: str, lat: str, dir: str):
    return db.search_proximity(Point.create(lon, lat), int(dir))
