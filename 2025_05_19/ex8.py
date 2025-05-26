"""
Criar um algoritmo que leia dez números inteiros e imprima
o maior e o menor número
"""
x = 1
maior = 0
menor = 0

while x<=10:
    num = int(input("Informe número: "))
    if x==1:
        maior = num
        menor = num
    else:
        if num>maior:
            maior = num
        if num<menor:
            menor = num
    x +=1

print(f"O maior: {maior}")
print(f"O menor: {menor}")