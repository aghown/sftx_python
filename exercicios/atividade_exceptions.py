#1. 
try: 
    num = int(input("Digite um número: "))

except:
    print("Apenas números inteiros!")

#2.
try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um segundo número: "))
    mult = num1*num2

except ValueError:
    print("Digite apenas números!")

#3.
try:
    num = int(input("Digite um número: "))

except ValueError:
    print("Digite apenas números!")

else:
    print("o número digitado foi", num)

#4.

try:
    f = open("dados.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Algo deu errado")
    finally:
        f.close()
except:
    print("Encerrando o programa")

#5.
def dividir():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    if b == 0:
        raise ZeroDivisionError("O segundo número precisa ser diferente de zero")
    
    print(a/b)

dividir()

#6.
class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade():
    idade = int(input("Digite sua idade: "))
    if idade <= 0:
        raise IdadeInvalidaError("A idade digitada é invalida")
    
    print(idade)

cadastrar_idade()

#7.
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    div = num1/num2

except ZeroDivisionError:
    print("O segundo numero deve ser diferente de zero")

except ValueError:
    print("Só informar números")

