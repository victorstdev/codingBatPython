class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  def teste(self):
    print('Nome: {}, Idade: {}'.format(self.nome, self.idade))