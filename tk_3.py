'''import tkinter as tk
from tkinter import messagebox

root=tk.Tk()

messagebox.showwarning("info","last warning for you")

root.mainloop()'''



import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self,root):
        self.label=tk.Label(root,text="hello")
        self.label.pack()
root=tk.Tk()
app=App (root)

root.mainloop()

