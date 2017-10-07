#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open('t_preenche_2014_1.csv', 'r')
arquivosaida = open ('t_preenche_2014_2.csv', 'w')

for linha in arquivoentrada:
    texto = linha.split(",")

    if texto[2] != '\n' and texto[2] != '\r\n':
        arquivosaida.writelines (texto[0]+","+texto[1]+","+texto[2])

arquivoentrada.close()
arquivosaida.close()