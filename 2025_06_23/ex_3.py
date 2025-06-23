'''Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e imprima a data com o mês escrito por extenso.
Exemplo: Data = 20/02/1995 
Resultado gerado pelo programa: Você nasceu em 20 de fevereiro de 1995
'''
data = input("Informe sua data de nascimento: ")

lista = data.split('/')

if lista[1] == "01" or lista[1] == "1":
    print(f"Você nasceu em {lista[0]} de janeiro de {lista[2]}")
if lista[1] == "02" or lista[1] == "2":
    print(f"Você nasceu em {lista[0]} de fevereiro de {lista[2]}")
print (lista)