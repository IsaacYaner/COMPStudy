from Client import *
import sys

if len(sys.argv) == 1:
    print('Please run this by single parameter: server_port')
#client = Client('localhost', sys.argv[1])
client = Client('localhost', 10086)
client.run()
