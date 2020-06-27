# kuzu.py
# COMP9444, CSE, UNSW

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import sys
import numpy
#！！！！！！！！！！！！Not Completed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class NetLin(nn.Module):
    # linear function followed by log_softmax
    def __init__(self):
        super(NetLin, self).__init__()
        self.linear = torch.nn.Linear(28*28,10)

    def forward(self, x):
        #torch.set_printoptions(profile="full")
        x = x.view(-1, 28*28)
        out = self.linear(x) 
        return F.log_softmax(out, dim = 0)

class NetFull(nn.Module):
    # two fully connected tanh layers followed by log softmax
    def __init__(self):
        super(NetFull, self).__init__()
        # INSERT CODE HERE

    def forward(self, x):
        return 0 # CHANGE CODE HERE


class NetConv(nn.Module):
    # two convolutional layers and one fully connected layer,
    # all using relu, followed by log_softmax
    def __init__(self):
        super(NetConv, self).__init__()
        # INSERT CODE HERE

    def forward(self, x):
        return 0 # CHANGE CODE HERE
