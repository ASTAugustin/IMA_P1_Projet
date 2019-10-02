import numpy as np

## flag = 0 膨胀
def ero(image, flag=0, num=1):
    w = len(image[0])
    h = len(image)
    iChange = np.zeros((h,w), np.uint8)
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

def maxImage (f,g):
    w = len(f[0])
    h = len(f)
    iChange = np.zeros((h,w), np.uint8)
    for i in range(h):
        for j in range(w):
            iChange[i][j]=max(f[i][j],g[i][j])
    return iChange

def minImage (f,g):
    w = len(g[0])
    h = len(g)
    iChange = np.zeros((h,w), np.uint8)
    for i in range(h):
        for j in range(w):
            iChange[i][j]=min(f[i][j],g[i][j])
    return iChange

def op (mask,f):
    f0 = minImage(mask,f)
    newImage = 0
    while True:
        newImage = maxImage(ero(mask, flag=1),f0)
        if (newImage==mask).all():
            break
        mask = newImage
    return newImage
