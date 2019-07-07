from tkinter import *
from tkinter import ttk

#This is the main window, common practice is naming it root
root = Tk()

#This puts a title on the GUI Window
root.title("Frist GUI")

#This adds a button with a text lable
ttk.Button(root, text = "Hello Tkinter").grid()

#this keeps the window open. 
root.mainloop() 
