#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivoentrada = open('microdados_enem_2014_1.csv', 'r')
arquivosaida = open('t_responde_2014_1.csv', 'w')

k = 0
p = 45
o = 90
j = 135

for linha in arquivoentrada:
    texto = linha.split(",")

    for char in texto[75]:  # Resposta da Prova de CH
        k = k + 1
        a1 = texto[0] + "," + '2014' + texto[67] + str(k) + "," + char + '\n'
        arquivosaida.writelines(a1)

    for char in texto[74]:  # Resposta da Prova de CN
        p = p + 1
        a1 = texto[0] + "," + '2014' + texto[66] + str(p) + "," + char + '\n'
        arquivosaida.writelines(a1)

    T=texto[76].replace("9","") # Tirando o "9" da Resposta da Prova de LC

    for char in T:  # Resposta da Prova de LC
        o = o + 1
        a1 = texto[0] + "," + '2014' + texto[68] + str(o) + "," + char + '\n'
        arquivosaida.writelines(a1)

    for char in texto[77]:  # Resposta da Prova de MT
        j = j + 1
        a1 = texto[0] + "," + '2014' + texto[69] + str(j) + "," + char + '\n'
        arquivosaida.writelines(a1)

    k = 0
    p = 45
    o = 90
    j = 135

arquivoentrada.close()
arquivosaida.close()
