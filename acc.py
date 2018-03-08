import numpy as np
import cv2
import tkinter as tk
import imutils
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter.messagebox import showinfo



def salvaConfig():
    if v.get()== '':
        showinfo("Window", "Digite a identificação! ")
    else:        
        arquivo = open('config.txt', 'r')  # Abra o arquivo (leitura)
        conteudo = arquivo.readlines()
        result = str(v.get())
        result += ','
        result += str(Hlo.get())
        result += ','
        result += str(Slo.get())
        result += ','
        result += str(Vlo.get())
        result += ','
        result += str(HUp.get())
        result += ','
        result += str(SUp.get())
        result += ','
        result += str(VUp.get())
        v.set('')#limpa texto anterior
        conteudo.append(str(result) + "\n")
        arquivo = open('config.txt', 'w')  # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.
        arquivo.close()
        showinfo("Window", "Novo item adicionado: " + str(result))
        print(str(result))


def close_window ():
    window.destroy()

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("A.C.C")
window.config(background="#000000")

#Graphics window
imageFrame = tk.Frame(window, width=400, height=250)
maskFrame = tk.Frame(window, width=400, height=250)
#captura camera e cria dois label
lmain = tk.Label(imageFrame)
maskL = tk.Label(maskFrame)

logoRR = tk.PhotoImage(file="images/RR_font.png")
logo_r = tk.Label(window, image=logoRR)
logo_r.imagem = logoRR
logo_r.config(background="#000000")
logo_r.grid(row=0, column=0, columnspan=4)

#Declaração dos labels
lbl_titulo = ttk.Label(text="Real Race - Color calibration", style="BW.TLabel", font=("Segoe UI", 15))
lbl_titulo.config(background="#000000", foreground="#FFFFFF")
lbl_lower_H = ttk.Label(text="- H", style="BW.TLabel", font=("Segoe UI", 10))
lbl_lower_H.config(background="#000000", foreground="#FFFFFF")
lbl_lower_S = ttk.Label(text="- S", style="BW.TLabel", font=("Segoe UI", 10))
lbl_lower_S.config(background="#000000", foreground="#FFFFFF")
lbl_lower_V = ttk.Label(text="- V", style="BW.TLabel", font=("Segoe UI", 10))
lbl_lower_V.config(background="#000000", foreground="#FFFFFF")
lbl_upper_H = ttk.Label(text="+ H", style="BW.TLabel", font=("Segoe UI", 10))
lbl_upper_H.config(background="#000000", foreground="#FFFFFF")
lbl_upper_S = ttk.Label(text="+ S", style="BW.TLabel", font=("Segoe UI", 10))
lbl_upper_S.config(background="#000000", foreground="#FFFFFF")
lbl_upper_V = ttk.Label(text="+ V", style="BW.TLabel", font=("Segoe UI", 10))
lbl_upper_V.config(background="#000000", foreground="#FFFFFF")

#Declaração dos Sliders
Hlo = tk.Scale(orient='vertical', from_=1, length=200, to=255)
Hlo.config(background="#000000", foreground="#FFFFFF")
HUp = tk.Scale(orient='vertical', from_=1,length=200, to=255)
HUp.config(background="#000000", foreground="#FFFFFF")
Slo = tk.Scale(orient='vertical', from_=1,length=200, to=255)
Slo.config(background="#000000", foreground="#FFFFFF")
SUp = tk.Scale(orient='vertical', from_=1,length=200, to=255)
SUp.config(background="#000000", foreground="#FFFFFF")
Vlo =tk.Scale(orient='vertical', from_=1,length=200, to=255)
Vlo.config(background="#000000", foreground="#FFFFFF")
VUp =tk.Scale(orient='vertical', from_=1,length=200, to=255)
VUp.config(background="#000000", foreground="#FFFFFF")

