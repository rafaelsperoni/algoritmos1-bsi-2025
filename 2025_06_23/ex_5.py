'''Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''
frase = input("Informe uma frase!")
lista = ["a", "e", "i", "o", "u", " "]

for x in lista:
    print(f" A contagem de {x} = {frase.count(x)}")
