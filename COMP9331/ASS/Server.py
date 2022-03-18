from Receiver import *
from Listener import *
from Sender import *

class Server():
    def __init__(self, ip, port):
        self.receiver = CommandLineReceiver
        self.client = CommandListener()
        self.sender = UDPSender()

    def run(self):
        while True:
            command = self.receiver.read()
            response = self.client.read(command)
            if response is not None:
                print(response)
            else:
                self.sender.send(command)
            # catch return phrase