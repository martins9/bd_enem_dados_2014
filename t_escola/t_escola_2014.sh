#!/bin/bash

# Executa o programa python
python t_escola_2014.py

# Excluindo as linhas que não tem dados
sed '/,,,,/d' t_escola_2014.csv > t_escola_2014_1.csv

# Deletando arquivo  
rm t_escola_2014.csv

# Excluindo linhas com esse padrao
sed '/,,null,,,/d' t_escola_2014_1.csv > t_escola_2014_2.csv

# Deletando arquivo
rm t_escola_2014_1.csv

# Eliminando as linhas em branco
sed 's/ //g' t_escola_2014_2.csv > t_escola_2014_3.csv

# Deletando arquivo
rm t_escola_2014_2.csv

# Eliminando as linhas repetidas com base na primeira coluna
sort -u t_escola_2014_3.csv > t_escola_2014_final.csv

# Deletando arquivo 
rm t_escola_2014_3.csv

# Fazendo o load para a tabela
./load_tabela.sh
