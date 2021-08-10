from monobehaviour import monobehaviour
class Test(monobehaviour):
    def Start(self):
        self.name='Test'
        self.fixeddelay=10000
    def FixedUpdate(self):
        print('Asd')
Test()