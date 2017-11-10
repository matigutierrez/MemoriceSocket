import socket
import time
import os

from Escuchador import Escuchador


class Cliente():

    def __init__(self):
        self.s = socket.socket()
        self.s.connect(('localhost', 9999))
        self.nombre=""
        self.reciv = []
        self.matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.matriz2 = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
        self.cont2 = 0
        self.a = ""
        self.b = ""
        #escuchador = Escuchador(self.s)
        #escuchador.start()

    def inicio(self):
        self.nombre = raw_input("Ingrese su nombre")
        print "Bienvenido " + self.nombre + " al juego de Memorice"
        print " "
        print "Memorice las posiciones de los numeros"
        self.s.send(self.nombre)
        self.RecibirMatriz()
        self.MostrarMatriz()
        time.sleep(5)
        os.system('cls')
        print "Encuentra la pareja de Numeros"
        self.RecibirMatriz()
        self.MatrizFalsa()
        print "Utiliza las coordenadas de una matriz"

    def enviar(self):
        mensaje = raw_input(">")
        self.s.send(self.nombre+","+mensaje)

    def recivir(self):
        recivido = self.s.recv(1024)
        rec = str(recivido).split(".")
        if rec[0] == "0":
            self.ActualizarMatriz(rec[1])
            self.MatrizFalsa()
        else:
            print "Usted a Fallado "

    def MostrarMatriz(self):
        self.cont2 = 0
        self.a = ""
        for i in range(0, 4):
            self.a = ""
            for j in range(0, 4):
                self.matriz[i][j] = self.reciv[self.cont2]
                self.cont2 = self.cont2 + 1
                self.a = self.a + str(self.matriz[i][j]) + " | "
            print self.a

    def MatrizFalsa(self):
        self.cont2 = 0
        self.a = ""
        for i in range(0, 4):
            self.a = ""
            for j in range(0, 4):
                self.matriz2[i][j] = self.reciv[self.cont2]
                self.cont2 = self.cont2 + 1
                self.a = self.a + str(self.matriz2[i][j]) + " | "
            print self.a


    def RecibirMatriz(self):
        self.reciv = []
        recivo = self.s.recv(1024)
        recivo = recivo.replace("[", "")
        recivo = recivo.replace("]", "")
        recivo = recivo.replace(" ", "")
        self.reciv = recivo.split(",")

    def ActualizarMatriz(self, var):
        self.reciv = []
        recivo = var
        recivo = recivo.replace("[", "")
        recivo = recivo.replace("]", "")
        recivo = recivo.replace(" ", "")
        self.reciv = recivo.split(",")


if __name__ == '__main__':
    while True:
        c = Cliente()
        c.inicio()
        c.enviar()
        c.recivir()