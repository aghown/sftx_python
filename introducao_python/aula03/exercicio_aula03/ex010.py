valor_compra = int(input("Digite o valor da compra: "))
valor_pago = int(input("Digite o valor pago: "))

troco = valor_pago - valor_compra

print(f"Valor da compra R${valor_compra:2}\nValor pago R${valor_pago}\nTroco: R${troco}")
