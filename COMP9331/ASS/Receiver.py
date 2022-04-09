from email import message
from socket import *

MAX_WAIT_TIME = 600 

class Receiver():
    def __init__(self):
        pass

    def read(self):
        pass

class CommandLineReceiver(Receiver):
    def __init__(self):
        pass

    def read(self):
        return input()

class UDPReceiver(Receiver):
    def __init__(self, buffsize=None, maxwait=None, sock=None, ip=None, port=None, no_timeout=False):
        self.buffsize = buffsize
        if buffsize is None:
            self.buffsize = 2048
        self.maxwait = maxwait if maxwait is not None else MAX_WAIT_TIME

        self.socket = sock
        if sock is None:
            self.socket = socket(AF_INET, SOCK_DGRAM) # IPV4, UDP

        if not no_timeout:
            self.socket.settimeout(self.maxwait/1000)     # Time out criteria

        if ip is not None and port is not None:
            self.socket.bind((ip, port))
        #self.socket.setblocking(0) #Non-blocking
        #create socket
        pass

    def read(self, buffsize=None):
        buff = self.buffsize if buffsize is None else buffsize
        message, _ = self.socket.recvfrom(buff)
        return message
    
    def reads(self, buffsize=None):
        buff = self.buffsize if buffsize is None else buffsize
        message, address = self.socket.recvfrom(buff)
        return message, address
    

class BufferReceiver(Receiver):
    def __init__(self, buffer=None):
        self.buffer = buffer
        if buffer is None:
            self.buffer = []
        
    def read(self):
        while True:
            pass
        return self.buffer.pop()

class TCPReceiver(Receiver):
    def __init__(self, ip=None, port=None, buffsize=None, sock=None):
        self.socket = sock
        self.port = port
        if sock is None:
            self.socket = socket(AF_INET, SOCK_STREAM)     # IPv4 and TCP connection

        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.buffsize = buffsize
        if buffsize is None:
            self.buffsize = 2048
        if ip is not None and port is not None:
            self.socket.bind((ip, port))
        self.socket.listen(1)
    
    def read(self, cont=None):
        connectionSocket, addr = self.socket.accept()

        data = connectionSocket.recv(self.buffsize).decode() # Get data from client
        if cont is not None:
            connectionSocket.send(cont)
        connectionSocket.close()
        return data
