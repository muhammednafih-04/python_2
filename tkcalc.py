import tkinter as tk
def add():
    r=int(e1.get())+int(e2.get())
    label.config(text=r)
def subtract():
    r=int(e1.get())-int(e2.get())
    label.config(text=r)
def multiply():
    r=int(e1.get())*int(e2.get())
    label.config(text=r)
def divide():
    r=float(e1.get())/float(e2.get())
    label.config(text=r)

root=tk.Tk()
root.title("Calculator")


e1=tk.Entry(root)
e1.grid(row=0,column=0,columnspan=4,pady=5)

e2=tk.Entry(root)
e2.grid(row=1,column=0,columnspan=4,pady=5)


tk.Button(root,text="add",command=add).grid(row=2, column=0)

tk.Button(root,text="subtract",command=subtract).grid(row=2, column=1)

tk.Button(root,text="multiply",command=multiply).grid(row=2, column=2)

tk.Button(root,text="divide",command=divide).grid(row=2, column=3)

label=tk.Label(root,text="")
label.grid(row=3,column=0,columnspan=4,pady=10)

root.mainloop()