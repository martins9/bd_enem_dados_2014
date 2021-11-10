#!/usr/bin/python
# -*- coding: utf-8 -*-

# Abrindo o arquivo para a leitura e escrita
arquivoentrada = open ('microdados_enem_2014.csv', 'r')
arquivosaida = open ('t_candidato_2014.csv', 'w')

# Percorrendo cada linha do arquivo
for linha in arquivoentrada:
	texto = linha.split(",") # Realizando o split em cada linha e alocando na variável
	
	# Montando a nova linha somente com os dados necessarios para a tabela, utilizando a posicao
	# da lista. Apos montar a linha nova, entao grava no arquivosaida. 
	arquivosaida.writelines (texto[0]+","+texto[2]+","+texto[18]+","+texto[54]+","+texto[7]+",2,"+
		texto[17]+","+texto[23]+","+texto[26]+","+texto[22]+","+texto[25]+","+texto[27]+","+texto[1]+
		","+texto[15]+","+texto[16]+","+texto[84]+","+texto[85]+","+texto[86]+","+
    	texto[87]+","+texto[88]+","+texto[89]+","+texto[78]+","+texto[83]+'\n')

# Fechando os arquivos abertos
arquivoentrada.close()
arquivosaida.close()
