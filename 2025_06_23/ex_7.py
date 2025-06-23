'''Escreva um programa que leia duas strings. Verifique se a segunda ocorre na primeira e imprima a posição de início. Exemplo:
String 1: AABBEEEFAATT
String 2: BE
'''
frase = input("Informe uma frase! ").lower()
frase2 = input("Informe a segunda frase! ").lower()

if frase2 in frase:
    print(f"A segunda frase tem inicio na posição {frase.find(frase2)}")
else:
    print("Não foi encontrada")