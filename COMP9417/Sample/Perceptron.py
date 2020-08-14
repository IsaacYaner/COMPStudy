import numpy as np

class tron:
    def __init__(self, w0, w, learning_rate=0.5):
        self.eta = learning_rate
        self.w = w
        self.w0 = w0

    def train(self, x, y, pri = False):
        stop = False
        iteration = 1
        while stop == False:
            stop = True
            for i in range(len(y)):
                if pri:
                    print(iteration, end = '\t')
                    iteration += 1
                    print("%.2f"%((np.dot(self.w, x[i])+self.w0)), end='\t')
                    print("%.2f"%(y[i]*(np.dot(self.w, x[i])+self.w0)), end='\t')

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
        print(str(out).replace('[', '').replace(']',''))



model = tron(5,[1, 1], 0.4)

x1 = np.array([[-2, 2, 1, -1, 3]]).reshape(-1,1)
x2 = np.array([[-1, -1, 1, -1, 2]]).reshape(-1,1)

x = np.concatenate((x1, x2), axis = 1)
y = np.array([-1,1,1,-1,1])

model.train(x, y, True)
model.predict([-5, 3], True)
