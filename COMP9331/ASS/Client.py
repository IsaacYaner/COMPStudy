from Communicator import UDPCommunicator
from Receiver import *
from Listener import *
from Sender import *

class Client():
    def __init__(self, ip, port):
        self.receiver = CommandLineReceiver()
        self.client = CommandListener()
        self.host = UDPCommunicator("127.0.0.1", 10086)

    def run(self):
        while True:
            command = self.receiver.read()
            logging = self.client.read(command)
            if logging is not None:
                print(logging)
            else:
                response = self.host.fetch(command)
                print(response)
            # catch return phrase
            # Prompt commands