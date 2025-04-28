"""
Faça um programa que receba o código correspondente
ao cargo de um funcionário e seu salário atual
e mostre o cargo, o valor do aumento e seu novo salário.
Os cargos estão na tabela a seguir:
"""
codigo = int(input("Informe o código do cargo (1 a 5): "))
salario = float(input("Informe o salario: "))

if codigo==1:
    aumento = salario * 0.5

if codigo==2:
    aumento = salario * 0.35

if codigo==3:
    aumento = salario * 0.2

if codigo==4:
    aumento = salario * 0.1

if codigo==5:
    aumento = salario * 0

novo = salario + aumento

print(f"O novo salário é de R${novo:.2f}")