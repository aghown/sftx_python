#classe usuario e cliente
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}")

    def saudacao(self):
        return "Olá, usuário"


class Cliente(Usuario):
    def __init__(self, nome, email, saldo=0):
        super().__init__(nome, email) 
        self.saldo = saldo

    def saudacao(self):
        return "Olá, cliente"


cliente = Cliente("Ana", "ana@email.com", 1500)
print(cliente.nome)          
print(cliente.email)         
print(cliente.saldo)        

cliente.exibir_informacoes()  
print(cliente.saudacao())     


#funcionario e gerente
class Funcionario(Usuario):
    def __init__(self, nome, email, salario=0):
        super().__init__(nome, email)
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, email, salario, setor):
        super().__init__(nome, email, salario)
        self.setor = setor

gerente = Gerente("Carlos", "carlos@email.com", 8000, "Vendas")
print(gerente.nome)       
print(gerente.email)      
print(gerente.salario)    
print(gerente.setor)      

#herança com administrador
class Autenticacao:
    def login(self):
        print("Login realizado com sucesso.")

    def status(self):
        print("Status da Autenticacao")

class Permissao:
    def verificar_permissao(self):
        print("Permissão verificada.")

    def status(self):
        print("Status da Permissao")

class Administrador(Autenticacao, Permissao):
    pass

admin = Administrador()
admin.login()                 
admin.verificar_permissao()   

admin.status()

print(Administrador.__mro__)
