from threading import *
from time import sleep,time

class monobehaviour:
    def __init__(self) -> None:
        self.name=None
        self.Start()
        self.fpss=0
        self.callFixed()
    def fps(self):
        a=0
        b=0
        t1=time()
        while a!=100:
            for i in range(10):
                b+=1
        self.fpss=1/(time()-t1)

    def Start(self):
        pass
    def updatec(self):
        while True:
            self.Update()
            sleep(1/self.fpss)
    def display(self):
        print(self.name)
    def callFixed(self):
        while True:
            self.FixedUpdate()
            sleep(self.fixeddelay/1000)
    def FixedUpdate(self):
        pass
    def Update(self):
        pass