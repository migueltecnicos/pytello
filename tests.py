import socket
import threading
import tello

class test:
    def __init__(self, dron):
        self.dron = dron
        self.con = None
        self.thread = threading.Thread(target=self.leer_udp(), args=())

    def conectar(self):
        print "Comando: "
        resp = self.dron.send_command("command")

    def leer_telemetria(self):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.con.bind(("192.168.10.2", 8881))

        self.con.sendto(("192.168.10.1", 8889), "command")

        self.thread.start()

    def leer_udp(self):
        while True:
            self.con.recvfrom()


