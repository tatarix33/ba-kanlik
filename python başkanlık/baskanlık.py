from tkinter import *
import time
import pygame
from PIL import Image,ImageTk,ImageGrab
import win32api
import threading
import random
import time


pencere= Tk()

pencere.title("ÇFL 17-18 BAŞKANLIK")
pencere.geometry("520x339")

image=Image.open("başkan.JPG")
photo_image=ImageTk.PhotoImage(image)
bg_label= Label(pencere,image=photo_image)
bg_label.pack()
pencere.resizable(False, False)



giris_label = Label(pencere, text="2017-18 Çorum Fen Lisesi Başkanlık seçimlerinde kime oy vereceksin",
                    font=("bold", 13), fg="#993300", bg="#00ff66")


def ses():
    pygame.mixer.init()
    pygame.mixer.music.load("deneme.mp3")
    pygame.mixer.music.play()
    time.sleep(.1)

giris_label.place(x=2, y=10)

buton_uftade = Button(pencere, text="Üftade\nDUMAN", bg="#3300cc", fg="#ff6601", width=10, height=3, font=("bold", 10),command=ses)
buton_uftade.place(x=50, y=200)

buton_beyza = Button(pencere, text="DİĞERLERİ", bg="#003333", fg="#ff6600", width=10, height=3, font=("bold", 10))
buton_beyza.place(x=350, y=200)


def xxx():
    cord = [[275, 150], [425, 250], [425, 150], [275, 250]]


    while True:

        sa=ImageGrab.grab()
        x,y=win32api.GetCursorPos()
        a=sa.getpixel((x,y))
        if a in ((0,51,51),(255,102,0)):
            c=random.choice(cord)
            x,y=c[0],c[1]
            buton_beyza.place(x=x,y=y)
            time.sleep(0.01)



rT = threading.Thread(target=xxx)
rT.start()


pencere.mainloop()
