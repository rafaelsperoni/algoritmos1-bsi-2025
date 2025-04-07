"""
Faça um programa que leia o nome de um aluno e duas notas, 
calcule e mostre a média ponderada dessas notas, 
considerando peso 2 para a primeira nota e peso 3 para a segunda nota.
"""

nome = input("Informe o nome: ")
nota1 = float(input("Informe nota 1: "))
nota2 = float(input("Informe nota 1: "))

media = (nota1 * 2 + nota2 * 3) / 5

print(f"A média ponderada de {nome}: {media}")