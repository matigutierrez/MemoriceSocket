import socket
import threading

from Memorice import Memorice


class Server():

    def __init__(self):
        self.host = 'localhost'
        self.port = 9999
        self.maxcon = 10
        self.memorice = Memorice()
        self.memorice.llenar()
        self.cont = 0

    def start(self):
        self.s = socket.socket()
        self.s.bind((self.host, self.port))
        self.s.listen(self.maxcon)
        while True:
            client = Client(self.s.accept(), self.memorice, self.cont)
            client.start()
            self.cont = self.cont + 1

class Client(threading.Thread):

    def __init__(self, (sc, address), memorice, cont):
        threading.Thread.__init__(self)
        self.sc = sc
        self.address = address
        self.memor = memorice.matriz
        self.matriz2 = memorice.matriz2
        self.conta = cont

    def run(self):
        nombre = self.sc.recv(1024)
        self.sc.send(str(self.memor))
        self.sc.send(str(self.matriz2))
        print self.memor
        self.conta = self.conta + 1
        print 'El usuario '+ str(self.conta) +' '+ nombre + ' se ha conectado'
        while True:
            recibido = self.sc.recv(1024)
            reciv = str(recibido).split(",")
            if (self.memor[int(reciv[1])][int(reciv[2])] == self.memor[int(reciv[3])][int(reciv[4])]):
                self.matriz2[int(reciv[1])][int(reciv[2])] = str(self.memor[int(reciv[1])][int(reciv[2])])
                self.matriz2[int(reciv[3])][int(reciv[4])] = str(self.memor[int(reciv[1])][int(reciv[2])])
                self.sc.send("0"+"."+str(self.matriz2))
            else:
                self.sc.send("1" + "." + str(int(reciv[1])) + "," + str(int(reciv[2])) + "," + str(int(reciv[3])) + "," + str(int(reciv[4])))
            if recibido == 'quit':
                break
            print nombre + ': ' + recibido
        print 'Adios'
        print 'El usuario ' + nombre + ' se ha desconectado'
        self.sc.close()

if __name__ == '__main__':
    server = Server()
    server.start()



