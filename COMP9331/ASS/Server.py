from turtle import end_fill
from pytest import fail
from torch import addr
from Receiver import *
from Listener import *
from Sender import *
from Communicator import *
import HashMessage
from PassManager import PassManager
from ThreadManager import *

class Server():
    def __init__(self, port):
        self.host = UDPCommunicator(src_ip="127.0.0.1", src_port=port, no_timeout=True)
        self.auth = PassManager()
        self.auth.read()
        self.threads = ThreadManager()
        self.commands = ['CRT', 'MSG', 'DLT', 'EDT', 'LST', 'RDT', 'UPD', 'DWN', 'RMV', 'XIT']

    def run(self):
        print('Waiting for clients')
        # DELETE simulate packet loss
        failrate = 0

        seenCommands = {}
        while True:
            # Decode the message received to command and stamp
            # The stamp here is similar to sequence number
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
        if command[1] == 'LOGIN':
            name = command[0]
            # If only two parameters
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
        
        elif command[1] in self.commands:
            try:
                response = None
                name = command[0]
                if command[1] == 'CRT':
                    response = self.threads.create(name, command[2])
                if command[1] == 'MSG':
                    response = self.threads.post(name, command[2], ' '.join(command[3:]))
                if command[1] == 'DLT':
                    response = self.threads.delete(name, int(command[2]))
                if command[1] == 'EDT':
                    response = self.threads.edit(name, command[2],int(command[3]), ' '.join(command[4:]))
                if command[1] == 'LST':
                    response = self.threads.listTitles()
                if command[1] == 'RDT':
                    response = self.threads.readTitle(command[2])
                if command[1] == 'UPD':
                    response = self.threads.

                # Print log
                print(f'{name} issued {command[1]} command')
                if command[1] != 'LST':
                    print(response)
                return response
            except Exception as e:
                return str(e)


server = Server(10095)
server.run()
