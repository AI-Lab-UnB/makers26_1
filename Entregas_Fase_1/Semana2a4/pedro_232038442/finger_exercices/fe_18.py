class Circle():
    def __init__(self, radius):
        """ Initialize self with radius """
        self.radius = radius

    def get_radius(self):
        """ Return self radius """
        return self.radius

    def __add__(self, c):
        """
        c is a Circle object
        Return a new Circle object whose radius is the sum of the radius of self and c
        """
        new_radius = self.radius + c.radius
        return Circle(new_radius)

    def __str__(self):
        """ The string representation of a Circle and your radius """
        return str('Circle with radius ' + self.radius)

    