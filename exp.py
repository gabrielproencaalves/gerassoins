IGUALDADE     = 0
ADICAO        = 1
SUBTRACAO     = -ADICAO
MULTIPLICACAO = 2
DIVISAO       = -MULTIPLICACAO
POTENCIACAO   = 3
RADICIACAO    = -POTENCIACAO
VALOR         = 4
INCOGNITA     = -VALOR

class exp:
    tipo = None
    opdos = [None, None]

    def __init__(self, NovoTipo, NovoOpdos=[0, 0]):
        self.tipo = NovoTipo
        if type(NovoOpdos) == list:
            self.opdos = NovoOpdos
