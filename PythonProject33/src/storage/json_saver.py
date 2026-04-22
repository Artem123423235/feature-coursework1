import json
import os
from src.storage.abstract_storage import AbstractStorage
from src.models.aeroplane import Aeroplane


class JSONSaver(AbstractStorage):
    def __init__(self, filename: str = "aeroplanes.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def _load(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def _save(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_aeroplane(self, aeroplane):
        data = self._load()
        if isinstance(aeroplane, Aeroplane):
            data.append(aeroplane.to_dict())
        elif isinstance(aeroplane, dict):
            data.append(aeroplane)
        else:
            raise TypeError("Допустимы только Aeroplane или dict")
        self._save(data)

    def get_aeroplanes(self, **filters):
        data = self._load()
        result = data
        for key, value in filters.items():
            result = [item for item in result if str(item.get(key, "")).lower() == str(value).lower()]
        return result

    def delete_aeroplane(self, aeroplane):
        data = self._load()
        target = aeroplane.to_dict() if isinstance(aeroplane, Aeroplane) else aeroplane
        data = [item for item in data if item != target]
        self._save(data)
