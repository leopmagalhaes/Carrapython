#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 08:55:45 2019

@author: usuario
"""

import requests


url = 'http://www.agrariasusp.com.br/agrariasusp01/NOAAMO.TXT'
url2= 'http://www.agrariasusp.com.br/agrariasusp01/NOAAYR.TXT'

r = requests.get(url)

with open('dados.txt', 'wb') as f:
	f.write(r.content)

arquivo = open('dados.txt', 'rb')


df = arquivo.read()
arquivo.close()

r2 = requests.get(url2)

with open('dados2.txt', 'wb') as f:
	f.write(r2.content)

arquivo = open('dados2.txt', 'rb')
df2 = arquivo.read()
arquivo.close()
input("Pressione ENTER para visualizar os dados anuais")
print(df2)
input("Pressione ENTER para visualizar os dados mensais")
print(df)