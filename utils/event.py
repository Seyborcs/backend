from dataclasses import dataclass

@dataclass
class Event:
    lon: float
    lat: float
    kind: str
    t: float

DURATION = {
    "warning": 30 
}