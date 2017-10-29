#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivo1=open('t_questao_2014.csv','r')
arquivo2=open('t_questao_2014_1.csv','w')

a=b=c=d=e=0 #CN
f=g=h=i=j=0 # CH
k=l=m=n=o=p1=0 # LC
q=r=s=t=u=v=0 # MT

for line in arquivo1:
	p=line.split(",")

	# Prova de CN
	if ((p[66]=='199' and a==0) and (p[78]=='0' or p[78]=='1')): # Filtro por codigo da prova ingles ou espanhol
		a=a+1
		if (a==1):
			arquivo2.writelines(p[66])
			for char in p[79]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (a>1):
			continue
	elif ((p[66]=='200' and b==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		b=b+1
		if (b==1):
			arquivo2.writelines(p[66])
			for char in p[79]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (b>1):
			continue	
	elif ((p[66]=='201' and c==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		c=c+1
		if (c==1):
			arquivo2.writelines(p[66])
			for char in p[79]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (c>1):
			continue
	elif ((p[66]=='202' and d==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		d=d+1
		if (d==1):
			arquivo2.writelines(p[66])
			for char in p[79]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (d>1):
			continue
	elif ((p[66]=='216' and e==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		e=e+1
		if (e==1):
			arquivo2.writelines(p[66])
			for char in p[79]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (e>1):
			continue
	  
	# Prova de CH
	elif ((p[67]=='195' and f==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		f=f+1
		if (f==1):
			arquivo2.writelines(p[67])
			for char in p[80]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (f>1):
			continue 	
	elif ((p[67]=='196' and g==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		g=g+1
		if (g==1):
			arquivo2.writelines(p[67])
			for char in p[80]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (g>1):
			continue
	elif ((p[67]=='197' and h==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		h=h+1
		if (h==1):
			arquivo2.writelines(p[67])
			for char in p[80]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (h>1):
			continue
	elif ((p[67]=='198' and i==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		i=i+1
		if (i==1):
			arquivo2.writelines(p[67])
			for char in p[80]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (i>1):
			continue
	elif ((p[67]=='215' and j==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		j=j+1
		if (j==1):
			arquivo2.writelines(p[67])
			for char in p[80]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (j>1):
			continue
	
	# Prova de LC
	elif ((p[68]=='203' and k==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		k=k+1
		if (k==1):
			arquivo2.writelines(p[68])
			for char in p[81]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (k>1):
			continue      	
	elif ((p[68]=='204' and l==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		l=l+1
		if (l==1):
			arquivo2.writelines(p[68])
			for char in p[81]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (l>1):
			continue 
	elif ((p[68]=='205' and m==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		m=m+1
		if (m==1):
			arquivo2.writelines(p[68])
			for char in p[81]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (m>1):
			continue  
	elif ((p[68]=='206' and n==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		n=n+1
		if (n==1):
			arquivo2.writelines(p[68])
			for char in p[81]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (n>1):
			continue
	elif ((p[68]=='213' and o==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		o=o+1
		if (o==1):
			arquivo2.writelines(p[68])
			for char in p[81]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (o>1):
			continue
	elif ((p[68]=='217' and p1==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		p1=p1+1
		if (p1==1):
			arquivo2.writelines(p[68])
			for char in p[81]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (p1>1):
			continue

	# Prova de MT
	elif ((p[69]=='207' and q==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		q=q+1
		if (q==1):
			arquivo2.writelines(p[69])
			for char in p[82]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (q>1):
			continue
	elif ((p[69]=='208' and r==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		r=r+1
		if (r==1):
			arquivo2.writelines(p[69])
			for char in p[82]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (r>1):
			continue
	elif ((p[69]=='209' and s==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		s=s+1
		if (s==1):
			arquivo2.writelines(p[69])
			for char in p[82]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (s>1):
			continue
	
	elif ((p[69]=='210' and t==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		t=t+1
		if (t==1):
			arquivo2.writelines(p[69])
			for char in p[82]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (t>1):
			continue
	elif ((p[69]=='214' and u==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		u=u+1
		if (u==1):
			arquivo2.writelines(p[69])
			for char in p[82]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (u>1):
			continue
	elif ((p[69]=='218' and v==0) and (p[78]=='1' or p[78]=='0')): # Filtro por codigo da prova ingles ou espanhol
		v=v+1
		if (v==1):
			arquivo2.writelines(p[69])
			for char in p[82]: # Separando cada resposta do gabarito
				a1=","+char,
				arquivo2.writelines(tuple(a1))
			arquivo2.writelines('\n')
		elif (v>1):
			continue

arquivo1.close()
arquivo2.close()