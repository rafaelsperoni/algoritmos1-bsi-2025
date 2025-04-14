idade = int(input("Informe a idade do competidor: "))

if idade<5:
    categoria = "Não se encaixa em nehuma categoria"

if idade>=5 and idade<8:
    categoria = "Infantil A"

if idade>=8 and idade<11:
    categoria = "Infantil B"

if idade>=11 and idade<14:
    categoria = "Juvenil A"

if idade>=14 and idade<18:
    categoria = "Juvenil B"

if idade>=18:
    categoria = "Sênior"

print(f"O competidor tem {idade} anos, e sua categoria é {categoria}.")