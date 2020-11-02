import tkinter as tk
from tkinter import *
from tkinter import filedialog

def browse_folder():
    global search_path
    filename = filedialog.askdirectory()
    search_path.set(filename)
    print(filename)


def save_folder():
    global save_path
    filename = filedialog.askdirectory()
    save_path.set(filename)
    print(filename)

box = tk.Tk()
box.geometry("400x550")
search_path = StringVar()
save_path = StringVar()

lbl = Label(master=box,textvariable=search_path)
lbl.grid(row=0, column=1)

lbl1 = Label(master=box,textvariable=save_path)
lbl1.grid(row=0, column=1)
lbl1.place(x=0,y=50)

button = Button(text="Browse", command=browse_folder)
button.place(x=300,y=0)

button1 = Button(text="save in", command = save_folder)
button1.place(x=300,y=50)

mainloop()