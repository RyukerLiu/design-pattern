import math


class RoundPeg:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def fits(self, peg: RoundPeg):
        return self.radius >= peg.get_radius()


class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width


class SquarePegAdapter(RoundPeg):
    '''
    In order to check if we can insert SquarePeg in a RoundHole
    '''

    def __init__(self, peg: SquarePeg):
        self.peg = peg

    def get_radius(self):
        width = self.peg.get_width()
        radius = (width / 2) * math.sqrt(2)

        return radius
