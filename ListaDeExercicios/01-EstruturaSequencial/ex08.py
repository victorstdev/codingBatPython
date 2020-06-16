# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Insira o valor por hora: '))
numHoras = int(input('Insira as horas trabalhadas: '))

total = valorHora * numHoras

print('O salário no mês é: {:.2f}'.format(total))