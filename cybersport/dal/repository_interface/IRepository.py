from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def insert(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def get(self, entity):
        pass

    @abstractmethod
    def get_all(self, entity):
        pass
