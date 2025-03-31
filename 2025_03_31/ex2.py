"""
Faça um programa que receba 
o valor de um depósito e o valor da taxa de juros anual,
calcule e mostre o valor do rendimento 
e o valor total depois do rendimento (após 1 ano);
"""

#entradas
deposito = float(input("Valor do deposito: "))
taxa = float(input("% Taxa de juros anual: "))

#processamentos
rendimento = deposito * taxa/100
total = deposito + rendimento
#saidas
print(f"O rendimento: {rendimento}")
print(f"O valor total após um ano: {total}")