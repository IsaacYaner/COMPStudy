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
    '''
    Description:
        Communicator using UDP sockets.
    Init arguments:
        dest_ip: destination ip for sender
        dest_port: destination port for sender
        buffsize: buffsize of recv()
        maxwait: timeout limit for receiver
        sock: Ready-to-use socket, default None
        src_ip: source ip for receiver
        src_port: source port for reciver
        no_timeout: whether set time_out value
    '''
    def __init__(self, dest_ip=None, dest_port=None, buffsize=None, maxwait=None, sock=None, src_ip=None, src_port=None, no_timeout=False):
        self.socket = sock
        if sock is None:
            self.socket = socket(AF_INET, SOCK_DGRAM) # IPV4, UDP
        # Ensure that the port freed after program is terminated
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        self.sender = UDPSender(dest_ip, dest_port, self.socket)
        self.receiver = UDPReceiver(buffsize, maxwait, self.socket, src_ip, src_port, no_timeout)
        pass

    # Send through sender
    def send(self, message, ip=None, port=None):
        self.sender.send(message, ip, port)
    
    def read(self, buffsize=None):
        return self.receiver.read(buffsize)

    # wrapper for receiver.reads()
    def reads(self, buffsize=None):
        return self.receiver.reads(buffsize)

    # Send message and return the response for this message
    def fetch(self, message):
        # Ensure that one conversation is done
        while True:
            try:
                self.send(message)
                reply = self.read()
                # Strip the redundant '\x00's
                return reply.rstrip(b'\x00').decode("utf-8")
            except:
                continue
