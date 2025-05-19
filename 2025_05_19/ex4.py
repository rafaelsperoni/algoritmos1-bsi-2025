"""
Escreva um algoritmo que leia dez números do usuário e imprima a metade de cada número
"""
x = 1

while x<=10:
    num = int(input("Informe número: "))
    print(f"A metade do valor lido: {num/2}")
    x +=1