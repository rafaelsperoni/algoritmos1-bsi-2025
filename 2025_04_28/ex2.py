"""
Faça um programa que receba o ano de nascimento de uma pessoa, calcule e mostre:
Se ele já tem idade para votar (16 anos ou mais);
E para conseguir carteira de habilitação (18 anos ou mais);
"""
anonasc = int(input("Informe o ano de nascimento: "))
idade = 2025-anonasc

print(f"Idade: {idade}")

if idade>=16:
    print("Tem idade para votar")

if idade>=18:
    print("Tem idade para tirar CNH") 
else:
    print("Não tem idade para tirar CNH")   