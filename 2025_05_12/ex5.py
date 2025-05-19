"""
Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina). 
Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o 
preço do litro da gasolina é R$ 6,79 o preço do litro do álcool é R$ 4,49.
O posto está vendendo combustíveis com a seguinte tabela de descontos:

Alcool - até 20 litros, desconto de 3% por litro no valor
acima de 20 litros, desconto de 5% por litro no valor

Gasolina - até 20 litros, desconto de 4% por litro no valor
acima de 20 litros, desconto de 6% por litro no valor
"""
#Entradas
# tipo de combustivel, litros, preco do litro
valor_pago = 0.0

litros = float(input("Quantos litros: "))  #convertendo para float

tipo = input("Tipo de combustível (G/A): ") #textual

gasolina = 6.79
alcool = 4.49
#Processamentos
# transformar as entradas em saídas (atribuições e operações - condicional)

if tipo=="G":
    parcial = litros * gasolina
    if litros<=20:
        desconto = parcial * 4 / 100
    else:
        desconto = parcial * 6 / 100
else:
    parcial = litros * alcool
    if litros<=20:
       desconto = parcial * 3 / 100
    else:
       desconto = parcial * 5 / 100

valor_pago = parcial - desconto

#Saidas
# valor a ser pago
print(f"O valor a ser pago é R$ {valor_pago:.2f}")