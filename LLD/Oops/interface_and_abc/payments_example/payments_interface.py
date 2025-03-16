from abc import ABC, abstractmethod


class PaymentsInterface(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

    def random_not_abstract_method(self):
        print("Python interface can have concrete class methods like this one which is not compulsory to be implemented")

