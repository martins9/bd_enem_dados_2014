#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open ('microdados_enem_2014.csv', 'r')
arquivosaida = open ('t_candidato_2014.csv', 'w')

for linha in arquivoentrada:
	texto = linha.split(",")


	arquivosaida.writelines (texto[0]+","+texto[2]+","+texto[18]+","+texto[54]+","+texto[7]+",2,"+
		texto[17]+","+texto[23]+","+texto[26]+","+texto[22]+","+texto[25]+","+texto[27]+","+texto[1]+
		","+texto[15]+","+texto[16]+","+texto[84]+","+texto[85]+","+texto[86]+","+
    	texto[87]+","+texto[88]+","+texto[89]+","+texto[78]+","+texto[83]+'\n')

arquivoentrada.close()
arquivosaida.close()
