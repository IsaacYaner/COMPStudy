import numpy as np

r1 = [5,3,4,4,None]
r2 = [3,1,2,3,3]
def mean(r1):
    r1 = [i for i in r1 if i is not None]
    return sum(r1)/len(r1)

def pcc(r1, r2):
    nom = sum([(i-mean(r1))*(j-mean(r2)) for i,j in zip(r1,r2) if i is not None and j is not None])
    denom = np.sqrt(sum([(i-mean(r1))**2 for i in r1 if i is not None])) * np.sqrt(sum([(i-mean(r2))**2 for i in r2 if i is not None]))
    return nom/denom


r1 = [1,2,3,5,8]
r2 = [0.11, 0.12, 0.13, 0.15, 0.18]
print(pcc(r1, r2))