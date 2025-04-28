"""
João recebeu seu salário e precisa pagar duas contas atrasadas. 
Em razão do atraso, ele deverá pagar multa de 2% 
sobre cada conta. 
Faça um programa que lê o valor do salário, 
das duas contas e calcule e mostre quanto 
restará do salário de João.
"""

salario = float(input("VAlor do salario: "))
conta1 = float(input("Valor da primeira conta:"))
conta2 = float(input("Valor da segunda conta:"))

saldo = salario - 1.02*conta1 - 1.02*conta2

print(f"O saldo após o pagamento das contas será de R${saldo:.2f}")