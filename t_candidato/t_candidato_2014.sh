#!/bin/bash

# Pegando todos os dados para o candidato 
python t_candidato_2014.py

# Colando null nos espacos ,, 
sed 's/,,/,null,/g' t_candidato_2014.csv > t_candidato_2014_2.csv

# Excluindo o arquivo
rm t_candidato_2014.csv

# Colando null nos lugares de "." e "*"
cat t_candidato_2014_2.csv | sed 's/,\.,/,null,/g' | sed 's/,\*,/,null,/g' > t_candidato_final.csv

# Excluindo o arquivo
rm t_candidato_2014_2.csv

# Load para o table candidato
./load_tabela.sh
