#!/bin/bash

# Primeiro grep realiza o filtro por codigo da prova, segundo grep realiza o filtro em cima da primeiro pegando por 1,1,1,1
# Terceiro grep realiza o filtro em cima do segundo grep e pega a primeira ocorrencia da prova de ingles (0) ou espanhol (1)

grep ,199, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >  t_questao_2014.csv
grep ,200, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,201, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,202, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,216, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv

grep ,195, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,196, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,197, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,198, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,215, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv

grep ,203, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,204, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,205, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,206, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,213, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv
grep ,217, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv

grep ,207, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv 
grep ,208, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv 
grep ,209, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv 
grep ,210, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv 
grep ,214, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv 
grep ,218, microdados_enem_2014.csv | grep 1,1,1,1 | grep -m1 -e [A-Z],1,[A-Z] -e [A-Z],0,[A-Z] >> t_questao_2014.csv


# Executando o primeiro script para extrair os dados 
python t_questao_2014.py

# Executando o segundo script para extrair os dados
python t_questao_2014_1.py

# Retirando as linhas em brancos
sed '/^$/d' t_questao_2014_2.csv > t_questao_2014_3.csv

# Eliminando arquivos
rm t_questao_2014.csv t_questao_2014_1.csv t_questao_2014_2.csv   

# Colocar vírgulas no final da linha
grep ,[A-Z],[A-Z] t_questao_2014_3.csv > t_questao_2014_4.csv 
grep -v ,[A-Z],[A-Z] t_questao_2014_3.csv | sed 's/$/,null/g' >> t_questao_2014_4.csv

sort -n -t, -k1 t_questao_2014_4.csv > t_questao_final.csv

# Eliminando arquivos
rm t_questao_2014_3.csv t_questao_2014_4.csv

# Load para a tabela
./load_tabela.sh