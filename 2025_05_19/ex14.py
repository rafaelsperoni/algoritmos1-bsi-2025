"""
Um cinema possui capacidade de 20 lugares e está sempre 
com ocupação total.
Certo dia, cada espectador respondeu a um questionário,
em que constava:
● sua idade;
● sua opinião em relação ao filme, segundo as seguintes notas:
"""

x = 1 
conta_otimo = 0
conta_bom = 0
conta_regular = 0
conta_ruim = 0
conta_pessimo = 0
soma_idade_ruim = 0
maior_otimo = 0
maior_ruim = 0
maior_pessimo = 0
while x<=2:
    idade = int(input("Informe a idade: "))
    nota = input("Informe a nota (A - E): ")

    if nota=="A":
        conta_otimo += 1
        if idade>maior_otimo:
            maior_otimo = idade
    elif nota=="B":
        conta_bom += 1
    elif nota=="C":
        conta_regular += 1
    elif nota=="D":
        conta_ruim += 1
        soma_idade_ruim += idade
        if idade>maior_ruim:
            maior_ruim = idade
    elif nota=="E":
        conta_pessimo += 1
        if idade>maior_pessimo:
            maior_pessimo = idade

    x+=1

perc_bom = conta_bom/20
perc_regular = conta_regular/20

#a - quantidade de respostas ótimo
print(f"A quantidade de respostas ótimo: {conta_otimo}")
#b - a diferença percentual entre respostas bom e regular
print(f"A diferença percentual: {(perc_bom - perc_regular)*100}")
#c - a média de idade das pessoas que responderam ruim;
if conta_ruim!=0:
    print(f"A media de idade de quem respondeu ruim: {soma_idade_ruim/conta_ruim}")
else:
    print("Nenhuma avaliação Ruim")
#d - a percentagem de respostas péssimo e a maior idade que utilizou esta opção;
print(f"Percentagem de respostas Pessimo: {conta_pessimo/20*100}% - Maior idade: {maior_pessimo}")
#e - a diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim.
print(f"Maior que respondeu Ótimo: {maior_otimo}. O maior que respondeu Ruim: {maior_ruim}. Diferença de idade entre eles: {abs(maior_otimo-maior_ruim)} anos")