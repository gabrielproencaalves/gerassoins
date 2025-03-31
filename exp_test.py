import exp as e
import nutils

# Verifica se a expressao e uma operacao
def e_operacao(expr):
    return nutils.mod(expr.tipo) != e.VALOR

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

# Verifica se a expressao e uma potenciacao
def e_potenciacao(expr):
    return expr.tipo == e.POTENCIACAO

# Verifica se a expressao e uma radiciacao
def e_radiciacao(expr):
    return expr.tipo == e.RADICIACAO
