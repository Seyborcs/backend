from math import sqrt
from .event import Event

class Point:
    def __init__(self, lon, lat):
        self.lon = float(lon)
        self.lat = float(lat)

    def add(self, p):
        return Point.create(self.lon + p.lon, self.lat + p.lat)

    def scale(self, v):
        return Point.create(self.lon * v, self.lat * v)

    def dist(self, p):
        return sqrt((self.lon - p.lon)**2 + (self.lat - p.lat)**2)

    def to_dict(self):
        return {
            "lon": self.lon,
            "lat": self.lat
        }

    @staticmethod
    def from_dict(obj):
        return Point(
            obj["lon"],
            obj["lat"]
        )

    @staticmethod
    def create(lon, lat):
        return Point(
            lon,
            lat
        )

    @staticmethod
    def from_event(event: Event):
        return Point(
            event.lon,
            event.lat
        )

