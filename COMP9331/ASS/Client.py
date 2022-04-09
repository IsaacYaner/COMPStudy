from Communicator import UDPCommunicator
from Receiver import *
from Listener import *
from Sender import *
import HashMessage
from PassManager import *
import time

class Client():
    def __init__(self, ip="127.0.0.1", port=10085):
        self.receiver = CommandLineReceiver()
        self.client = CommandListener()
        self.host = UDPCommunicator(ip, port)
        self.fileSender = TCPSender(ip, port)
        self.name = None

    def run(self):
        self.login()
        while True:
            print('Enter one of the following commands: CRT, MSG, DLT, EDT, LST, RDT, UPD, DWN, RMV, XIT: ', end='')
            command = self.receiver.read()
            logging = self.client.read(command)
            if logging is not None:
                print(logging)
            else:
                response = self.communicate(self.name + ' ' + command)
                if response != 'None':
                    print(response)
            # catch return phrase
            # Prompt commands
    
    def communicate(self, command):
        feat = HashMessage.feature(command)
        originalCommand = command
        command = HashMessage.encode(command, feat=feat)
        # Set timeout thing? QUESTION
        while True:
            # To check that the message from server is for this command
            response = self.host.fetch(command)
            response, featReply = HashMessage.decode(response)
            if featReply == feat:
                break
            time.sleep(0.1)     # Avoid overloading # DELETE
        # Upload the file TODO
        if 'uploaded' in response and 'UPD' in originalCommand.split()[1]:
            filename = originalCommand.split()[3]
            with open(str(filename), 'rb') as fp:
                fileContent = fp.read()
                self.fileSender.send(fileContent)

        if 'successful' in response and 'DWN' in originalCommand.split()[1]:
            data = self.fileSender.send(b'sth')
            filename = originalCommand.split()[3]
            print(originalCommand)
            with open(filename, 'wb') as f:
                f.write(bytewise(data))
        return response
    
    def login(self):
        while True:
            print('Enter username: ', end='')
            name = self.receiver.read()
            self.name = name
            loginStatus = self.communicate(name+' LOGIN')
            print(loginStatus, end='')
            if 'logged' in loginStatus:
                continue

            password = self.receiver.read()
            successful = self.communicate(name+' LOGIN '+password)
            print(successful, end='')
            if 'Welcome' in successful:
                break


import sys
client = Client(port = int(sys.argv[1]))
client.run()