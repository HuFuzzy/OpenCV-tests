import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt


face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('img/teste1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
   cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
   roi_gray = gray[y:y + h, x:x + w]
   roi_color = img[y:y + h, x:x + w]
   font = cv2.FONT_HERSHEY_COMPLEX
   cv2.putText(img, "Rosto", (x, y), font, 0.5, (200, 255, 255), 2, cv2.LINE_AA)


cv2.imshow('Sasha Grey', img)
k = cv2.waitKey(0)

if k == 27:
    img.release()
    cv2.destroyAllWindows()
    img.release()
    cv2.destroyAllWindows()