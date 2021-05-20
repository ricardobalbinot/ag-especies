def getPopulacaoEspecie(especie):
  f = open('database/' + str(especie) + '.txt')
  return f.readlines()

def getNomeEspecie(especie):
  if especie == 'australopithecus_afarensis':
    return 'Australopithecus afarensis'
  elif especie == 'homo_habilis':
    return 'Homo habilis' 
  elif especie == 'homo_erectus':
    return 'Homo erectus'

def limpaArquivoOutput():
  f = open('output/resultados_experimento.txt', 'w')
  f.writelines([''])
  f.close()

def setOutputHeader(especie):
  f = open('output/resultados_experimento.txt', 'a')
  f.writelines(['\n\nEspécie: ', getNomeEspecie(especie), '\nMelhor indivíduo\tScore\tGeraçao'])
  f.close()

def setOutputResults(melhor_individuo, score, geracao):
  f = open('output/resultados_experimento.txt', 'a')
  f.writelines(['\n', str(melhor_individuo), '\t', str(score), '\t', str(geracao)])
  f.close()
  
def setOutputRodape(tempo):
  f = open('output/resultados_experimento.txt', 'a')
  f.writelines(['\nTempo de execução: \t', str(round(tempo, 2)), ' segundos'])
  f.close()

def setOutputFinal(tempo):
  f = open('output/resultados_experimento.txt', 'a')
  f.writelines(['\n\nTempo total de execução: \t', str(round(tempo, 2)), ' segundos'])
  f.close()