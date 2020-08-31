import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x1 = [-3,-2,-1,0,1,2,3]
x2 = [9,4,1,-3,1,4,9]
y = [-1,-1,-1,1,1,-1,-1]
'''
x1 = [-1,2,1]
x2 = [1,4,1]
y = [-1,-1,1]
'''
x1 = np.array(x1).reshape(-1, 1)
x2 = np.array(x2).reshape(-1, 1)

x = np.concatenate((x1, x2), axis = 1)
#print(x)

for i in range(len(y)):
    if y[i] == 1:
        plt.scatter(x1[i], x2[i], c = '#1f77b4') #blue
    else:
        plt.scatter(x1[i], x2[i], c = '#ff7f0e')
plt.show()

w = [1,-1]

yHat = np.sign(np.dot(x,w)+1)

clf = SVC(C = 1e5, kernel = 'linear')
clf.fit(x, y) 

print(clf.support_)
print(clf.dual_coef_)
print(clf.coef_)
print(clf.intercept_)

x1 = [-3,-2,-1,0,1,2,3]
x2 = [9,4,1,-3,1,4,9]
x1 = np.array(x1).reshape(-1, 1)
x2 = np.array(x2).reshape(-1, 1)
y = [-1,-1,-1,1,1,-1,-1]

x = np.concatenate((x1, x2), axis = 1)
#yHat = clf.predict(x)
print(yHat)

for i in range(len(y)):
    if yHat[i] == 1:
        plt.scatter(x1[i], x2[i], c = '#1f77b4') #blue
    else:
        plt.scatter(x1[i], x2[i], c = '#ff7f0e')
plt.show()
