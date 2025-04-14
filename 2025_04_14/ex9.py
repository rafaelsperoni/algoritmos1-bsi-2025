"""
Construa um algoritmo para determinar se o indivíduo está com um peso favorável.
Essa situação é determinada através do IMC (Índice de Massa Corpórea),
que é definida como sendo a relação entre o peso (PESO) e o quadrado da Altura (ALTURA)
do indivíduo. Ou seja,

IMC = PESO / ALTURA^2
"""
peso = float(input("Informe o peso em kg: "))
altura = float(input("Informe a altura, em metros: "))

imc = peso / altura**2

print(f"O IMC calculado é: {imc}")

if imc<20: 
    print("Abaixo do peso")

if imc>=20 and imc<25: 
    print("Peso normal")

if imc>=25 and imc<30: 
    print("Sobrepeso")

if imc>=30 and imc<40: 
    print("Obeso")

if imc>=40: 
    print("Obeso mórbido")