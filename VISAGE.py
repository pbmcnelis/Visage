from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
import os, random


##root window 
root = tk.Tk()
root.title("VISAGE")
root.geometry("1000x1000")

#frame = Frame(root)
#frame.pack()


##canvas to work with
canvas = Canvas(root, width = 800, height = 500)
canvas.pack()

desc = tk.StringVar() #var to hold the description of the picture

##save the text input about the image to a file
def saveTextToFile ():
    to_save=desc.get() #assign text to local var
    saved = open("saved_text.txt", "a") #open the file with append
    saved.write(to_save) #write text to the file
    saved.write("\n") #newline for readability  
    saved.close() #close file
    return;
    
##retrieve the image to be studied and resize it TODO: Dynamic resizing
def getImageAndResize ():
    rand = random.choice(os.listdir("C:\Python34\VISAGE_PICS\\")) #select random pic from this dir
    img=Image.open("C:\\Python34\\VISAGE_PICS\\"+ rand, "r") #open the pic from rand selection  
    img2=img.resize((800, 400), Image.ANTIALIAS) #resize the image to fit app
    to_display=ImageTk.PhotoImage(img2) #resave resized image
    canvas.create_image(20,20, anchor=NW, image=to_display, tags=('pic')) #display the image
    canvas.update() #update canvas
    return;
 

##sleep for 5 seconds and then clear the image TODO: make user configurable
def sleepAndClear ():
    time.sleep(5) #sleep 5 seconds TODO: make user configurable
    canvas.delete('pic') #delete the pic
    root.update() #update root
    return;

##Create the label, text entry box, and button for the user to enter what they can rememeber
def entryBox ():
    label = tk.Label(root, text = "Enter every detail you remember no matter the signifigance: ") #label

    TextArea =  Text() #text
    ScrollBar = Scrollbar(root) #scrollbar

    #make textbox have a scrollbar
    ScrollBar = Scrollbar(root)
    ScrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollBar.set)
    ScrollBar.pack(side=RIGHT, fill=Y)

    TextArea = tk.Entry(root, width = 100, textvariable = desc) #get the text from usr
    button1  = tk.Button(text='Save', command = lambda:[funcSve(), TextArea.delete(0,END)]) #save text and clear box
    button2  = tk.Button(text='Play Again', command = restart) #play again
    button3  = tk.Button(root, text='Exit', command = close_window) #exit the program

    #pack them in the gui
    label.pack()
    TextArea.pack(expand = TRUE, fill =  BOTH, side = TOP) #expand to fit canvas and push to top of space
    button1.pack(side = LEFT)
    button2.pack(side = BOTTOM)
    button3.pack(side = RIGHT)
    return;

#save text to file from button labmda
def funcSve():
    saveTextToFile() 
    return;

#close program by destroying the root window
def close_window():
    root.destroy()
    return;

#restart
def restart():
    canvas.delete(all)
    getImageAndResize()
    sleepAndClear()


getImageAndResize()
sleepAndClear()
entryBox()

root.mainloop()

