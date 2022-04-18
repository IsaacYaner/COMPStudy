from Communicator import UDPCommunicator
from Receiver import *
from Listener import *
from Sender import *
import HashMessage
from PassManager import *
import time

class Client():
    def __init__(self, ip="127.0.0.1", port=10085):
        self.receiver = CommandLineReceiver()   # Receiving commands from command line
        self.client = CommandListener()         # Pre-process commands
        self.host = UDPCommunicator(ip, port)   # Communicate with Server
        self.fileSender = TCPSender(ip, port)   # Send file through this interface
        self.name = None    # Username of this client, None as default

    def run(self):
        # Go through login process first
        self.login()
        while True:
            # Prompt and read commands
            print('Enter one of the following commands: CRT, MSG, DLT, EDT, LST, RDT, UPD, DWN, RMV, XIT: ', end='')
            command = self.receiver.read()
            # Return logging for invalid command
            logging = self.client.read(command)
            if logging is not None: #Invalid command
                print(logging)
            else:
                # Attach user name to the command sent
                response = self.communicate(self.name + ' ' + command)
                # Print response
                if response != 'None':
                    print(response)
            # To avoid over whelming the network
            time.sleep(0.1)
    
    def communicate(self, command):
        # Feat is the unique feature value of this command for identifying duplicated command.
        feat = HashMessage.feature(command)
        # Original command content
        originalCommand = command
        # Encoded command used for communication
        command = HashMessage.encode(command, feat=feat)
        # Set timeout thing? QUESTION Answer: notimeout, close client manually if timeout
        while True:
            # Get response
            response = self.host.fetch(command)
            response, featReply = HashMessage.decode(response)
            # To check that  the message from server is for this command
            if featReply == feat:
                break
        # Upload the file once the server has received the request
        if 'uploaded' in response and 'UPD' in originalCommand.split()[1]:
            filename = originalCommand.split()[3]
            with open(str(filename), 'rb') as fp:
                fileContent = fp.read()
                self.fileSender.send(fileContent)

        # Download the file once the server has received the request
        if 'successful' in response and 'DWN' in originalCommand.split()[1]:
            data = self.fileSender.send(b'sth')
            filename = originalCommand.split()[3]
            print(originalCommand)
            with open(filename, 'wb') as f:
                f.write(bytewise(data))
        
        # Exit
        if 'Goodbye' in response and 'XIT' in originalCommand.split()[1]:
            print(response)
            exit(0)
        
        # Return the response to run()
        return response
    
    # Login process
    def login(self):
        while True:
            print('Enter username: ', end='')
            name = self.receiver.read()
            self.name = name
            # Send LOGIN request with username only
            loginStatus = self.communicate(name+' LOGIN')
            print(loginStatus, end='')

            # If logged in, ask for username again
            if 'logged' in loginStatus:
                continue
            
            # Send LOGIN request with password
            password = self.receiver.read()
            successful = self.communicate(name+' LOGIN '+password)
            print(successful, end='')
            if 'Welcome' in successful:
                break


import sys
# Run client by python3 Client.py [dest_port]
client = Client(port = int(sys.argv[1]))
client.run()