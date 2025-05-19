"""Faça um algoritmo que lê valores para duas variáveis X e Y. 
Se o valor correspondente a 30% da soma de x por y for maior que 500
trocar os valores entre X e Y, senão mostrar o menor valor entre as
duas variáveis."""

x = int(input("valor de X: "))
y = int(input("valor de Y: "))

if ((x+y)+0.3)>500:
    aux = x
    x = y
    y = aux
else:
    if x>y:
        print(x)
    else:
        print(y)