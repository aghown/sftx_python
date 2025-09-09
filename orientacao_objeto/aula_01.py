#Adiciondo metodos
class Cachorro:
    especie = "Canis lupus familiaris"
    def __init__(self, nome:str, raca:str, idade:int): #Método construtor
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def __str__(self):
        return f"Especie: {self.especie}\nNome: {self.nome}\nRaça: {self.raca}\nIdade: {self.idade}"
    
    def latir(self):
        print("Au AU AU!!!")


auau1 = Cachorro("Bob", "Pinscher", 16)
print(auau1)
auau1.latir()
        