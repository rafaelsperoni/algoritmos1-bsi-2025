"""
Faça um programa que imprima na tela
 apenas os números ímpares
entre 1 e 50 (use o for)
"""
#50 repetições, testando cada valor
# for i in range(50):
#     if i % 2 != 0:
#         print(i)

#25 repetições, valores de 2 em 2
range(50)  # 0 a 49, varia de 1 em 1
range(1, 50) #1 a 49, varia de 1 em 1
range(1, 50, 2) #1 a 49, varia de 2 em 2

for i in range(1, 50, 2):
    print(i)