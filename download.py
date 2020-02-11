#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:40:48 2019

@author: usuario
"""
import requests
import pandas as pd


url = 'http://www.agrariasusp.com.br/agrariasusp01/NOAAMO.TXT'

r = requests.get(url)

with open('dados.txt', 'w') as f:
	f.write(r.content)

arquivo = open('dados.txt', 'r')
df = arquivo.read()
arquivo.close()

print(df)
