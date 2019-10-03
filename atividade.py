# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:30:48 2019

@author: lucas
"""

import cv2

"""carregando e mostrando uma imagem"""

imagemTeste = cv2.imread("fzea.jpeg")

cv2.imshow("imagem orignal", imagemTeste)

imagem_cinza = cv2.cvtColor(imagemTeste, cv2.COLOR_BGR2GRAY)

cv2.imshow("imagem escala de cinza", imagem_cinza)

valor, imagem_limiarizada = cv2.threshold(imagem_cinza, 100, 255, cv2.THRESH_BINARY)


cv2.imshow("imagem limiarizada", imagem_limiarizada)




cv2.waitKey(0)
cv2.destroyAllWindows()
