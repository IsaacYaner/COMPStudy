import numpy as np

def log(a, b):
    return np.log(b)/np.log(a)

def log2(b):
    return log(2, b)

def entropy(C, n = 2, pri = False):
    occ = C.occ
    p = []
    H = 0
    card = C.card
    for i in range(n):
        p.append(occ[i]/card)
        H = H - p[i]*log2(p[i])
        if pri:
            print('- ', occ[i], '/', card, 'log2(', occ[i], '/', card, ')', sep = '', end = ' ')
    return H

def sep(A, C, n = 2):
    subC = []
    for i in range(n):
        subC.append([])
    for i in range(A.card):
        subC[A[i]].append(C[i])
    return data(subC)

def gain(C, A, n = 2, pri = False):
    if pri:
        print('Gain(C,A)=', end = '')
    ans = entropy(C)
    if pri:
        print(ans, end='\n', sep='')
    card = C.card
    subC = sep(A, C, n)
    for i in range(n):
        print('-', subC[i].card, '/', card, '(', end = ' ', sep = '')
        ans = ans - subC[i].card/card*entropy(subC[i], pri = pri)
        print(")")
    if pri:
        print("=", ans)
    return ans

class data:
    def __init__(self, arr, n = 2):
        self.occ = []
        self.list = arr
        self.card = len(arr)
        for i in range(n):
            self.occ.append(arr.count(i))
    
    def __getitem__(self, index):
        if type(self.list[index]) == type([]):
            return data(self.list[index])
        return self.list[index]

def gen(arr):
    ret = []
    n = len(arr)
    for i in range(n):
        ret = ret + [i for j in range(arr[i])]
    return ret


'''
A = gen([26, 38])       # gen([sumof C1, sumof C2])
C1 = gen([21,5])
C2 = gen([8, 30])
C = C1+C2
'''

A = [1,0,1,1,1,1,0,1,0,0]
B = [0,1,1,0,1,1,0,1,0,0]
C = [1,0,0,1,0,0,1,1,1,0]

A = data(A)
B = data(B)
C = data(C)

print(entropy(C, pri = True))

ans = gain(C, A, pri = True)
ans = gain(C, B, pri = True)

print(2*log(np.exp(1), 6))
