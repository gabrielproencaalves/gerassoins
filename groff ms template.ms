
\# $ groff -e -Tpdf groff\ ms\ template.ms -ms -P-pa4 -p > ARQUIVO.pdf

\# Tamanho da fonte
.nr PS 12p

\# Divida o arquivo em duas colunas
.2C

\# Defina $ como o delimitador de equações
.EQ
delim $$
.EN

\# Declare e defina a variável de contagem para
\# a geração das equações
.nr step 0 1

\# A seguir, está um modelo de como
\# será a notação de cada linha no formato groff
\n+[step]. $ f(x) = ax + b $
.br
