# 1) Crie um dicionário simples
aluno = {"nome": "Hanna", "idade": 23, "nota": 9.5}
print(aluno)

# 2) Acessando valores
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print("Produto:", produto["nome"])
print("Estoque:", produto["estoque"])

# 3) Adicionando novos pares chave-valor
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"
print(pessoa)

# 4) Removendo elementos
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
del carro["ano"]
print(carro)

# 5) Verificando existência de uma chave
contato = {"nome": "Ana", "email": "ana@email.com"}
print("telefone" in contato)  # retorna False
print("email" in contato)     # retorna True

# 6) Contando frequência de palavras
def contar_palavras(lista):
    freq = {}
    for palavra in lista:
        freq[palavra] = freq.get(palavra, 0) + 1
    return freq

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(contar_palavras(palavras))

# 7) Invertendo um dicionário
d = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in d.items()}
print(invertido)

# 8) Dicionário com listas (médias dos alunos)
notas = {
    "João": [7, 8, 9],
    "Maria": [10, 9, 8],
    "Pedro": [6, 7, 8]
}

for aluno, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{aluno} -> média: {media:.2f}")

# 9) Mesclando dois dicionários
def mesclar_dicts(d1, d2):
    return {**d1, **d2}  # o segundo sobrescreve o primeiro

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(mesclar_dicts(d1, d2))

# 10) Ordenando dicionário por valor
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
ordenado = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)
print(ordenado)
