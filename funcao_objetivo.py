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
