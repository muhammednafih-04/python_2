import tkinter as tk

def show():
    print("button clicked")

root=tk.Tk()

btn=tk.Button(root,text="press",command="show")
btn.pack()

root.mainloop()