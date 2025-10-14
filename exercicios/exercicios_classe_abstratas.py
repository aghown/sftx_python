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

#2
#a = Animal()

#TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'falar'
#Você não pode instanciar uma classe abstrata diretamente se ela tiver métodos abstratos não implementados.
#É preciso primeiro criar uma subclasse que implemente todos os métodos abstratos.

#3

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


r = Retangulo(5, 3)
print("Área:", r.area())        
print("Perímetro:", r.perimetro()) 

#4
from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

"""class Carro(Transporte):
    def mover(self):
        return "Carro em movimento"

TypeError: Can't instantiate abstract class Carro without an implementation for abstract method 'parar'
carro = Carro()"""

#Correção
class Carro(Transporte):
    def mover(self):
        return "Carro em movimento"

    def parar(self):
        return "Carro parado"

carro = Carro()
print(carro.mover())  # Saída: Carro em movimento
print(carro.parar())  # Saída: Carro parado
