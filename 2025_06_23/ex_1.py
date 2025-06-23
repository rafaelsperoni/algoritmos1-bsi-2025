'''Faça um programa que leia o nome do usuário e mostre o nome de trás para frente, utilizando somente letras maiúsculas. 
Exemplo: Nome = Lidiane
Resultado gerado pelo programa: ENAIDIL'''

nome = input("Informe seu nome: ")
nome_contrario = ""
nome = nome.upper()
x = len(nome)- 1

while x >= 0:
    print(nome[x])
    nome_contrario = nome_contrario + nome[x]
    x = x - 1

print(nome_contrario)