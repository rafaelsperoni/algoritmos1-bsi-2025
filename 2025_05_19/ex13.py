"""
Escreva um algoritmo, que leia um conjunto de 10 fichas,
cada uma contendo, a altura e o código do sexo de uma pessoa
(código = 1 se for masculino e 2 se for feminino), 
e calcule e imprima:
● a maior e a menor altura da turma;
● a média de altura das mulheres;
● a média de altura da turma.
"""

x = 1
maior=0
somamul = 0
somatodos = 0
contamul = 0

while x<=10:
    altura = float(input("Informe a altura: "))
    sexo = int(input("Informe o código do sexo (1|2)"))

    if x==1:
        maior = altura
    else:
        if altura>maior:
            maior = altura

    if sexo==2:
        somamul += altura
        contamul += 1
    
    somatodos += altura
    x += 1

print(f"A maior altura: {maior}")
print(f"A media de altura das mulheres: {somamul/contamul}")
print(f"A média de altura da turma: {somatodos/10}")