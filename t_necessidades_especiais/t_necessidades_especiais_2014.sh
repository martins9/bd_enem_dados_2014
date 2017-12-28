#!/bin/bash

# Executa o programa python
python t_necessidades_especiais_2014.py

# Elimina as linhas que contem so zero
sed '/0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0/d' t_necessidadesespeciais_1.csv > t_necessidadesespeciais_final.csv

# Deletando o arquivo
#rm t_necessidadesespeciais_1.csv

# Fazendo a carga dos dados
#./load_tabela.sh
