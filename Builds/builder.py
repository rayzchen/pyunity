from tkinter import *
from tkinter import filedialog
from os import *
import shutil
from PIL import Image
cd=getcwd()
print(cd)
chdir('./Builds')
root = Tk()
root.geometry('500x200')
root.title("Build your game")
class Builder:
    #Init for the class
    def __init__(self) -> None:
        self.Spath=StringVar(value=f'{path.join(cd,"icon.png")}')
        self.Epath=Entry(width=60,textvariable=self.Spath).place(x=50,y=10)
        self.Lpath=Label(text='Path:').place(x=30,y=10)
        self.b=Button(root,text='Done, build the game',command=self.build)
        self.b2=Button(root,text='Browse',command=self.browse)
        self.b.place(x=250,y=60)
        self.b2.place(x=100,y=60)
    #Builds/converts the game into .exe file
    def build(self):
        for i,dirname,f in walk('.'):
            for dirnames in dirname:
                if dirnames=='Compile':
                    shutil.rmtree('./Compile')
        mkdir('./Compile')
        shutil.copy2('test.pyw','./Compile')
        path=self.Spath.get()
        img=Image.open(r'{}'.format(path))
        chdir('./Compile')
        img.save('icon.ico')

        system(f'pyinstaller --onefile test.pyw --icon=icon.ico')
    #Lets you browse the icon for exe file
    def browse(self):
        try:
            read=filedialog.askopenfile(filetypes=(('PNG(.png)','*.png'),('JPEG(.jpeg)','*.jpeg'),('Icon(.ico)','*.ico')))
            self.Spath.set(read.name)
        except AttributeError:pass
Builder()
root.wm_iconbitmap('Icon.ico')
root.mainloop()