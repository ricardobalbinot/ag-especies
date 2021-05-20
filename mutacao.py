import random

def mutacao(individuo, t_mut):
  # Checa a taxa de mutação
  if random.random() < t_mut:
    # Busca um atributo aleatório do indivíduo
    atributo = random.randint(0, len(individuo) - 1)
    # Define um fator de mutação aleatório
    fator_mutacao = random.uniform(0.98, 1.01)

    # Altera um atributo aleatório do indivíduo
    individuo[atributo] = round(individuo[atributo] * fator_mutacao, 2)
  
  return individuo