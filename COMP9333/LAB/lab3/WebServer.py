import sys
from socket import *
#using the socket module

def simpleServer(port=12000):
    # Create and listen from the socket
    serverPort = port
    serverSocket = socket(AF_INET, SOCK_STREAM)     # IPv4 and TCP connection
    serverSocket.bind(('localhost', serverPort))    # Bind port number with IP address
    serverSocket.listen(1)                          # Start to listen

    while True:
        # When a query arrives
        connectionSocket, addr = serverSocket.accept()

        data = connectionSocket.recv(1024).decode()      # Get data from client
        filename = data.split()[1][1:]
        print(data)
        status = b"HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(status)
        with open(filename, 'rb') as f:
            connectionSocket.send(f.read())
        connectionSocket.close()                # Close this connection

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # print('port is expected as argument')
        # exit(0)
        simpleServer(12001)
    simpleServer(int(sys.argv[1]))