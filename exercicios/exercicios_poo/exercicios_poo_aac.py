#1.Definição de classe abstrata
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

# Teste
cachorro = Cachorro()
gato = Gato()

print(cachorro.falar())  
print(gato.falar())      

#2. Proibição de instanciamento

animal = Animal()  # Tentativa de instanciar classe abstrata

#3.Múltiplos métodos abstratos

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

ret = Retangulo(5, 3)
print("Área:", ret.area())           
print("Perímetro:", ret.perimetro()) 

#4. Herança parcial

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("O carro está em movimento.")
        
#TypeError: Can't instantiate abstract class Carro with abstract method parar
carro = Carro()  

#correção
class Carro(Transporte):
    def mover(self):
        print("O carro está em movimento.")

    def parar(self):
        print("O carro parou.")

carro = Carro()
carro.mover()  
carro.parar()  
