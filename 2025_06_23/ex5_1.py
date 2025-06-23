frase = input("Informe a frase: ")

vogais = 'aeiou' #string - pode acessar cada caractere pelo indice

for i in range(len(vogais)):
    print(f"O caractere {vogais[i]} aparece {frase.count(vogais[i])} vezes")


# conta_a = frase.count(vogais[0])
# conta_e = frase.count(vogais[1])
# conta_i = frase.count(vogais[2])
# conta_o = frase.count(vogais[3])
# conta_u = frase.count(vogais[4])
