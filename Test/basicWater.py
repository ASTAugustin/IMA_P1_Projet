import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Ex1.PNG', 0)

markers = image.copy()
for i in range(0, len(markers)):
    for j in range(0, len(markers[0])):
        markers[i][j] = 0

markers[100][100] = 2
markers[50][50] = 3
'''
for i in range(0, len(markers)):
    markers[i][0]=0
    markers[i][len(markers[0])-1]=0
for j in range(0, len(markers[0])):
    markers[0][j]=0
    markers[len(markers)-1][j]=0

k = 2
for i in range(1, len(markers) - 1):
    for j in range(1, len(markers[0]) - 1):
        if (markers[i][j] <= image[i - 1][j] and markers[i][j] <= image[i][j - 1]
            and markers[i][j] <= image[i][j + 1] and markers[i][j] <= image[i + 1][j]):
            markers[i][j] = k
            k = k + 1
        else:
            markers[i][j] = 0
'''
print(markers)

markers = cv2.watershed(image, markers)
image[markers == -1] = [0, 0, 255]

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()
