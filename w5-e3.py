class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8
w2 = Wild(X, Y)
w3 = Wild(17, 18)
w4 = Wild(X, 18)
print(w4.getX())
X = w4.getX() + w3.getX() + w2.getX()
print(w4.getX())