# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Insira sua altura em cm: ')) / 100

pesoIdeal = (72.7 * (altura)) - 58

print('Sua altura é: {:.2f}, e seu peso ideal é: {:.2f}'.format(altura, pesoIdeal))