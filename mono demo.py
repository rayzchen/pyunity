import pyunity

class GameObject(monobehaviour):
    def Start(self):
        self.name='Class name here'
        #You can change the call delay between FixedUpdate() by 
        self.fixeddelay=12#Time in milliseconds
    def Update(self):
        #Your code
        print(63)
    def FixedUpdate(self):
        #Your code
        print(65)