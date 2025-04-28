"""
Faça um programa que receba três notas,
calcule e mostre a média ponderada dessas notas,
considerando peso 3 para a primeira nota,
peso 2 para a segunda nota e peso 5 para a terceira nota.
Mostre, ainda, a situação do estudante,
considerando que a média para aprovação é 6.0,
e o curso não tem exame.
"""
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 * 3 + nota2 * 2 + nota3 * 5)/10

if media>=6.0:
    print("Aprovado")
else:
    print("Reprovado")

print(f"A média do estudante: {media}")