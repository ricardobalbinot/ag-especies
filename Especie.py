def getAtributosEspecie(especie):
  if especie == 'australopithecus_afarensis':
    return ['Força', 'Caça', 'Comunicação']
  elif especie == 'homo_habilis':
    return ['Força', 'Manuseio', 'Comunicação'] 
  elif especie == 'homo_erectus':
    return ['Força', 'Ferramental', 'Comunicação']

def printPopulacaoDetalhes(populacao, especie):
  atributos = getAtributosEspecie(especie)

  for indP, individuo in enumerate(populacao):
    print('Indivíduo ' + str(indP))

    for indI, attr in enumerate(individuo):
      print(atributos[indI] + ': ' + str(attr))

    print('\n')