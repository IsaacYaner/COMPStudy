from socket import *
import time
import sys

from torch import mean

MAX_WAIT_TIME = 600 #millisecond
NUMBER_REQUESTS = 15

class Ping():
    def __init__(self, number=NUMBER_REQUESTS, maxwait=MAX_WAIT_TIME):
        self.requests = []
        self.number = number
        self.maxwait = maxwait
        self.rtt = []
        self.lost = 0
    
    def ping(self, host="127.0.0.1", portnum = 10086, number=None):
        sequence_number = 3331
        if number == None:
            number = self.number
        clientSocket = socket(AF_INET, SOCK_DGRAM) # IPV4, UDP
        clientSocket.setblocking(0) #Non-blocking

        for i in range(number):
            # Send message
            message = f"PING {sequence_number} \r\n"
            Rtt = time.time()
            clientSocket.sendto(message.encode('utf-8'),(host, portnum))

            # Process received packets
            clientSocket.settimeout(self.maxwait/1000)
            try:
                modifiedMessage, _ = clientSocket.recvfrom(2048)
                Rtt = time.time() - Rtt
                wait_time = Rtt
                Rtt = int(Rtt*1000)
                # Sleep until one sec
                if wait_time < 1000:
                    time.sleep(1-wait_time)
                print(f"ping to {host}, seq = {i+1}, rtt = {Rtt} ms")
                self.rtt.append(Rtt)
            except:
                time.sleep(1 - (time.time() - Rtt))
                print(f"ping to {host}, seq = {i+1}, time out")
                self.lost+=1
            sequence_number+=1
            
        
        # Print the statistics
        lostrate = int(100*(self.lost/self.number))
        print(f"Packages: Sent={self.number}, Received={len(self.rtt)}, Lost={self.lost} ({lostrate}% lost)")
        if self.rtt != []:
            print(f"Minimum RTT is:{min(self.rtt)} ms")
            print(f"Maximum RTT is:{max(self.rtt)} ms")
            print(f"Average RTT is:{int(sum(self.rtt)/len(self.rtt))} ms")
        clientSocket.close()

    def send(self):
        pass

    def clear(self):
        self.requests = []
        self.rtt = []
        self.lost = 0
        pass

if __name__ == "__main__":
    ping = Ping()
    if len(sys.argv) == 2:
        portnum = 10086
    else:
        portnum = int(sys.argv[2])
    ping.ping(sys.argv[1], portnum, 15)
