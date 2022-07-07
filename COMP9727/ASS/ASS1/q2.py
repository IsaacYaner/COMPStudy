import numpy as np
import pandas as pd
import torch 

# Data preparation
def read_data(): 
    r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
    df = pd.read_csv("q2.txt", sep="\t",names=r_cols,encoding="latin-1")

    # Data cleaning
    df = df.drop('timestamp', axis=1)
    return df
def get_data(split = 0.8):
    df = read_data()    
    train = df.head(int(split*df.__len__()))
    test = df.tail(int((1-split)*df.__len__()))
    return train, test

def get_matrix():
    df = read_data()
    rating_matrix = df.pivot_table(values='rating', index='user_id', columns='movie_id')
    rating_matrix = rating_matrix.fillna(0)
    R = rating_matrix
    return R

def in_matrix(user, item, matrix):
    if user+1 not in matrix:
        return False
    if item+1 not in matrix[user+1]:
        return False
    return True

def get_existence():
    result = []
    df = read_data()
    items = max(df['movie_id']) # Number of items
    users = max(df['user_id'])  # Number of users
    matrix = get_matrix()
    for u in range(users):    # items
        reviews = []
        for i in range(items):# users
            if not in_matrix(u, i, matrix):
                reviews.append(False)
                continue
            if matrix[u+1][i+1] == 0:
                reviews.append(False)
                continue
            reviews.append(True)
        result.append(reviews)
    return result

def prediction(user, item):
    return np.dot(Q[item-1], P.T[user-1])

def SE(y, y_bar):
    n = len(y) #finding total number of items in list
    summation = 0
    for i in range (0,n):  
        difference = y[i] - y_bar[i]  
        squared_difference = difference**2  
        summation = summation + squared_difference  
    SE = summation  
    return SE

def l2Norm(x):
    return np.sqrt(np.sum(np.square(x), axis=0))

def E(train):
    predictions = [prediction(d[1]['user_id'], d[1]['movie_id']) for d in train.T.iteritems()]
    cost = SE(predictions, train['rating'])
    normP = sum([l2Norm(u)**2 for u in P])
    normQ = sum([l2Norm(i)**2 for i in Q])
    normFactor = lam * (normP + normQ)
    cost += normFactor
    return cost

def single_gradient(user, item, user_tar, item_tar, exist):
    if not ((user_tar is None) ^ (item_tar is None)):
        return "Exactly one arg is needed"
    gradient = 0
    pu = P.T[user]
    qi = Q[item]
    pred = prediction(user+1, item+1)#Forgot+1！sb
    real = 0
    if exist[item][user]:
        real = R[item+1][user+1]
    else:
        real = 0
    if user_tar is not None:
        elem = qi[user_tar]
    else:
        elem = pu[item_tar]
    gradient += 2*(real - pred) * elem
    gradient += 2 * elem * elem
    # print(real, pred, elem, gradient)
    return gradient

def user_gradient(user, feature, exist):
    result = 0
    divider = 0
    for item in range(m):
        if not exist[user][item]:
            continue
        result += single_gradient(user, item, feature, None, exist)
        divider += 1
    if divider == 0:
        return result
    return result/divider

def item_gradient(item, feature, exist):
    result = 0
    divider = 0
    for user in range(n):
        if not exist[user][item]:
            continue
        result += single_gradient(user, item, None, feature, exist)
        divider += 1
    if divider == 0:
        return result
    return result/n

def update_user(eta, exist):
    for i in range(n):
        for j in range(k):
            P[j][i] += eta * user_gradient(i, j, exist)
        # if i%20 == 0:
            # print(i/n)

def update_item(eta, exist):
    for i in range(m):
        for j in range(k):
            Q[i][j] += eta * item_gradient(i, j, exist)
        # if i%20 == 0:
            # print(i/m)


def learn(eta, exist):
    for i in range(iterations):
        print(i, ': ', E(train))
        # print(P)
        # print(Q)
        update_user(eta, exist)
        update_item(eta, exist)

k = 20
lam = 0.1
eta = 0.01
iterations = 40
split = 1.0
df = read_data()
m = max(df['movie_id']) # Number of items
n = max(df['user_id'])  # Number of users
Q = np.random.uniform(low=0.1, high=0.9, size=(m,k)) # Item
P = np.random.uniform(low=0.1, high=0.9, size=(k,n)) # User
R = get_matrix()


# print(R[1000])
train, test = get_data(split)

exist = get_existence()
learn(eta, exist)
