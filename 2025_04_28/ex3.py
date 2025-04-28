"""
O custo ao consumidor de um carro novo é a soma do preço
de fábrica com o percentual de lucro do distribuidor e 
 dos impostos aplicados ao preço de fábrica. 
Faça um programa que receba o preço de fábrica 
de um veículo, o percentual de lucro do distribuidor 
e o percentual de impostos, calcule e mostre:
O valor correspondente ao lucro do distribuidor;
O valor correspondente aos impostos;
O preço final do veículo;
"""
fabrica = float(input("Informe o preço de fábrica: "))
lucro = float(input("Informe o percentual de lucro: "))
impostos = float(input("Informe o percentual de impostos: "))

valorlucro = fabrica*lucro/100
valorimpostos = fabrica*impostos/100
preco = fabrica+valorlucro+valorimpostos

print(f"O preço de fábrica: R${fabrica:.2f}")
print(f"O valor do lucro: R${valorlucro:.2f}")
print(f"O valor em impostos: R${valorimpostos:.2f}")
print(f"O preço final: R${preco:.2f}")