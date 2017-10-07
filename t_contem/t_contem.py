#!/usr/bin/python
# encoding: utf-8

arquivo1=open('tabela_contem_2014.csv','r')
arquivo2=open('t_contem_final.csv','w')

for f in arquivo1:
	texto=f.split(',')
	
	if (texto[2]=='CH' and (texto[0]=='195' or texto[0]=='196' or texto[0]=='197' or texto[0]=='198' or texto[0]=='215')): # Prova de CH
		for i in range(1,46):
			a='2014'+texto[0]+','+'2014'+texto[0]+str(i)+'\n'
			arquivo2.writelines(a)
	elif (texto[2]=='CN' and (texto[0]=='199' or texto[0]=='200' or texto[0]=='201' or texto[0]=='202' or texto[0]=='216')): # Prova de CN
		for i in range(46,91):
			a='2014'+texto[0]+','+'2014'+texto[0]+str(i)+'\n'
			arquivo2.writelines(a)
	elif (texto[2]=='LC' and (texto[0]=='203' or texto[0]=='204' or texto[0]=='205' or texto[0]=='206' or texto[0]=='213' or texto[0]=='217')): # Prova de LC 
		for i in range(91,136):
			a='2014'+texto[0]+','+'2014'+texto[0]+str(i)+'\n'
			arquivo2.writelines(a)
	elif (texto[2]=='MT' and (texto[0]=='207' or texto[0]=='208' or texto[0]=='209' or texto[0]=='210' or texto[0]=='214' or texto[0]=='218')): # Prova de MT
		for i in range(136,181):
			a='2014'+texto[0]+','+'2014'+texto[0]+str(i)+'\n'
			arquivo2.writelines(a)

arquivo1.close()
