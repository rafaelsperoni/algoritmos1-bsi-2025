'''Escreva um programa que recebe uma frase e 
retorna o número de palavras que a frase contém. Considere que a palavra pode começar e/ou terminar por espaços. '''

frase = input("Informe uma frase!").strip() # strip remove os espaços no inicio e no fim
lista = frase.split(" ")   # transforma em uma lista quebrando e removendo os espaços em branco
x = 0
while x < len(lista): # o tamanho da lista será atualizado a cada remoção
    if(lista[x] == ''):  # se for igual a '' podemos remover, caso contrário ele irá gerar um erro
        lista.remove("")
        x = x - 1   # a cada remoção é uma posição a menos que preciso acessar da lista
    x = x + 1 # é preciso incrementar para passar para a próxima posição da lista
    print(lista) # mostra a lista a cada iteração do while

print(f" A quantidade de palavras é: {len(lista)}")
