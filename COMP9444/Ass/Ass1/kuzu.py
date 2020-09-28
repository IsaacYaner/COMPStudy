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
        #Local minima is h=110
        hinddenSize = 110
        super().__init__()
        self.linear1 = torch.nn.Linear(28*28,hinddenSize)
        self.Tanh = torch.nn.Tanh()
        self.linear2 = torch.nn.Linear(hinddenSize,10)

    def forward(self, x):
        x = x.view(-1, 28*28)
        out = self.linear1(x)
        out = self.Tanh(out)
        out = self.linear2(out)
        return F.log_softmax(out, dim = 0)


class NetConv(nn.Module):
    # two convolutional layers and one fully connected layer,
    # all using relu, followed by log_softmax
    def __init__(self):
        super(NetConv, self).__init__()
        channel1 = 10
        channel2 = 50
        self.conv1 = nn.Conv2d(1, channel1, 5, stride = 1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(channel1, channel2, 5, stride = 1)
        self.dropOut = nn.Dropout()
        self.linear = nn.Linear(453, 256)
        self.fcOut = nn.Linear(256,10)
        self.relu = nn.ReLU()
    def forward(self, x):
        out = self.pool(F.relu(self.conv1(x)))
        out = F.relu(self.conv2(out))
        out = out.reshape(out.size(0), -1)
        out = self.dropOut(out)
        out = self.linear(out)
        out = self.relu(out)
        out = self.fcOut(out)
        out = F.log_softmax(out, dim = 0)
        return out


