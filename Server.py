from socket import *


def createsocket(players):
    server =socket()
    host = gethostbyname(gethostname())
    connections=[]
    port=2024
    server.bind((host,port))
    server.listen(players)
    c,addr=server.accept()
    connections.append(c)
    while True:
        for i in connections:
            msg=i.recv(6000)
            msg=msg+'.transform'
            if not i:
                for i in connections:
                    i.send(msg) 
createsocket(3)
