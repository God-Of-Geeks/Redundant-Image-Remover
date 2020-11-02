import tkinter as tk
from tkinter import *
from tkinter import filedialog

def browse_folder():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


box = tk.Tk()
folder_path = StringVar()
lbl1 = Label(master=box,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button = Button(text="Browse", command=browse_folder)
button.grid(row=0, column=3)

mainloop()