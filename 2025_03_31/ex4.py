saldo = 0.0
salario = float(input("Informe o salario: "))
saldo += salario

primeiro = float(input("Valor do 1o saque: "))
desconto1 = primeiro*(1+(0.38/100))
saldo = saldo - desconto1
print(f"Saldo após o primeiro saque: {saldo}")

segundo = float(input("Valor do 2o saque: "))
desconto2 = segundo*(1+0.38/100)
saldo = saldo - desconto2
print(f"Saldo após o segundo saque: {saldo}")
