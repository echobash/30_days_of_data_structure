from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

