'''Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas. 
Exemplo: Nome = RAFAEL
Resultado gerado pelo programa: 
R
RA
RAF
RAFA
RAFAE
RAFAEL '''

nome = input("Informe seu nome: ")
nome = nome.upper()
tam = len(nome) #tamanho da string
for i in range(0, tam+1, 1):
    print(nome[0:i:1])