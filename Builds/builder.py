from tkinter import *
from os import *
cu=getcwd()
root = Tk()
root.geometry('1000x1000')
img=PhotoImage(file='icon.png')
root.iconphoto(img)
root.title("Build your game")
root.mainloop()