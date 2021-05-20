import random

# Cruzamento entre 2 pais para gerar 2 filhos
def cruzamento(p1, p2, t_cruz):
	# Filhos começam como cópias dos pais
	f1, f2 = p1.copy(), p2.copy()

	# Utiliza o cruzamento se satisfazer a taxa
	if random.random() < t_cruz:
		# Ponto de corte do cruzamento
		pc = int((len(p1) / 2))

		# Realiza o cruzamento por ponto de corte
		f1 = p1[:pc] + p2[pc:]
		f2 = p2[:pc] + p1[pc:]

	return [f1, f2]
