import exp as e
import exp_test as et

# Retorna o nome extenso do tipo numerico recebido
def tipo_str(tipo):
    if tipo == e.IGUALDADE:
        return "IGUALDADE"
    if tipo == e.VALOR:
        return "VALOR"
    if tipo == e.INCOGNITA:
        return "INCÓGNITA"
    if tipo == e.ADICAO:
        return "ADIÇÃO"
    if tipo == e.SUBTRACAO:
        return "SUBTRAÇÃO"
    if tipo == e.MULTIPLICACAO:
        return "MULTIPLICAÇÃO"
    if tipo == e.DIVISAO:
        return "DIVISÃO"
    if tipo == e.POTENCIACAO:
        return "POTENCIAÇÃO"
    if tipo == e.RADICIACAO:
        return "RADICIAÇÃO"

# Mostra a exp e suas descendentes no formato de notacao do python
def mostrar_exp(expr):
    if et.e_operacao(expr):
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

# Detalha recusivamente a exp atual e suas descendentes
def detalhar_exp(expr, nivel=0, ptrs=[], limit=10):
    if limit > 0:
        tabulacao = "\t|" * nivel
        if type(expr) == e.exp:
            print(tabulacao + str(expr))
            for ptr in ptrs:
                if ptr is expr:
                    print(f"\n{ptrs}\nCyclical reference inside, and to, expr{expr}")
                    return
            print(tabulacao + "tipo  = " + tipo_str(expr.tipo))
            print(tabulacao + "opdos = [")
            detalhar_exp(expr.opdos[0], nivel + 1, ptrs + [expr], limit - 1)
            detalhar_exp(expr.opdos[1], nivel + 1, ptrs + [expr], limit - 1)
            print(tabulacao + "]")
        else:
            print(tabulacao + str(expr))
