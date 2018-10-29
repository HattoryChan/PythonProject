import pyautogui as pygui
from pynput.keyboard import Key, Listener
import pynput
import cv2 as cv
import time

def main():
    fl = 1
    while(bool(fl)):
        print (getCursorCoord())
        if '<Key.f1: 0>' == pynput.keyboard.Key.esc:
            fl = 0
    cv.destroyAllWindows()
    
        
def getCursorCoord():
    x,y = pygui.position()
    return(x,y)




      
main()            
    
