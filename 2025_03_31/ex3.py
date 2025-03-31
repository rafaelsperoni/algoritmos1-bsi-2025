"""
Sabe-se que:
1 Pé =12 polegadas
1 jarda = 3 pés
1 milha = 1.760 jardas
Faça um programa que receba uma medida em pés, faça as conversões e a seguir mostre os resultados em:
Polegadas
Jardas
Milhas
"""

pes = 50

pe = 12
jardas = pes / 3
milhas = jardas / 1760


print("Polegadas: ", pes * pe)
print("Jardas: ", jardas)
print(f"Milhas: {milhas:.5f}")