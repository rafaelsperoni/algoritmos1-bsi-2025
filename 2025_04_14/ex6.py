"""
Faça um programa que leia três valores inteiros fornecidos 
pelo usuário e exiba o maior e o menor dos valores lidos. 
Supor que não sejam iguais.
"""

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a>b and a>c:
    print(f"a é o maior: {a}")

if b>a and b>c:
    print(f"b é o maior: {b}")

if c>a and c>b:
    print(f"c é o maior: {c}")

if a<b and a<c:
    print(f"a é o menor: {a}")

if b<a and b<c:
    print(f"b é o menor: {b}")

if c<a and c<b:
    print(f"c é o menor: {c}")