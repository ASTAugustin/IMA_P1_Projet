import matplotlib.pyplot as plt
import cv2
import numpy as np
import Watershed
import operator

np.set_printoptions(threshold=np.inf)


w = Watershed.Watershed()
image = np.array(cv2.imread('test.PNG', 0))

mask = np.linspace(255,255,len(image)*len(image[0])).reshape(len(image),len(image[0]))
mask[0][0]=0
mask[5][6]=0
image[4][4]=50

image = operator.op(mask,image)

labels = w.apply(image)
print(labels)

##plt.imshow(labels, cmap='Paired', interpolation='nearest')
plt.imshow(labels)
plt.show()