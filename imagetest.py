#!/usr/bin/python

""" New Image Viewer used MatPlotLib, since i cant figure anything else out"""
""" Current Working directory = dir of this file """

import tkinter as tk
import os
from  PIL import Image, ImageTk

Extensions = ['JPG', 'BMP', 'PNG']


# TODO: get a list of Current Working Directoy
cwd = os.getcwd()
Images = []
for ImageP in cwd:
    for i in os.listdir(ImageP):
        Pic = os.path.join(ImageP,i)
        ext = Pic.split('.')[::-1][0].upper()
        if ext in Extensions:
            Images.append(Image)
            return Images
            
##testimg = 'Bikes Cropped.jpg'           

# TODO: Build Canvas

HEIGHT = 768
WIDTH = 1024

root = tk.Tk()

# TODO: Import Image
size = 1024, 768 
img1 = (Image.open(testimg)) # Opens as Image object
img1_resized = img1.resize(size, Image.ANTIALIAS) # resizes image to size
tkimg1 = ImageTk.PhotoImage(img1_resized) # Converts to tk Image


background_img = tk.Label(root, image=tkimg1)
background_img.pack()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

root.mainloop()

