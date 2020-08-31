import numpy as np
import math
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

A = [2,0,3,0,0,3,4,4]
B = [0,3,0,0,0,0,3,0]
C = [4,3,0,2,0,0,0,0]
D = [4,0,2,0,1,0,0,1]
y = [1,1,1,1,-1,-1,-1,-1]
t = [1,0,0,2]
X = t

A = np.array(A).reshape(-1, 1)
B = np.array(B).reshape(-1, 1)
C = np.array(C).reshape(-1, 1)
D = np.array(D).reshape(-1, 1)
t = np.array(t).reshape(1, -1)

x = np.concatenate((A, B, C, D), axis = 1)

model = BernoulliNB(alpha = 0).fit(x, y)

yHat = model.predict_proba(t)
para = model.get_params()

print(yHat)
print(np.exp(model.feature_log_prob_))
'''
model = MultinomialNB(alpha = 1).fit(x, y)
yHat = model.predict_proba(t)
para = model.get_params()

print(yHat)
print(model.feature_log_prob_)

def P(x, a=0):
    #p = [5/23,3/23,9/23,6/23]
    #p=[6/27,4/27,10/27,7/27]
    #p = [12/20,4/20,1/20,3/20]
    p=[16/39,6/39,9/39,8/39]
    pro = 1
    for i in range(len(x)):
        pro = pro * ((p[i])**x[i])
    print(pro)
    base = 1
    for i in x:
        base = base * math.factorial(i)
    print(base)
    nume = math.factorial(sum(x))
    print(nume)
    return nume/base*pro

print(P(X))'''