#Declaração dos botões
button = tk.Button(window, text="Salvar", width=20, height= 3, command=salvaConfig)
button.config(background="#000000", foreground="#FFFFFF", activebackground="#66E0FF")
buttonc = tk.Button(window, text="Fechar", width=20, height= 3, command=close_window)
buttonc.config(background="#000000", foreground="#FFFFFF", activebackground="#66E0FF")
#Declaração do input text nome Cor
v = tk.StringVar()
in_e = tk.Entry(window, textvariable=v, width=50)
lbl_w = tk.Label(window, text="Digite a identificação: ", font=("Segoe UI", 10))
lbl_w.config(background="#000000", foreground="#FFFFFF")
lbl_invisible1 = tk.Label(window, text=" ")
lbl_invisible1.config(background="#000000")
lbl_invisible2 = tk.Label(window, text=" ")
lbl_invisible2.config(background="#000000")
lbl_invisible3 = tk.Label(window, text=" ")
lbl_invisible3.config(background="#000000")
imagem = tk.PhotoImage(file="images/LogoREALGAMES.png")
w = tk.Label(window, image=imagem)
w.imagem = imagem
w.config(background="#000000")
w.grid(row=0, column=16, pady= 2, columnspan=6)

#Organizando elementos no grid
#lbl_titulo.grid(row=0, column=0, columnspan=5, padx=1, pady=2)
lbl_invisible1.grid(row=1, column=0)

imageFrame.grid(row=2, column=0,  columnspan=10, rowspan=10, padx=10, pady=2)
maskFrame.grid(row=2, column=10, columnspan=10, rowspan=10,padx=10, pady=2)
lmain.grid(row=2, column=0, columnspan=10,rowspan=10)
maskL.grid(row=2, column=10, columnspan=10,rowspan=10)
lbl_invisible2.grid(row=13, column=0)
lbl_lower_H.grid(row=14, column=10, padx=0, pady=0)
lbl_invisible3.grid(row=15, column=0)
Hlo.grid(row=16, column=10, rowspan=10, padx=0, pady=0)
lbl_upper_H.grid(row=14, column=11, padx=0, pady=0)
HUp.grid(row=16, column=11, rowspan=10, padx=0, pady=0)
lbl_lower_S.grid(row=14, column=12, padx=0, pady=0)
Slo.grid(row=16, column=12,rowspan=10, padx=0, pady=0)
lbl_upper_S.grid(row=14, column=13, padx=0, pady=0)
SUp.grid(row=16, column=13, rowspan=10, padx=0, pady=0)


lbl_lower_V.grid(row=14, column=14, padx=0, pady=0)
Vlo.grid(row=16, column=14, rowspan=10)
lbl_upper_V.grid(row=14, column=15, padx=0, pady=0)
VUp.grid(row=16, column=15, rowspan=10)

lbl_w.grid(row=14, column=1)
in_e.grid(row=14, column=2, columnspan=4)
button.grid(row=24, column=17, columnspan=3)
buttonc.grid(row=25, column=17, columnspan=3)
#captura a camera
cap = cv2.VideoCapture(0)

def show_frame():
    _, frame = cap.read()
    frame = imutils.resize(frame, width=480)

##################
    lower_cor = np.array([Hlo.get(), Slo.get(), Vlo.get()])
    upper_cor = np.array([HUp.get(), SUp.get(), VUp.get()])

    mask = cv2.inRange(frame, lower_cor, upper_cor)

    b, g, r = cv2.split(frame)
    frame = cv2.merge((r, g, b))

    kernel = np.ones((9, 9), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#################
    mask = Image.fromarray(mask)
    img = Image.fromarray(frame)

    imgtk = ImageTk.PhotoImage(image=img)
    masktk = ImageTk.PhotoImage(image=mask)

    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)


    maskL.imgtk = masktk
    maskL.configure(image=masktk)
    window.after(1, show_frame)



show_frame()  #
window.mainloop()  #GUI
