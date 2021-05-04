from utils import getPopulacaoEspecie
import random

def populacao_inicial(especie):
  populacao = []

  # Busca o range base dos atributos daquela espécie
  informacoesEspecie = getPopulacaoEspecie(especie)
  
  i = 0

  while i < 10:
    individuo = []
    ignoraHeader = True

    # Define os parâmetros aleatórios do indivíduo com base no range da sua espécie
    for linha in informacoesEspecie:
      if(ignoraHeader):
        ignoraHeader = False
        continue
      
      infosEspecie = linha.replace('\n', '').split('-')
      novoAtributo = round(random.uniform(int(infosEspecie[0]), int(infosEspecie[1])), 2)
      individuo.append(novoAtributo)

    # Adiciona o individuo à população
    populacao.append(individuo)  
    i += 1

  # Retorna a população de indivíduos gerados
  return populacao



  



