preco = float(input("Informe o preço do litro: "))
valor = float(input("Informe qual o valor em R$ que deseja abastecer: "))

litros = valor/preco

print(f"Abasteceu {litros:.2f} litros")