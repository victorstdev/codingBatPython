# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notaA = float(input('Insira a primeira nota: '))
notaB = float(input('Insira a segunda nota: '))
notaC = float(input('Insira a terceira nota: '))
notaD = float(input('Insira a quarta nota: '))

media = (notaA + notaB + notaC + notaD) / 4

print(\
  'Notas: {:.2f}, {:.2f}, {:.2f}, {:.2f}\n\
  Média: {:.2f}'.format(notaA, notaB, notaC, notaD, media))