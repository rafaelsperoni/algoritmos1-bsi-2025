"""
Escreva um algoritmo que leia o código de um
determinado produto e mostre a sua classificação.
Utilize a seguinte tabela como referência:
"""
codigo = int(input("Informe o código do produto (1 a 15): "))

if codigo==1:
    classificacao = "Alimento não perecível"

if codigo>1 and codigo<5:
    classificacao = "Alimento perecível"

if codigo==5 or codigo==6:
    classificacao = "Vestuário"

if codigo==7:
    classificacao = "Higiene Pessoal"

if codigo>7 and codigo<16:
    classificacao = "Limpeza e utensílios domésticos"

if codigo<1 or codigo>15:
    classificacao = "código inválido"

print(f"Classificação: {classificacao}")
