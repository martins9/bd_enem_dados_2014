#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open ('t_municipio_2014_2.csv', 'r')
arquivosaida = open ('t_municipio_2014_final.csv', 'w')

for linha in arquivoentrada:
	texto = linha.split(",")
	
	if texto[2]=='AC\n':
		a=texto[2]='1\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='AL\n':
		a=texto[2]='2\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='AP\n':
		a=texto[2]='3\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='AM\n':
		a=texto[2]='4\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='BA\n':
		a=texto[2]='5\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='CE\n':
		a=texto[2]='6\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='DF\n':
		a=texto[2]='7\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='ES\n':
		a=texto[2]='8\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='GO\n':
		a=texto[2]='9\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='MA\n':
		a=texto[2]='10\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)				
	elif texto[2]=='MT\n':
		a=texto[2]='11\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='MS\n':
		a=texto[2]='12\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='MG\n':
		a=texto[2]='13\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='PA\n':
		a=texto[2]='14\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='PB\n':
		a=texto[2]='15\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='PR\n':
		a=texto[2]='16\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='PE\n':
		a=texto[2]='17\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='PI\n':
		a=texto[2]='18\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='RJ\n':
		a=texto[2]='19\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='RN\n':
		a=texto[2]='20\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='RS\n':
		a=texto[2]='21\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='RO\n':
		a=texto[2]='22\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='RR\n':
		a=texto[2]='23\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='SC\n':
		a=texto[2]='24\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='SP\n':
		a=texto[2]='25\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='SE\n':
		a=texto[2]='26\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)
	elif texto[2]=='TO\n':
		a=texto[2]='27\n'
		b=texto[0]+','+texto[1]+','+a
		arquivosaida.writelines(b)

arquivoentrada.close()
arquivosaida.close()