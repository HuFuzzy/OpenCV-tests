import cv2
import numpy as np
import imutils
from tkinter import *

def nothing (x):
    pass







def salvar(Hlo, HUp, Slo, Sup, Vlo, Vup):
    print(Hlo, HUp, Slo, Sup, Vlo, Vup)



cv2.namedWindow('Calibrador')
cap = cv2.VideoCapture('vid/sub.avi')

cv2.createTrackbar('Hlo','Calibrador',0,255,nothing)
cv2.createTrackbar('HUp','Calibrador',0,255,nothing)
cv2.createTrackbar('Slo','Calibrador',0,255,nothing)
cv2.createTrackbar('Sup','Calibrador',0,255,nothing)
cv2.createTrackbar('Vlo','Calibrador',0,255,nothing)
cv2.createTrackbar('Vup','Calibrador',0,255,nothing)


while True:
    #root = Tk()
    _, frame = cap.read()
    frame = imutils.resize(frame, width=300)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    #hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    Hlo = cv2.getTrackbarPos('Hlo','Calibrador')
    HUp = cv2.getTrackbarPos('HUp','Calibrador')
    Slo = cv2.getTrackbarPos('Slo','Calibrador')
    Sup = cv2.getTrackbarPos('Sup','Calibrador')
    Vlo = cv2.getTrackbarPos('Vlo','Calibrador')
    Vup = cv2.getTrackbarPos('Vup','Calibrador')

    lower_cor = np.array([Hlo, Slo, Vlo])
    upper_cor = np.array([HUp, Sup, Vup])

    mask = cv2.inRange(hsv, lower_cor, upper_cor)

    res = cv2.bitwise_and(frame, frame, mask)
    kernel = np.ones((9, 9), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    salvar(Hlo, HUp, Slo, Sup, Vlo, Vup)

    #btn = Button(root, text="Salvar Config", command= lambda: salvar(Hlo,HUp,Slo,Sup,Vlo,Vup)).pack()


    #res2 = cv2.cvtColor(res,cv2.COLOR_BAYER_BG2GRAY)
    #res2 = cv2.medianBlur(res2, 15)

    #cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    #cv2.imshow('res', res)




    k = cv2.waitKey(100) & 0xFF
    if cv2.waitKey(33) == ord('a'):
        break
    #root.mainloop()
cv2.destroyAllWindows()
#root.destroy()