# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math #pra calcular o pi e potência

raio = float(input('Insira o raio do círculo: '))
area = math.pi * math.pow(raio, 2)

print('A área do círculo com {:.2f} de raio é: {:.2f}'.format(raio, area))