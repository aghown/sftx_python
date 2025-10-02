#1 Dobro dos números (map + lambda)

lista = [1, 2, 3, 4, 5]
print(list(map(lambda num:num * 2, lista)))

#2 Filtrar pares (filter + lambda)
lista = [10, 15, 20, 25, 30]
print(list(filter(lambda num:num % 2 == 0, lista)))

#3 Soma dos números (reduce + lambda)
from functools import reduce

lista = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, lista))

#4 Ordenação por comprimento da palavra (sorted + lambda)
palavras = ["uva", "banana", "maçã", "laranja"]
ordenadas = sorted(palavras, key=lambda x:len(x))
print(ordenadas)

#5 Primeira letra maiúscula (map + lambda)
nome = ["ana", "pedro", "maria"]
print(list(map(lambda nome:nome.capitalize(), nome)))

#6 Produto dos números (reduce + lambda)
lista = [2, 3, 4, 5]
print(reduce(lambda x, y: x * y, lista))

#7 Ordenar por último caractere (sorted + lambda)
palavras = ["banana", "uva", "maçã", "laranja"]
ordenadas = sorted(palavras, key=lambda x: x[-1])
print(ordenadas)
