class Point(object):
    # static methods
    @staticmethod
    def _zero():
        return Point(0, 0)

    # static fields
    zero = _zero()

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def equals(self, other):
        """
        Checks if given object is a Point and if so, checks if its equal to this one
        :param other:
        :return:
        """
        if not isinstance(other, Point):
            return False
        if self.x == other.x:
            return self.y == other.y

        return False

    def __str__(self):
        return f'X:{self.x} Y:{self.y}'