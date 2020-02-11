#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:59:21 2019

@author: usuario
"""
import requests
 
url = 'http://www.agrariasusp.com.br/agrariasusp01/Images/Profile1/Rain.gif'
 
r = requests.get(url)
with open("precipitacao.gif", "wb") as code:
    code.write(r.content)

