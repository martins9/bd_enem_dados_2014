#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open ('t_preenche_2014_0.csv', 'r')
arquivosaida = open ("t_preenche_2014_1.csv", 'w')

for linha in arquivoentrada:
    a=linha.replace("\r\n","\n")

    arquivosaida.writelines(a)

arquivoentrada.close()
arquivosaida.close()
