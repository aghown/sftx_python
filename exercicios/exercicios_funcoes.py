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

#8.
def calculadora():
    operacao = input("Qual operação deseja fazer? soma, subtração, multiplicação ou divisão? ")

    if operacao == "soma":
        x = float(input("Digite o rimeiro numero: "))
        y = float(input("Digite o segundo numero: "))
        soma = x + y
        print("Resultado da soma: ",soma)

    elif operacao == "subtração":
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        sub = x - y
        print("Resultado da subtração: ",sub)

    elif operacao == "divisão":
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        div = x / y
        print("Resultado da divisão: ",div)

    elif operacao == "multiplicação":
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        mult = x * y
        print("Resultado da multiplicação: ",mult)

calculadora()

def aplicar_operacao(a, b, operacao):
    return operacao(a, b)

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

resultado1 = aplicar_operacao(3, 4, soma)
print("Soma:", resultado1)

resultado2 = aplicar_operacao(3, 4, multiplicacao)
print("Multiplicação:", resultado2)
