#Criando lista de livros:
livros = ["Carmilla", "A revolução dos bichos", "A Metamorfose"]
print(livros)

#Primeiro e Ultimo livro:
print("O primeiro livro da lista é: ",livros[0])
print("O ultimo livro da lista é: ",livros[-1])

#Adicionando mais dois livros a lista:
livros.append("Drácula")
livros.append("A biblioteca da meia noite")
print("Lista de livros atualizada: ",livros)

#Adicionando Duna a lista:
livros.insert(1, "Duna")
print("lista de livros atualizada: ",livros)

#Removendo livro
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")
print(livros)

#Quantas vezes o numero aparece:
numeros = [1, 2, 3, 2, 4, 5]
print("O número 2 aparece",numeros.count(2),"vezes!")

#Percorrer a lista de livros:
for livro in livros:
    print(f"O livro {livro} é interessante")

#Maior de 18:
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
        print(idade)

#Calculando a soma:
valores = [0, 20, 30, 40]
soma = 0
for v in valores:
    soma += v
print("A soma dos valores é:",soma)

#Calculando a media de cada aluno:
notas = []

for i in range(2):  # dois alunos
    aluno = []
    print(f"\nDigite as notas do aluno {i+1}:")
    for j in range(3):  # três notas
        nota = float(input(f"Nota {j+1}: "))
        aluno.append(nota)
    notas.append(aluno)

print("\nNotas:", notas)

for i, aluno in enumerate(notas):
    media = sum(aluno) / len(aluno)
    print(f"Média do aluno {i+1}: {media:.1f}")

#Criando tabuleiro de Xadrez: 
