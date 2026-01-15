# ⚠️ ATENÇÃO. WARNING ⚠️

Por razões pessoais, todos os meus repositórios do github, incluindo este, estão em processo de transferência a outra plataforma. Por isso, este repositório será excluído no dia 21 de janeiro de 2026, mas sua continuação poderá ser encontrada em **codeberg ponto org barra Gabrielovsky barra gerassoins**.

For personal reasons, all my github repositories, including this one, are in the process of transferring to another platform. Therefore, this repository will be deleted on January 21, 2026, but its continuation can be found in **codeberg dot org slash Gabrielovsky slash gerassoins**.

# gerassoins
Um gerador de equações para fins educacionais. An equations generator for educational purposes.

## Requirements

* Python 3.*
* GNU Roff 1.22.4 (a.k.a. groff)

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

## História

No fim do ano de 2024, prestei o Exame Nacional de Ensino Médio (ENEM) como treineiro, porque desejava saber quais eram meus pontos fracos na prova para corrigir-me e conseguir ingressar futuramente em um curso de ensino superior. Porém, no segundo dia da prova, percebi que minhas resoluções das questões de Matemática eram lentas demais, embora corretas, pois não possuía prática em desenvolver equações de primeiro grau, o tipo de equação mais comum naquela prova. Por isso, decidi treinar o isolamento de variáveis e a resolução de equações por meio de baterias de exercícios. Ao procurar por algum programa confiável capaz de gerar baterias dessas equações para sua impressão em papel, constatei que isso não existia, não do modo que eu precisava. A partir de então, aceitei que eu não solucionaria o problema original das equações se não desenvolvesse um software para solucioná-lo. Por essa razão, comecei a idealizar em uma sulfite o atual gerassoins, definindo a estrutura de dados mais básica, pela qual o programa poderia funcionar e representar qualquer expressão matemática, a exp, cuja definição permanece praticamente a mesma desde as primeiras versões do projeto.
