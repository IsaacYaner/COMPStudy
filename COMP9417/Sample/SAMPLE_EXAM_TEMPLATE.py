
## Please rename this file to your student ID.py. e.g. z1234567.py
## STUDENT ID: FILL IN YOUR ID
## STUDENT NAME: FILL IN YOUR NAME


## Question 6

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_blobs

np.random.seed(2)
n_points = 15
X, y = make_blobs(n_points, 2, centers=[(0,0), (-1,1)])
y[y==0] = -1       # use -1 for negative class instead of 0
'''
plt.scatter(*X[y==1].T, marker="+", s=100, color="red")
plt.scatter(*X[y==-1].T, marker="o", s=100, color="blue")
#plt.savefig("boosting_data.png")
plt.show()
'''
def plotter(classifier, X, y, title, ax=None):
    # plot decision boundary for given classifier
    plot_step = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:,0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:,1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step), 
                            np.arange(y_min, y_max, plot_step)) 
    Z = classifier.predict(np.c_[xx.ravel(),yy.ravel()])
    Z = Z.reshape(xx.shape)
    if ax:
        ax.contourf(xx, yy, Z, cmap = plt.cm.Paired)
        ax.scatter(X[:, 0], X[:, 1], c = y)
        ax.set_title(title)
    else:
        plt.contourf(xx, yy, Z, cmap = plt.cm.Paired)
        plt.scatter(X[:, 0], X[:, 1], c = y)
        plt.title(title)


## Question 6 part a
# your code here
fig, axs = plt.subplots(3,3)
for i in range(9):
    clf = DecisionTreeClassifier(max_depth=i+1).fit(X, y)
    plotter(clf, X, y, "MaxDepth" + str(i+1), ax = axs[int(i/3)][i%3])
plt.tight_layout()
plt.show()
    

## Question 6 part b
def weighted_error(w, y, yhat):
    err = 0
    for i in range(len(w)):
        err = err + (w[i] if y[i] != yhat[i] else 0)
    return err
T = 15
w = np.zeros((T+1, n_points))
w[0] = np.ones(n_points)/n_points
# storage for boosted model
alphas = np.zeros(T); component_models = []
M = np.zeros(n_points)
for t in range(T):
    component_models.append(DecisionTreeClassifier(max_depth=1).fit(X,y,w[t]))
    yhat = component_models[t].predict(X)
    err = weighted_error(w[t], y, yhat)
    alphas[t] = 1/2*np.log((1-err)/err)
    for i in range(n_points):
        if y[i] != yhat[i]:
            w[t+1][i] = w[t][i]/(2*err)
        else:
            w[t+1][i] = w[t][i]/(2*(1-err))
    m = component_models[t].predict(X)
    M = M+alphas[t]*m
M = np.array([1 if m>0 else -1 for m in M])

print(M)
print(y)

## Question 6 part d
class boosted_model:
    def __init__(self, T):
        self.T = t
        self.alphas = np.zeros(T)
        self.component_models = []
    
    def predict(self, x):
        M = np.zeros(n_points)  
        M = np.array([m.predict(x) for m in self.component_models])
        M = self.alphas*M.T
        aM = np.array([m.sum() for m in M])
        print(aM.shape)
        M = np.array([1 if m>0 else -1 for m in aM])
        return M
        
fig, axs = plt.subplots(4,4)
models = []
for T in range(1,17):
    w = np.zeros((T+1, n_points))
    w[0] = np.ones(n_points)/n_points
    model = boosted_model(T)
    for t in range(T):
        model.component_models.append(DecisionTreeClassifier(max_depth=1).fit(X,y,w[t]))
        yhat = model.component_models[t].predict(X)
        err = weighted_error(w[t], y, yhat)
        model.alphas[t] = 1/2*np.log((1-err)/err)
        for i in range(n_points):
            if y[i] != yhat[i]:
                w[t+1][i] = w[t][i]/(2*err)
            else:
                w[t+1][i] = w[t][i]/(2*(1-err))
    models.append(model)
                
for i in range(16):
    plotter(models[i], X, y, "MaxDepth" + str(i+1), ax = axs[int(i/4)][i%4])

plt.show()
    