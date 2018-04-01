#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:07:13 2018

@author: dexter

"""
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import time
import random

x= random.randint(60,201)
def click_me1():
    time.sleep(3)
    action1.configure(text=" getting ")
    #a_label1.configure(foreground= "red")
    action1.destroy()
    root.geometry("300x300")
    w = Label(root, text="RESULT:", font=("Helvetica", 18),fg="black")
    w.place(x=50,y=50)
    if x>=60 and x<=110:
        w = Label(root, text="Image saved", font=("Helvetica", 16),fg="blue")
        w.place(x=100,y=150)
    elif x>110 and x<=126:
        w = Label(root, text="Image sent", font=("Helvetica", 16),fg="blue")
        w.place(x=100,y=150)
    else:
        w = Label(root, text="Image crashed ", font=("Helvetica", 16),fg="blue")
        w.place(x=100,y=150)
        
def select_image():
    global panelA, panelB
    path = filedialog.askopenfilename()  
    time.sleep(2)
    if len(path) > 0:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)
        
        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)
            
        else:	
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged
    btn.destroy()
         


im = Image.open('index.jpeg')
roo= Tk()

tkimage = ImageTk.PhotoImage(im)
a=Label(roo, image=tkimage).pack()
b= Label(roo, text="A TUTORIAL TO KNOW ABOUT TKINTER GUI AND EDGE DETECTION ",font=("Helvetica", 18),fg="red")
b.place(x=10,y=300)
roo.geometry("820x420")

root = Tk()
panelA = None
panelB = None

action = Button(root,text= " Quit ",font=("Helvetica", 10),command=root.quit)
action.pack(side="bottom")
action1 = Button(root,text= "Get data",font=("Helvetica", 10),command=click_me1)
action1.pack(side="bottom")
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom")

# kick off the GUI
roo.after(2000,roo.destroy)
root.mainloop()
