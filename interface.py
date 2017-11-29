import numpy as np
import cv2
import tkinter as tk


from PIL import ImageTk,Image





def salvaConfig():
    if v.get()== '':
        return print('Digite um nome de cor para salvar')
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
    print(str(result))

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("A.C.C")

window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

maskFrame = tk.Frame(window, width=600, height=500)
maskFrame.grid(row=0, column=1, padx=10, pady=2)



#captura camera e cria dois label
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)

maskL = tk.Label(maskFrame)
maskL.grid(row=0, column=1)

#captura a camera
cap = cv2.VideoCapture('vid/bg.avi')

#SLIDES
Hlo =tk.Scale(orient='horizontal', from_=1, to=255,)
Hlo.grid(row=600, column=0, padx=0, pady=0)

HUp =tk.Scale(orient='horizontal', from_=1, to=255,)
HUp.grid(row=602, column=0, padx=0, pady=0)

Slo =tk.Scale(orient='horizontal', from_=1, to=255)
Slo.grid(row=604, column=0, padx=0, pady=0)

SUp =tk.Scale(orient='horizontal', from_=1, to=255)
SUp.grid(row=606, column=0, padx=0, pady=0)

Vlo =tk.Scale(orient='horizontal', from_=1, to=255)
Vlo.grid(row=608, column=0)

VUp =tk.Scale(orient='horizontal', from_=1, to=255)
VUp.grid(row=610, column=0)

#botao salvar
button = tk.Button(window, text="Salvar", width=20,height = 3, command=answer)
button.grid(row=614, column=1, columnspan=3)


#input text nome Cor
v = tk.StringVar()
e = tk.Entry(window, textvariable=v,width=50)
w = tk.Label(window, text="Digite o nome da cor:")
w.grid(row=600, column=1)
e.grid(row=601, column=1)




def show_frame():
    _, frame = cap.read()

##################
    lower_cor = np.array([Hlo.get(), Slo.get(), Vlo.get()])
    upper_cor = np.array([HUp.get(), SUp.get(), VUp.get()])

    mask = cv2.inRange(frame, lower_cor, upper_cor)

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
    window.after(10, show_frame)



show_frame()  #
window.mainloop()  #GUI