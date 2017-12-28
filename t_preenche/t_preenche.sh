#!/usr/bin/env bash
# !/bin/bash

# Extraindo os dados
python t_preenche_0.py

# Limpando os dados
python t_preenche_1.py
python t_preenche_2.py

# Excluindo arquivos de base
rm t_preenche_2014_0.csv t_preenche_2014_1.csv

# Pegando o maior divisor
TAMANHO=$(python t_preenche_divisor.py)

# Achando o caminho
path1=$(pwd)

# Fazendo split dos arquivos e colocando 
split -d -a6 -l $TAMANHO --additional-suffix=.csv t_preenche_2014_2.csv $path1/t_preenche/t_preenche_2014_

# Excluindo os arquivos de base
rm t_preenche_2014_2.csv

# Contando quantos arquivos tem na pasta
QTD_ARQ=$(find $path1/t_preenche/ -type f | wc -l)

data=$(date "+%d/%m/%Y %H:%M:%S") 
echo "------------- START:" $data "-------------" > t_preenche_log.txt

QTD_ARQ1=$((QTD_ARQ-1))
# Fazendo o Load das tabelas
for i in $(seq -f "%06g" 0 $QTD_ARQ1)
do
	time (psql -h localhost -d bd_enem_dados -U anacrl -c "\copy preenche from $path1/t_preenche/t_preenche_2014_$i.csv with delimiter as ',' NULL AS 'null' csv") &>> t_preenche_log.txt
	
done

data1=$(date "+%d/%m/%Y %H:%M:%S")
echo "---------------END:" $data1 "-------------------------" >> t_preenche_log.txt
