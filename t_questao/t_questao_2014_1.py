#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivo1=open('t_questao_2014_1.csv','r')
arquivo2=open('t_questao_2014_2.csv','w')

z=0
y=0

for line in arquivo1:

	k=1	#Agora está certo só falta mudar as letras lá em cima
	l=6
	m=11
	
	p=line.split(",")
	
	
	if (p[0]=='195' or p[0]=='196' or p[0]=='197' or p[0]=='198' or p[0]=='215'): # Prova de CH
		for i in range(1,46):
			b='2014'+p[0]+str(i)+","+p[i]+'\n'
			arquivo2.writelines(b)
	elif (p[0]=='199' or p[0]=='200' or p[0]=='201' or p[0]=='202' or p[0]=='216'): # Prova de CN
		for i in range(46,91):
			z=z+1

			b='2014'+p[0]+str(i)+","+p[z]+'\n'
			arquivo2.writelines(b)
		z=0
	elif (p[0]=='203' or p[0]=='204' or p[0]=='205' or p[0]=='206' or p[0]=='213' or p[0]=='217'): # Prova de LC
		for i in range(91,136):						
			if (i <=95):
				b='2014'+p[0]+str(i)+","+p[k]+","+p[l]+'\n'
				arquivo2.writelines(b)
				k=k+1
				l=l+1
			elif (i >= 96):
				b='2014'+p[0]+str(i)+","+p[m]+'\n'
				arquivo2.writelines(b)
				m=m+1

	elif(p[0]=='207' or p[0]=='208' or p[0]=='209' or p[0]=='210' or p[0]=='214' or p[0]=='218'): # Prova de MT
		for i in range(136,181):
			y=y+1

			b='2014'+p[0]+str(i)+","+p[y]+'\n'
			arquivo2.writelines(b)

		y=0
	
arquivo1.close()
arquivo2.close()