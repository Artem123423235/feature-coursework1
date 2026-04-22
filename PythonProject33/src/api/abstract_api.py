from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def get_country_coordinates(self, country: str):
        """Получить bounding box страны."""
        raise NotImplementedError

    @abstractmethod
    def get_aeroplanes(self, country: str):
        """Получить данные о самолетах в воздушном пространстве страны."""
        raise NotImplementedError
