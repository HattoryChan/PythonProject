# -*- coding: utf-8 -*-
"""
@author: HattoryChan
"""

import cv2 
import numpy as np
from PIL import Image
import glob
import os
from tqdm import tqdm
#from skimage import transform,io


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
        
        
        #resizing image
        resizing_arr = img[: 1, :, :] 
        for i in range(40):        
            img = cv2.vconcat([img, resizing_arr])
            
        resizing_arr = img[: ,: 1, :]    
        for i in range(30):                
            img = cv2.hconcat([img, resizing_arr])
        
        
        # The number of pixels shift
        num_rows, num_cols = img.shape[:2]
        
        #expand picture
        
        #move the mask
        mask_translation = cv2.warpAffine(img[:,:,-1], translation_matrix, (num_cols,num_rows))
        #repaint
        mask_translation = np.where(mask_translation==255, 125, mask_translation)
        
        #Apply Gaussian blur to shadow
        mask_translation = cv2.GaussianBlur(mask_translation, gauss_sh_ksize, 0)
        
        if blurred == 1:
            img = cv2.GaussianBlur(img, gauss_img_ksize, 0)
        
                
        out = img.copy()
        
        #Crete shadow mask
        shadow_mask = cv2.bitwise_or(img[:,:,-1], mask_translation)  
        shadow_mask_inv = shadow_mask
        shadow_mask = 255 - shadow_mask
        shadow_mask = cv2.bitwise_or(img[:,:,-1], shadow_mask)
        
        #Concatinate shadow and image
        for i in range(out.shape[2]): 
            out[:,:,i] = cv2.bitwise_and(out[:,:,i], shadow_mask)
            
        #For background layer    
        out[:,:,3] = cv2.bitwise_or(img[:,:,-1], shadow_mask_inv)
        #RGB to BGR
        out[...,[0,2]]=out[...,[2,0]]
        
        #Convert to PIL
        out_pil = Image.fromarray(out)
        #out_pil.save("out.png","PNG")
        #out_pil.show()
        '''
        #Debugg part
        #print(hsv.shape[2])
        #print(out.shape[2])
        #print(img[:,:,0].shape)
        
        #Save it
        #cv2.imwrite('out.png', out)

        #Im show
        cv2.imshow('out', out)
        #cv2.imshow('mask_translation', mask_translation)
        #cv2.imshow('shadow_mask', shadow_mask)
        cv2.imshow('mask', mask)
       
        for i in range(out.shape[2]):            
            cv2.imshow(str(i),out[:,:,i])      
        '''  
        #cv2.resizeWindow('result',600,600)        
        return out_pil
        
        
        
    
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
    #cv2.imwrite('NormalShadow.png', a.ShadowBlur('Your_PNG_Path',
    #                               **a.NormalShadow()))  
    
    #To create shadows for all images in a folder
    path = 'D:\\ChromeDownload\\donors_364_items\\removebg\\'
    path_save = 'D:\\ChromeDownload\\donors_364_items\\removebg_Normal_shadow\\'
    
    print("Check directory exist: " + str(os.path.exists(path)))
    
    image_in_path = glob.glob(path+'*.png')
    
    for name in tqdm(image_in_path):
            a.ShadowBlur(name, **a.NormalShadow()).save(path_save + name.split('\\')[-1], "PNG")        
          