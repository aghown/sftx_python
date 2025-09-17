"""try:
    num1 = int(input(""))
    num2 = int(input(""))
    div = num1/num2

except ZeroDivisionError:
    print("O segundo numero deve ser diferente de zero")

except ValueError:
    print("Só informar números")

except:
    print("Algo deu errado!")

#Caso não haja erros, o else será executado
else:
    print(soma)

#Encerra a conexão, independente se deu erro ou não
finally:
    print("qualquer coisa")

print("depois da divisão")
"""

class erroIdade(Exception):
    pass

try:
    idade = int(input("Informe a sua idade: "))
    if idade <= 0:
        raise ValueError("Idade tem que ser maior que zero") 
    
except TypeError:
    print("Apenas números")

except erroIdade:
    print(erroIdade)
