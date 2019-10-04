import numpy as np
#import pylab as pl
#import matplotlib.pyplot as pl
import cv2
vert = open('vert.txt', 'w')
gor  = open('gor.txt', 'w')
test = open ('test.txt','w')
test2 = open ('test2.txt','w')
cap = cv2.VideoCapture("bandicam 2018-08-04 14-12-19-996.avi")

for i in range(30):
    cap.read()

ret, color_image = cap.read()

gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
gray_480 = gray[0:0+480, 80:80+480]
cv2.imshow("Face_gray", gray_480)
cv2.waitKey(0)
cv2.destroyAllWindows()
pic= np.zeros((480,480, 10))
for k in range(0,480): 
    a=480
    for n in range (0,480):
        a=a-1
        pic[k][n][0]=gray_480[k][n]
cv2.imwrite('cam.png', pic[:,:,0])
cap.release()
delitel=1
delt=0
l=0
for k in range (1,10):
    gor.write ('\n')
   
    vert.write ('\n')
    for i in  range (0,int(round(480.0/(2**delt)))):
        vert.write ('\n')
        for n in range (0,int(round(480.0/(2**delitel)))):
            pic[n][i][k]=(0.5)*(pic[2*n][i][k-1]+pic[2*n+1][i][k-1])
            vert.write(str(pic[n][i][k])+ " " )
    delt=delt+1
    for j in range (0,int(round(480.0/(2**delitel)))):
        gor.write ('\n')
        for l in range (0,int(round(480.0/(2**delitel)))): 
            
            
            (pic[j][l][k])=(0.5)*(pic[j][2*l][k]+pic[j][2*l+1][k])
            gor.write(str(pic[j][l][k])+' ')
    delitel=delitel+1
   
for i in range (0,480):
     test.write ('\n')
     test2.write ('\n')
    
     for j in range (0,480):
         
         test.write(str(pic[j][i][1])+ " ")
         test2.write( str(pic[j][i][4])+ " ")
       
 

##  
##for k in range(0,240): 
 ##       pic1[int(k)][int(n)]=pic[k][n][0]
##cv2.imshow("Face_gray",(pic1))
cv2.waitKey(0)
cv2.destroyAllWindows() 

vert.close()
gor.close()
test.close()
test2.close()
