import matplotlib.pyplot as plt
import cv2
import numpy as np


from collections import deque

import ope
import Watershed
import AMR

# Implementation of:
# Pierre Soille, Luc M. Vincent, "Determining watersheds in digital pictures via
# flooding simulations", Proc. SPIE 1360, Visual Communications and Image Processing
# '90: Fifth in a Series, (1 September 1990); doi: 10.1117/12.24211;
# http://dx.doi.org/10.1117/12.24211

np.set_printoptions(threshold=np.inf)

w = Watershed.Watershed()
image = np.array(cv2.imread('TestExemple/Ex3.jpg', 0))

kernel = np.ones((5,5),np.uint8)
gradient = np.array(cv2.morphologyEx(cv2.imread('TestExemple/Ex3.jpg', 0), cv2.MORPH_GRADIENT, kernel))

'''

mask = np.linspace(255, 255, len(image) * len(image[0])).reshape(len(image), len(image[0]))
mask[0][0] = 0
mask[5][6] = 0
mask[8][8] = 0
mask[9][3] = 0
mask[1][9] = 0
mask[7][2] = 0
image[4][4] = 50
print(image)

image = ope.reconstructionE(mask, image)

labels = w.apply(image)
print(labels)

##plt.imshow(labels, cmap='Paired', interpolation='nearest')


'''
result=AMR.AMR(gradient, 2, 10, 10)
labels = w.apply(result)
print(labels)

for i in range(len(image)):
    for j in range(len(image[0])):
        if labels[i][j] == 0:
            image[i][j] = 0

plt.imshow(image)
plt.show()



