#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open ('t_realiza_1.csv', 'r')
arquivosaida = open ('t_realiza_final.csv', 'w')

for linha in arquivoentrada:
	texto = linha.split(",")

	# Pegando os dados dados somente que nao tiver '\n' no texto[3]
	if texto[3]!='\n':
		arquivosaida.writelines (texto[0]+","+texto[1]+","+texto[2]+","+texto[3])
	else:
		continue

arquivoentrada.close()
arquivosaida.close()