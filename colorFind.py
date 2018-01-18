import cv2
import numpy as np


print ("")



vermelho = input("VERMELHO ")
verde = input("VERDE ")
azul = input("AZUL ")

cor = np.uint8([[[azul,verde,vermelho ]]]) #neste caso VERDE
hsv_cor = cv2.cvtColor(cor,cv2.COLOR_BGR2HSV) #Converte para HSV
print (hsv_cor)
