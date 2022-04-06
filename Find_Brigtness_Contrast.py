# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 12:40:00 2022

@author: hredoy
"""

import numpy as num       
import cv2;               
img= cv2.imread("baby.png",0);
cv2.imshow('image',img);
cv2.waitKey();
cv2.destroyAllWindows();
brightness=round((num.sum(img))/(num.size(img)))
contrast=num.max(img)-num.min(img)
print("The brightness of the image is {}\nThe contrast of the image is {}".format(brightness,contrast))






#mathematical operations on arrays
#module import name for opencv-python,
#round() rounds a number to zero decimal places
#(str. format())
#display a window until any key is pressed.