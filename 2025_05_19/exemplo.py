x = 0
pares = 0
impares = 0
while x<10:
    x+=1

    num = int(input("Informe numero"))
    if num%2==0: # é par
        print(x)
        pares += 1
    else:
        impares += 1

print(f"Aconteceram {x} repetições")
print(f"São {pares} numeros pares")
print(f"São {impares} numeros ímpares")