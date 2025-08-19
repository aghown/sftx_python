'''LISTAS'''

frutas = ["limão", "banana", "morango", "coco"]

### Adicionando elementos

frutas.insert(1, "maçã")
#print(frutas)

### Adiciona ao final da lista
frutas.append("kiwi")
#print(frutas)

### Adiciona mais elementos utilizando outra lista
frutas_vermelhas = ["cereja", "morango", "framboesa", "amora", "uva"]
frutas+=frutas_vermelhas
#print(frutas)

### Remover elementos
print("Removendo elementos")
print(frutas.count("morango"))
frutas.remove("morango")
print(frutas)

print("Primeiro Pop")
frutas.pop()
print(frutas)

print("Segundo Pop")
frutas.pop(1)
print(frutas)

del frutas[5]
print(frutas)

### Copia de Listas
print("----------"*10)
frutas2 = frutas[:]
frutas2 = frutas.copy()
print(frutas2)
print(id(frutas))
print(id(frutas2))

print("----------"*10)
frutas.sort()
print("Ordem alfabetica")
print(frutas)
