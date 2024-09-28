class Point:
    def __init__(self, lon, lat):
        self.lon = float(lon)
        self.lat = float(lat)

        if not self.validate():
            print("warn: invalid point")

    def validate(self):
        return self.long >= -180 and self.long <= 180 and self.lat >= -90 and self.lat <= 90


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

