# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

c = float(input('Insira a temperatura em celsius: '))

f = 32 + (9 * c)/5

print('{:.2f} Celsius em Farenheit: {:.2f}'.format(c, f))