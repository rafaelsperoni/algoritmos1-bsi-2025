'''Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string. Exemplo:

    String 1: TTAC

Resultado: 
T:  2x
A: 1x
C: 1x
'''
frase = input("Informe uma frase!").upper()

for x in frase:
    print(x)
    if(frase.count(x)!= 0):
        print(f" A contagem de {x} = {frase.count(x)}")
        frase = frase.replace(x, "")