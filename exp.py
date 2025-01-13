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
    opdos = []

    def __init__(self, type, operands):
      self.tipo = type
      if type(operands) == list:
          self.opdos = operands
