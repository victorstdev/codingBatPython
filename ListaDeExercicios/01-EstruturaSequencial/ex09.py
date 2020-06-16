# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

f = float(input('Insira a temperatuda em Farenheit: '))

c = (5 * (f - 32)) / 9

print('{:.2f} em Celsius é: {:.2f}'.format(f, c))