#1.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)

#2.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("João", 25)
pessoa1.apresentar()

#3.
class Carro:
    def __init__(self, marca:str, modelo:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano        
    
carro1 = Carro("Chevrolet", "Impala", "1967")
carro2 = Carro("Chrysler", "Dodge Charger", "1970")
carro3 = Carro("Chevrolet", "Corvette C1", "1962")

print(carro1.marca, carro1.modelo, carro1.ano)
print(carro2.marca, carro2.modelo, carro2.ano)
print(carro3.marca, carro3.modelo, carro3.ano)

#4. 

carro = Carro("Chevrolet", "Chevelle SS", "1968")

print("Antes:",carro.ano)
carro.ano = 1970
print("Depois:",carro.ano)

#5.Classe ContaBancaria com métodos depositar e sacar
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

conta = ContaBancaria("Lucas", 1000)
conta.depositar(500)
print("Saldo após depósito:", conta.saldo)
conta.sacar(300)
print("Saldo após saque:", conta.saldo)
conta.sacar(1500)

#6. agora sacar retorna True ou False
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

conta = ContaBancaria("Sam", 1000)

if conta.sacar(200):
    print("Saque realizado com sucesso.")
else:
    print("Saque não realizado. Saldo insuficiente")

if conta.sacar(2000):
    print("Saque realizado com sucesso.")
else:
    print("Saque não realizado. Saldo insuficiente.")

#7.8.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

aluno1 = Aluno("Maria", 9.5)
aluno2 = Aluno("João", 7.8)
aluno3 = Aluno("Ana", 8.2)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)


for aluno in turma.alunos:
    print(aluno)

#9.
class Cachorro:
    especie = "Canis familiaris"  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

dog1 = Cachorro("Rex", 5)
dog2 = Cachorro("Luna", 3)

print(dog1.especie)  # Acesso pelo objeto
print(Cachorro.especie)  # Acesso pela classe

print(dog1.nome, dog1.idade)
print(dog2.nome, dog2.idade)

