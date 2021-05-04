def getPopulacaoEspecie(especie):
  f = open('database/' + str(especie) + '.txt')
  return f.readlines()

  