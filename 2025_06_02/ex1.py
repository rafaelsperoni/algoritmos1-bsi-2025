"""
Desenvolva um gerador de tabuada (use o for),
capaz de gerar a tabuada de qualquer número inteiro
 entre 1 a 10. O usuário deve informar de qual
 número ele deseja ver a tabuada. A saída deve ser
conforme o exemplo abaixo:
"""
num = int(input("Informe o número: "))

print(f"A tabuada de {num}: ")
for i in range(1, 11):
    res = i * num
    print(f"{i} x {num} = {res}")
