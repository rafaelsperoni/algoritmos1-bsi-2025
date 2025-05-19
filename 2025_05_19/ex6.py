"""
Criar um algoritmo que imprima todos os números de 1 até 100,
e a soma de todos eles (intervalo fechado)
"""
x = 1
soma = 0
while x<=100:
    print(x)
    soma += x
    x+=1
print(f"A soma: {soma}")