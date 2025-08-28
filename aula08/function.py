def nome_funcao():
    print("definindo função.")
nome_funcao()

##Função com parametro
def ola_funcao(msg):
    print(msg)

ola_funcao("Olá mundo!")


def soma(num1, num2):
    valor_soma = num1+num2
    return valor_soma

valor = soma(2,2)
print(f"a soma retornou: {valor}")
