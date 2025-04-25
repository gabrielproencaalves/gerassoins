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
eqs   = 40

# Nome do arquivo de saida
caminho_saida = "output.ms"

# Precisao de arredondamento
precisao_decimal = 2

# Retorna o modulo de um inteiro
def mod(i):
    return (i ** 2) ** (1/2)

# Retorna numeros primos de 0 a x
# Obrigado, Eratóstenes
def primos(x):
    # x deve ser positivo!
    x = mod(x)

    # Se o usuario fornecer um limite valido
    if x > 1:
        # Declara lista de primos, com o primeiro deles
        vals = [2]
        # Próximo número a partir do primeiro primo
        i = 3

        # Até i chegar a x
        while i <= x:
            j = 0
            while j < len(vals):
                # Se i for divisível por um valor primo anterior
                if i % vals[j] == 0:
                    # Interrompa o processo
                    break
                j += 1

            # Se j percorreu toda a lista, sem interrupcoes
            if j == len(vals):
                # i é primo, guarde-o em vals
                vals += [i]

            # Avance para o proximo inteiro
            i += 1

        # Retorne os primos encontrados
        return vals

# Retorna um produto de fatores primos equivalente a x
def fatorar(x):
    # Declara lista onde ficarao os fatores
    fatores = []

    # Se o numero for negativo
    if x < 0:
        # Sinalize com o fator -1
        fatores += [-1]
        # Torne o x positivo
        x = -x

    # Se x for um produto de fatores primos
    if x > 3:
        # Armazene os primos necessarios para fatora-lo
        fprimos = primos(x ** (1/2))
        fprimos_len = len(fprimos)
        i = 0

        # Enquanto o x for redutivel e houverem primos disponiveis
        while x > 1 and i < fprimos_len:
            # Se x nao for um produto de fprimos[i]
            if x % fprimos[i] != 0:
                # Tente o proximo fator
                i += 1

            else: # se for
                # Retire este fator de x
                x /= fprimos[i]
                # e coloque na lista de fatores
                fatores += [fprimos[i]]

        # Retorne os fatores encontrados
        if x > 1:
            return fatores + [int(x)]
        return fatores
    return fatores + [x]

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

# Verifica se a expressao e uma adicao
def e_adicao(expr):
    return expr.tipo == e.ADICAO

# Verifica se a expressao e uma subtracao
def e_subtracao(expr):
    return expr.tipo == e.SUBTRACAO

# Verifica se a expressao e uma multiplicacao
def e_multiplicacao(expr):
    return expr.tipo == e.MULTIPLICACAO

# Verifica se a expressao e uma divisao
def e_divisao(expr):
    return expr.tipo == e.DIVISAO

# Verifica se a expressao e uma fracao
def e_fracao(expr):
    return e_divisao(expr)

# Verifica se a expressao e uma potenciacao
def e_potenciacao(expr):
    return expr.tipo == e.POTENCIACAO

# Verifica se a expressao e uma radiciacao
def e_radiciacao(expr):
    return expr.tipo == e.RADICIACAO

# Retorna o resultado da expressao fornecida apos calcular seus operandos,
# recursivamente
def resolver_exp(expr):
    if e_operacao(expr):
        if e_adicao(expr):
            return resolver_exp(expr.opdos[0]) + resolver_exp(expr.opdos[1])
        if e_subtracao(expr):
            return resolver_exp(expr.opdos[0]) - resolver_exp(expr.opdos[1])
        if e_multiplicacao(expr):
            return resolver_exp(expr.opdos[0]) * resolver_exp(expr.opdos[1])
        if e_divisao(expr):
            return resolver_exp(expr.opdos[0]) / resolver_exp(expr.opdos[1])
        if e_potenciacao(expr):
            return resolver_exp(expr.opdos[0]) ** resolver_exp(expr.opdos[1])
        if e_radiciacao(expr):
            return resolver_exp(expr.opdos[0]) ** (1/resolver_exp(expr.opdos[1]))
    return expr.opdos[0]

# Mostra a exp e suas descendentes no formato de notacao do python
def mostrar_exp(expr):
    if e_operacao(expr):
        sinal = None
        expr_final = " ( %s ) %s ( %s ) "
        if expr.tipo == e.IGUALDADE:     sinal = "=="
        elif expr.tipo == e.ADICAO:        sinal = "+"
        elif expr.tipo == e.SUBTRACAO:     sinal = "-"
        elif expr.tipo == e.MULTIPLICACAO: sinal = "*"
        elif expr.tipo == e.DIVISAO:       sinal = "/"
        elif expr.tipo == e.POTENCIACAO:   sinal = "^^"
        elif expr.tipo == e.RADICIACAO:    sinal = "vv"

        return expr_final % \
               (mostrar_exp(expr.opdos[0]),
                sinal,
                mostrar_exp(expr.opdos[1]))
    return str(expr.opdos[0])


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
            elif expr.opdos[0].tipo == e.INCOGNITA \
             and not e_operacao(expr.opdos[1]):
                return operandos[0] % saida(expr.opdos[1]) \
                     + sinal                               \
                     + operandos[1] % saida(expr.opdos[0])

        elif expr.tipo == e.DIVISAO:     sinal = " over "
        elif expr.tipo == e.POTENCIACAO: sinal = " sup "
        elif expr.tipo == e.RADICIACAO:
            operandos[1] = " \"\" sup " + operandos[1]
            operandos[0] = " sqrt "     + operandos[0]

            # Troca ordem strings
            operandos[0], operandos[1] = operandos[1], operandos[0]

        return operandos[0] % saida(expr.opdos[0]) \
             + sinal                               \
             + operandos[1] % saida(expr.opdos[1])

    if expr.tipo == e.VALOR:
        return " { " + str(expr.opdos[0]) + " } "

    return " { x } "

# Programa principal
def main():
    global operacoes_utilizadas

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
        try:
            raiz.opdos[1] = e.exp(e.VALOR, [resolver_exp(raiz.opdos[0]), 0])
        # Se houver um erro de divisao por zero
        except ZeroDivisionError:
            # Tente tudo novamente
            main()
            # Interrompa a funcao atual
            return

        # Arredondar resultado da equacao deixando duas casas decimais
        # apos a virgula
        raiz.opdos[1].opdos[0] = round(raiz.opdos[1].opdos[0], precisao_decimal)

        # Interpretar arvore de exp's, traduzi-la e guarda-la em um arquivo
        # e o x em outro
        arquivo_saida.writelines([
            "\\n+[step])  $ " + saida(raiz).replace(".", ",") + " $\n",
            ".sp\n"
        ])

        arquivo_respostas.writelines([
            "\\n+[step])  $ x = ", str(x), " $\n",
            ".br\n"
        ])

if __name__ == "__main__":
    main()
