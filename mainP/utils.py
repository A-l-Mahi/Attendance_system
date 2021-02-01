
import cv2
import pyzbar.pyzbar as pyzbar

import numpy as np

#opening Camera
cap = cv2.VideoCapture(0)

#font

font = cv2.FONT_HERSHEY_PLAIN


def scanner():
    
    #loop
    while True:

        #reading Qr
        _, frame = cap.read()

        #Qr Detection

        decodedObjects = pyzbar.decode(frame)

        for obj in decodedObjects:
            print('Data : ', obj.data,'\n')

            cv2.putText(frame , str(obj.data), (50, 50), font, 3, (255, 0 , 0)
            , 1)

            
        #Displaying Camera
                        
        cv2.imshow("QrScanner", frame)

        #Breaking loop
        key = cv2.waitKey(1)

        if key == 2:
            break