from populacao_inicial import populacao_inicial
from funcao_objetivo import funcao_objetivo
from selecao import selecao
from cruzamento import cruzamento
from mutacao import mutacao


# Limite máximo de iterações
n_iter = 1000
# Tamanho da população
n_pop = 100
# Número de indivíduos selecionados por iteração para cruzamento
n_selec= 50
# Taxa de cruzamento
t_cruz = 0.9
# Taxa de mutação
t_mut = 0.8

# Espécie usada na execução 
# especie = 'australopithecus_afarensis'
especie = 'homo_erectus'
# especie = 'homo_habilis'


# Cria população inicial
populacao = populacao_inicial(especie, n_pop)

# Inicia a verificação do melhor indivíduo
melhor, melhor_score = populacao[0], funcao_objetivo(populacao[0], especie)

for geracao in range(n_iter):
  # Avaliar as soluções candidatas da população
  scores = [funcao_objetivo(ind, especie) for ind in populacao]

  # Checa por um novo melhor indivíduo
  for i in range(n_pop):
    if scores[i] > melhor_score:
      # Encontramos um novo melhor indivíduo!!!
      melhor, melhor_score = populacao[i], scores[i]
      print("\nGeração", geracao, " = Indivíduo: ", populacao[i], ". Score: ", scores[i])


  # Seleciona o melhor indivíduo de um grupo aleatório
  selecionados = [selecao(populacao, scores) for _ in range(n_selec)]


  # Cria a lista de filhos
  filhos = list()

  for i in range(0, n_selec, 2):
    # Separa os pais selecionados em pares
    pai1, pai2 = selecionados[i], selecionados[i + 1]

    # Cruzamento e mutação dos indivídeuos
    for filho in cruzamento(pai1, pai2, t_cruz):
      # Mutação no indivíduo
      filho = mutacao(filho, t_mut)
      # Guarda o indivíduo para a próxima geração
      filhos.append(filho)


  # Verifica se atingiu o critério de parada da espécie
  if (melhor_score == 1):
    break

  # Substitui a população da próxima geração 
  populacao = filhos

# Printa o indivíduo selecionado
print('\nMelhor:\n' + str(melhor) + '\nScore: ' + str(melhor_score))



