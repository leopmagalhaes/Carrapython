#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:52:19 2020

@author: usuario
"""

import pylab
import matplotlib.pyplot as plt
import cv2
import numpy as np


img =  cv2.imread("area_1912.JPG").astype(np.float)
img = cv2.resize(img,None,fx=0.2,fy=0.2)


MPRI = ((img[:, :, 1] - img[:, :, 2])/(img[:, :, 1]+ img[:, :, 2]))  
print("MPRI:", np.mean(MPRI))
print("Maximo:", np.max(MPRI))
print("Minimo:", np.min(MPRI))
print("")
imgplot = plt.imshow(MPRI)

# Choose a color palette
#imgplot.set_cmap('jet')
imgplot.set_cmap('RdYlGn') 

plt.colorbar()
plt.axis('off')

pylab.show()

Gn = ((img[:, :, 1])/(img[:, :, 1]+ img[:, :, 2] + img[:, :, 0]))  
print("Gn:", np.mean(Gn))
print("Maximo:", np.max(Gn))
print("Minimo:", np.min(Gn))
print("")
imgplot = plt.imshow(Gn)

# Choose a color palette
#imgplot.set_cmap('jet')
imgplot.set_cmap('RdYlGn') 

plt.colorbar()
plt.axis('off')

pylab.show()

SAVI = ((1.5*(img[:, :, 1] - img[:, :, 2]))/(img[:, :, 1]+ img[:, :, 2] + 0.5))  
print("SAVI:", np.mean(SAVI))
print("Maximo:", np.max(SAVI))
print("Minimo:", np.min(SAVI))
imgplot = plt.imshow(SAVI)

# Choose a color palette
#imgplot.set_cmap('jet')
imgplot.set_cmap('RdYlGn') 

plt.colorbar()
plt.axis('off')

pylab.show()

cv2.waitKey(0)

cv2.destroyAllWindows()
