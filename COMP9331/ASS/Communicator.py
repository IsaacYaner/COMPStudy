from inspect import signature
from socket import *
from Sender import *
from Receiver import *

class Communicator():
    def __init__(self):
        pass

    def read(self):
        pass

    def send(self):
        pass

    def fetch(self):
        pass

class UDPCommunicator(Communicator):
    def __init__(self, dest_ip, dest_port, buffsize=None, maxwait=None, sock=None):
        self.socket = sock
        if sock is None:
            self.socket = socket(AF_INET, SOCK_DGRAM) # IPV4, UDP
        
        self.sender = UDPSender(dest_ip, dest_port, self.socket)
        if maxwait is not None:
            self.receiver = UDPReceiver(buffsize, maxwait, self.socket)
        else:
            self.receiver = UDPReceiver(buffsize, sock=self.socket)
        pass

    def send(self, message, ip=None, port=None):
        self.sender.send(message, ip=None, port=None)
    
    def read(self, buffsize=None):
        return self.receiver.read(buffsize)

    def reads(self, buffsize=None):
        return self.receiver.reads(buffsize)

    def fetch(self, message):
        # Ensure that one conversation is done
        while True:
            try:
                self.send(message)
                reply= self.read()
                return reply.rstrip(b'\x00').decode("utf-8")
            except:
                continue
