from socket import *

from HashMessage import bytewise

class Sender():
    def __init__(self):
        pass

    def send(self, message):
        #Send via socket
        #Monitor response by multithread or blocking?
        pass

class messageLineSender(Sender):
    def __init__(self):
        pass

    def send(self, message):
        print(message)

class UDPSender(Sender):
    '''
    Description:
        Communicator using UDP sockets.
    Init arguments:
        ip: destination ip for sender
        dest_port: destination port for sender
        sock: Ready-to-use socket, default None
    '''
    def __init__(self, dest_ip=None, dest_port=None, sock=None):
        self.ip = dest_ip
        self.port = dest_port
        self.socket = sock
        if sock is None:
            self.socket = socket(AF_INET, SOCK_DGRAM) # IPV4, UDP
        #create socket
        pass

    # Send message to socket
    def send(self, message, ip=None, port=None):
        dest_host = self.ip if ip is None else ip
        dest_port = self.port if port is None else port
        
        message = bytewise(message)
        self.socket.sendto(message,(dest_host, dest_port))
        return
    
class TCPSender(Sender):
    '''
    Description:
        Communicator using UDP sockets.
    Init arguments:
        ip: destination ip for sender
        port: destination port for sender
        buffsize: buffsize of recv()
        sock: Ready-to-use socket, default None
    '''
    def __init__(self, ip=None, port=None, buffsize=None, sock=None):
        self.socket = sock
        self.port = port
        self.ip = ip
        self.buffsize = buffsize
        if buffsize is None:
            self.buffsize = 2048
    
    # Send message to socket
    def send(self, message):
        self.socket = socket(AF_INET, SOCK_STREAM)     # IPv4 and TCP connection
        self.socket.connect((self.ip, self.port))
        self.socket.send(message)
        response = self.socket.recv(self.buffsize)
        self.socket.close()
        return response