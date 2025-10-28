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

#8.
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Valor invalido. Digite um número inteiro.")
else:
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
finally:
    print("Fim do programa")

#9. 
class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Salndo insuficientr par realizar o saque."):
        super().__init__(mensagem)

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError 
    return saldo - valor
    
try:
    saldo_atual = float(input("Digite seu saldo atual: "))
    valor_saque = float(input("Digit o valor que deseja sacar: "))
    novo_saldo = sacar(saldo_atual, valor_saque)
except SaldoInsuficienteError as e:
     print(f"Erro: {e}")
except ValueError:
    print("Erro: Digite valores numéricos válidos.")
else:
    print("Saque realizado")
finally:
    print("Fim do programa") 
