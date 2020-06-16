# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Insira o valor do lado do quadrado: '))

area = 2 * (lado * lado)

print('O dobro da área do quadrado é: {:.2f}'.format(area))