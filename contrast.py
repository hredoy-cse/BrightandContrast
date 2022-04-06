# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:54:22 2022

@author: hredoy
"""

from PIL import Image
import numpy as np
import math
oldImage = Image.open('baby.jpg')
h,w=oldImage.size
arr = np.array(oldImage)
total = 0
brightness = 67
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        total += (arr[(i,j,0)]-brightness) * (arr[(i,j,0)]-brightness)

print(total)
contrast = total/(h*w)
contrast =math.sqrt(contrast)
print(contrast)