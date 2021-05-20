def getAtributosEspecie(especie):
  if especie == 'australopithecus_afarensis':
    return ['Força', 'Caça', 'Comunicação', 'Resistência']
  elif especie == 'homo_habilis':
    return ['Força', 'Manuseio', 'Comunicação', 'Resistência'] 
  elif especie == 'homo_erectus':
    return ['Força', 'Ferramental', 'Comunicação', 'Resistência']

def getPesoAtributosEspecie(especie):
  # Alterar futuramente o peso dos atributos para diferentes espécies
  if especie == 'australopithecus_afarensis':
    return [0.25, 0.15, 0.4, 0.2]
  elif especie == 'homo_habilis':
    return [0.25, 0.15, 0.4, 0.2] 
  elif especie == 'homo_erectus':
    return [0.25, 0.15, 0.4, 0.2]

def printPopulacaoDetalhes(populacao, especie):
  atributos = getAtributosEspecie(especie)

  for indP, individuo in enumerate(populacao):
    print('Indivíduo ' + str(indP))

    for indI, attr in enumerate(individuo):
      print(atributos[indI] + ': ' + str(attr))

    print('\n')