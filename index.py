from populacao_inicial import populacao_inicial
from Especie import printPopulacaoDetalhes
from funcao_objetivo import funcao_objetivo
from selecao import selecao

especie = 'homo_erectus'

# Cria população inicial
populacao = populacao_inicial(especie)

# Printa população gerada com seus atributos
printPopulacaoDetalhes(populacao, especie)

# Avaliar as soluções candidatas
scores = [funcao_objetivo(ind) for ind in populacao]

# Printa os scores obtidos
print('Scores: ' + str(scores))

# Seleciona o melhor indivíduo de um grupo aleatório
[selected, index, score] = selecao(populacao, scores)

# Printa o indivíduo selecionado
print('\nMelhor:\nIndivíduo ' + str(index) + '\n' + str(selected) + '\nScore: ' + str(score))

