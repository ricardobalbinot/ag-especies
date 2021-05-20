import time

from algoritmo_genetico import algoritmo_genetico
from utils import limpaArquivoOutput, setOutputResults, setOutputHeader, setOutputRodape, setOutputFinal

# Espécie usada na execução 
especies = ['australopithecus_afarensis', 'homo_erectus', 'homo_habilis']

# Variáveis de controle
n_experimentos = 50
tempo_total = 0

# Reseta o arquivo de output
limpaArquivoOutput()

for e in especies:
  # Registra o tempo decorrido dos experimentos de cada espécie
  tempo_inicio = time.time()

  # Insere o cabeçalho da espécie no arquivo de saída
  setOutputHeader(e)

  # Realiza os experimentos
  for i in range(n_experimentos):
    melhor, melhor_score, geracao = algoritmo_genetico(e)

    setOutputResults(melhor, melhor_score, geracao)
  
  # Registra o tempo decorrido
  tempo_execucao = time.time() - tempo_inicio
  setOutputRodape(tempo_execucao)

  # Incrementa o tempo total
  tempo_total += tempo_execucao

# Registra o tempo total decorrido
setOutputFinal(tempo_total)