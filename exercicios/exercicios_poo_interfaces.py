from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} com Cartão de Crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} com Boleto.")

cartao = CartaoCredito()
cartao.processar(150.0)

boleto = Boleto()
boleto.processar(300.0)

#2 
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligado.")

    def desligar(self):
        print("Computador desligado.")

pc = Computador()
pc.ligar()
pc.desligar()

#3
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Relatório impresso.")

    def exportar(self):
        print("Relatório exportado em PDF.")

rel = Relatorio()
rel.imprimir()
rel.exportar()

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

# Classe que NÃO implementa todos os métodos (gera erro ao instanciar)
"""class RepositorioMemoriaIncompleto(Repositorio):
    def salvar(self, objeto):
        print("Objeto salvo na memória.")"""

# Tentativa de uso
# repo = RepositorioMemoriaIncompleto()  # Isso causará um erro:
# TypeError: Can't instantiate abstract class RepositorioMemoriaIncompleto with abstract method buscar

# Classe corrigida
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória.")

    def buscar(self, id):
        print(f"Buscando objeto com ID {id} na memória.")
        return {"id": id, "nome": "Objeto Exemplo"}

repo = RepositorioMemoria()
repo.salvar("MeuObjeto")
print(repo.buscar(1))
