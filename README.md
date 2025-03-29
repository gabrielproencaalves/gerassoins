# gerassoins
Um gerador de equações. An equations generator.

## Requirements

* Python 3.*
* GNU Roff (a.k.a. groff)

## Usage

1. If you want, set values to the forward initial program variables: operacoes_disponiveis, k_max, k_min, x_max, x_min, eqs, caminho_saida and precisao_decimal.
2. Then, run the program as a simple python3 script:
```
$ python3 main.py
```

3. With the previous command, the equations structure file, and his answers file, will be generated. To convert them into pdf files, run:
```
$ groff -e -ms -Tpdf -P-pa4 OUTPUT.MS > OUTPUT.PDF
$ groff -e -ms -Tpdf -P-pa4 ANSWERS_OUTPUT.MS > ANSWERS_OUTPUT.PDF
```

Remember: the OUTPUT.MS must coincide with filename stored in variable caminho_saida.
