from utils import getPopulacaoEspecie
from Especie import getPesoAtributosEspecie


def funcao_objetivo(individuo, especie):
  maxAttr = 25

  attrPesos = getPesoAtributosEspecie(especie)
  
  totalScore = 0

  for i, attr in enumerate(individuo):
    # Não atribui score caso indivíduo seja inválido
    if (attr > maxAttr):
      totalScore += 0
      continue
    
    # Aumenta o score do indivíduo com base no peso do atributo
    totalScore += (attr * attrPesos[i]) / maxAttr

  return round(totalScore, 5)


def get_max_ranges(especie):
  # Busca o range base dos atributos daquela espécie
  informacoesEspecie = getPopulacaoEspecie(especie)

  maxRanges = list()
  ignoraHeader = True

  for linha in informacoesEspecie:
    if(ignoraHeader):
      ignoraHeader = False
      continue
    
    # Adiciona o range máximo do atributo à lista
    infosEspecie = linha.replace('\n', '').split('-')
    maxRange = int(infosEspecie[1])
    maxRanges.append(maxRange)
  
  return maxRanges