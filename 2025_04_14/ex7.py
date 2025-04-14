"""
Escreva um programa que pergunte a que velocidade do carro de um usuário.
Caso o valor informado seja maior que 80km/h, exiba uma mensagem dizendo 
que o usuário foi multado.
Neste caso, exiba o valor da multa , cobrando R$ 5,00 por Km acima dos 80 km/h
"""
velocidade = float(input("Informe a velocidade: "))

if velocidade>80:
    multa = (velocidade - 80) * 5
    print(f"Sua velocidade foi de {velocidade}, e você foi multado em {multa}")
