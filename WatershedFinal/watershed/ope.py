import numpy as np
import cv2


## flag = 0 膨胀
## num 是单元格长度
def ero(image, flag=0, num=1):
    w = len(image[0])
    h = len(image)
    iChange = np.zeros((h, w), np.uint8)
    for i in range(h):
        for j in range(w):
            a = []
            for k in range(2 * num + 1):
                for l in range(2 * num + 1):
                    if -1 < (i - num + k) < h and -1 < (j - num + l) < w:
                        a.append(image[i - num + k, j - num + l])
            if flag == 0:
                k = max(a)
            else:
                k = min(a)
            iChange[i, j] = k
    return iChange


def maxImage(f, g):
    w = len(f[0])
    h = len(f)
    iChange = np.zeros((h, w), np.uint8)
    for i in range(h):
        for j in range(w):
            iChange[i][j] = max(f[i][j], g[i][j])
    return iChange


def minImage(f, g):
    w = len(g[0])
    h = len(g)
    iChange = np.zeros((h, w), np.uint8)
    for i in range(h):
        for j in range(w):
            iChange[i][j] = min(f[i][j], g[i][j])
    return iChange


# 腐蚀重建
def reconstructionE(mask, f, structure):
    print("Reconstruction Erosion")
    f0 = minImage(mask, f)
    newImage = 0
    while True:
        newImage = maxImage(ero(mask, flag=1, num=structure), f0)
        if (newImage == mask).all():
            break
        print("Diff ", maxDifference(newImage, mask))
        print("Sum ", maxDSum(newImage, f0))
        mask = newImage
    return newImage


# 膨胀重建
def reconstructionD(mask, f, structure):
    print("Reconstruction Dilatation")
    f0 = maxImage(mask, f)
    newImage = 0
    while True:
        newImage = minImage(ero(mask, flag=0, num=structure), f0)
        if (newImage == mask).all():
            break
        print("Diff ", maxDifference(newImage, mask))
        print("Sum ", maxDSum(newImage, f0))
        mask = newImage
    return newImage


def openingreconstruction(mask, f, structure):
    # 先腐蚀重建再膨胀重建
    return reconstructionD(reconstructionE(mask, f, structure), f, structure)


def closingreconstruction(mask, f, structure):
    # 先腐蚀重建再膨胀重建
    return reconstructionE(reconstructionD(mask, f, structure), f, structure)


def maxMatrix(image):
    maxM = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            maxM = max(maxM, image[i][j])
    return maxM


def maxDifference(image1, image2):
    maxM = 0
    for i in range(len(image1)):
        for j in range(len(image1[0])):
            maxM = max(maxM, abs(image1[i][j] - image2[i][j]))
    return maxM


def maxDSum(image1, image2):
    maxM = 0
    for i in range(len(image1)):
        for j in range(len(image1[0])):
            maxM = maxM + abs(image1[i][j] - image2[i][j])
    return maxM
