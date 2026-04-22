from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def add_aeroplane(self, aeroplane):
        raise NotImplementedError

    @abstractmethod
    def get_aeroplanes(self, **filters):
        raise NotImplementedError

    @abstractmethod
    def delete_aeroplane(self, aeroplane):
        raise NotImplementedError
