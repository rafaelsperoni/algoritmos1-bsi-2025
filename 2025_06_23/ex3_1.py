data = "23/06/2025"

partes = data.split("/") # gera uma lista de strings ('23', '06', '2025')
#nessa lista, cada pedaço está em um indice

dia = partes[0]
mes = partes[1]
ano = partes[2]

mes_ext = ""
if mes=='01':
    mes_ext = 'Janeiro'
elif mes=='02':
    mes_ext = 'Janeiro'
elif mes=='03':
    mes_ext = 'Março'
elif mes=='04':
    mes_ext = 'Abril'
elif mes=='05':
    mes_ext = 'Maio'
elif mes=='06':
    mes_ext = 'Junho'
else:
    mes_ext = 'Outro mês'


print(f"Olá, você nasceu no dia {partes[0]} do mês {mes_ext} do ano de {partes[2]}")
# print(partes[0])
# print(partes[1])
# print(partes[2])