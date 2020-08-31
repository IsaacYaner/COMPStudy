import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

#Reference for distance
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html

def disM(x, y):
    x = [x]
    y = [y] 
    if type(x) != type([]):
        x = [x]
        y = [y]
    return cdist(x, y, metric='cityblock')

X = [2.01,3.49, 4.58, 4.91, 4.99, 5.01, 5.32, 5.78, 5.99, 6.21, 7.26, 8.00]
c = [3.33, 6.67]
k = 2
features = 1
data = np.array(X).reshape(-1, 1)
centroid = np.array(c).reshape(k, features)

kmeans = KMeans(k, max_iter=2, init = centroid).fit(data)

np.set_printoptions(precision=2)
print(kmeans.labels_)
print(kmeans.cluster_centers_)

'''
class kMean:
    def __init__(self, k, points, centroid, distance):
        self.k = k
        self.n = len(points)
        self.list = points
        self.P = []
        for i in range(self.n):
            self.P.append(0)
        self.c = centroid
        self.dis = distance
        self.E = self.error()

    def centroid(self):
        for

    def error(self, i=-1, j=-1):
        E = 0
        oP = self.P[i]
        if i >= 0:
            self.P[i] = j
        for i in range(self.n):
            E = E + self.dis(i, self.c[self.P[i]])
        self.P[i] = oP
        return E

    def train(self):
        stop = False
        while stop == False:
            stop = True
            for i in range(self.n):
                minE = float('inf')
                for j in range(self.k):
                    if self.P[i] == j:
                        continue
                    
                    
'''
