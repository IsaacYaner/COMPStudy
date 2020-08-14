import numpy as np
from sklearn.linear_model import LinearRegression

def SquareErrorLoss(y, yH):
    y = y.reshape((1, -1))
    yH = yH.reshape((1, -1))
    Loss = ((y- yH)**2).sum()
    return Loss

class LinearModel:
    def __init__(self, w1, w0):
        self.a = w1
        self.b = w0

    def predict(self, x):
        return self.a*x + self.b

    def show(self):
        print('Slope: ', self.a,'Inter: ', self.b)

def MSELearning(x, y):
    x = x.reshape((1, -1))
    y = y.reshape((1, -1))
    xy = np.multiply(x, y)
    xS = x**2
    xBar = x.mean()
    yBar = y.mean()
    xyBar = xy.mean()
    xSBar = xS.mean()

    a = (xyBar - xBar * yBar)/(xSBar - xBar**2)
    b = yBar - a * xBar
    
    return LinearModel(a, b)

def MSELearningSci(x, y):
    x = x.reshape(-1,1)
    model = LinearRegression()
    model.fit(x, y)

    print('intercept:\t', model.intercept_)
    print('slope:\t', model.coef_[0])
    return model


x = np.array([4, 6, 12, 25, 29, 46, 59]).reshape((-1, 1))
y = np.array([2, 4, 10, 23, 28, 44, 60])

model = MSELearning(x, y)
model.show()
model = MSELearningSci(x, y)
yH = model.predict(x)
yP = model.predict(np.array([50]).reshape(-1, 1))
print(yP)
print(SquareErrorLoss(y, yH))