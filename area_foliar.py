#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:43:22 2019

@author: usuario
"""
import cv2
from matplotlib import pyplot as plt

# pega os 4 vizinhos de uma coordenada
def vizinhos(img, y, x):
    vizinhos = [];
    if (y + 1 < len(img)):
        vizinhos.append((y + 1, x));
    if (y - 1 >= 0):
        vizinhos.append((y - 1, x));
    if (x + 1 < len(img[y])):
        vizinhos.append((y, x + 1));
    if (x - 1 >= 0):
        vizinhos.append((y, x - 1));
    return vizinhos;

# busca em largura na imagem
def bfs(img, ponto, pintado):
    y, x = ponto
    img[y][x] = pintado
    fila = [ponto];
    while fila:
        y, x = fila.pop()
        for vizinho in vizinhos(img, y, x):
            y_v, x_v = vizinho;
            cor = img[y_v][x_v];
            if (cor > 0 and cor != pintado):
                img[y_v][x_v] = pintado;
                fila.append(vizinho);

# conta quantidade de objetos em uma imagem binaria
def contar_objetos(img):
    pintado = 5
    total_objetos = 0;
    for y in range(0, len(img)):
        for x in range(0, len(img[y])):
            cor = img[y][x];
            if cor == 255 and cor != pintado:
                total_objetos += 1;
                bfs(img, (y, x), pintado);
        	pintado += 5  
    print 'Quantidade de objetos:', total_objetos;

img=cv2.imread('microscopio2.jpg', 0)
cv2.imshow("original", img)
#blur = cv2.GaussianBlur(img,(9,9),0)
#ret,imgT = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, imgT = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)

contar_objetos(imgT);
n,bins,patches = plt.hist(imgT.ravel(), 256, [1, 255])
plt.show();
cv2.imshow("imagem", imgT);
cv2.waitKey();
cv2.destroyAllWindows();