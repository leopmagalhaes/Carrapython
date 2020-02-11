#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:43:04 2019

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
print(df2)


Tmax = input("Digite T Max Mensal (Coluna MAX correspondente ao mes desejado):")
Tmin = input("Digite T Min Mensal (Coluna MIN correspondente ao mes desejado):")
Tef = 0.36*(3 * Tmax - Tmin)

TA = input("Digite T Media Anual (Final da Tabela, na coluna correspondente a MEAN):")
I = 12*(0.2 * TA)**1.514

A = 0.49239 + (1.792*((10**(-2))*I))- (7.71*(10**(-5))*I**(2)) + (6.75*(10**(-7))*(I**(3)))

ETO = 16 * (((10*Tef)/I)**A)
ETOd = ETO / 30

Kc = input("Digite o Kc da cultura:")
ETC = ETOd * Kc
print("A evapotranspiracao diaria da cultura e: ", ETC)
raw_input("Pressione ENTER para continuar")

print(df)
Chuva = input("Digita a quantidade de chuva do dia anterior (Coluna RAIN correspondente ao dia desejado):")
Irrigacao = ((ETC-Chuva) * 64)
Vazao = input("Digite a vazao do aspersor em l/s:")
Tempo = ((Irrigacao / Vazao)/60)/2
if Tempo < 0:
    print("NAO E NECESSARIO IRRIGAR")
else:
    print("O tempo de irrigacao por parcela e: ", Tempo)