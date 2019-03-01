import numpy as np
import cv2 as cv
import imutils

MOT_THRESHOLD =40 #Пороговое значение поиска обьектов 


#vid = cv.VideoCapture("videoplayback (4).mp4")
vid = cv.VideoCapture("MotionVideo.mp4")


cont_Start = []     #Инициализируем пустые листы
cont_Start2 = []
extLeftOld = [0,0]
extRightOld = [0,0]
extTopOld = [0,0]
extBotOld = [0,0]
SpeedOld = 0.0

while(vid.isOpened()):  #Если видео открыто
    ret, frame = vid.read()  #Читаем первый кадр
    pos_frame = vid.get(cv.CAP_PROP_POS_FRAMES) #Получаем количество кадров

    if frame is None:   #Проверяем не конец ли видео
        break
    
    prev_frame=frame[:]     #Сохранияем прошлый кадр
    ret, frame = vid.read() #Читаем новый кадр

    
    if frame is None:   #Проверям не кончилось ли видео
        break
    
    #Оттенки серого и сглаживание для текущего
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(hsv,(3,3),-1)
    #Оттенки серого для прошлого кадра
    hsvPr = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
    

    diff = cv.absdiff( blur,hsvPr) #Ищем различия между кадрами
     
    ret2, thres = cv.threshold( diff, MOT_THRESHOLD, 255, 0)  #Применяем пороговый поиск
    thres =  cv.morphologyEx(thres, cv.MORPH_OPEN, np.ones((7,7),np.uint8)) #Смазываем мелкие обьекты
    thres = cv.morphologyEx(thres, cv.MORPH_CLOSE, np.ones((5,5),np.uint8)) #Смазываем крупный обьекты

    #Находим контура
    thres, contours, hierarchy = cv.findContours(thres,1, 2)
    
    
    #Находим контура и переформируем их для удобной работы      
    cnts = cv.findContours(thres.copy(), cv.RETR_EXTERNAL,
	cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

        
    if cnts: #Если контура не пустые
        
        c = max(cnts, key=cv.contourArea) #Сортируем контура
        
        extLeft = tuple(c[c[:, :, 0].argmin()][0]) #создаем кортежи экстремумов
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        extBot = tuple(c[c[:, :, 1].argmax()][0])
        #Считаем скорость, если скачек большой - не меняем ее.        
        Speed = (((extLeft[0]-extLeftOld[0] + extRight[0]-extRightOld[0] +
              extTop[0] - extTopOld[0] + extBot[0]-extBotOld[0])/2) + SpeedOld)/2

        if abs(Speed) > 200: #Если скорость больше 200 пикселей - не верим ему
            SpeedOld = SpeedOld
        else:
            SpeedOld = Speed
        
        try:  #Пробуем вывести скорость на экран
            if Speed > 0: #Считаем в каком направлении движется обьект
                SpeedT = "Right"
            if Speed < 0:
                SpeedT = "Left"
            # Выводим скорость и направление движения   
            cv.putText(thres,  str(round(abs(Speed))), (20,40), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            cv.putText(thres,  SpeedT, (20,70), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        except:
            print("NO TEXT")
        #Запоминаем старые значения для дальнейшего расчет скорости
        extLeftOld = extLeft
        extRightOld = extRight
        extTopOld = extTop
        extBotOld = extBot
        
                
        
    cv.drawContours(thres, contours , -1, (255,0,0), 2)  #рисуем контура
    cv.imshow('video',thres) #выводим видео

    
    if cv.waitKey(1) & 0xFF == ord('q'): 
          break    
    cv.waitKey(50)

vid.release()
cv.destroyAllWindows()

