import numpy
def CSdistribution(F, N, us, di):
    return max(N*F/us, F/di)

def P2Pdistribution(F, N, us, di, u):
    return max([F/us, F/di, N*F/(us + N*u)])

F = 10*1024*1024
us = 20*1024
di = 1024
u = [0.2*1024, 0.6*1024, 1024]
N = [10, 100, 1000]

resultP2P = []
resultCS = []
for uu in u:
    zz = []
    yy = []
    for n in N:
        zz.append(P2Pdistribution(F,n,us,di,uu))
        yy.append(CSdistribution(F,n,us,di))
    resultCS.append(yy)
    resultP2P.append(zz)

print(numpy.array(resultCS))
print(numpy.array(resultP2P))




