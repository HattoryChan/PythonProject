# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:48:02 2019

@author: HattoryChan
"""

import cv2 
import numpy as np



#White color max sensitivity parameters
sensitivity = 30
hsv_min = np.array([0,0,255-sensitivity])
hsv_max = np.array([255,sensitivity,255])

#Open
img = cv2.imread('kisspng-laptop-paper-notebook-notebook-5a8153ef0caa60.4451607215184250710519.png'
                 , cv2.IMREAD_UNCHANGED)


#HSV color and cheate mask for non white object
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, hsv_min, hsv_max)
#inverse the mask
mask = 255 - mask
# The number of pixels
num_rows, num_cols = img.shape[:2]

# Creating a translation matrix(how much we will push shadow)
translation_matrix = np.float32([ [1,0,20], [0,1,25] ])
#move the mask
mask_translation = cv2.warpAffine(mask, translation_matrix, (num_cols,num_rows))
#repaint
mask_translation = np.where(mask_translation==255, 125, mask_translation)

#Apply Gaussian blur to shadow
mask_translation = cv2.GaussianBlur(mask_translation,(55,55), 0)
#Cut out by mask
for i in range(img.shape[2]):    
    img[:,:,i] = cv2.bitwise_and(img[:,:,i], mask)

#Copy to finish image
out = img.copy()

#Concatinate shadow and image
out[:,:,3] = cv2.addWeighted(mask_translation, 0.4, 
                       img[:,:,3], 1. ,0. )

#I like watch >.<
print(img.shape)
print(img[:,:,0].shape)
print(mask_translation.shape)
#Save it
cv2.imwrite('out.png', out)

#Im show
#cv2.imshow('mask_translation', mask_translation)#cv2.imshow('out', out)

#cv2.imshow('3', hsv[:, : ,2])
#cv2.resizeWindow('result',600,600)

