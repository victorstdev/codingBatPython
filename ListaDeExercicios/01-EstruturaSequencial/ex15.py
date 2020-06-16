# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

valorHora = float(input('Insira seu valor por hora: '))
numHoras = int(input('Insira a quantidade de horas trabalhadas: '))
salarioBruto = valorHora * numHoras
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato

print(\
  '+ Salário Bruto: R${:.2f}\n\
  - IR: R${:.2f}\n\
  - INSS: R${:.2f}\n\
  - Sindicato: R${:.2f}\n\
  = Salário Líquido: R${:.2f}'.format(salarioBruto, ir, inss, sindicato, salarioLiquido))