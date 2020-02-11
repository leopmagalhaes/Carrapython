#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:54:15 2020

@author: usuario
"""
import cv2
import numpy as np


im =  cv2.imread("area_1912.JPG")
im = cv2.resize(im,None,fx=0.2,fy=0.2)

avg_amostras = []
for n in range(6):
    r = cv2.selectROI(im)
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv2.imshow("Image", imCrop)
    canalAzul, canalVerde, canalVermelho = cv2.split(imCrop)
    gn = np.average(canalVerde, axis=0)
    gn = np.average(gn, axis=0)
    rn = np.average(canalVermelho, axis=0)
    rn = np.average(rn, axis=0)
    MPRI = (gn - rn) / (gn + rn)
    #print('', avg_color)
    avg_amostras.append(MPRI)
    print(avg_amostras)

cv2.destroyAllWindows()

braquiaria1 = avg_amostras[0]
braquiaria2 = avg_amostras[1]
braquiaria3 = avg_amostras[2]
solo1 = avg_amostras[3]
solo2 = avg_amostras[4]
solo3 = avg_amostras[5]

medio_braquiaria = (((braquiaria1 + braquiaria2 + braquiaria3)/3))
medio_solo = (((solo1 + solo2 + solo3)/3))

print('Media do solo', medio_solo)
print('Selecione area a ser classificada')


r = cv2.selectROI(im)
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv2.imshow("Image", imCrop)
canalAzul, canalVerde, canalVermelho = cv2.split(imCrop)
gn = np.average(canalVerde, axis=0)
gn = np.average(gn, axis=0)
rn = np.average(canalVermelho, axis=0)
rn = np.average(rn, axis=0)
MPRI2 = (gn - rn) / (gn + rn)


ponto1 = MPRI2

D1 = (ponto1 - medio_braquiaria)
D2 = (ponto1 - medio_solo)
print(D1)
print(D2)

if D1 > D2:
    print('')
    print('SOLO')
else:
    print('')
    print('BRAQUIARIA')
        
        
cv2.waitKey(0)

cv2.destroyAllWindows()