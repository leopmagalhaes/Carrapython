# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 13:18:23 2019

@author: lucas
"""

import cv2


"""carregando e mostrando uma imagem"""
img = cv2.imread("C:/Users/lucas/Documents/Python Scripts/Leaf area index/imagens_verso/000.jpg", 1)


crop = img[:, :200]

cv2.imshow('imagem', img)
cv2.imshow('corte', crop)
cv2.imwrite("C:\\Users\\lucas\Documents\\Python Scripts\\Leaf area index\\Fotos originais cortadas\\teste.jpg", crop)

print('verificar imagem recortada na pasta')
cv2.waitKey(0)
cv2.destroyAllWindows()
