from socket import *
from threading import *
class Server:
    def __init__(self,number_player) -> None:
        self.host=gethostbyname(gethostname())
        self.port=5507
        self.socket=socket()
        self.socket.bind((self.host,self.port))
        self.socket.listen(number_player)
        self.connections=[]
        self.tacc=Thread(target=self.acc())
        self.tacc.setDaemon(True)
        self.tacc.start()
        self.trecv=Thread(target=self.recvs())
        self.trecv.start()

    def acc(self):
        a,b=self.socket.accept()
        self.connections.append(a)
    def recvs(self):
        while True:
            for i in self.connections:
                msg=i.recv(4250)
                index=self.connections.index(i)+1
                for j in range(i,len(self.connections)+1):
                    self.connections[j].send(msg)
