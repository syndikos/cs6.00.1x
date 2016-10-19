def sqrt(y):
    tolerance = 0.00001
    def neo(x):
        assert x != 0, 'divisor cannot be zero'
        return average(y/x, x)
    def average(x, y):
        return (x + y)/2.0
    def test(x, y):
        if abs(x**2 - y) <= tolerance:
            return x
        else:
            neo = neo(x)
            return test(neo)
    return test(0.000001, y)


def Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(origin, point):
        h_distance = abs(origin.x - point.x)**2
        v_distance = abs(origin.y - point.y)**2
        return sqrt(h_distance + v_distance)

    
