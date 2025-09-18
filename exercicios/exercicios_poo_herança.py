class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"nome = {self.nome} email = {self.email}")

    def saudacao(self):
        print(f"Olá, usúario: {self.nome}!")
    
class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
      
cliente01 = Cliente("Jigsaw", "Jig@saw.ripmail.com")

print(cliente01)
cliente01.saudacao()
cliente01.exibir_informacoes()
