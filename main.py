import exp as e
import random as r

# Lista do numero de repeticoes permitidas para cada operacao onde
# operacoes_disponiveis[OPERACAO + 3] indica a quantidade permitida de
# ocorrencias de OPERACAO nas equacoes
global operacoes_disponiveis
operacoes_disponiveis = [0, 1, 1, 0, 1, 1, 0]

# Lista de contagem das operacoes ja utilizadas
global operacoes_utilizadas
operacoes_utilizadas  = [0, 0, 0, 0, 0, 0, 0]

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

# Nome do arquivo de saida
caminho_saida = "output.ms"

# Retorna o modulo de um inteiro
def mod(i)
    return (i ** 2) ** (1/2)

# Escolhe randomicamente uma das operacoes disponiveis e atualiza a lista de
# contagem de operacoes utilizadas
def escolher_op():
    # Alerta o python o uso de variaveis ja existentes
    global operacoes_disponiveis
    global operacoes_utilizadas

    # Escolha um indice das operacoes
    indice_ops = r.randint(0, 6)

    # Se a operacao do indice escolhido estiver disponivel
    if operacoes_disponiveis[indice_ops] - operacoes_utilizadas[indice_ops] > 0:
        # Atualize a lista de contagem
        operacoes_utilizadas[indice_ops] += 1

        # Converta o indice no numero da operacao e retorne-o
        return indice_ops - 3
    # Senao... repita o processo
    return escolher_op()

# Verifica se a expressao e uma operacao
def e_operacao(expr):
    return mod(expr.tipo) != e.VALOR

# Retorna o resultado da expressao fornecida apos calcular seus operandos,
# recursivamente
def resolver_exp(expr):
    if e_operacao(expr):
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
    return expr.opdos[0]

# Retorna a exp fornecida reescrita em groff eqn
def saida(expr):
    if e_operacao(expr):
        sinal = ""
        operandos = [" { %s } ", " { %s } "]

        if   expr.tipo == e.IGUALDADE:   sinal = " = "
        elif expr.tipo == e.ADICAO:      sinal = " + "
        elif expr.tipo == e.SUBTRACAO:   sinal = " - "
        elif expr.tipo == e.MULTIPLICACAO:
            if  expr.opdos[0].tipo != e.INCOGNITA \
            and expr.opdos[1].tipo != e.INCOGNITA:
                operandos = [" { ( %s ) } ", " { ( %s ) } "]
                if mod(expr.opdos[0].tipo) != e.ADICAO:
                    operandos[0] = " { %s } "

        elif expr.tipo == e.DIVISAO:     sinal = " over "
        elif expr.tipo == e.POTENCIACAO: sinal = " sup "
        elif expr.tipo == e.RADICIACAO:
            operandos[1] = " \"\" sup " + operandos[1]
            operandos[0] = " sqrt "     + operandos[0]

        return operandos[0] % saida(expr.opdos[0]) \
             + sinal                               \
             + operandos[1] % saida(expr.opdos[1])

    if expr.tipo == e.VALOR:
        return " " + str(expr.opdos[0]) + " "

    return " x "

if __name__ == "__main__":

    # Abre o arquivo de saida de equacoes, truncando-o
    arquivo_saida = open(caminho_saida, "w+")

    # Abre o arquivo de saida de respostas, truncando-o
    arquivo_respostas = open("respostas_" + caminho_saida, "w+")

    # e acrescenta as definicoes necessarias a ele
    arquivo_saida.writelines([
        ".nr PS 12p",
        ".2C",
        ".EQ",
        "delim $$",
        ".EN",
        ".nr step 0 1",
    ])

    # Gere equacoes ate a eqs-esima
    for eqnum in range(eqs):
        operacoes_utilizadas = [0, 0, 0, 0, 0, 0, 0]

        # Instancie a exp raiz, o sinal de igualdade
        raiz = e.exp(e.IGUALDADE)

        # Define um valor aleatorio para x
        x = r.randint(x_min, x_max)

        # Armazena este valor a esquerda da igualdade
        raiz.opdos[0] = e.exp(e.INCOGNITA, [x])

        # Enquanto houver operacoes disponiveis para a arvore
        while(sum(operacoes_disponiveis) - sum(operacoes_utilizadas) > 0):
            # Crie uma lista com os novos operandos
            tmp_opdos = [raiz.opdos[0],
                         e.exp(e.VALOR, [r.randint(k_min, k_max), 0])]

            # e embaralhe-a
            r.shuffle(tmp_opdos)

            # Atribuir novo exp de operacao a arvore
            raiz.opdos[0] = e.exp(escolher_op(), tmp_opdos)

        # Calcular alteracoes aplicadas em x e armazenar noutro lado da
        # igualdade
        raiz.opdos[1] = e.exp(e.VALOR, [resolver_exp(raiz.opdos[0]), 0])

        # Interpretar arvore de exp's, traduzi-la e guarda-la em um arquivo
        # e o x em outro
        arquivo_saida.writelines([
            "\\n+[step]. $ " + saida(raiz) + " $",
            ".br"
        ])

        arquivo_respostas.writelines([
            ""
        ])
