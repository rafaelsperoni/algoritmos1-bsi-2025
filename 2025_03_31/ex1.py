"""
Faça um programa que receba o salário base
de um funcionário, calcule e mostre o salário 
a receber, sabendo-se que o funcionário
tem gratificação de 5% sobre o salário
base e paga 7% de imposto também sobre
o salário base;
"""
#entradas - salario base
salario_base = float(input("Informe salario base: "))

#processamentos
  # salario a receber será o salario base mais a gratificação menos o imposto
gratificacao = salario_base * 0.05
#considerando o imposto sobre todo o valor
salario_bruto = salario_base + gratificacao
imposto = salario_bruto * 0.07
salario_receber = salario_base + gratificacao - imposto

#saidas - salario a receber
print(salario_receber)