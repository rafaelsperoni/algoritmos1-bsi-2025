"""
A granja Frangotech possui um controle automatizado de cada frango da sua produção.
No pé direito do frango há um anel com um chip de identificação;
no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir.

Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50 cada,
faça um algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.
"""

chip = 4.0
ident = 3.5
frangos = int(input("Informe a quantidade de frangos: "))

custo = chip*frangos + 2*ident*frangos

print(f"O custo para a granja: R$ {custo:.2f}")