from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import time

from ..utils.directions import Directions
from ..utils.event import Event 
from ..utils.point import Point
from ..utils import db

class EventForm(BaseModel):
    lon: float
    lat: float
    kind: str

router = APIRouter()

@router.get("/")
def return_events(lon: float, lat: float):
    return db.search_proximity(Point.create(lon, lat))

@router.post("/", status_code=201)
def add_event(event: EventForm):
    if event.kind not in db.USER_ADDED and event.kind not in db.MALOPOLSKA_ADDED:
        raise HTTPException(status_code=400, detail="Unknown kind!")
    t = time.time()
    id = len(db.get_all()) + 1

    e = Event(id, event.lon, event.lat, event.kind, t)
    db.insert(e)
