# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Insira sua altura em cm: ')) / 100
sexo = input('Insira seu sexo(m, f): ')

if sexo == 'm':
  pesoIdeal = (72.7 * altura) - 58
else:
  pesoIdeal = (62.1 * altura) - 44.7

print('Sua altura é: {:.2f} e seu peso ideal é: {:.2f}'.format(altura, pesoIdeal))