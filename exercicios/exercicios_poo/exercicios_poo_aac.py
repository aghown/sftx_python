#1
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def ler_livro(self, livro):
        print(f"{self.nome} está lendo '{livro.titulo}'.")

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

pessoa = Pessoa("Maria")
livro = Livro("O Pequeno Príncipe")
pessoa.ler_livro(livro)
