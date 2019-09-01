#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:23:14 2019

@author: usuario
"""


import cv2
import numpy as np 

r_petri=4.5 #definindo o raio da placa de petri
area_real_petri = np.pi*r_petri**2 #calculando a área real da placa de petri utilizando o raio definido



imagem=cv2.imread('imagem123.jpeg',0) 

cv2.imshow('imagem original', imagem) # plotando a imagem em uma nova janela.

imagem = cv2.GaussianBlur(imagem,(21,21),0)#suavizando a imagem utilizando filtro gaussiano

imagem=255-imagem #invertendo a imagem (negativo)para evitar problemas com contorno extra

#imagem_bi = cv2.adaptiveThreshold(imagem,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, 10)              

imagem_bi=255-imagem

cv2.imshow('imagem binarizada', imagem_bi) #plotando a imagem binarizada

img_cont, contorno, hierarchy = cv2.findContours(imagem_bi,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #determinando os pontos de contorno.

print(len(contorno)) #mostra o número de pontos presentes no vertor "contorno"

#as próximas linhas, até a linha 33, atribui os diferentes contornos encontrados à variáveis;
cont_0 = contorno[0]
cont_1 = contorno[1] 
cont_2 = contorno[2]
cont_3 = contorno[3]
#cont_4 = contorno[4]

#atribui agora variáveis à área relativa à cada contorno encontrado, neste caso, foram encontrados 4 contornos na imagem.
area_0 = cv2.contourArea(contorno[0])
area_1 = cv2.contourArea(contorno[1])
area_2 = cv2.contourArea(contorno[2])
area_3 = cv2.contourArea(contorno[3])
#area_4 = cv2.contourArea(contorno[4]) 

#desenhando os contornos na imagem original chamda de "imagem"
a=cv2.drawContours(imagem, contorno, 3, (0,0,255), 2)
#b=cv2.drawContours(imagem, contorno, 3, (0,0,255), 2)

#calcula a área da tricodarma por diferença
area_tr=area_2-area_3

#como a área até omomento foi dada em número de pixels, calcula-se a relação entre o número de pixels de toca a placa de Petri e o número de pixels da tricodarma. Esse passo é importante para conversar número de pixels em únidade física.
area_ratio = area_3/area_2

#uma vez conhecendo a relação entre placa de Petri e área da tricoderma e conhecendo também a área real do prato de Petri (medida manualmente), por proporção é determinadada a área da tricoderma.
area_tr_real = area_ratio*area_real_petri

#mostra o valor da área da placa de Petri
print('área placa petri', area_real_petri, 'cm')

#mostra o valor da area da tricoderma
print('área thricoderma',area_tr_real, 'cm')


#próximos cv2.imshow's mostram os contornos nas imagens. Note que apenas plotei 2 contornos, mas existem 5 contornos na figura.
cv2.imshow('imagem 1',a)

#cv2.imshow('imagem 2',b)

#IMPOTANTE!! Sempre que for carregar uma imagem, colocas os comandos abaixo como mostrado
cv2.waitKey(0)
cv2.destroyAllWindows()
#Esses comandos fazem com que o sistema "pare" de ler a imagem ao acionar qualquer tecla do teclado.
#caso a imagem seja carregada sem uma forma de finalizar sua leitura, o programa irá travar por entrar em um loop infinito.



