from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Gerassoins")

rootFrameBase = ttk.Frame(root, padding=10)
rootFrameBase.grid()

BaseLabelframeOperacoes = ttk.LabelFrame(rootFrameBase, text="Operações", padding=10)
BaseLabelframeOperacoes.grid()

OperacoesLabelSoma = ttk.Label(BaseLabelframeOperacoes, text="+")
OperacoesLabelSoma.grid(column=0, row=0, padx=10)

OperacoesLabelSubtracao = ttk.Label(BaseLabelframeOperacoes, text="-")
OperacoesLabelSubtracao.grid(column=1, row=0, padx=10)

OperacoesLabelMultiplicacao = ttk.Label(BaseLabelframeOperacoes, text="×")
OperacoesLabelMultiplicacao.grid(column=2, row=0, padx=10)



root.mainloop()
