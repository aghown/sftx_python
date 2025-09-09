#1 & 2
class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"

    def apresentar(self):
         print(f"Olá, meu nome é {self.nome} e tenho {self.idade}") 

pessoa1 = Pessoa("João", 26)
print(pessoa1)

pessoa1.apresentar()

#3.
class Carro:
    def __init__(self, marca:str, modelo:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano        

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"
    
carro1 = Carro("Chevrolet", "Impala", "1978")
print(carro1)

#5.
class ContaBancaria:
    def __init__(self, titular:str, saldo:int):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.valor = valor
        