VALOR         = 0
INCOGNITA     = 1
ADICAO        = 2
SUBTRACAO     = 3
MULTIPLICACAO = 4
DIVISAO       = 5
POTENCIACAO   = 6
RADICIACAO    = 7
IGUALDADE     = 8

class exp:
    tipo = None
    opdos = []

    def __init__(self, type, operands):
      self.tipo = type
      if type(operands) == list:
          self.opdos = operands
