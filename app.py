import numpy as np
import cv2
import tkinter as tk
from PIL import ImageTk,Image
import imutils
from tkinter import ttk



############### DEPENDENCIAS ##############
##                                       ##
##  pip install numpy                    ##
##  pip install OpenCV-python            ##
##  pip install Pillow                   ##
##  pip install imutils                  ##
##                                       ##
###########################################


lower = {} #dicionario para as cores lower do arquivo config.txt
upper = {} #dicionario para as cores uppers
labels = {} #dicionario para os labels que iremos usar
colors = [] #array para guardar todas os nomes de cores salvas no config.txt
frames = {} # dicionario armazenar qual foi o ultimo frame de cada cor
voltasCor = {} #dicionario com voltas de cada cor

with open('config.txt') as f: # le o arquivo config.txt
    lines = f.readlines()
 
for x in range(0,len(lines)):

    var = lines[x].split(",")
    lower[var[0]] = int (var[1]),int (var[2]),int (var[3])
    upper[var[0]] = int(var[4]), int(var[5]), int(var[6].split('\n')[0])

print(lower)
print(upper)

aux = 0
for key, value in upper.items():
    frames[key] = 0 #frame de todas as cores comecam com zero
    voltasCor[key] = 0 #voltas de cada cor comecam com zero
    colors.append(key) #coloca todas as cores em nosso array de cores
    aux += 1


#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Real Race ")
window.config(background="#000000")

#

logoRR = tk.PhotoImage(file="images/RR_font.png")
logo_r = tk.Label(window, image=logoRR)
logo_r.imagem = logoRR
logo_r.config(background="#000000")
logo_r.grid(row=0, column=0, pady= 2, columnspan=1)


imagem = tk.PhotoImage(file="images/LogoApp.png")
w = tk.Label(window, image=imagem)
w.imagem = imagem
w.config(background="#000000")
w.grid(row=0, column=23, pady= 2, columnspan=4)

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=1, column=0, padx=10, pady=2, columnspan=20, rowspan=10)


header_name = tk.Label(window, text="Identificação  Voltas")
header_name.config(background="#000000", foreground="#FFFFFF")
header_name.grid(row=12, column=0)


i = 13

for labs in colors: #Cria um label para cada Cor do arquivo config.txt
    lb = tk.Label(window, text=labs + "       0")
    lb.config(background="#000000", foreground="#FFFFFF")
    lb.grid(row=i, column=0)
    labels[labs] = lb
    i += 1



#Cria um label para colocarmos os frames de nossa camera

lmain = tk.Label(imageFrame)
lmain.grid(row=1, column=0, columnspan=10, rowspan=10)


#conecta com a camera
cap = cv2.VideoCapture(0)


frameAtual = 0
def show_frame(frameAtual):
   _, frame = cap.read()
   frame = imutils.resize(frame, width=500)
   frameAtual += 1
   b, g, r = cv2.split(frame)
   frame = cv2.merge((r, g, b))

   blurred = cv2.GaussianBlur(frame, (11, 11), 0)
   hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

   for key, value in upper.items():

       kernel = np.ones((9, 9), np.uint8)
       mask = cv2.inRange(hsv, lower[key], upper[key])
       mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
       mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
       cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)[-2]
       if len(cnts) > 0:
           for x in range(0,len(colors)):
                if key == str(colors[x]):
                    if(frameAtual - frames[str(colors[x])] > 30):
                        frames[str(colors[x])] = frameAtual
                        voltasCor[str(colors[x])] += 1
                        labels[str(colors[x])]['text'] = colors[x] + "       " + str(voltasCor[str(colors[x])])


#aqui passamos o video para o labal lmain
   img = Image.fromarray(frame)
   imgtk = ImageTk.PhotoImage(image=img)
   lmain.imgtk = imgtk
   lmain.configure(image=imgtk)
   window.after(1, show_frame, frameAtual)



show_frame(frameAtual)  #
window.mainloop() #GUI
