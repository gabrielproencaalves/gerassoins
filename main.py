import exp as e
import random as r

# Lista do numero de repeticoes permitidas para cada operacao onde
# operacoes_disponiveis[OPERACAO + 3] indica a quantidade permitida de
# ocorrencias de OPERACAO nas equacoes
operacoes_disponiveis = [0, 1, 1, 0, 1, 1, 0]

# Lista de contagem das operacoes ja utilizadas
operacoes_utilizadas = [0, 0, 0, 0, 0, 0, 0]

# Limite maximo dos operandos e coeficientes inseridos nas equacoes
k_max = 10

# Limite minimo dos operandos e coeficientes inseridos nas equacoes
k_min = 1

# Limite maximo de x, ou seja, do resultado das equacoes
x_max = 10

# Limite minimo de x, ou seja, do resultado das equacoes
x_min = 1

if __name__ == "__main__":
  igualdade_raiz = exp(IGUALDADE)
