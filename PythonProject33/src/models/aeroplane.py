from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Aeroplane:
    callsign: str
    country_of_origin: str
    velocity: float
    altitude: float
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    on_ground: Optional[bool] = None
    squawk: Optional[str] = None

    def __post_init__(self):
        self.callsign = self._validate_callsign(self.callsign)
        self.country_of_origin = self._validate_country(self.country_of_origin)
        self.velocity = self._validate_number(self.velocity, "velocity")
        self.altitude = self._validate_number(self.altitude, "altitude")

    @staticmethod
    def _validate_callsign(value):
        if not isinstance(value, str):
            raise TypeError("callsign должен быть строкой")
        return value.strip()

    @staticmethod
    def _validate_country(value):
        if not isinstance(value, str):
            raise TypeError("country_of_origin должен быть строкой")
        return value.strip()

    @staticmethod
    def _validate_number(value, field_name):
        if value is None:
            raise ValueError(f"{field_name} не может быть None")
        try:
            return float(value)
        except (TypeError, ValueError):
            raise TypeError(f"{field_name} должен быть числом")

    def __lt__(self, other):
        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.altitude < other.altitude

    def __gt__(self, other):
        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.velocity > other.velocity

    @classmethod
    def cast_to_object_list(cls, states: list) -> List["Aeroplane"]:
        result = []
        for state in states:
            try:
                aeroplane = cls(
                    callsign=state[1] or "",
                    country_of_origin=state[2] or "",
                    velocity=state[9] or 0.0,
                    altitude=state[13] or 0.0,
                    longitude=state[5],
                    latitude=state[6],
                    on_ground=state[8],
                    squawk=state[14],
                )
                result.append(aeroplane)
            except Exception:
                continue
        return result

    def to_dict(self):
        return {
            "callsign": self.callsign,
            "country_of_origin": self.country_of_origin,
            "velocity": self.velocity,
            "altitude": self.altitude,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "on_ground": self.on_ground,
            "squawk": self.squawk,
        }
