#1.
def saudacao():
    print("Olá, visitante!")

saudacao()

#2.
def dobro(numero):
    return numero * 2

print(dobro(2))

#3.
def soma(num1, num2):
    return num1 + num2

print(soma(10, 20))

#4.
def mensagem(nome=None):
    if not nome:
        print("Olá, visitante!")
    else:
        print(f"Olá, {nome}!")

mensagem("Hanna")
mensagem()

#5.
def operacoes(num1, num2):

    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2

    return soma, subtracao, multiplicacao

resultado = operacoes(10, 5)

print("Soma: ", resultado[0])
print("Subtração: ", resultado[1])
print("Multiplicação: ", resultado[2])

#6.
def media(*numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

print("Média:", media(4, 5, 6))

#7.
def dados_pessoais(**info):
    for chave, valor in info.items():
        print(f"{chave.capitalize()}: {valor}")

dados_pessoais(nome="Hanna", idade=23, cidade="Recife")

