from tkinter import *
from tkinter import ttk

# Janela raiz
root = Tk()
root.title("Gerassoins")

# Frame basico
rootFrameBase = ttk.Frame(root, padding=10)
rootFrameBase.grid()

# Labelframe para as operacoes
BaseLabelframeOperacoes = ttk.LabelFrame(rootFrameBase, text="Operações", padding=10)
BaseLabelframeOperacoes.grid()

# Label de soma
OperacoesLabelSoma = ttk.Label(BaseLabelframeOperacoes, text="+")
OperacoesLabelSoma.grid(column=0, row=0, padx=10)
# Spinbox de soma
OperacoesSpinboxvarSoma = StringVar()
OperacoesSpinboxSoma = ttk.Spinbox(
    BaseLabelframeOperacoes,
    from_=0,
    to=100,
    textvariable=OperacoesSpinboxvarSoma
)
OperacoesSpinboxSoma.configure(width=3)
OperacoesSpinboxSoma.grid(column=0, row=1, padx=10)
OperacoesSpinboxSoma.set(1)

# Label de subtracao
OperacoesLabelSubtracao = ttk.Label(BaseLabelframeOperacoes, text="-")
OperacoesLabelSubtracao.grid(column=1, row=0, padx=10)
# Spinbox de subtracao
OperacoesSpinboxvarSubtracao = StringVar()
OperacoesSpinboxSubtracao = ttk.Spinbox(
    BaseLabelframeOperacoes,
    from_=0,
    to=100,
    textvariable=OperacoesSpinboxvarSubtracao
)
OperacoesSpinboxSubtracao.configure(width=3)
OperacoesSpinboxSubtracao.grid(column=1, row=1, padx=10)
OperacoesSpinboxSubtracao.set(1)

# Label de multiplicacao
OperacoesLabelMultiplicacao = ttk.Label(BaseLabelframeOperacoes, text="×")
OperacoesLabelMultiplicacao.grid(column=2, row=0, padx=10)
# Spinbox de multiplicacao
OperacoesSpinboxvarMultiplicacao = StringVar()
OperacoesSpinboxMultiplicacao = ttk.Spinbox(
    BaseLabelframeOperacoes,
    from_=0,
    to=100,
    textvariable=OperacoesSpinboxvarMultiplicacao
)
OperacoesSpinboxMultiplicacao.configure(width=3)
OperacoesSpinboxMultiplicacao.grid(column=2, row=1, padx=10)
OperacoesSpinboxMultiplicacao.set(1)

# Label de divisao
OperacoesLabelDivisao = ttk.Label(BaseLabelframeOperacoes, text="÷")
OperacoesLabelDivisao.grid(column=3, row=0, padx=10)
# Spinbox de divisao
OperacoesSpinboxvarDivisao = StringVar()
OperacoesSpinboxDivisao = ttk.Spinbox(
    BaseLabelframeOperacoes,
    from_=0,
    to=100,
    textvariable=OperacoesSpinboxvarDivisao
)
OperacoesSpinboxDivisao.configure(width=3)
OperacoesSpinboxDivisao.grid(column=3, row=1, padx=10)
OperacoesSpinboxDivisao.set(1)

# Label de potenciacao
OperacoesLabelPotenciacao = ttk.Label(BaseLabelframeOperacoes, text="kⁿ")
OperacoesLabelPotenciacao.grid(column=4, row=0, padx=10)
# Spinbox de potenciacao
OperacoesSpinboxvarPotenciacao = StringVar()
OperacoesSpinboxPotenciacao = ttk.Spinbox(
    BaseLabelframeOperacoes,
    from_=0,
    to=100,
    textvariable=OperacoesSpinboxvarPotenciacao
)
OperacoesSpinboxPotenciacao.configure(width=3)
OperacoesSpinboxPotenciacao.grid(column=4, row=1, padx=10)
OperacoesSpinboxPotenciacao.set(0)

# Label de radiciacao
OperacoesLabelRadiciacao = ttk.Label(
    BaseLabelframeOperacoes,
    text="√"
)
OperacoesLabelRadiciacao.grid(column=5, row=0, padx=10)
# Spinbox de radiciacao
OperacoesSpinboxvarRadiciacao = StringVar()
OperacoesSpinboxRadiciacao = ttk.Spinbox(
    BaseLabelframeOperacoes,
    from_=0,
    to=100,
    textvariable=OperacoesSpinboxvarRadiciacao
)
OperacoesSpinboxRadiciacao.configure(width=3)
OperacoesSpinboxRadiciacao.grid(column=5, row=1, padx=10)
OperacoesSpinboxRadiciacao.set(0)

# Labelframe para os limites
BaseLabelframeLimites = ttk.Labelframe(
    rootFrameBase,
    text="Limites",
    padding=10
)
BaseLabelframeLimites.grid()

# Label 'de'
LimitesLabelDe = ttk.Label(
    BaseLabelframeLimites,
    text="De"
)
LimitesLabelDe.grid(column=1, row=0)

# Label 'ate'
LimitesLabelAte = ttk.Label(
    BaseLabelframeLimites,
    text="Ate"
)
LimitesLabelAte.grid(column=2, row=0)

# Label K
LimitesLabelK = ttk.Label(
    BaseLabelframeLimites,
    text="K (coeficientes):"
)
LimitesLabelK.grid(column=0, row=1)
# Spin KDe
LimitesSpinvarKDe = StringVar()
LimitesSpinKDe = ttk.Spinbox(
    BaseLabelframeLimites,
    from_=-100,
    to=100,
    textvariable=LimitesSpinvarKDe
)
LimitesSpinKDe.grid(column=1, row=1)
LimitesSpinKDe.set(10)

# Label X
LimitesLabelX = ttk.Label(
    BaseLabelframeLimites,
    text="X (variável):"
)
LimitesLabelX.grid(column=0, row=2)

# Label Precisao Decimal
LimitesLabelPrecisaoDecimal = ttk.Label(
    BaseLabelframeLimites,
    text="Precisão decimal:"
)
LimitesLabelPrecisaoDecimal.grid(column=0, row=3)

# Label Equacoes
LimitesLabelEquacoes = ttk.Label(
    BaseLabelframeLimites,
    text="Equações:"
)
LimitesLabelEquacoes.grid(column=0, row=4)

# Tk mainloop
root.mainloop()
