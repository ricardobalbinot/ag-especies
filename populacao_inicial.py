from utils import getPopulacaoEspecie
import random

def populacao_inicial(especie, n_pop):
  populacao = []

  # Busca o range base dos atributos daquela espécie
  informacoesEspecie = getPopulacaoEspecie(especie)
  
  i = 0

  while i < n_pop:
    individuo = []

    # Busca os ranges do arquivo ignorando o cabeçalho
    ranges = informacoesEspecie[1].split(',')

    # Define os parâmetros aleatórios do indivíduo com base no range da sua espécie
    for attr in ranges:
      infosEspecie = attr.split('-')
      novoAtributo = round(random.uniform(int(infosEspecie[0]), int(infosEspecie[1])), 2)
      individuo.append(novoAtributo)

    # Adiciona o individuo à população
    populacao.append(individuo)  
    i += 1

  # Retorna a população de indivíduos gerados
  return populacao



  



