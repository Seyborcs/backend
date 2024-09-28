from dataclasses import dataclass
import json
import dataclasses

@dataclass
class Event:
    lon: float
    lat: float
    kind: str
    t: float


class EventEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)

        return super().default(o)


DURATION = {
    "warning": 30 
}
