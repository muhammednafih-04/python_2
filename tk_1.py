import tkinter as tk

def click():
    print("button clicked")


root = tk.Tk()
tk.Label(root,text="name").grid(row=0,column=0)
tk.Entry(root).grid(row=0,column=1)
tk.Label(root,text="age").grid(row=1,column=0)
tk.Entry(root).grid(row=1,column=1)

btn=tk.Button(root,text="click",command=click)
btn.grid(row=2,column=0,columnspan=2)

root.mainloop()

