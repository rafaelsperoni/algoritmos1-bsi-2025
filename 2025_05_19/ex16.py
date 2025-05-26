"""
Os professores da disciplina Algoritmos do IFC- Camboriú 
necessitam de um programa capaz de calcular
as médias de cada aluno. 
Para cada aluno, a média semestral é calculada por:

ms = 0.3 x AV1 + 0.3 x AV2 + 0.4 x mt

onde AV1 e AV2 são, respectivamente, a primeira 
e a segunda avaliação e mt é a média aritmética dos 4
trabalhos, t1, t2, t3 e t4.

O número de alunos (N) deve ser lido no início do programa.]

Caso a média de um aluno seja inferior a 7,
informar que o mesmo está em recuperação final, 
caso contrário mostrar aprovado.
"""

n = int(input("Informe a quantidade de alunos: "))

x = 0
while x<n:
    print(f"Aluno {x+1}")
    av1 = float(input("Informe nota da AV1: "))
    av2 = float(input("Informe nota da AV2: "))
    t1 = float(input("Informe nota do t1: "))
    t2 = float(input("Informe nota do t2: "))
    t3 = float(input("Informe nota do t3: "))
    t4 = float(input("Informe nota do t4: "))

    mt = (t1+t2+t3+t4) / 4
    media = av1*0.3 + av2*0.3 + mt*0.4

    print(f"Média do aluno {x+1}: {media}")
    if media<7.0:
        print("Em recuperação")
    else:
        print("Aprovado")
    
    x+=1