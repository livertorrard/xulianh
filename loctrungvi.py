import tkinter as tk
from tkinter.constants import *
import os
from numpy import pad
from tkinter import Grid, PhotoImage, filedialog
from PIL import Image , ImageTk
import numpy
import random
import cv2
def chonanh():
    pathname = filedialog.askopenfilename(initialdir = "E:\Xử lí ảnh\baitap",
                                          title = "Vui lòng chọn ảnh",
                                          filetypes = (("Image files",
                                                        "*.png .jpg .jpeg .gif"),
                                                       ("all files",
                                                        "*.*")))                                             
    filename = os.path.basename(pathname)
    chonanhh(filename)
    img = cv2.imread(filename)
    blur_img = cv2.medianBlur(img, ksize=9)
    
    radomimg = random.randint(1, 1000000)
    cv2.imwrite(str(radomimg)+'anhsaukhiloc.png', blur_img)
    taolao = tk.PhotoImage(file=str(radomimg)+"anhsaukhiloc.png")
    test1.configure(image=taolao)
    test1.image = taolao

def chonanhh(filename):
    alo = tk.PhotoImage(file=filename)
    test.configure(image=alo)
    test.image = alo  

win = tk.Tk()
win.title("Xử lí ảnh")
win.geometry('900x700')
win.resizable(width=False,height=False)
tieude = tk.Label(win,text="LỌC ẢNH TRUNG VỊ",font="Times 20 bold",fg="white",bg="black")
tieude.pack(side=TOP,pady=15)

FrameButton = tk.Frame(win)
FrameButton.pack(padx=120)

photo =tk.PhotoImage(file="logo.png")
test = tk.Label(win,image=photo)
test.place(width=350,height=400,x=50,y=180)

test1 = tk.Label(win,image=photo,width=200,height=200)
test1.place(width=350,height=400,x=490,y=180)

label = tk.Label(win,text="ẢNH GỐC",font="Times 20 bold",fg="green")
label.place(x =150,y = 130)

label2 = tk.Label(win,text="ẢNH SAU KHI LỌC",font="Times 20 bold",fg="green")
label2.place(x =530,y = 130)

chonAnh =  tk.Button(FrameButton,text="Chọn Ảnh",command=chonanh)
chonAnh.grid(row=1,column=1)



win.bind("<Return>", chonanhh)
win.mainloop()