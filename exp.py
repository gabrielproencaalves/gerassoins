import nutils as n

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

    def clone(self):
        if n.mod(self.tipo) == VALOR:
            return exp(self.tipo, [self.opdos[0], self.opdos[1]])
        return exp(self.tipo, [self.opdos[0].clone(),
                               self.opdos[1].clone()])
