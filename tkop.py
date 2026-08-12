import tkinter as tk

root=tk.Tk()

options=["spain","portugal","brazil"]
var=tk.StringVar(root)
var.set(options[0])

dropdown=tk.OptionMenu(root,var,*options)
dropdown.pack()

status =tk.Label(root,text="Ready",bd=1,relief="sunken",anchor="w")
status.pack(side="bottom",fill='x')

toolbar=tk.Frame(root)

btn=tk.Button(toolbar,text="save")
btn.pack(side="left")

toolbar.pack(side="top",fill="x")

root.mainloop()