import exp as e
import exp_test as et
import exp_debug as edbg
import random as r
import fracs as f

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
eqs   = 40

# Nome do arquivo de saida
caminho_saida = "output.ms"

# Precisao de arredondamento
precisao_decimal = 2

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

# Retorna o resultado da expressao fornecida apos calcular seus operandos,
# recursivamente, no formato de uma outra exp
def resolver_exp(expr):
    if et.e_operacao(expr):
        resultado = e.exp(e.VALOR)

        opdos = [
          resolver_exp(expr.opdos[0]),
          resolver_exp(expr.opdos[1])
        ]

        if et.e_divisao(opdos[0]) or et.e_divisao(opdos[1]):
            opdos[0] = f.fracao(opdos[0])
            opdos[1] = f.fracao(opdos[1])

            if   et.e_adicao(expr):
                resultado = f.somar(opdos[0], opdos[1])
            elif et.e_subtracao(expr):
                resultado = f.subtrair(opdos[0], opdos[1])
            elif et.e_multiplicacao(expr):
                resultado = f.multiplicar(opdos[0], opdos[1])
            elif et.e_divisao(expr):
                resultado = f.dividir(opdos[0], opdos[1])
            elif et.e_potenciacao(expr):
                resultado.opdos = [
                  e.exp(e.VALOR, [
                    opdos[0].opdos[0].opdos[0]     \
                    ** (opdos[1].opdos[0].opdos[0] \
                        / opdos[1].opdos[1].opdos[0]),
                    0
                  ]),
                  e.exp(e.VALOR, [
                    opdos[0].opdos[1].opdos[0]     \
                    ** (opdos[1].opdos[0].opdos[0] \
                        / opdos[1].opdos[1].opdos[0]),
                    0
                  ])
                ]

            elif et.e_radiciacao(expr):
                resultado.opdos = [
                  e.exp(e.VALOR, [
                    opdos[0].opdos[0].opdos[0]         \
                    ** (1 / opdos[1].opdos[0].opdos[0] \
                        / opdos[1].opdos[1].opdos[0]),
                    0
                  ]),
                  e.exp(e.VALOR, [
                    opdos[0].opdos[1].opdos[0]         \
                    ** (1 / opdos[1].opdos[0].opdos[0] \
                        / opdos[1].opdos[1].opdos[0]),
                    0
                  ])
                ]

            return resultado
        if   et.e_adicao(expr):
            resultado.opdos[0] = opdos[0].opdos[0] + opdos[1].opdos[0]
        elif et.e_subtracao(expr):
            resultado.opdos[0] = opdos[0].opdos[0] - opdos[1].opdos[0]
        elif et.e_multiplicacao(expr):
            resultado.opdos[0] = opdos[0].opdos[0] * opdos[1].opdos[0]
        elif et.e_divisao(expr):
            resultado.tipo = e.DIVISAO
            resultado.opdos = opdos
        elif et.e_potenciacao(expr):
            resultado.opdos[0] = opdos[0].opdos[0] \
                                 ** opdos[1].opdos[0]
        elif et.e_radiciacao(expr):
            resultado.opdos[0] = opdos[0].opdos[0] \
                                 ** (1/opdos[1].opdos[0])
        return resultado
    return expr.clone()

# Retorna a exp fornecida reescrita em groff eqn
def saida(expr):
    if et.e_operacao(expr):
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
            elif expr.opdos[0].tipo == e.INCOGNITA \
             and not et.e_operacao(expr.opdos[1]):
                return operandos[0] % saida(expr.opdos[1]) \
                     + sinal                               \
                     + operandos[1] % saida(expr.opdos[0])

        elif expr.tipo == e.DIVISAO:     sinal = " over "
        elif expr.tipo == e.POTENCIACAO: sinal = " sup "
        elif expr.tipo == e.RADICIACAO:
            operandos[1] = " \"\" sup " + operandos[1]
            operandos[0] = " sqrt "     + operandos[0]

        return operandos[0] % saida(expr.opdos[0]) \
             + sinal                               \
             + operandos[1] % saida(expr.opdos[1])

    if expr.tipo == e.VALOR:
        return " { " + str(expr.opdos[0]) + " } "

    return " { x } "

if __name__ == "__main__":

    # Abre o arquivo de saida de equacoes, truncando-o
    arquivo_saida = open(caminho_saida, "w+")

    # Abre o arquivo de saida de respostas, truncando-o
    arquivo_respostas = open("respostas_" + caminho_saida, "w+")

    # Definicoes recomendadas para os arquivos groff
    groff_configs = [
        ".nr PS 10p\n",
        ".2C\n",
        ".EQ\n",
        "delim $$\n",
        ".EN\n",
        ".nr step 0 1\n"
    ]

    # e acrescenta as definicoes necessarias a eles
    arquivo_saida.writelines(groff_configs)
    arquivo_respostas.writelines(groff_configs)

    # Gere equacoes ate a eqs-esima
    for eqnum in range(eqs):
        operacoes_utilizadas = [0, 0, 0, 0, 0, 0, 0]

        # Instancie a exp raiz, o sinal de igualdade
        raiz = e.exp(e.IGUALDADE)

        # Define um valor aleatorio para x
        x = r.randint(x_min, x_max)

        # Armazena este valor a esquerda da igualdade
        raiz.opdos[0] = e.exp(e.INCOGNITA, [x, 0])

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
        raiz.opdos[1] = resolver_exp(raiz.opdos[0])

        # Interpretar arvore de exp's, traduzi-la e guarda-la em um arquivo
        # e o x em outro
        arquivo_saida.writelines([
            "\\n+[step])  $ " + saida(raiz) + " $\n",
            ".sp\n"
        ])

        arquivo_respostas.writelines([
            "\\n+[step])  $ x = ", str(x), " $\n",
            ".br\n"
        ])
