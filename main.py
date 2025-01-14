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

# Quantidade padrao de equacoes
eqs   = 1

# Escolhe randomicamente uma das operacoes disponiveis e atualiza a lista de
# contagem de operacoes utilizadas
def escolher_op():
    # Alerta o python o uso de variaveis ja existentes
    global operacoes_disponiveis
    global operacoes_utilizadas

    # Escolha um indice das operacoes
    indice_ops = randint(0, 6)

    # Se a operacao do indice escolhido estiver disponivel
    if operacoes_disponiveis[indice_ops] - operacoes_utilizadas[indice_ops] > 0:
        # Atualize a lista de contagem
        operacoes_utilizadas[indice_ops] += 1

        # Converta o indice no numero da operacao e retorne-o
        return indice_ops - 3
    # Senao... repita o processo
    return escolher_op()

# Retorna o resultado da expressao fornecida apos calcular seus operandos,
# recursivamente
def resolver_exp(expr):
    if expr.tipo == e.ADICAO:
        return resolver_exp(expr.opdos[0]) + resolver_exp(expr.opdos[1])
    if expr.tipo == e.SUBTRACAO:
        return resolver_exp(expr.opdos[0]) - resolver_exp(expr.opdos[1])
    if expr.tipo == e.MULTIPLICACAO:
        return resolver_exp(expr.opdos[0]) * resolver_exp(expr.opdos[1])
    if expr.tipo == e.DIVISAO:
        return resolver_exp(expr.opdos[0]) / resolver_exp(expr.opdos[1])
    if expr.tipo == e.POTENCIACAO:
        return resolver_exp(expr.opdos[0]) ** resolver_exp(expr.opdos[1])
    if expr.tipo == e.RADICIACAO:
        return resolver_exp(expr.opdos[0]) ** (1/resolver_exp(expr.opdos[1]))
    if expr.tipo == e.VALOR or expr.tipo == e.INCOGNITA:
        return expr.opdos[0]

if __name__ == "__main__":
  igualdade_raiz = exp(IGUALDADE)
