from fastapi import APIRouter
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

@router.post("/")
def add_event(event: EventForm):
    t = time.time()

    e = Event(event.lon, event.lat, event.kind, t)
    db.insert(e)
