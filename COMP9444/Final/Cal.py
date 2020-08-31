import numpy as np

def log(a, b):
    return np.log(b)/np.log(a)

def log2(b):
    return log(2, b)

def entropy(p, pri = False):
    H = 0
    for i in p:
        H = H - i*log2(i)
    return H

def DKL(p, q):
    H = 0
    for i, j in zip(p, q):
        H = H + i*(log2(i) - log2(j))
    return H
    
def Prob(z, i):
    i = i - 1
    return np.exp(z[i])/sum(np.exp(z))

def dProb(z, i, j):
    if i == j:
        return 1-Prob(z, j)
    else:
        return -Prob(z, j)

class Conv:
    def __init__(self, imageSize, numFilters, filterSize, stride, padding = 0):
        self.J, self.K, self.L = imageSize[0],imageSize[1],imageSize[2]
        self.M, self.N = filterSize[0], filterSize[1]
        self.num = numFilters
        self.s = stride
        self.P = padding
    
    def weight(self):
        return self.L*self.M*self.N+1

    def neurons(self):
        return self.num*self.layerSize()[0]*self.layerSize()[1]

    def connections(self):
        return self.neurons()*self.weight()

    def layerSize(self):
        return (1+int((self.J-self.M+2*self.P)/self.s)), (1+int((self.K-self.N+2*self.P)/self.s))

    def independent(self):
        return self.weight()*self.num

class Hopfield():
    def __init__(self, x, w=0, b=0):
        self.x = x
        if w == 0:
            self.w = np.zeros((len(x), len(x)))
        elif w == 1:
            self.w = np.outer(x, x)
            for i in range(len(x)):
                self.w[i][i] = 0
        else:
            self.w = w
        if b == 0:
            self.b = np.zeros((len(x)))
        else:
            self.b = b
        self.b = np.array(self.b)
        self.x = np.array(self.x)
        self.w = np.array(self.w)
        
    def Energy(self):
        E = 0
        for i in range(len(self.x)):
            for j in range(len(self.x)):
                E = E + self.x[i]*self.w[i][j]*self.x[j]
        return -(1/2*E + sum(self.b*self.x))

    def criteria(self, i, x):
        return sum(self.w[i]*x)+self.b[i]

    def update(self, i, x=0):
        if type(x) == type(0):
            x = self.x
        cri = self.criteria(i, x)
        if cri > 0:
            x[i] = 1
        elif cri <0:
            x[i] = -1
        return x

    def train(self, x = 0, asyn = False):
        if self.isStable(x):
            return
        if type(x) == type(0):
            x = self.x
        cri = np.dot(self.w, x)
        if asyn:
            for i in range(len(x)):
                if np.sign(cri[i]) == np.sign(x[i]) or cri[i] == 0:
                    continue
                else:
                    if cri[i] > 0:
                        x[i] = 1
                    elif cri[i] <0:
                        x[i] = -1
                    self.train(x, True)
                    break
                    
        else:
            for i in range(len(x)):
                if cri[i] > 0:
                    x[i] = 1
                elif cri[i] <0:
                    x[i] = -1
        return
        

    def isStable(self, x = 0):
        if type(x) == type(0):
            x = list(self.x)
        if type(x) == type(self.x):
            x = x.tolist()
        x = x[:]
        ox = x[:]
        for i in range(len(x)):
            self.update(i, x)
        return ox == x

    def merge(self, w):
        return (1/len(w[0])*(sum(w))).tolist()

def Energy(w, x, b):
    E = 0
    for i in range(len(x)):
        for j in range(len(x)):
            E = E + x[i]*w[i][j]*x[j]
    return -(1/2*E + sum(b*x))

class Reinforcement():
    def __init__(self, s, delta):
        self.s = s
        self.delta = (np.array(delta)-1).tolist()

class QLearning():
    def __init__(self, s, delta, reward, gamma):
        self.s = s
        self.r = reward
        self.delta = (np.array(delta)-1).tolist()
        self.Q = []
        self.gamma = gamma
        for i in range(s):
            subQ=[]
            for j in range(len(delta[i])):
                subQ.append(0)
            self.Q.append(subQ)

    def pi(self, s):
        return np.argmax(self.Q[s-1])+1

    def Vmax(self, s):
        #print(s)
        return np.max(self.Q[s])

    def train(self):
        for s in range(self.s):
            for a in range(len(self.delta[s])):
                self.Q[s][a] = self.r[s][a] + self.gamma * self.Vmax(self.delta[s][a])

'''
'''
s = 2
gamma = 0.66
for i in range(200):
    gamma = gamma + 0.001
    delta = [[1, 2], [1, 2]]
    reward = [[4, 8], [-2, 1]]
    model = QLearning(s, delta, reward, gamma)
    for i in range(10000):
        model.train()
    #print(model.Q)
    print("%.3f"%gamma, model.pi(1), model.pi(2))
    #print(model.pi(2))

'''
p = [1/2, 1/4, 1/8, 1/16, 1/16]
q = [1/8, 1/16, 1/4, 1/2, 1/16]
print(entropy(p))
print(DKL(p, q))
z = [1.3, 2.1, 3.7]
print(Prob(z, 1))
print(dProb(z, 1, 1))
print(dProb(z, 1, 2))
print(dProb(z, 1, 3))
'''


'''
imageSize = (84, 84, 4)
numFilters = 16
filterSize = (8, 8)
stride = 4
padding = 0
model = Conv(imageSize, numFilters,filterSize, stride, padding)
print(model.weight())
print(model.layerSize())
print(model.neurons())
print(model.connections())
print(model.independent())
'''


'''
w =[
[0,0,-1,0,0],
[0,0,0,0,+1],
[-1,0,0,-1,0],
[0,0,-1,0,+1],
[0,+1,0,+1,0]
]
b = 0
x = [1,1,1,1,-1]
x1 = [-1,1,1,1,1]
x2 = [1,1,-1,-1,-1]
x3 = [1,1,-1,1,1]

model = Hopfield(x3, w)
model.train(x1)
print(x1)
model.train(x2)
print(x2)
model.train(x3)
print(x3)
print(model.isStable(x1))
print(model.isStable(x2))
print(model.isStable(x3))
'''



'''
w1 = [0.5, -1, -1]
w2 = [1.5, -1, -1]
w3 = [-0.5, 1, 1]

for x1 in range(2):
    for x2 in range(2):
        #print(x1, x2)
        x3 = w1[0] + w1[1]*x1 + w1[2]*x2
        x4 = w2[0] + w2[1]*x1 + w2[2]*x2

        x3 = 1 if x3>0 else 0
        x4 = 1 if x4>0 else 0
        x5 = w3[0] + w3[1]*x3 + w3[2]*x4
        x5 = 1 if x5>0 else 0
        print(x5)
'''



