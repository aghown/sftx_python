"""
Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.

Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

"Olá, [nome]!"

          Caso o nome não seja informado, mostre "Olá, visitante!".

Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.

Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.

Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:

dados_pessoais(nome="Ana", idade=25, cidade="Recife")
Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.

Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:

 def soma(a, b): return a + b
 aplicar_operacao(3, 4, soma)"""
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

