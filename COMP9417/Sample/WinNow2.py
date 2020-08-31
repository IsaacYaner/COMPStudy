import numpy as np

class tron:
    def __init__(self, alpha, Sigma, w):
        self.w = w
        self.alpha = alpha
        self.Sigma = Sigma

    def train(self, x, y, pri = False):
        stop = False
        iteration = 1
        while stop == False:
            stop = True
            for i in range(len(y)):
                if pri:
                    print(iteration, end = '\t')
                    iteration += 1
                    print(self.predict(x[i]), y[i], end='\t')
                
                yH, _ = self.predict(x[i])
                if y[i] == 1:
                    a = self.alpha
                else:
                    a = 1/self.alpha
                if yH != y[i]:
                    stop = False
                    for j in range(len(x[i])):
                        if x[i][j] == 1:
                            self.w[j] = a*self.w[j]

                if pri:
                    print(self.predict(x[i]), end= '\t')
                    self.show()

    def predict(self, x, pri = False):
        ans = np.dot(self.w, x)
        y = 1 if ans>self.Sigma else 0
        if pri:
            print("Value is %.2f"%ans, "Class is %d"%y, end='\t')
        return y, ans

    def show(self):
        print(str(self.w).replace('[', '').replace(']',''))



model = tron(2, 2, [1, 1, 1, 1, 1, 1])

x1 = np.array([[0,1,0,0,1]]).reshape(-1,1)
x2 = np.array([[0,0,1,1,1]]).reshape(-1,1)
x3 = np.array([[0,1,0,1,0]]).reshape(-1,1)
x4 = np.array([[0,1,1,0,0]]).reshape(-1,1)
x5 = np.array([[1,0,0,0,0]]).reshape(-1,1)
x6 = np.array([[1,1,1,1,0]]).reshape(-1,1)

x = np.concatenate((x1, x2, x3, x4, x5, x6), axis = 1)
y = np.array([1, 1, 0, 0, 1])
print(x)

model.show()
model.train(x, y, True)
#model.predict(, True)

