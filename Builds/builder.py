import json
from tkinter import *
from tkinter import filedialog
import os
import shutil
from PIL import Image
cd=os.getcwd()
print(cd)
os.chdir('./Builds')
root = Tk()
root.geometry('500x200')
root.title("Build your game")
class Builder:
    #Init for the class
    def __init__(self) -> None:
        #Path variables
        self.Spath=StringVar(value=f'{os.path.join(cd,"icon.png")}')
        self.Epath=Entry(width=60,textvariable=self.Spath).place(x=50,y=40)
        self.Lpath=Label(text='Path:').place(x=30,y=40)
        #Button variables
        self.b=Button(root,text='Done, build the game',command=self.build)
        self.b2=Button(root,text='Browse',command=self.browse)
        self.b.place(x=250,y=60)
        self.b2.place(x=100,y=60)
        #Design
        self.un_click1=Button(text='Bruh') 
        self.un_click1.pack()
    #Builds/converts the game into .exe file
    def build(self):
        for i,dirname,f in os.walk('.'):
            for dirnames in dirname:
                if dirnames=='Compile':
                    shutil.rmtree('./Compile')
        os.mkdir('./Compile')
        shutil.copy2('test.pyw','./Compile')
        path=self.Spath.get()
        img=Image.open(r'{}'.format(path))
        os.chdir('./Compile')
        img.save('icon.ico')

        os.system(f'pyinstaller --onefile test.pyw --icon=icon.ico')
    #Lets you browse the icon for exe file
    def browse(self):
        try:
            read=filedialog.askopenfile(filetypes=(('PNG(.png)','*.png'),('JPEG(.jpeg)','*.jpeg'),('Icon(.ico)','*.ico')))
            self.Spath.set(read.name)
        except AttributeError:pass
Builder()
root.wm_iconbitmap('Icon.ico')
root.mainloop()