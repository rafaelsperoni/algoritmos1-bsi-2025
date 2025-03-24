"""
Declare as seguintes variáveis: nome do funcionario, 
anoNascimento, numero de filhos, rg, salario, status.
Atribua valores às respectivas variáveis. A
variável status deverá receber um valor lógico.
Mostre os dados conforme exemplo abaixo:

O funcionário <<nome>> com rg <<rg>> possui <<idade>> anos de vida.
O salario do funcionario <<nome>> é de R$ <<salario>>, e possui <<filhos>>
filhos.
Situação:<<status>>
"""

nome = "Pedro"
anoNascimento = 2000
filhos = 1
rg = "65465465-4"
salario = 2500.15
status = True
idade = 2025 - anoNascimento

print(f"O funcionário {nome} com rg {rg}")
print("tem ", idade, " anos de vida")
print(f"O salario do funcionário {nome} é de R$ {salario}")
print(f"Status: {status}")
