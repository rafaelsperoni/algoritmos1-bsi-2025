'''Faça um programa que solicite o nome do usuário e imprima-o na vertical.
Exemplo: Nome = Lidiane
Resultado gerado pelo programa: 
L
I
D
I
A
N
E
'''

nome = input("Informe seu nome: ")
nome = nome.upper()
x = 0

while x < len(nome):
    print(nome[x])
    x = x + 1

