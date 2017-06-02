class QuadraticEquation(object):
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = (self.b ** 2) - (4 * self.a * self.c)

    def solve(self):
        if self.d > 0:
            self.x1 = (-self.b + (self.d ** (0.5))) / (2 * self.a)
            self.x2 = (-self.b - (self.d ** (0.5))) / (2 * self.a)
        elif self.d == 0:
            self.x = -self.b / (2 * self.a)