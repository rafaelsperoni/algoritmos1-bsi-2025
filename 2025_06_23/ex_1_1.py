'''Faça um programa que leia o nome do usuário e mostre o nome de trás para frente, utilizando somente letras maiúsculas. 
Exemplo: Nome = Lidiane
Resultado gerado pelo programa: ENAIDIL'''

nome = input("Informe seu nome: ")
nome = nome.upper()
invertido = nome[::-1]
print(invertido)