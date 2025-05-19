"""
Escreva um algoritmo que receba 15 números e imprima quantos números
maiores que 30 foram digitados.
"""
x = 1
conta = 0
while x<=15:
    num = int(input("Informe inteiro: "))
    if num>30:
        conta+=1
    x+=1

print(f"Foram informados {conta} números maiores que 30.")