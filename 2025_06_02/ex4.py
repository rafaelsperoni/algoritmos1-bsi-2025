"""
Faça um algoritmo que imprima os
10 primeiros números primos.
"""
conta_primos = 0 
numero = 2
while conta_primos<10: 
    cont = 0
    for i in range(2, numero):
        if (numero % i ==0):
            cont += 1

    if cont==0:
        conta_primos+=1
        print(f"{numero} é primo {conta_primos}")
    numero +=1