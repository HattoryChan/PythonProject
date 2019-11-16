# -*- coding: utf-8 -*-
"""
@author: HattoryChan
"""

import cv2
import numpy as np
from PIL import Image, ImageFilter
import PIL.ImageOps    
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
    def ShadowBlur(self, img_name, mode):
        """
        This function calls own helper for generate shadow by mode.

        Keyword arguments:
        img -- Pillow image
        mode -- string with the mode

        Returns:
        Image in PIL format.
        """

        parameters = None
        if mode == "NormalShadow":
            parameters = self.NormalShadow()
        elif mode == "WeaklyShadows":
            parameters = self.WeaklyShadows()
        elif mode == "StrongShadows":
            parameters = self.StrongShadows()
        elif mode == "NormalShadowWithNormalBlur":
            parameters = self.NormalShadowWithNormalBlur()
        elif mode == "WeaklyShadowsWithStrongBlur":
            parameters = self.WeaklyShadowsWithStrongBlur()
        elif mode == "StrongShadowsWithWeaklyBlur":
            parameters = self.StrongShadowsWithWeaklyBlur()
        return self.ShadowBlurHelper(img_name, **parameters)




    def ShadowBlurHelper(self, img, shadowColor, 
                         shadowBlurLvl, imageBlurLvl, shadowdShiftPercents):

       #Get image size
        width, height = img.size        
        #Create white canvas
        total_width = int(width * 1.05)
        max_height = int(height * 1.05)    
        out_pil = Image.new('RGBA', (total_width, max_height), (255, 255, 255))  # common canvas
        
        #Create shadow   
        pixelMap = img.load()
        shadow = Image.new('RGBA',img.size)
        pixelsNew = shadow.load() 
        width,height = shadow.size
        for i in range(width): 
            for j in range(height):
                if pixelMap[i,j][3] < 240:
                    pixelsNew[i,j] = (255,255,255)   #white background
                if pixelMap[i,j][3] > 240:
                    pixelsNew[i,j] = shadowColor   #grey shadow
                    
                        
        #Paste shadow           
        shift = (int(width* shadowdShiftPercents[0]), int(height* shadowdShiftPercents[1]))
        out_pil.paste(shadow, shift, img)
        
        #Add blur on shadow       
        for i in range(shadowBlurLvl):
                out_pil = out_pil.filter(ImageFilter.BLUR)
        
        #Paste image
        out_pil.paste(img, (1, 1), img) 
        
        #Add blur on image       
        for i in range(imageBlurLvl):
                out_pil = out_pil.filter(ImageFilter.BLUR)
        
        
        #Delete White background
        datas = out_pil.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        
        out_pil.putdata(newData)
        
        return out_pil




    def NormalShadow(self):

        return dict(shadowColor = (100,100,100), 
                    shadowBlurLvl = 2, 
                    imageBlurLvl = 0,
                    shadowdShiftPercents = (0.02, 0.03))


    def WeaklyShadows(self):

        return dict(shadowColor = (150,150,150),
                    shadowBlurLvl = 8,
                    imageBlurLvl = 0,
                    shadowdShiftPercents = (0.02, 0.03))


    def StrongShadows(self):

        return dict(shadowColor = (70,70,70),
                    shadowBlurLvl = 2,
                    imageBlurLvl = 0,
                    shadowdShiftPercents = (0.02, 0.03))

    def NormalShadowWithNormalBlur(self):

        return dict(shadowColor = (100,100,100), 
                    shadowBlurLvl = 2, 
                    imageBlurLvl = 1,
                    shadowdShiftPercents = (0.02, 0.03))

    def WeaklyShadowsWithStrongBlur(self):

        return dict(shadowColor = (150,150,150), 
                    shadowBlurLvl = 8, 
                    imageBlurLvl = 3,
                    shadowdShiftPercents = (0.02, 0.03))

    def StrongShadowsWithWeaklyBlur(self):

        return dict(shadowColor = (70,70,70), 
                    shadowBlurLvl = 2, 
                    imageBlurLvl = 1,
                    shadowdShiftPercents = (0.02, 0.03))





if __name__ == "__main__":
    
    a = RiseAndShine()    
    #img = Image.open("flower_2.png")
    #a.ShadowBlur(img, "NormalShadow").show()
    
    
    #To create shadows for all images in a folder
    path = 'D:\\ChromeDownload\\donors_364_items\\removebg\\'
    path_save = 'D:\\ChromeDownload\\donors_364_items\\removebg_Normal_shadow\\'

    print("Check directory exist: " + str(os.path.exists(path)))

    image_in_path = glob.glob(path+'*.png')

    for name in tqdm(image_in_path):
           a.ShadowBlur(Image.open(name), "NormalShadow").save(path_save + name.split('\\')[-1], "PNG")
           
    
    
   
