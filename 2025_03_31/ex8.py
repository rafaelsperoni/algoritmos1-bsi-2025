preco_kg = 45.00
peso = float(input("Informe o peso em Kg: "))
tara = float(input("Informe o peso do prato (tara): "))

peso_liq = peso - tara

valor = peso_liq * preco_kg

print(f"Peso líquido: {peso_liq}. \nO valor a ser pago: R$ {valor:.2f}")