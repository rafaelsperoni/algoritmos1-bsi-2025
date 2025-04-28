"""
Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.
"""
c1 = int(input("Primeiro Cateto: "))
c2 = int(input("Segundo Cateto: "))

hipotenusa = (c1**2 + c2**2)**0.5

print(f"Hipotenusa: {hipotenusa}")