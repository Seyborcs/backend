from fastapi import APIRouter
from pydantic import BaseModel
import time

from ..utils.directions import Directions
from ..utils.event import Event 

class EventForm(BaseModel):
    lon: float
    lat: float
    kind: str

router = APIRouter()

@router.get("/")
def return_events(prevlon: float, prevlat: float, furlon: float, furlat: float):
    dx = furlon - prevlon
    dy = furlat - prevlat

    if dx == 0:
        if dy > 0:
            direction = Directions.NORTH
        elif dy < 0:
            direction = Directions.SOUTH
        else:
            direction = Directions.NONE
    elif dy == 0:
        if dx > 0:
            direction = Directions.EAST
        else:
            direction = Directions.WEST
    else:
        tan = dy/dx 
        if tan > 0:
            if dx > 0:
                direction = Directions.EAST_NORTH
            else:
                direction = Directions.WEST_SOUTH
        else:
            if dx > 0:
                direction = Directions.EAST_SOUTH
            else:
                direction = Directions.WEST_NORTH

    return {"direction": direction}

@router.post("/")
def addEvent(event: EventForm):
    t = time.time()
    # serializacja
    e = Event(event.lon, event.lat, event.kind, t)
