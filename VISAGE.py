from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
import os, random


##root window 
root = tk.Tk()
root.title("VISAGE")
root.geometry("1000x620")

#frame = Frame(root)
#frame.pack()


##canvas to work with
canvas = Canvas(root, width = 960, height = 540)
canvas.pack()

desc = tk.StringVar() #var to hold the description of the picture

##save the text input about the image to a file
#assign text to local var
#open the file with append
#write text to the file
#newline for readability
#close file
##
def saveTextToFile ():
    to_save=desc.get() 
    saved = open("saved_text.txt", "a") 
    saved.write(to_save) 
    saved.write("\n") 
    saved.close() 
    return;
    
##retrieve the image to be studied and resize it TODO: Dynamic resizing
#select random pic from this dir
#open the pic from rand selection  
#resize the image to fit app
#resave resized image
#display the image
#update canvas
##
def getImageAndResize ():
    rand = random.choice(os.listdir("C:\Python34\VISAGE_PICS\\")) 
    img=Image.open("C:\\Python34\\VISAGE_PICS\\"+ rand, "r") 
    img2=img.resize((960, 540), Image.ANTIALIAS) 
    to_display=ImageTk.PhotoImage(img2) 
    canvas.create_image(0,0, anchor=NW, image=to_display, tags=('pic')) 
    canvas.pack(expand=1)
    canvas.update()
    return;
 

##sleep for 5 seconds and then clear the image TODO: make user configurable
#sleep 5 seconds TODO: make user configurable
#delete the pic
#update root
##
def sleepAndClear ():
    time.sleep(5) 
    canvas.delete('pic') 
    root.update() 
    return;

##Create the label, text entry box, and button for the user to enter what they can rememeber
def entryBox ():
    label = tk.Label(root, text = "Enter every detail you remember no matter the signifigance, seperated by commas: ") #label

    TextArea =  Text() #text
    #ScrollBar = Scrollbar(root) #scrollbar

    #make textbox have a scrollbar
    #ScrollBar = Scrollbar(root)
    #ScrollBar.config(command=TextArea.yview)
    #TextArea.config(yscrollcommand=ScrollBar.set)
    #ScrollBar.pack(side=RIGHT, fill=Y)

    TextArea = tk.Entry(root, width = 100, textvariable = desc) #get the text from usr
    button1  = tk.Button(text='Save', background = "green", command = lambda:[funcSve(), TextArea.delete(0,END)]) #save text and clear box
    button2  = tk.Button(text='Play Again', command = restart) #play again
    button3  = tk.Button(root, text='Exit', background = "red", command = close_window) #exit the program

    #pack them in the gui
    label.pack()
    TextArea.pack(expand = True, fill = BOTH, side = TOP) #expand to fit canvas and push to top of space
    button1.pack(side = LEFT, expand = True, fill = BOTH)
    button2.pack(side = LEFT, expand = True, fill = BOTH)
    button3.pack(side = LEFT, expand = True, fill = BOTH)
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

entryBox()
getImageAndResize()
sleepAndClear()


root.mainloop()

