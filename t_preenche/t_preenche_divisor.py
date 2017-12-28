#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

arquivoentrada = open ('t_preenche_2014_2.csv', 'r')

i=0
k=[]

if not os.path.exists("t_preenche"):
        os.makedirs("t_preenche")

for linha in arquivoentrada:
	if (linha !='\n'):
		i=i+1
		a=i/2
for j in range(a,i):
    if (a%j==0):
		k.append(j)

print k[-1]

arquivoentrada.close()
