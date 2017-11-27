from tkinter import *
import cv2


root = Tk()

w = Canvas(root, width=500, height=300, bd = 10, bg = 'white')
w.grid(row = 0, column = 0, columnspan = 2)

b = Button(width = 10, height = 2, text = 'Button1')
b.grid(row = 1, column = 0)
b2 = Button(width = 10, height = 2, text = 'Button2')
b2.grid(row = 1,column = 1)

cv2.namedWindow("camera",1)
capture = cv2.VideoCapture(1)


while True:
    result, img = capture.read()
    Canvas.create_image(0,0,img)

    if cv2.WaitKey(10) == 27:
        break

root.mainloop()