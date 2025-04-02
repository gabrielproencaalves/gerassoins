import exp as e
import exp_test as et

# Retorna uma exp equivalente a expr, porem, em formato racional
def fracao(expr):
    if et.e_divisao(expr):
        return expr.clone()
    return e.exp(e.DIVISAO, [
        expr.clone(),
        e.exp(e.VALOR, [1, 0])
    ])

# Retorna o endereço do numerador da fracao frac
def numerador(frac):
    assert et.e_divisao(frac), "Trying to extract a non-fraction numerator"
    return frac.opdos[0]

# Retorna o endereço do denominador da fracao frac
def denominador(frac):
    assert et.e_divisao(frac), "Trying to extract a non-fraction denominator"
    return frac.opdos[1]


# Retorna nova exp resultante da soma das fracoes frac0 e frac1
def somar(frac0, frac1):
    return e.exp(e.DIVISAO, [
        e.exp(e.VALOR, [
            numerador(frac0).opdos[0]     \
            * denominador(frac1).opdos[0] \
            + numerador(frac1).opdos[0]   \
            * denominador(frac0).opdos[0],
            0
        ]),
        e.exp(e.VALOR, [
            denominador(frac0).opdos[0]
            * denominador(frac1).opdos[0],
            0
        ])
    ])

# Retorna nova exp resultante da subtracao das fracoes frac0 e frac1
def subtrair(frac0, frac1):
    return e.exp(e.DIVISAO, [
        e.exp(e.VALOR, [
            numerador(frac0).opdos[0]     \
            * denominador(frac1).opdos[0] \
            - numerador(frac1).opdos[0]   \
            * denominador(frac0).opdos[0],
            0
        ]),
        e.exp(e.VALOR, [
            denominador(frac0).opdos[0]
            * denominador(frac1).opdos[0],
            0
        ])
    ])

# Retorna nova exp resultante da multiplicacao das fracoes frac0 e frac1
def multiplicar(frac0, frac1):
    return e.exp(e.DIVISAO, [
        e.exp(e.VALOR, [
            numerador(frac0).opdos[0]
            * numerador(frac1).opdos[0],
            0
        ]),
        e.exp(e.VALOR, [
            denominador(frac0).opdos[0]
            * denominador(frac1).opdos[0],
            0
        ])
    ])

# Retorna nova exp resultante da divisao das fracoes frac0 e frac1
def dividir(frac0, frac1):
    return e.exp(e.DIVISAO, [
        e.exp(e.VALOR, [
            numerador(frac0).opdos[0]
            * denominador(frac1).opdos[0],
            0
        ]),
        e.exp(e.VALOR, [
            denominador(frac0).opdos[0]
            * numerador(frac1).opdos[0],
            0
        ])
    ])

# Torna uma fracao expr em seu resultado absoluto
def razao(expr):
    # [ ] Verificar se operandos de expr sao tambem
    # valores absolutos

    if et.e_divisao(expr):
        # Altera o tipo da exp para VALOR
        expr.tipo = e.VALOR
        # E atribui o resultado real da antiga frac a aquela
        expr.opdos = [
                       expr.opdos[0].opdos[0]
                       / expr.opdos[1].opdos[0],
                       0
                     ]
    # Retorna expressao
    return expr

# Torna uma fracao expr em uma equivalente, porem, com menos fatores no
# denominador e no numerador
def simplificar(expr):
    # Se a exp for uma fracao de produtos de fatores primos
    if  et.e_divisao(expr)                    \
        and et.e_multiplicacao(expr.opdos[0]) \
        and et.e_multiplicacao(expr.opdos[1]):

        # Define variaveis para referencia e para iteracao
        menor_produto     = None
        menor_produto_len = None
        maior_produto     = None
        maior_produto_len = None
        i = 1
        j = 1

        # Define qual produto possui mais fatores e qual possui menos
        if len(expr.opdos[0].opdos) < len(expr.opdos[1].opdos):
            menor_produto = expr.opdos[0].opdos
            maior_produto = expr.opdos[1].opdos
        else:
            menor_produto = expr.opdos[1].opdos
            maior_produto = expr.opdos[0].opdos

        # Armazena o a quantidade de fatores de cada produto para economizar
        # processamento
        menor_produto_len = len(menor_produto)
        maior_produto_len = len(maior_produto)

        # Percorre os fatores dos produtos, eliminando os comuns
        while i < menor_produto_len:
            # Se encontrar um fator comum
            if menor_produto[i].opdos[0] == maior_produto[j].opdos[0]:
                # Remova-o do denominador e do numerador
                del(menor_produto[i], maior_produto[j])
                # E atualize o tamanho das listas
                menor_produto_len -= 1
                maior_produto_len -= 1
            # Senao
            else:
            # Mire para o proximo fator,
            # seja do numerador, seja do denominador
                if menor_produto[i].opdos[0] < maior_produto[j].opdos[0]:
                    i += 1
                else:
                    j += 1
                    if j >= maior_produto_len:
                        break

        # Se todos os fatores do produto do numerador foram removidos
        if len(expr.opdos[0].opdos) == 1:
            # Simplifique tudo para um inteiro 1
            expr.opdos[0] = exp(e.VALOR, [1, 0])

        # Se todos os fatores do produto do denominador foram removidos
        if len(expr.opdos[1].opdos) == 1:
            # Simplifique tudo para um inteiro 1
            expr.opdos[1] = e.exp(e.VALOR, [1, 0])
    # Retorna expressao
    return expr
