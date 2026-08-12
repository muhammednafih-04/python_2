import tkinter as tk
root = tk.Tk()


canvas=tk.Canvas(root,width=300,height=500)
canvas.pack()

canvas.create_line(6,1,200,300)
canvas.create_rectangle(50,50,300,300)

root.mainloop()