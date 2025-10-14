#1.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

c = Cachorro()
g = Gato()

print(c.falar())  # Saída: Au au!
print(g.falar())  # Saída: Miau!
