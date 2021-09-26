from tkinter import *

menu=Tk()

button = []
for i in range(3):
    m = 3+i
    button.append(i)
    button[i] = []
    for j in range(3):
        n = j
        button[i].append(j)
        button[i][j] = Button( bd=5, height=4, width=8)
        button[i][j].grid(row=m, column=n)

menu.mainloop()
