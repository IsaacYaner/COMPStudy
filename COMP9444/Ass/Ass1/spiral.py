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

class PolarNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(PolarNet, self).__init__()
        self.linear1 = torch.nn.Linear(2, num_hid)
        self.linear2 = torch.nn.Linear(num_hid, 1)  # Why 1 instead of 2?
        self.Tanh = torch.nn.Tanh()
        self.sigmoid = nn.Sigmoid()

    def forward(self, input):
        r = cartToPolar(input[:, 0], input[:, 1])
        out = torch.from_numpy(r)
        #print(input)
        #print(out)
        out = self.linear1(out)
        out = self.Tanh(out)
        out = self.linear2(out)
        #print(self.sigmoid(out))
        return self.sigmoid(out)

class RawNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(RawNet, self).__init__()
        self.linear1 = torch.nn.Linear(2, num_hid)
        self.linear2 = torch.nn.Linear(num_hid, num_hid)
        self.linear3 = torch.nn.Linear(num_hid, 1)
        self.Tanh = torch.nn.Tanh()
        self.sigmoid = nn.Sigmoid()

    def forward(self, input):
        out = input
        out = self.linear1(out)
        out = self.Tanh(out)
        out = self.linear2(out)
        out = self.Tanh(out)
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

    def forward(self, input): ### Merge
        out = input
        out = self.linear1(out)
        out = self.Tanh(out)
        out = self.linear2(out)
        out = self.Tanh(out)
        out = self.linear3(out)
        out = self.sigmoid(out)
        return out

def graph_hidden(net, layer, node):
    plt.clf()
    # INSERT CODE HERE
