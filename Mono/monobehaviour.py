from threading import *
from time import sleep
class monobehaviour:
    def __init__(self) -> None:
        self.name=None
        self.Start()
        self.callFixed()
    def Start(self):
        pass
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