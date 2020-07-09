# spiral.py
# COMP9444, CSE, UNSW

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.nn.functional as F
from math import sqrt
import numpy as np

def cartToPolar(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    rho = np.array(rho).reshape(-1,1)
    phi = np.array(phi).reshape(-1,1)
    p = np.hstack((rho, phi))
    return p

# python3 spiral_main.py --net polar --hid 7
class PolarNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(PolarNet, self).__init__()
        self.linear1 = torch.nn.Linear(2, num_hid)
        self.linear2 = torch.nn.Linear(num_hid, 1)  # Why 1 instead of 2?
        self.Tanh = torch.nn.Tanh()
        self.sigmoid = nn.Sigmoid()
        self.hid1 = 0

    def forward(self, input):
        r = cartToPolar(input[:, 0], input[:, 1])
        out = torch.from_numpy(r)
        #print(input)
        #print(out)
        out = self.linear1(out)
        out = self.Tanh(out)
        self.hid1 = out
        out = self.linear2(out)
        #print(self.sigmoid(out))
        return self.sigmoid(out)

# python3 spiral_main.py --net raw --init 0.2
class RawNet(torch.nn.Module): 
    def __init__(self, num_hid):
        super(RawNet, self).__init__()
        self.linear1 = torch.nn.Linear(2, num_hid)
        self.linear2 = torch.nn.Linear(num_hid, num_hid)
        self.linear3 = torch.nn.Linear(num_hid, 1)
        self.Tanh = torch.nn.Tanh()
        self.sigmoid = nn.Sigmoid()
        self.hid1 = 0
        self.hid2 = 0

    def forward(self, input):
        out = input
        out = self.linear1(out)
        out = self.Tanh(out)
        self.hid1 = out
        out = self.linear2(out)
        out = self.Tanh(out)
        self.hid2 = out
        out = self.linear3(out)
        out = self.sigmoid(out)
        return out

class ShortNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(ShortNet, self).__init__()
        self.linear1 = torch.nn.Linear(2, num_hid)
        self.linear2 = torch.nn.Linear(num_hid +2, num_hid)
        self.linear3 = torch.nn.Linear(num_hid + num_hid + 2, 1)
        self.Tanh = torch.nn.Tanh()
        self.sigmoid = nn.Sigmoid()
        self.hid1 = 0
        self.hid2 = 0

# python3 spiral_main.py --net short --hid 9
    def forward(self, input):       # --hid 8 doesn't work a lot of times
        out = input
        out1 = self.linear1(out)
        out1 = self.Tanh(out1)
        self.hid1 = out1
        out1 = torch.cat([out1, out], 1)
        out2 = self.linear2(out1)
        out2 = self.Tanh(out2)
        self.hid2 = out2
        out2 = torch.cat([out1, out2], 1)
        out3 = self.linear3(out2)
        out3 = self.sigmoid(out3)
        return out3

def graph_hidden(net, layer, node): # Module, int, int
    xrange = torch.arange(start=-7,end=7.1,step=0.01,dtype=torch.float32)
    yrange = torch.arange(start=-6.6,end=6.7,step=0.01,dtype=torch.float32)
    xcoord = xrange.repeat(yrange.size()[0])
    ycoord = torch.repeat_interleave(yrange, xrange.size()[0], dim=0)
    grid = torch.cat((xcoord.unsqueeze(1),ycoord.unsqueeze(1)),1)
    plt.clf()
    with torch.no_grad(): # suppress updating of gradients
        net.eval()        # toggle batch norm, dropout
        output = net(grid)
        net.train() # toggle batch norm, dropout back again

        hid = 0
        if layer == 1:
            hid = net.hid1[:,node]
        else:
            hid = net.hid2[:,node]

        pred = (hid >= 0.5).float()

        # plot function computed by model
        plt.pcolormesh(xrange,yrange,pred.cpu().view(yrange.size()[0],xrange.size()[0]), cmap='Wistia')
