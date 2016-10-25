class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def get_vals(self):
        """return the value of intSet"""
        return self.vals
    def intersect(self, other):
        """Returns a new intSet containing elements that appear in
        both sets"""
        s = intSet()
        for e in self.get_vals():
            if other.member(e):
                s.insert(e)
        return s


    def __len__(self):
        """ Returns the number of elements in the set"""
        s = self.get_vals()
        s = list(s)
        return len(s)


    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
