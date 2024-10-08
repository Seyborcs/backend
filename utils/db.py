import json
from typing import List
from .event import Event, EventEncoder
from .point import Point
from .directions import Directions
import os.path
from time import time


DB_FILE_NAME = "db.json"

USER_ADDED = [
    "road_closed",
    "end_of_the_road",
    "bad_surface",
    "hanging_branches",
    "dangerous_intersection",
    "heavy_traffic",
    "accident",
    "steep_incline"
]

MALOPOLSKA_ADDED = [
    "repair_points",
    "dangerous_place"
]

def create_file(file_name):
    with open(file_name, "x") as file:
        pass


def read_db(file_name, fun, *args, **kwargs):
    if not os.path.exists(file_name):
        create_file(file_name)

    with open(file_name, "r") as data:
        data = data.read() or "[]"

    return fun([
        Event(**obj)
        for obj in json.loads(data)
    ], *args, **kwargs)


def write_db(file_name, data: List[Event]):
    if not os.path.exists(file_name):
        create_file(file_name)

    with open(file_name, "w") as file:
        file.write(json.dumps(data, cls=EventEncoder))


def _insert(data: List[Event], new_point: Event) -> List[Event]:
    return data + [new_point]
    

def insert(event: Event):
    data = read_db(DB_FILE_NAME, _insert, event)

    write_db(DB_FILE_NAME, data)

def get_all():
    return read_db(DB_FILE_NAME, lambda data: data)


def dir_to_point(dir: Directions):
    match Directions(dir):
        case Directions.SOUTH:
            return Point.create(0, -1)
        case Directions.WEST_SOUTH:
            return Point.create(-1, -1)
        case Directions.WEST:
            return Point.create(-1, 0)
        case Directions.WEST_NORTH:
            return Point.create(-1, 1)
        case Directions.NORTH:
            return Point.create(0, 1)
        case Directions.EAST_NORTH:
            return Point.create(1, 1)
        case Directions.EAST:
            return Point.create(1, 0)
        case Directions.EAST_SOUTH:
            return Point.create(1, -1)
        case Directions.NONE:
            return Point.create(0, 0)


def _search_proximity(data: List[Event], point: Point):
    area_radius = 15

    return [
        event
        for event in data
        if Point.from_event(event).dist(point) <= area_radius
    ]

def search_proximity(point: Point):
    return list(filter(_active, read_db(DB_FILE_NAME, _search_proximity, point)))

def _get_duration(kind: str) -> float:
    if kind in USER_ADDED:
        return 86400
    return 9999999999999999

def _active(e: Event) -> bool:
    duration = _get_duration(e.kind)
    now = time()
    return e.t + duration > now

def _distance(x: Point, center: Point) -> float:
    return x.dist(center)

def search_proximity_active(point: Point):
    events = search_proximity(point)
    distance = lambda x: _distance(x, point)
    return events.sort(key=distance)
