class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
        + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() - other.getNumer() \
        * self.getDenom()
        return fraction(numerNew, denomNew)
    def conver(self):
        return self.getNumer() / self.getDenom()
one_half = fraction(1, 2)
two_thirds = fraction(2, 3)
print(one_half)
print(two_thirds)
print(one_half.getNumer())
new = one_half + two_thirds
print(new)
decimal = new.conver()
print(decimal)
