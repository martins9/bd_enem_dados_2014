#!/bin/bash

# Executando o comando de retirada de dados
python t_contem.py

# Fazendo load para a tabela
./load_tabela.sh
