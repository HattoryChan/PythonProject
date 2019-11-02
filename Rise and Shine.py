# -*- coding: utf-8 -*-
"""
@author: HattoryChan
"""

import cv2 
import numpy as np


class RiseAndShine():
    '''
    Get image and return with shadow or/and blurred
    Input:
        
    #Default for white    
    sensitivity -  Color sensitivity parameters    
    hsv_min - Background color min border
    hsv_max - Background color max border
    translation_matrix - Translation matrix(how much we will push shadow)   
    blurred - Bluring image on/off (bool)
    shadow - On/Off shadow (bool)
    gauss_img_ksize - gauss kernel size for image(how much blur)
    gauss_sh_ksize - gauss kernel size for shadow(how much blur) 
    translation_matrix - shift position for shadow
    
    Output: 
    out - Image np.array with shadow or/and blurred    
    '''    
    def ShadowBlur(self, img_name, blurred, shadow, gauss_img_ksize, 
                   gauss_sh_ksize, sensitivity, hsv_min, hsv_max, 
                   translation_matrix, shadow_power, img_power):
        
        """
        img_name,
        blurred = 0,
        shadow = 1,
        gauss_img_ksize =(55,55),
        gauss_sh_ksize =(55,55),
        sensitivity = 30,
        hsv_min = np.array([0,0,255-sensitivity]),
        hsv_max = np.array([255,sensitivity,255]),
        translation_matrix = np.float32([ [1,0,20], [0,1,25] ]),
        shadow_power = 0.4,
        img_power = 1.0):  
        """
                   
                   
        
        #Open
        img = cv2.imread(img_name
                         , cv2.IMREAD_UNCHANGED)
        
        
        #HSV color and cheate mask for non white object
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, hsv_min, hsv_max)
        #inverse the mask
        mask = 255 - mask
        # The number of pixels
        num_rows, num_cols = img.shape[:2]
        
        #move the mask
        mask_translation = cv2.warpAffine(mask, translation_matrix, (num_cols,num_rows))
        #repaint
        mask_translation = np.where(mask_translation==255, 125, mask_translation)
        
        #Apply Gaussian blur to shadow
        mask_translation = cv2.GaussianBlur(mask_translation, gauss_sh_ksize, 0)
        
        if blurred == 1:
            img = cv2.GaussianBlur(img, gauss_img_ksize, 0)
        
        #Cut out by mask
        for i in range(img.shape[2]):    
            img[:,:,i] = cv2.bitwise_and(img[:,:,i], mask)
        
        
        #Copy to finish image
        out = img.copy()
        
        
        #Concatinate shadow and image
        if shadow == 1:
            out[:,:,3] = cv2.addWeighted(mask_translation, shadow_power, 
                                   img[:,:,3], img_power ,0. )
        
        
        return out
    
        #Debugg part
        #print(img.shape)
        #print(img[:,:,0].shape)
        
        #Save it
        #cv2.imwrite('out.png', out)
        
        #Im show
        #cv2.imshow('out', out)
        #cv2.imshow('3', hsv[:, : ,2])
        #cv2.resizeWindow('result',600,600)
        
    
    def NormalShadow(self):
        
        return dict(blurred = 0,
                    shadow = 1,
                    gauss_img_ksize =(55,55),
                    gauss_sh_ksize =(55,55),
                    sensitivity = 30,
                    hsv_min = np.array([0,0,255-30]),
                    hsv_max = np.array([255,30,255]),
                    translation_matrix = np.float32([ [1,0,20], [0,1,25] ]),
                    shadow_power = 0.4,
                    img_power = 1.0)          
        
        
    def WeaklyShadows(self):    
        
        return dict(blurred = 0,
                    shadow = 1,
                    gauss_img_ksize =(55,55),
                    gauss_sh_ksize =(155,155),
                    sensitivity = 30,
                    hsv_min = np.array([0,0,255-30]),
                    hsv_max = np.array([255,30,255]),
                    translation_matrix = np.float32([ [1,0,20], [0,1,25] ]),
                    shadow_power = 0.4,
                    img_power = 1.0) 
    
    
    def StrongShadows(self):    
        
        return dict(blurred = 0,
                    shadow = 1,
                    gauss_img_ksize =(55,55),
                    gauss_sh_ksize =(15,15),
                    sensitivity = 30,
                    hsv_min = np.array([0,0,255-30]),
                    hsv_max = np.array([255,30,255]),
                    translation_matrix = np.float32([ [1,0,20], [0,1,25] ]),
                    shadow_power = 0.8,
                    img_power = 1.0) 
                
    def NormalShadowWithNormalBlur(self):
        
        return dict(blurred = 1,
                    shadow = 1,
                    gauss_img_ksize =(21,21),
                    gauss_sh_ksize =(55,55),
                    sensitivity = 30,
                    hsv_min = np.array([0,0,255-30]),
                    hsv_max = np.array([255,30,255]),
                    translation_matrix = np.float32([ [1,0,20], [0,1,25] ]),
                    shadow_power = 0.4,
                    img_power = 1.0) 
        
    def WeaklyShadowsWithStrongBlur(self):
        
        return dict(blurred = 1,
                    shadow = 1,
                    gauss_img_ksize =(55,55),
                    gauss_sh_ksize =(55,55),
                    sensitivity = 30,
                    hsv_min = np.array([0,0,255-30]),
                    hsv_max = np.array([255,30,255]),
                    translation_matrix = np.float32([ [1,0,20], [0,1,25] ]),
                    shadow_power = 0.4,
                    img_power = 1.0) 
    
    def StrongShadowsWithWeaklyBlur(self):    
        
        return dict(blurred = 1,
                    shadow = 1,
                    gauss_img_ksize =(15,15),
                    gauss_sh_ksize =(15,15),
                    sensitivity = 30,
                    hsv_min = np.array([0,0,255-30]),
                    hsv_max = np.array([255,30,255]),
                    translation_matrix = np.float32([ [1,0,20], [0,1,25] ]),
                    shadow_power = 0.8,
                    img_power = 1.0) 
    



if __name__ == "__main__":
    a = RiseAndShine()
    cv2.imwrite('NormalShadow.png', a.ShadowBlur('kisspng-paper-notebook-notebook-5a7b16d269e617.3736536315180162104338.png',
                                   **a.NormalShadow()))
   # print(a.NormalShadow('kisspng-paper-notebook-notebook-5a7b16d269e617.3736536315180162104338.png'))