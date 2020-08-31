
## STUDENT ID: FILL IN YOUR ID
## STUDENT NAME: FILL IN YOUR NAME


## Question 2

import numpy as np
import matplotlib.pyplot as plt

'''np.random.seed(42)       # make sure you run this line for consistency 
x = np.random.uniform(1, 2, 100)
y = 1.2 + 2.9 * x + 1.8 * x**2 + np.random.normal(0, 0.9, 100)
plt.scatter(x,y)
plt.show()'''

## (c)

# YOUR CODE HERE

## plotting help
'''fig, ax = plt.subplots(3,3, figsize=(10,10))
alphas = [10e-1, 10e-2, 10e-3,10e-4,10e-5,10e-6,10e-7, 10e-8, 10e-9]
for i, ax in enumerate(ax.flat):
    # losses is a list of 9 elements. Each element is an array of length 100 storing the loss at each iteration for that particular step size
    ax.plot(losses[i])         
    ax.set_title(f"step size: {alphas[i]}")	 # plot titles	
    plt.tight_layout()      # plot formatting
    plt.show()'''





## Question 3

# (c)
# YOUR CODE HERE





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
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    if ax:
        ax.contourf(xx, yy, Z, cmap=plt.cm.Paired)
        ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
        ax.set_title(title)
    else:
        plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
        plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
        plt.title(title)
    plt.show()

X, y = create_dataset()
X_train, X_test, y_train, y_test = train_test_split(X ,y,test_size = 0.2, train_size = 0.8)
#fig,ax = plt.subplots(2,3,figuresize = (10,10))

'''clf = SVC()
clf.fit(X_train,y_train)
plotter(clf,X,X_test,y_test,'SVM')
clf = DecisionTreeClassifier()
clf.fit(X_train,y_train)
plotter(clf, X, X_test, y_test, 'DecisionTree')
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
plotter(clf, X, X_test, y_test, 'RandomForest')
clf = AdaBoostClassifier()
clf.fit(X_train, y_train)
plotter(clf, X, X_test, y_test, 'AdaBoost')
clf = LogisticRegression()
clf.fit(X_train, y_train)
plotter(clf, X, X_test, y_test, 'LogisticRegression')
clf = MLPClassifier()
clf.fit(X_train, y_train)
plotter(clf, X, X_test, y_test, 'MLP')'''

titleList = ["DecisionTree", "RandomForest","AdaBoost", "LogisticRegression", "NeuralNetwork","SVM"]
trainSize = [50,100,200,300,400,500,600,700,800,900,1000]
result = np.zeros((6,11))
resultTime = np.zeros((6, 11))
#DATAList = [DT,RF,AB,LR,NN,SVM]
for i in range(6):
    for j in range(10):
        for k in range(11):
            X_train1, X_test1, y_train1, y_test1 = train_test_split(X,y,test_size = 1250-trainSize[k], train_size = trainSize[k])
            clf = None
            if i == 0 : clf = DecisionTreeClassifier()
            elif i == 1 : clf = RandomForestClassifier()
            elif i == 2: clf = AdaBoostClassifier()
            elif i == 3: clf = LogisticRegression()
            elif i == 4: clf = MLPClassifier()
            elif i == 5: clf = SVC()
            start_time = time.time()
            clf.fit(X_train1,y_train1)
            time_use = time.time()-start_time
            result[i][k] += clf.score(X_test1, y_test1)/10
            resultTime[i][k] += time_use
print(result)
print(resultTime)

plt.plot(trainSize,result[0],color = "blue")
plt.plot(trainSize, result[1], color="orange")
plt.plot(trainSize,result[2],color = "green")
plt.plot(trainSize, result[3], color="red")
plt.plot(trainSize,result[4],color = "purple")
plt.plot(trainSize, result[5], color="brown")
plt.xlabel("TrainSize")
plt.ylabel("Accuracy")
plt.savefig('Accuracy.png')
plt.show()
# (a)
# YOUR CODE HERE




# (b)
# YOUR CODE HERE

# (c)
# YOUR CODE HERE
plt.plot(trainSize, resultTime[0], color="blue")
plt.plot(trainSize, resultTime[1], color="orange")
plt.plot(trainSize, resultTime[2], color="green")
plt.plot(trainSize, resultTime[3], color="red")
plt.plot(trainSize, resultTime[4], color="purple")
plt.plot(trainSize, resultTime[5], color="brown")
plt.xlabel("TrainSize")
plt.ylabel("TimeUsed")
plt.savefig('Time.png')
plt.show()
