"""
Deseja-se estudar o perfil dos consumidores de energia elétrica de uma cidade,
para um dado mês do ano.
Para tanto, deverão ser lidos os seguintes dados para cada um dos n consumidores de uma amostragem 
(n deve ser solicitado ao usuário no início do programa):
● consumo do mês, em kWh;
● código do tipo de consumidor (1 para residencial, 2 para comercial e 3 para industrial);

Antes de ler os dados dos consumidores, o preço do kWh deve ser fornecido ao programa. Escrever um
programa que leia os dados indicados acima e calcule e imprima:
● Para cada consumidor, o total a pagar;
● O maior consumo verificado na amostra de consumidores;
● O menor consumo verificado na amostra de consumidores;
● O total do consumo para cada um dos três tipos de consumidores;
"""

consumidores = int(input(f"Quantos consumidores: "))
kwh = float(input("Informe o preço do KWh: "))
x = 0
maior = 0
totalR = 0.0
totalC = 0.0
totalI = 0.0
while x<consumidores:
    tipo = int(input("Informe o tipo de consumidor: "))
    consumo = float(input("Informe a leitura do mês, em KWh: "))

    pagar = consumo*kwh
    print(f"Valor a pagar no mês: R$ {pagar}")

    if x == 0:
        maior = consumo
        menor = consumo
    else:
        if consumo>maior:
            maior = consumo
        if consumo<menor:
            menor = consumo

    if tipo==1:
        totalR += consumo
    elif tipo==2:
        totalC += consumo
    elif tipo==3:
        totalI += consumo

    x+=1

print(f"O maior consumo no mês: {maior} kWh")
print(f"O menor consumo no mês: {menor} kWh")
print(f"Total de consumo Residencial: {totalR} kWh")
print(f"Total de consumo Residencial: {totalC} kWh")
print(f"Total de consumo Residencial: {totalI} kWh")