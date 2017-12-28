#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open ('microdados_enem_2014.csv', 'r')
arquivosaida = open ('t_municipio_2014.csv', 'w')

for linha in arquivoentrada:
	texto = linha.split(",")
	
	arquivosaida.writelines (texto[2]+","+texto[3]+","+texto[5]+'\n')
	arquivosaida.writelines (texto[8]+","+texto[9]+","+texto[11]+'\n')
	arquivosaida.writelines (texto[58]+","+texto[59]+","+texto[61]+'\n')

arquivoentrada.close()
arquivosaida.close()