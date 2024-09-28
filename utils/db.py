import json
from typing import List
from .point import Point
from .directions import Directions
import os.path


DB_FILE_NAME = "db.json"


def create_file(file_name):
    with open(file_name, "x") as file:
        pass


def read_db(file_name, fun, *args, **kwargs):
    if not os.path.exists(file_name):
        create_file(file_name)

    with open(file_name, "r") as data:
        data = data.read() or "[]"

        return fun([
            Point.from_dict(obj)
            for obj in json.loads(data)
        ], *args, **kwargs)


def write_db(file_name, data: List[Point]):
    if not os.path.exists(file_name):
        create_file(file_name)

    with open(file_name, "w") as file:
        file.write(json.dumps([
            p.to_dict()
            for p in data
        ]))


def _insert(data: List[Point], new_point: Point) -> List[Point]:
    return data + [new_point]
    

def insert(p: Point):
    data = read_db(DB_FILE_NAME, _insert, p)

    write_db(DB_FILE_NAME, data)

def get_all():
    return read_db(DB_FILE_NAME, lambda data: data)


def search_proximity(point: Point, dir: Directions):
    ...
