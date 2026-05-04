class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self.radius = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        area = 3.14*(self.radius**2)
        return area

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        return self.radius == c.get_radius()

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        if self.radius > c.get_radius():
            return self
        else:
            return c