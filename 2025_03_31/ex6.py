preco_pao = 0.5
preco_broa = 1.5
qtde_paes = int(input("Informe a quantidade de pães vendidos: "))
qtde_broas = int(input("Informe a quantidade de broas vendidas: "))

total_vendas = qtde_paes*preco_pao + qtde_broas*preco_broa
poupanca = total_vendas*10/100

print(f"O valor total vendido foi de R${total_vendas:.2f}. \nA sugestão de poupança é de R${poupanca:.2f}")