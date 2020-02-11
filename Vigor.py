#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:03:14 2019

@author: usuario
"""


import cv2
import numpy as np

im = cv2.imread("area_1912.JPG", 1) #abre a imagem desejada
im = cv2.resize(im,None,fx=0.2,fy=0.2)
r = cv2.selectROI(im) #selecionada a regiao a ser calculada os indices
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]


canalAzul, canalVerde, canalVermelho = cv2.split(imCrop) #obtem as bandas de cor no RGB
avg_color_per_row1 = np.average(canalVerde, axis=0) #calcula a media por linha de cada banda na area selecionada
avg_color_per_row2 = np.average(canalVermelho, axis=0)
avg_color_per_row3 = np.average(canalAzul, axis=0)

avg_color1 = np.average(avg_color_per_row1, axis=0) #calcula a media geral de cada banda na area selecionada
avg_color2 = np.average(avg_color_per_row2, axis=0)
avg_color3 = np.average(avg_color_per_row3, axis=0)

MPRI = (avg_color1 - avg_color2)/(avg_color1 + avg_color2) #calcula o indice MPRI
SAVI = (1.5)*(avg_color1 - avg_color2)/(avg_color1 + avg_color2 + 0.5) #calcula o SAVI adaptado
Gn = (avg_color1)/(avg_color1 + avg_color2 + avg_color3) #calcula o verde normalizado
Rn = (avg_color2)/(avg_color1 + avg_color2 + avg_color3) #calcula o vermelho normalizado
Bn = (avg_color3)/(avg_color1 + avg_color2 + avg_color3) #calcula o azul normalizado

print('MPRI =', MPRI)
print('SAVI =', SAVI)
print('Gn =', Gn)
print('Rn =', Rn)
print('Bn =', Bn)

cv2.waitKey(0)

cv2.destroyAllWindows()