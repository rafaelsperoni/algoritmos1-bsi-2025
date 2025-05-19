"""
Elabore um algoritmo que leia a idade e o sexo de uma pessoa.
Mostre a mensagem conforme a tabela abaixo

"""

gen = input("Informe o gênero (M|F): ")
idade = int(input("Informe a idade: "))

if gen=="M":
    if idade<12:
        tratamento = "menina"
    elif idade < 24:
        tratamento = "moça"
    else:
        tratamento = "mulher"

else:
    if idade<12:
        tratamento = "menino"
    elif idade < 24:
        tratamento = "rapaz"
    else:
        tratamento = "homem"


print(f"O tratamento será: {tratamento}")