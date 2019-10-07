# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:30:48 2019

@author: lucas
"""

import cv2 #Abre a biblioteca Opencv

"""carregando e mostrando uma imagem"""

imagemTeste = cv2.imread("fzea.jpeg") #Abre uma imagem

cv2.imshow("imagem orignal", imagemTeste) #Mostra uma imagem em uma nova janela

imagem_cinza = cv2.cvtColor(imagemTeste, cv2.COLOR_BGR2GRAY) #Converte uma imagem para escala de cinza

cv2.imshow("imagem escala de cinza", imagem_cinza) #Mostra a imagem em escala de cinza em uma janela diferente da anterior

valor, imagem_limiarizada = cv2.threshold(imagem_cinza, 100, 255, cv2.THRESH_BINARY) #Realiza a limiarizacao da imagem


cv2.imshow("imagem limiarizada", imagem_limiarizada) #Mostra a imagem limiarizada

cv2.imwrite("imagem.png", imagem_limiarizada) #Salva a imagem limiarizada na mesma pasta que o programa esta rodando

canalAzul, canalVerde, canalVermelho = cv2.split(imagemTeste) #Separa a imagem nos tres canais de cor, azul, verde e vermelho

cv2.imshow("Verde", canalVerde) #Abre em uma nova janela somente o canal verde da imagem

linha1 = np.average(canalVerde, axis=0) #calcula a media por linha de cada banda na area selecionada
linha2 = np.average(canalVermelho, axis=0)
linha3 = np.average(canalAzul, axis=0)

avg_color1 = np.average(linha1, axis=0) #calcula a media geral de cada banda na area selecionada
avg_color2 = np.average(linha2, axis=0)
avg_color3 = np.average(linha3, axis=0)

print(avg_color1) #Mostra a média de verde na imagem

cv2.waitKey(0)
cv2.destroyAllWindows()
