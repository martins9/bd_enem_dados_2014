#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open ('microdados_enem_2014.csv', 'r')
arquivosaida = open ('t_realiza_1.csv', 'w')

for linha in arquivoentrada:
	texto = linha.split(",")
	
	# Pegando os dados nos intervalos
	arquivosaida.writelines (texto[0]+",2014"+texto[66]+","+texto[62]+","+texto[70]+'\n')
	arquivosaida.writelines (texto[0]+",2014"+texto[67]+","+texto[63]+","+texto[71]+'\n')
	arquivosaida.writelines (texto[0]+",2014"+texto[68]+","+texto[64]+","+texto[72]+'\n')
	arquivosaida.writelines (texto[0]+",2014"+texto[69]+","+texto[65]+","+texto[73]+'\n')

arquivoentrada.close()
arquivosaida.close()