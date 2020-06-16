# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   o produto do dobro do primeiro com metade do segundo .
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.

import math #biblioteca pra deixar mais elegante

x = int(input('Insira um número inteiro: '))
y = int(input('Insira um número inteiro: '))
z = float(input('Insira um número real: '))

produto = (2 * x) * (y / 2)
soma = (3 * x)+z
cubo = math.pow(z, 3)

print(\
  'X: {}; Y: {};  Z: {:.2f}; \n\
  Primeira conta: {}\n\
  Segunda conta: {}\n\
  Terceira conta: {}'.format(x, y, z, produto, soma, cubo))