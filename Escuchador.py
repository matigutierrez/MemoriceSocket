import threading
import socket

class Escuchador(threading.Thread):

    def __init__(self, sc):
        threading.Thread.__init__(self)
        self.s = sc

    def run(self):
        recivido = self.s.recv(1024)
        #rec = str(recivido).split(".")
        print recivido