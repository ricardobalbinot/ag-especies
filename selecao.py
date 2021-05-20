import random

# Função de seleção por Torneio
def selecao(populacao, scores):
	individuosAleatorios = []
	
	# Define o número de indivíduos que serão utilizados no torneio (10%)
	numIndividuosSelecionados = int(len(populacao) / 10)

	# Seleciona 1/10 dos indivíduos aleatóriamente
	for _ in range(numIndividuosSelecionados):
		individuo = random.randint(0, len(populacao) - 1)
		individuosAleatorios.append(individuo)

	# Primeira seleção aleatória de index
	selecionado_idx = individuosAleatorios[random.randint(0, numIndividuosSelecionados - 1)]
	
	# Seleção aleatória com 1/4 dos indivíduos
	for idx in individuosAleatorios:
		# Realiza o torneio
		if scores[idx] > scores[selecionado_idx]:
			selecionado_idx = idx

	# Retorna o melhor indivíduo encontrado
	return populacao[selecionado_idx]
