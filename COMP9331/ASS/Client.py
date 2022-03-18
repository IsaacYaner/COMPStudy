from Communicator import UDPCommunicator
from Receiver import *
from Listener import *
from Sender import *
import HashMessage

class Client():
    def __init__(self, ip="127.0.0.1", port=10086):
        self.receiver = CommandLineReceiver()
        self.client = CommandListener()
        self.host = UDPCommunicator(ip, port)

    def run(self):
        while True:
            command = self.receiver.read()
            logging = self.client.read(command)
            if logging is not None:
                print(logging)
            else:
                feat = HashMessage.feature(command)
                command = HashMessage.encode(command, feat=feat)
                # Set timeout thing? QUESTION
                while True:
                    # To check that the message from server is for this command
                    response = self.host.fetch(command)
                    response, featReply = HashMessage.decode(response)
                    if featReply == feat:
                        break
                    print('unmatch')
                print(response)
            # catch return phrase
            # Prompt commands