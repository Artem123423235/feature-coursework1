import requests
from src.api.abstract_api import AbstractAPI


class AeroplanesAPI(AbstractAPI):
    NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    OPENSKY_URL = "https://opensky-network.org/api/states/all"

    def __init__(self, user_agent: str = "aeroplane-app/1.0"):
        self.headers = {"User-Agent": user_agent}

    def get_country_coordinates(self, country: str):
        params = {
            "q": country,
            "format": "json",
            "limit": 1,
            "polygon_geojson": 0,
        }
        response = requests.get(self.NOMINATIM_URL, params=params, headers=self.headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data:
            raise ValueError(f"Страна '{country}' не найдена")

        boundingbox = data[0].get("boundingbox")
        if not boundingbox or len(boundingbox) != 4:
            raise ValueError("Bounding box отсутствует или имеет неверный формат")

        south, north, west, east = map(float, boundingbox)
        return {
            "south": south,
            "north": north,
            "west": west,
            "east": east,
        }

    def get_aeroplanes(self, country: str):
        coords = self.get_country_coordinates(country)
        params = {
            "lamin": coords["south"],
            "lomin": coords["west"],
            "lamax": coords["north"],
            "lomax": coords["east"],
        }
        response = requests.get(self.OPENSKY_URL, params=params, headers=self.headers, timeout=20)
        response.raise_for_status()
        data = response.json()
        return data.get("states", [])
