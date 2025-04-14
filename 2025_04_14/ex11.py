valor = float(input("Informe o valor da compra: "))

if valor<10.0:
    lucro = 70

if valor>=10.0 and valor<30.0:
    lucro = 50

if valor>=30.0 and valor<50.0:
    lucro = 40

if valor>=50:
    lucro = 30

print(f"Para a compra de R${valor:.2f}, o lucro será de {lucro}%")