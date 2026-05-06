class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.r = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.r

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        sum = c.r + self.r
        
        return Circle(sum)

    def __str__(self):
        """ A Circle's string representation is the radius """
        return str(self.r)