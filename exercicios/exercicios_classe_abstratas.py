from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        print()

    @abstractmethod
    def 