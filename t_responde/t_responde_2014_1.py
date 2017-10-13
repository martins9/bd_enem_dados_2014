#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

arquivoentrada = open ('t_responde_2014_1.csv', 'r')
arquivosaida = open ('t_responde_2014_2.csv', 'w')


if not os.path.exists("t_responde"):
        os.makedirs("t_responde")

for linha in arquivoentrada:
    texto=linha.split(",")

    if texto[2]!='.':
        arquivosaida.writelines(texto[0] + "," + texto[1] + "," + texto[2])
    elif texto[2]!='*':
        arquivosaida.writelines(texto[0] + "," + texto[1] + "," + texto[2])
    elif (not texto[2].isspace()):
        arquivosaida.writelines(texto[0] + "," + texto[1] + "," + texto[2])

arquivoentrada.close()
arquivosaida.close()