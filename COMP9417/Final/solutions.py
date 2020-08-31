
## STUDENT ID: FILL IN YOUR ID
## STUDENT NAME: FILL IN YOUR NAME


## Question 2

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)       # make sure you run this line for consistency 
x = np.random.uniform(1, 2, 100)
y = 1.2 + 2.9 * x + 1.8 * x**2 + np.random.normal(0, 0.9, 100)

plt.scatter(x,y)
plt.show()

## (c)

# YOUR CODE HERE

c = 2
minLoss = float('inf')
optw = []       # Optimum weights, confirmed to be the final value with alpha = 0.01
w0Record = []   # Used to record value for w0
w1Record = []   # Used to record value for w1
losses = []
alphas = [10e-1, 10e-2, 10e-3,10e-4,10e-5,10e-6,10e-7, 10e-8, 10e-9]
for k in range(9):
    w = np.array([1.,1.]).reshape(-1, 1)
    w0Record.append([])
    w1Record.append([])
    losses.append([])
    for t in range(100):
        w0Record[k].append([])
        w1Record[k].append([])
        w0Arr = np.full(100, w[0]) # convert w0 into an array to fit the computation of delta loss
        w1Arr = np.full(100, w[1]) # Same as above
        yHat = w[0] + w[1]*x       # calculate yHat
        lossT = sum(np.sqrt(1./(c**2)*((y-yHat)**2)+1.)-1.) # calculate loss

        # calculate nabla loss of w0 and w1 according to b) and c)
        nablaLossw0 = sum(-(y-w0Arr-w1Arr*x)/(c*np.sqrt((y-w0Arr-w1Arr*x)**2+c)))
        nablaLossw1  = sum(-x*(y-w0Arr-w1Arr*x)/(c*np.sqrt((y-w0Arr-w1Arr*x)**2+c)))

        w[0] = w[0] - alphas[k]*nablaLossw0 #Update by multiplying alpha with nablaloss
        w[1] = w[1] - alphas[k]*nablaLossw1

        # Append values into Record lists for w0, w1 and loss
        w0Record[k][t].append(float(w[0]))
        w1Record[k][t].append(float(w[1]))
        losses[k].append(lossT) # append to losses list

        # Record the final model
        if lossT < minLoss:
            minLoss = lossT
            optw = w

# Plotting weights of the final model through 100 iterations
# w0 is blue and w1 is orange
for i in range(100):       
    plt.scatter(i, w0Record[2][i], c='#1f77b4')
    plt.scatter(i, w1Record[2][i], c='#ff7f0e')

plt.show()

# Plotting the data with the final model super-imposed
# data is blue and model output is orange
plt.scatter(x,y)
plt.scatter(x,optw[0] + x*optw[1])
plt.show()

print(minLoss)

## plotting help
fig, ax = plt.subplots(3,3, figsize=(10,10))
alphas = [10e-1, 10e-2, 10e-3,10e-4,10e-5,10e-6,10e-7, 10e-8, 10e-9]
for i, ax in enumerate(ax.flat):
    # losses is a list of 9 elements. Each element is an array of length 100 storing the loss at each iteration for that particular step size
    ax.plot(losses[i])         
    ax.set_title(f"step size: {alphas[i]}")	 # plot titles	
    plt.tight_layout()      # plot formatting
plt.show()





## Question 3

# (c)
# YOUR CODE HERE

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

eta = 0.2
w = np.array([1.,1.,1.])

class perceptron:
    def __init__(self, w0, w, learning_rate=0.5):
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

model.train(x, y, pri = True)

np.set_printoptions(suppress=True)
print('xi is')
print(str(xo).replace('[', '').replace(']',''), end = '\n\n')
print('phi(xi)is')
print(str(x).replace('[', '').replace(']',''), end = '\n\n')

print("r = yiphi^T(xi)w* is")
for i in range(len(y)):
    print(y[i]*(np.dot(model.w, x[i])+model.w0))



# Question 5

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import time
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

def create_dataset():
    X, y = make_classification( n_samples=1250,
                                n_features=2,
                                n_redundant=0,
                                n_informative=2,
                                random_state=5,
                                n_clusters_per_class=1)
    rng = np.random.RandomState(2)
    X += 3 * rng.uniform(size = X.shape)
    linearly_separable = (X, y)
    X = StandardScaler().fit_transform(X)
    return X, y

def plotter(classifier, X, X_test, y_test, title, ax=None):
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
        ax.scatter(X_test[:, 0], X_test[:, 1], c = y_test)
        ax.set_title(title)
    else:
        plt.contourf(xx, yy, Z, cmap = plt.cm.Paired)
        plt.scatter(X_test[:, 0], X_test[:, 1], c = y_test)
        plt.title(title)


# (a)
# YOUR CODE HERE


X, y = create_dataset()

X_train, X_test, y_train, y_test = train_test_split(X ,y,test_size = 0.2, train_size = 0.8)
Titles = ['Decision Tree', 'Random Forest', 'Adaptive Boost', 'Logistic Regression', 'MLP classifier', 'SVM classifier']
clfs = [DecisionTreeClassifier(),RandomForestClassifier(),AdaBoostClassifier(),LogisticRegression(),MLPClassifier(),SVC()]

fig, axs = plt.subplots(2,3)
for i in range(6):
    clfs[i].fit(X_train,y_train)
    plotter(clfs[i], X, X_test, y_test, Titles[i], ax = axs[int(i/3)][i%3])
plt.tight_layout()
plt.show()

clfs = [DecisionTreeClassifier(),RandomForestClassifier(),AdaBoostClassifier(),LogisticRegression(),MLPClassifier(),SVC()]
trainSize = [50,100,200,300,400,500,600,700,800,900,1000]
score = np.zeros((6,11))
timeUsed = np.zeros((6, 11))
for i in range(6):
    for j in range(10):
        for k in range(11):
            X_train1, X_test1, y_train1, y_test1 = train_test_split(X,y,test_size = 1250-trainSize[k], train_size = trainSize[k])
            clf = clfs[i]
            timeStart = time.time()
            clf.fit(X_train1,y_train1)
            timeUsed[i][k] += time.time()-timeStart
            score[i][k] += clf.score(X_test1, y_test1)/10

colorList = ['blue', 'orange', 'green', 'red', 'purple', 'brown']

# (b)
# YOUR CODE HERE

for i in range(6):
    plt.plot(trainSize, score[i], color = colorList[i])
plt.xlabel("Size")
plt.ylabel("Score")
plt.show()

# (c)
# YOUR CODE HERE

for i in range(6):
    plt.plot(trainSize, timeUsed[i], color= colorList[i])
plt.xlabel("Size")
plt.ylabel("Time used")
plt.show()
