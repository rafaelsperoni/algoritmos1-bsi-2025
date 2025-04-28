"""
Pedro comprou um saco de ração, com peso em quilos.
Ele possui dois gatos, para os quais fornece a 
quantidade de ração em gramas. 
A quantidade diária de ração fornecida para cada gato
é sempre a mesma, para ambos os gatos. 
Faça um programa que receba o peso do saco de ração 
e a quantidade de ração fornecida para cada gato, 
calcule e mostre quanto restará de ração no saco
após 5 dias de consumo.
"""
racao = float(input(f"Quantos kg tem o saco de ração: "))
gato = float(input(f"Quantos gramas de ração para cada gato, por dia: "))
dias = 5

total = dias * gato * 2
sobra = racao*1000 - total

print(f"Em 5 dias, o consumo será de {total}, sobrando {sobra} gramas de ração.")