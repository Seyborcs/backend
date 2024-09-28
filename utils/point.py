from math import sqrt

class Point:
    def __init__(self, lon, lat):
        self.lon = float(lon)
        self.lat = float(lat)

        if not self.validate():
            print("warn: invalid point")

    def validate(self):
        return self.lon >= -180 and self.lon <= 180 and self.lat >= -90 and self.lat <= 90

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

