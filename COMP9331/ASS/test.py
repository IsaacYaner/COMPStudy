from Client import *
from PassManager import *
from ThreadManager import *
import sys

# if len(sys.argv) == 1:
    # print('Please run this by single parameter: server_port')
#client = Client('localhost', sys.argv[1])
# client = Client('localhost', 10095)
# client.run()

from Thread import *
manager = ThreadManager()
name = 'Zaxi'
title = input()
manager.create(name, title)
while True:
    message = input()
    manager.

# self.auth = PassManager()
# def login(self):
#     self.auth.read()
#     while True:
#         name = print('Enter username: ')
#         if not self.auth.exist(name):
#             print('User doesn\'t exist, you are creating a new account')
#         if self.auth.isOnline(name):
#             print(f'{name} has already logged in')
#             continue
#         password = input('Enter password: ')
#         if self.auth.login(name, password):
#             print('Welcome to the forum')
#             break
#         print('Invalid password')