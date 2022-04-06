# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:50:22 2022

@author: hredoy
"""

from PIL import Image
import  numpy as np
img = Image.open('baby.jpg')
h,w=img.size
arr = np.array(img)
brightness = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        for k in range(arr.shape[2]):
            brightness+=arr[(i,j,k)]
a=h*w
bright=(brightness)/a
print(bright)
