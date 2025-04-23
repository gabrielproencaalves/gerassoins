import exp as e
import main as m
from tkinter import *
from tkinter import ttk

global OperacoesSpinvarRadiciacao
global OperacoesSpinvarDivisao
global OperacoesSpinvarSubtracao
global OperacoesSpinvarSoma
global OperacoesSpinvarMultiplicacao
global OperacoesSpinvarPotenciacao

# Limite maximo dos operandos e coeficientes inseridos nas equacoes
global LimitesSpinvarKAte

# Limite minimo dos operandos e coeficientes inseridos nas equacoes
global LimitesSpinvarKDe

# Limite maximo de x, ou seja, do resultado das equacoes
global LimitesSpinvarXAte

# Limite minimo de x, ou seja, do resultado das equacoes
global LimitesSpinvarXDe

# Quantidade padrao de equacoes
global LimitesSpinvarEquacoesAte

# Precisao de arredondamento
global LimitesSpinvarPrecisaoDecimalAte


class gerassoins():
    def __init__(self, root):
        global OperacoesSpinvarRadiciacao
        global OperacoesSpinvarDivisao
        global OperacoesSpinvarSubtracao
        global OperacoesSpinvarSoma
        global OperacoesSpinvarMultiplicacao
        global OperacoesSpinvarPotenciacao

        # Limite maximo dos operandos e coeficientes inseridos nas equacoes
        global LimitesSpinvarKAte

        # Limite minimo dos operandos e coeficientes inseridos nas equacoes
        global LimitesSpinvarKDe

        # Limite maximo de x, ou seja, do resultado das equacoes
        global LimitesSpinvarXAte

        # Limite minimo de x, ou seja, do resultado das equacoes
        global LimitesSpinvarXDe

        # Quantidade padrao de equacoes
        global LimitesSpinvarEquacoesAte

        # Precisao de arredondamento
        global LimitesSpinvarPrecisaoDecimalAte

        # Janela raiz
        root.title("Gerassoins")
        root.resizable(False, False)

        # Frame basico
        rootFrameBase = ttk.Frame(root, padding=10)
        rootFrameBase.grid()

        # Labelframe para as operacoes
        BaseLabelframeOperacoes = ttk.LabelFrame(
            rootFrameBase,
            text="Operações",
            padding=10
        )
        BaseLabelframeOperacoes.grid(
            column=0,
            row=0,
            sticky=(N,S,E,W)
        )

        # Label de soma
        OperacoesLabelSoma = ttk.Label(BaseLabelframeOperacoes, text="+")
        OperacoesLabelSoma.grid(column=0, row=0, padx=10)
        # Spinbox de soma
        OperacoesSpinvarSoma = IntVar()
        OperacoesSpinSoma = ttk.Spinbox(
            BaseLabelframeOperacoes,
            from_=0,
            to=100,
            textvariable=OperacoesSpinvarSoma
        )
        OperacoesSpinSoma.configure(width=3)
        OperacoesSpinSoma.grid(column=0, row=1, padx=10)
        OperacoesSpinSoma.set(
            m.operacoes_disponiveis[e.ADICAO + 3]
        )

        # Label de subtracao
        OperacoesLabelSubtracao = ttk.Label(BaseLabelframeOperacoes, text="-")
        OperacoesLabelSubtracao.grid(column=1, row=0, padx=10)
        # Spinbox de subtracao
        OperacoesSpinvarSubtracao = IntVar()
        OperacoesSpinSubtracao = ttk.Spinbox(
            BaseLabelframeOperacoes,
            from_=0,
            to=100,
            textvariable=OperacoesSpinvarSubtracao
        )
        OperacoesSpinSubtracao.configure(width=3)
        OperacoesSpinSubtracao.grid(column=1, row=1, padx=10)
        OperacoesSpinSubtracao.set(
            m.operacoes_disponiveis[e.SUBTRACAO + 3]
        )

        # Label de multiplicacao
        OperacoesLabelMultiplicacao = ttk.Label(BaseLabelframeOperacoes, text="×")
        OperacoesLabelMultiplicacao.grid(column=2, row=0, padx=10)
        # Spinbox de multiplicacao
        OperacoesSpinvarMultiplicacao = IntVar()
        OperacoesSpinMultiplicacao = ttk.Spinbox(
            BaseLabelframeOperacoes,
            from_=0,
            to=100,
            textvariable=OperacoesSpinvarMultiplicacao
        )
        OperacoesSpinMultiplicacao.configure(width=3)
        OperacoesSpinMultiplicacao.grid(column=2, row=1, padx=10)
        OperacoesSpinMultiplicacao.set(
            m.operacoes_disponiveis[e.MULTIPLICACAO + 3]
        )

        # Label de divisao
        OperacoesLabelDivisao = ttk.Label(BaseLabelframeOperacoes, text="÷")
        OperacoesLabelDivisao.grid(column=3, row=0, padx=10)
        # Spin de divisao
        OperacoesSpinvarDivisao = IntVar()
        OperacoesSpinDivisao = ttk.Spinbox(
            BaseLabelframeOperacoes,
            from_=0,
            to=100,
            textvariable=OperacoesSpinvarDivisao
        )
        OperacoesSpinDivisao.configure(width=3)
        OperacoesSpinDivisao.grid(column=3, row=1, padx=10)
        OperacoesSpinDivisao.set(
            m.operacoes_disponiveis[e.DIVISAO + 3]
        )

        # Label de potenciacao
        OperacoesLabelPotenciacao = ttk.Label(BaseLabelframeOperacoes, text="kⁿ")
        OperacoesLabelPotenciacao.grid(column=4, row=0, padx=10)
        # Spinbox de potenciacao
        OperacoesSpinvarPotenciacao = IntVar()
        OperacoesSpinPotenciacao = ttk.Spinbox(
            BaseLabelframeOperacoes,
            from_=0,
            to=100,
            textvariable=OperacoesSpinvarPotenciacao
        )
        OperacoesSpinPotenciacao.configure(width=3)
        OperacoesSpinPotenciacao.grid(column=4, row=1, padx=10)
        OperacoesSpinPotenciacao.set(
            m.operacoes_disponiveis[e.POTENCIACAO + 3]
        )

        # Label de radiciacao
        OperacoesLabelRadiciacao = ttk.Label(
            BaseLabelframeOperacoes,
            text="√"
        )
        OperacoesLabelRadiciacao.grid(column=5, row=0, padx=10)
        # Spinbox de radiciacao
        OperacoesSpinvarRadiciacao = IntVar()
        OperacoesSpinRadiciacao = ttk.Spinbox(
            BaseLabelframeOperacoes,
            from_=0,
            to=100,
            textvariable=OperacoesSpinvarRadiciacao
        )
        OperacoesSpinRadiciacao.configure(width=3)
        OperacoesSpinRadiciacao.grid(column=5, row=1, padx=10)
        OperacoesSpinRadiciacao.set(
            m.operacoes_disponiveis[e.RADICIACAO + 3]
        )

        # Labelframe para os limites
        BaseLabelframeLimites = ttk.Labelframe(
            rootFrameBase,
            text="Limites",
            padding=10
        )
        BaseLabelframeLimites.grid(
            column=0,
            row=1,
            sticky=(N,S,E,W)
        )
        BaseLabelframeLimites.columnconfigure(
            index=(0, 1, 2),
            pad=60
        )

        # Label 'de'
        LimitesLabelDe = ttk.Label(
            BaseLabelframeLimites,
            text="De"
        )
        LimitesLabelDe.grid(column=1, row=0)

        # Label 'ate'
        LimitesLabelAte = ttk.Label(
            BaseLabelframeLimites,
            text="Até"
        )
        LimitesLabelAte.grid(column=2, row=0)

        # Label K
        LimitesLabelK = ttk.Label(
            BaseLabelframeLimites,
            text="K (coeficientes):"
        )
        LimitesLabelK.grid(column=0, row=1)
        # Spin KDe
        LimitesSpinvarKDe = IntVar()
        LimitesSpinKDe = ttk.Spinbox(
            BaseLabelframeLimites,
            from_=-100,
            to=100,
            textvariable=LimitesSpinvarKDe
        )
        LimitesSpinKDe.configure(width=3)
        LimitesSpinKDe.grid(column=1, row=1)
        LimitesSpinKDe.set(m.k_min)
        # Spin KAte
        LimitesSpinvarKAte = IntVar()
        LimitesSpinKAte = ttk.Spinbox(
            BaseLabelframeLimites,
            from_=-100,
            to=100,
            textvariable=LimitesSpinvarKAte
        )
        LimitesSpinKAte.configure(width=3)
        LimitesSpinKAte.grid(column=2, row=1)
        LimitesSpinKAte.set(m.k_max)

        # Label X
        LimitesLabelX = ttk.Label(
            BaseLabelframeLimites,
            text="X (variável):"
        )
        LimitesLabelX.grid(column=0, row=2)
        # Spin XDe
        LimitesSpinvarXDe = IntVar()
        LimitesSpinXDe = ttk.Spinbox(
            BaseLabelframeLimites,
            from_=-100,
            to=100,
            textvariable=LimitesSpinvarXDe
        )
        LimitesSpinXDe.configure(width=3)
        LimitesSpinXDe.grid(column=1, row=2)
        LimitesSpinXDe.set(m.x_min)
        # Spin XAte
        LimitesSpinvarXAte = IntVar()
        LimitesSpinXAte = ttk.Spinbox(
            BaseLabelframeLimites,
            from_=-100,
            to=100,
            textvariable=LimitesSpinvarXAte
        )
        LimitesSpinXAte.configure(width=3)
        LimitesSpinXAte.grid(column=2, row=2)
        LimitesSpinXAte.set(m.x_max)

        # Label Precisao Decimal
        LimitesLabelPrecisaoDecimal = ttk.Label(
            BaseLabelframeLimites,
            text="Precisão decimal:"
        )
        LimitesLabelPrecisaoDecimal.grid(column=0, row=3)
        # Spin Precisao Decimal De
        LimitesSpinPrecisaoDecimalDe = ttk.Spinbox(
            BaseLabelframeLimites
        )
        LimitesSpinPrecisaoDecimalDe.configure(state="disabled", width=3)
        LimitesSpinPrecisaoDecimalDe.grid(column=1, row=3)
        LimitesSpinPrecisaoDecimalDe.set(0)
        # Spin Precisao Decimal Ate
        LimitesSpinvarPrecisaoDecimalAte = IntVar()
        LimitesSpinPrecisaoDecimalAte = ttk.Spinbox(
            BaseLabelframeLimites,
            from_=0,
            to=4,
            textvariable=LimitesSpinvarPrecisaoDecimalAte
        )
        LimitesSpinPrecisaoDecimalAte.configure(width=3)
        LimitesSpinPrecisaoDecimalAte.grid(column=2, row=3)
        LimitesSpinPrecisaoDecimalAte.set(m.precisao_decimal)

        # Label Equacoes
        LimitesLabelEquacoes = ttk.Label(
            BaseLabelframeLimites,
            text="Equações:"
        )
        LimitesLabelEquacoes.grid(column=0, row=4)
        # Spin Equacoes De
        LimitesSpinEquacoesDe = ttk.Spinbox(
            BaseLabelframeLimites
        )
        LimitesSpinEquacoesDe.configure(state="disabled", width=3)
        LimitesSpinEquacoesDe.grid(column=1, row=4)
        LimitesSpinEquacoesDe.set(0)
        # Spin Equacoes Ate
        LimitesSpinvarEquacoesAte = IntVar()
        LimitesSpinEquacoesAte = ttk.Spinbox(
            BaseLabelframeLimites,
            from_=0,
            to=100,
            textvariable=LimitesSpinvarEquacoesAte
        )
        LimitesSpinEquacoesAte.configure(width=3)
        LimitesSpinEquacoesAte.grid(column=2, row=4)
        LimitesSpinEquacoesAte.set(m.eqs)

        BaseButtonGerar = ttk.Button(
            rootFrameBase,
            text="Gerar",
            command=self.gerar,
            padding=10
        )
        BaseButtonGerar.grid(
            column=0,
            row=2,
            pady=10
        )
