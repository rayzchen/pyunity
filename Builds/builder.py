from tkinter import *
from tkinter import filedialog
from os import *
cd=getcwd()
print(cd)
root = Tk()
root.geometry('1000x1000')
root.title("Build your game")
class Builder:
    def __init__(self) -> None:
        self.Spath=StringVar(value=f'{path.join(cd,"icon.png")}')
        self.Epath=Entry(width=100,textvariable=self.Spath).place(x=100,y=10)
        self.Lpath=Label(text='Path:').place(x=60,y=10)
        self.b=Button(root,text='Done, build the game',command=self.build)
        self.b2=Button(root,text='Browse',command=self.browse)
        self.b.place(x=600,y=600)
        self.b2.place(x=100,y=600)
    def build(self):
        pass
    def browse(self):
        read=filedialog.askopenfile(filetypes=(('PNG(.png)','*.png'),('JPEG(.jpeg)','*.jpeg'),('Icon(.ico)','*.ico')))
        self.Spath.set(read.name)
Builder()
cw=chdir('Builds')
root.wm_iconbitmap('Icon.ico')
root.mainloop()