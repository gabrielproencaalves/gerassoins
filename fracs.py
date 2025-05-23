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
