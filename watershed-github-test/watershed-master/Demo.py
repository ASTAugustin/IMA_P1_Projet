import matplotlib.pyplot as plt
import cv2
import numpy as np


from collections import deque

import ope
import Watershed

# Implementation of:
# Pierre Soille, Luc M. Vincent, "Determining watersheds in digital pictures via
# flooding simulations", Proc. SPIE 1360, Visual Communications and Image Processing
# '90: Fifth in a Series, (1 September 1990); doi: 10.1117/12.24211;
# http://dx.doi.org/10.1117/12.24211

np.set_printoptions(threshold=np.inf)

w = Watershed.Watershed()
image = np.array(cv2.imread('test.PNG', 0))

mask = np.linspace(255, 255, len(image) * len(image[0])).reshape(len(image), len(image[0]))
mask[0][0] = 0
mask[5][6] = 0
image[4][4] = 50

image = ope.op(mask, image)

labels = w.apply(image)
print(labels)

##plt.imshow(labels, cmap='Paired', interpolation='nearest')

plt.imshow(labels)
plt.show()



