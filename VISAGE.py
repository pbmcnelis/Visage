from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
import os, random

##root window 
root = tk.Tk()
root.title("VISAGE")
root.geometry("1100x1100")

frame = Frame(root)
frame.pack()


##canvas to work with
canvas = Canvas(root, width = 1000, height = 1000)
canvas.pack()

desc = tk.StringVar()

##save the text input about the image to a file
def saveTextToFile ():
    to_save=desc.get()
    saved = open("saved_text.txt", "a")
    saved.write(to_save)
    saved.write("\n")
    saved.close()
    return;
    
##retrieve the image to be studied and resize it TODO: Dynamic resizing
def getImageAndResize ():
    rand = random.choice(os.listdir("C:\Python34\VISAGE_PICS\\")) 
    img=Image.open("C:\\Python34\\VISAGE_PICS\\"+ rand, "r")
    img2=img.resize((800, 400), Image.ANTIALIAS)
    to_display=ImageTk.PhotoImage(img2)
    canvas.create_image(20,20, anchor=NW, image=to_display, tags=('pic'))
    canvas.update()
    return;
 

##sleep for 5 seconds and then clear the image TODO: make user configurable
def sleepAndClear ():
    time.sleep(2)
    canvas.delete('pic')
    root.update()
    return;

##Create the label, text entry box, and button for the user to enter what they can rememeber
def entryBox ():
    label = tk.Label(root, text = "Enter every detail you remember no matter the signifigance: ")
    descEntered = tk.Entry(root, width = 100, textvariable = desc)
    button1 = tk.Button(text='Save', command = saveTextToFile)
    button2 = tk.Button(text='Play Again', command = start)
    button3 = tk.Button(root, text='Exit', command = close_window)

    #pack them in the gui
    label.pack()
    descEntered.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    return;

def close_window():
    root.destroy()
    return;

def start():
    canvas.delete(all)
    getImageAndResize()
    sleepAndClear()

getImageAndResize()
sleepAndClear()
entryBox()


root.mainloop()

