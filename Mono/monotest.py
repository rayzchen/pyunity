from monobehaviour import monobehaviour
class Test(monobehaviour):
    def Start(self):
        self.name='Test'
        self.fixeddelay=10000
    def Update(self):
        print('LOL')
Test()