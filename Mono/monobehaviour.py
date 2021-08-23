from threading import *
from time import sleep,time

class monobehaviour:
    def __init__(self) -> None:
        self.name=None
        self.Start()
        self.fpss=0
        
        self.thread1=Thread(target=self.callFixed)
        self.thread1.daemon=True
        self.thread1.start()
        self.thread2=Thread(target=self.callUpdate)
        self.thread2.setDaemon(True)
        self.thread2.start()
        self.thread1.join()
        self.thread2.join()
    def fps(self):
        a=0
        b=0
        t1=time()
        while a!=100:
            for i in range(10):
                b+=1
        self.fpss=1/(time()-t1)

    '''Callers start'''
    def callUpdate(self):   
        while 1:         
            self.Update()
            sleep(1/self.fpss)
    def callFixed(self):
        while 1:
            self.FixedUpdate()
            sleep(self.fixeddelay/1000)
    '''Callers end'''
    def Start(self):
        pass
    def FixedUpdate(self):
        pass
    def Update(self):
        pass