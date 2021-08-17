from tkinter import *
from tkinter import filedialog
from os import *
cd=getcwd()
print(cd)
root = Tk()
root.geometry('1000x1000')
root.title("Build your game")
def build(EV):
    pass
def browse(e):
    read=filedialog.askopenfile(filetypes=(('PNG(.png)','*.png'),('JPEG(.jpeg)','*.jpeg')))

Spath=StringVar(value=f'{path.join(cd,"icon.png")}')
Epath=Entry(width=100,textvariable=Spath).place(x=100,y=10)
Lpath=Label(text='Path:').place(x=60,y=10)
c=Canvas(root)

b=Button(root,text='Done, build the game')
b2=Button(root,text='Browse')
b.bind('<Button-1>',build)
b2.bind('<Button-1>',browse)
b.place(x=600,y=600)
b2.place(x=100,y=600)
cw=chdir('Builds')
root.wm_iconbitmap('Icon.ico')
root.mainloop()
