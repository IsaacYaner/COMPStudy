from turtle import end_fill
from pytest import fail
from torch import addr
from Receiver import *
from Listener import *
from Sender import *
from Communicator import *
import HashMessage
from PassManager import PassManager

class Server():
    def __init__(self, port):
        self.host = UDPCommunicator(src_ip="127.0.0.1", src_port=port, no_timeout=True)
        self.auth = PassManager()
        self.auth.read()

    def run(self):
        print('Waiting for clients')
        # DELETE simulate packet loss
        failrate = 0

        seenCommands = {}
        while True:
            originalCommand, address = self.host.reads()
            command, stamp = HashMessage.decode(originalCommand)
            command = str(command, encoding='utf-8')

            # DELETE
            import random
            if random.uniform(0, 1) < failrate:
                continue
            
            # To avoid processing a same command several times
            if stamp not in seenCommands:
                reply = bytewise(self.handle(command))
                seenCommands[stamp] = reply
                reply = stamp+reply
            else:
                reply = seenCommands[stamp]

            # DELETE
            if random.uniform(0, 1) < failrate:
                continue

            self.host.send(reply, address[0], address[1])

    def handle(self, command):
        command = command.split()
        if command[0] == 'LOGIN':
            name = command[1]
            if len(command) == 2:
                print('Client authenticating')
                if not self.auth.exist(name):
                    return 'User doesn\'t exist, you are creating a new account\nEnter password: '
                if self.auth.isOnline(name):
                    return f'{name} has already logged in\n'
                return 'Enter password: '
            
            password = command[2]
            if self.auth.login(name, password):
                print(f'{name} successful login')
                return 'Welcome to the forum\n'

            print('Incorrect password')
            return 'Invalid password\n'


server = Server(10095)
server.run()
