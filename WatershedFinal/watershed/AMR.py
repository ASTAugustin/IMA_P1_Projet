import ope

import cv2
import numpy as np

def AMR(input, s, m, err):
    g=input
    for i in range(s, m + 1):
        print ('case',i)
        tmp = ope.closingreconstruction(g, i)
        if i == s:
            output = tmp
            errGlobal = ope.maxMatrix(tmp)
        else:
            output = ope.maxImage(output,tmp)
            errGlobal = ope.maxDifference(output,tmp)
        if errGlobal <= err:
            break
    return output