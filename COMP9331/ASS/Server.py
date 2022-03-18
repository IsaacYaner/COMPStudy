from torch import addr
from Receiver import *
from Listener import *
from Sender import *
from Communicator import *
import HashMessage

class Server():
    def __init__(self, port):
        self.host = UDPCommunicator()

    def run(self):
        seenCommands = []
        while True:
            command, address = self.host.reads()
            command, stamp = HashMessage.decode(command)
            if stamp not in seenCommands:
                seenCommands.append(stamp)
                self.handle(command)
            self.host.send(command, address[0], address[1])

    def handle(self, command):
        pass

server = Server(10080)
server.run()
