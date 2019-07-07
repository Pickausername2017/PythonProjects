from tkinter import *
from tkinter import ttk

def get_sum (event):

    num1 = int (Num1Entry.get())
    num2 = int (Num2Entry.get()) 
    

    sum = num1 + num2
    EqualEntry.delete(0, "end") 

    EqualEntry.insert(0, sum) 
    
root = Tk()

label_one = Label(root, text = "Number One").grid(column = 1, row = 1)
Num1Entry = Entry (root)
Num1Entry.grid(column = 2, row = 1)


label_plus = Label (root, text = "+")
label_plus .grid (column = 2, row = 2)

label_two = Label(root, text = "Number Two")
label_two.grid(column = 1, row = 3)

Num2Entry = Entry (root)
Num2Entry.grid(column = 2, row = 3)

EqualButton = Button (root, text = "=")
EqualButton.grid(column = 1, row = 4)
EqualButton.bind('<Button-1>', get_sum)

EqualEntry = Entry(root)
EqualEntry.grid (column = 2, row = 5)


root.mainloop() 
