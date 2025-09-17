livros = {"Duna", "Hannibal", "O pistleiro", "Duna"}
print(livros)

for livro in livros:
    print(livro)

#Adicionando itens a um conjunto
livros.add("Se houver amanhã")
print(livros)

#Adicionar um grande conjunto de itens
livros_terror = ["Cujo", "IT", "Drácula"]
livros.update(livros_terror)
print(livros)

#Removendo itens remove ou discard
livros = {"Duna", "Hannibal", "O pistleiro"}
livros.remove("Duna")
print(livros)

livros = {"Duna", "Hannibal", "O pistleiro"}
livros.discard("Duna")
print(livros)

