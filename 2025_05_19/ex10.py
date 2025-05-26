"""
Criar um algoritmo que leia os limites inferior e superior de um
intervalo e imprima todos os números pares no intervalo aberto
e seu somatório.
Suponha que os dados digitados são para um intervalo crescente, ou seja, o primeiro valor é menor que o
segundo
"""
inferior = int(input("Informe limite inferior: "))
superior = int(input("Informe limite superior: "))
x = inferior
soma = 0
while x<=superior:
    if x%2==0:
        print(x)
        soma = soma + x
    x+=1