#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open ('microdados_enem_2014.csv', 'r')
arquivosaida = open ('t_escola_2014.csv', 'w')

for linha in arquivoentrada:
        texto = linha.split(",")

        # Quando tem intervalos
        arquivosaida.writelines (texto[7]+","+texto[8]+",null,"+texto[12]+","+texto[13]+","+texto[14]+' \n')

arquivoentrada.close()
arquivosaida.close()

