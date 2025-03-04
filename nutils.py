import exp as e

# Retorna o modulo de um inteiro
def mod(i):
    return (i ** 2) ** (1/2)

# Retorna numeros primos de 0 a x
# Obrigado, Eratostenes
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
    fatores = [
        e.exp(e.VALOR, [1, 0])
    ]

    # Se o numero for negativo
    if x < 0:
        # Sinalize com o fator -1
        fatores += [
            e.exp(e.VALOR, [-1, 0])
        ]
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
                fatores += [
                    e.exp(e.VALOR, [fprimos[i], 0])
                ]

        # Retorne os fatores encontrados
        if x > 1:
            return e.exp(e.MULTIPLICACAO, fatores + [int(x)])
        return e.exp(e.MULTIPLICACAO, fatores)
    return e.exp(e.MULTIPLICACAO, fatores + [x])
