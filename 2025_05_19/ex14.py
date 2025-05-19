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
while x<=20:
    idade = int(input("Informe a idade: "))
    nota = input("Informe a nota (A - E): ")

    if nota=="A":
        conta_otimo += 1
    elif nota=="B":
        conta_bom += 1
    elif nota=="C":
        conta_regular += 1
    elif nota=="D":
        conta_ruim += 1
        soma_idade_ruim += idade

    x+=1

perc_bom = conta_bom/20
perc_regular = conta_regular/20

print(f"A diferença percentual: {(perc_bom - perc_regular)*100}")
print(f"A media de idade de quem respondeu ruim: {soma_idade_ruim/conta_ruim}")

print("continua...")