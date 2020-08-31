import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x1 = [-0.8, 3.9, 1.4, 0.1, 1.2, -2.45, -1.5, 1.2]
x2 = [1, 0.4, 1, -3.3, 2.7, 0.1, -0.5, -1.5]
y = [1,-1,1,-1,-1,-1,1,1]

x1 = np.array(x1).reshape(-1, 1)
x2 = np.array(x2).reshape(-1, 1)
x3 = np.sqrt(2)*x1*x2
xo = np.concatenate((x1, x2), axis = 1)
x1 = x1**2
x2 = x2**2

x = np.concatenate((x1, x2, x3), axis = 1)
#print(x)

for i in range(len(y)):
    if y[i] == 1:
        plt.scatter(x1[i], x2[i], c = '#1f77b4') #blue
    else:
        plt.scatter(x1[i], x2[i], c = '#ff7f0e')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y)):
    if y[i] == 1:
        ax.scatter(x1[i], x2[i], x3[i], c = '#1f77b4') #blue
    else:
        ax.scatter(x1[i], x2[i], x3[i], c = '#ff7f0e')
plt.show()

eta = 0.2
w = np.array([1.,1.,1.])

def polynomial_kernel(x, y, p=2):
    return (1 + np.dot(x, y)) ** p

class perceptron:
    def __init__(self, w0, w, learning_rate=0.5, kernel = polynomial_kernel):
        self.eta = learning_rate
        self.w = w
        self.w0 = w0

    def train(self, x, y, pri = False):
        if pri:
            print('iter\tw0\t    w1\t         w2\t     w3')
        stop = False
        iteration = 1
        while stop == False:
            stop = True
            for i in range(len(y)):
                if pri:
                    print(iteration, end = '\t')
                    iteration += 1

                if y[i]*(np.dot(self.w, x[i])+self.w0) <= 0:
                    self.w = self.w + self.eta*y[i]*x[i]
                    self.w0 = self.w0 + self.eta*y[i]*1
                    stop = False

                if pri:
                    self.show()

    def predict(self, x, pri = False):
        ans = np.dot(self.w, x)+self.w0
        y = 1 if ans>=0 else -1
        if pri:
            print("Value is %.2f"%ans, "Class is %d"%y, end='\t')
        return y, ans

    def show(self):
        out = np.insert(self.w, 0, self.w0)
        print(str(out).replace('[', '').replace(']',''), sep='\t')

model = perceptron(1, w, eta)

model.train(x, y, False)

np.set_printoptions(suppress=True)
print('xi is')
print(str(xo).replace('[', '').replace(']',''), end = '\n\n')
print('phi(xi)is')
print(str(x).replace('[', '').replace(']',''), end = '\n\n')

print("r = yiphi^T(xi)w* is")
for i in range(len(y)):
    print(y[i]*(np.dot(model.w, x[i])+model.w0))
