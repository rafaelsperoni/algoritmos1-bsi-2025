"""
Elabore um algoritmo que leia o nome e o ano de nascimento
 de uma pessoa e mostre qual é a sua idade atual
"""

nome = input("Informe o seu nome: ")
ano = int(input("Informe o anode nascimento: "))

idade = 2025 - ano

print(f"Olá, {nome}, você tem {idade} anos.")