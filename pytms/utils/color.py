class Color:
    white = lambda c: Color(255, 255, 255, 0)

    def __init__(self, r=0, g=0, b=0, a=0):
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)
        self.a = float(a)
