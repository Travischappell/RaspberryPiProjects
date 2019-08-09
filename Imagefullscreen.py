#!/usr/bin/python

""" New Image Viewer uses Tkinter GUI, since I cant figure anything else out"""
""" Place script in photo dir first """

import tkinter as tk
import os, random, time
from  PIL import Image, ImageTk

Extensions = ['JPG', 'BMP', 'PNG']


# TODO: get a list of Current Working Directoy
# cwd = os.getcwd()
# Images = []
# for ImageP in cwd:
#     for i in os.listdir(ImageP):
#         Pic = os.path.join(ImageP,i)
#         ext = Pic.split('.')[::-1][0].upper()
#         if ext in Extensions:
#             Images.append(Image)
#             return Images

# path = os.curdir()
path = os.path.dirname(os.path.realpath(__file__))+'\\' #pulls the dir the file is in
# path = 'C:\\Users\\Travis Chappell\\Documents\\Projects\\Photographs\\Edited\\Edited and Cropped\\'
print('Getting files from path: '+path)

filename = path+'Wedding Edited.jpg'
files = os.listdir(path=path)

# Lists out only .jpg or .png
files = []
for filename in os.listdir(path=path):
   if (filename.endswith('.png') or filename.endswith('.jpg')):
       files.append(filename)
   else:
        continue



 # need to add in the next steps

# Manually set the screen dim
# screenheight = 768
# screenwidth = 1024


root = tk.Tk()

screenheight = root.winfo_screenheight()
screenwidth = root.winfo_screenwidth()


# for file in range(len(files)):
file = random.choice(files)
print('Showing image: ' + file)

# Opens and resizes the image
img1 = (Image.open(file)) # Opens as Image object (2461, 3691)
imwidth, imheight = img1.size
if imheight > imwidth:
    newimwidth = int(imwidth / (imheight / screenheight))
    imresize = [newimwidth, screenheight]
else:
    newimheight = int(imheight / (imwidth / screenwidth))
    imresize = [screenwidth, newimheight]

img1_resized = img1.resize(imresize, Image.ANTIALIAS) # resizes image to size

# SChanges Image obj to TkImage obj
tkimg1 = ImageTk.PhotoImage(img1_resized) # Converts to tk Image


background_img = tk.Label(root, image=tkimg1)
background_img.pack()

canvas = tk.Canvas(root, height=screenheight, width=screenwidth)
canvas.pack()

root.wm_attributes('-fullscreen',True)
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()


