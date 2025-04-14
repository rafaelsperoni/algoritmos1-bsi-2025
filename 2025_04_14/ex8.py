"""
Construa um algoritmo para determinar a situação (APROVADO/EXAME/REPROVADO)
de um aluno, dado a sua frequência (FREQ) (porcentagem de 0 a 100%) 
e sua nota (NOTA) (nota de 0.0 a 10.0), sendo que:
freq até 75% - reprovado
freq entre 75% e 100 e nota até 3.0 - reprovado
freq entre 75% e 100 e nota de 3.0 até 7.0 - exame
freq entre 75% e 100 e nota entre 7.0 e 10.0 - aprovado
"""

freq = float(input("Informe o percentual de frequência: "))
nota = float(input("Informe a nota: "))

if freq<75:
    print("Reprovado")

if nota<3.0: 
    print("Reprovado")

if nota>=3.0 and nota<7.0 and freq>=75 and freq<=100:
    print("Exame")

if nota>=7.0 and freq>=75 and freq<=100:
    print("Aprovado")