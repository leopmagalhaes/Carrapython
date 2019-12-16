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

with open('dados.txt', 'w') as f:
	f.write(r.content)

arquivo = open('dados.txt', 'r')
df = arquivo.read()
arquivo.close()

r2 = requests.get(url2)

with open('dados2.txt', 'w') as f:
	f.write(r2.content)

arquivo = open('dados2.txt', 'r')
df2 = arquivo.read()
arquivo.close()
raw_input("Pressione ENTER para visualizar os dados anuais")
print(df2)
raw_input("Pressione ENTER para visualizar os dados mensais")
print(df)