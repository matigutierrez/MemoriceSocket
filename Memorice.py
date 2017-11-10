from random import randrange

class Memorice():
    def __init__(self):
        self.numeros = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.matriz2 = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
        self.cont = 0
        self.cont2 = 0
        self.a = ""

    def llenar(self):
        while (self.cont < 16):
            num = randrange(8)+1
            par = 0

            for i in range(0, 16):
                if (self.numeros[i] == num):
                    par = par + 1

            if (par < 2):
                self.numeros[self.cont] = num
                self.cont = self.cont + 1

        for i in range(0, 4):
            self.a = ""
            for j in range(0, 4):
                self.matriz[i][j] = self.numeros[self.cont2]
                self.cont2 = self.cont2 + 1
                self.a = self.a + str(self.matriz[i][j]) + " "
            print self.a
