from socket import *
from pickle import *
import RGameObject as rgo
class Client:
    def __init__(self,gamename) -> None:
        self.client=socket()
        self.client.connect(('Vittala',5507))
        self.close=False
    def send(self):
        while not self.close:
            self.client.send(rgo.RGameObject.game)
    def recv(self):pass