#!/bin/bash

# Extraindo todos os dados para o candidato 
python t_candidato_2014.py

# Substituindo ",," por ",null,"
sed 's/,,/,null,/g' t_candidato_2014.csv > t_candidato_2014_2.csv

# Excluindo o arquivo gerado
rm t_candidato_2014.csv

# Substituindo "." e "*" por ",null,"
cat t_candidato_2014_2.csv | sed 's/,\.,/,null,/g' | sed 's/,\*,/,null,/g' > t_candidato_final.csv

# Excluindo o arquivo gerado
rm t_candidato_2014_2.csv

# Realizando o load dos dados para a tabela Candidato
./load_tabela.sh
