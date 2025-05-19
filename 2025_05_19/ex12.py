"""
Escreva um algoritmo que leia 20 números e imprima a soma
 dos positivos e o total de números negativos.
"""
x = 1
somapositivos = 0
contanegativos = 0
while x<=20:
    num = int(input("Informe inteiro: "))
    if num>0:
        somapositivos += num
    elif num<0:
        contanegativos += 1
    x+=1

print(f"A soma dos positivos: {somapositivos}")
print(f"A contagem dos negativos: {contanegativos}")